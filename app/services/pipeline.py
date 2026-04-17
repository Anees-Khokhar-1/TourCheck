import json
from app.services.llm_service import call_llm
from app.services.embedding_service import get_embedding
from app.services.category_engine import match_or_create
from app.utils.prompts import build_prompt
from app.db import get_conn


def process_activity(item):

    conn = get_conn()
    cur = conn.cursor()

    # Fetch existing
    cur.execute("SELECT name FROM categories")
    categories = [r["name"] for r in cur.fetchall()]

    cur.execute("SELECT name FROM subcategories")
    subcategories = [r["name"] for r in cur.fetchall()]

    prompt = build_prompt(item, categories, subcategories)

    result = call_llm(prompt)

    data = json.loads(result)

    # Category reuse
    category = match_or_create(data["category"], categories)

    # Insert category if new
    cur.execute("INSERT INTO categories(name) VALUES(%s) ON CONFLICT DO NOTHING", (category,))
    conn.commit()

    # Get category_id
    cur.execute("SELECT id FROM categories WHERE name=%s", (category,))
    category_id = cur.fetchone()["id"]

    # Subcategory
    subcategory = match_or_create(data["subcategory"], subcategories)

    cur.execute("""
        INSERT INTO subcategories(name, category_id)
        VALUES(%s, %s)
        ON CONFLICT DO NOTHING
    """, (subcategory, category_id))
    conn.commit()

    cur.execute("SELECT id FROM subcategories WHERE name=%s", (subcategory,))
    subcategory_id = cur.fetchone()["id"]

    # Embedding
    text = data["activity"] + " " + data["description"]
    embedding = get_embedding(text)

    # Save activity
    cur.execute("""
        INSERT INTO activities
        (name, description, category_id, subcategory_id, tags, price, currency, embedding)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        data["activity"],
        data["description"],
        category_id,
        subcategory_id,
        data["tags"],
        data["price"],
        data["currency"],
        embedding
    ))

    conn.commit()
    conn.close()

    return data
