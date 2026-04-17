import os

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/tourism")
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "vck_4XdjNAYb8zE8y3DhfOunGq90FZICYDaoIo3lySIhVwewsCv5HN36bZr1")

settings = Settings()
