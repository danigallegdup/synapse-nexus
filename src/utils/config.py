import os

class Config:
    KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/db")
