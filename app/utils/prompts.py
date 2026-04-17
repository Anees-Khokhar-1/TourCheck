def build_prompt(item, categories, subcategories):

    return f"""
You are a tourism AI system.

STRICT RULES:
- Reuse categories if possible
- Keep categories limited (max 10)
- Output ONLY JSON

Existing Categories:
{categories}

Existing Subcategories:
{subcategories}

Activity: {item['name']}
Description: {item['description']}
Price: {item['price']}
Currency: {item['currency']}

Return JSON:
{{
 "activity": "",
 "description": "",
 "category": "",
 "subcategory": "",
 "tags": [],
 "price": "",
 "currency": ""
}}
"""
