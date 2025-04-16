# Handles PostgreSQL database connection
import psycopg2
from psycopg2.extras import RealDictCursor


def connect_to_postgres():
    """Establishes a connection to PostgreSQL database."""
    return psycopg2.connect(
        host="18.224.56.248",
        database="dvdrental",
        user="postgres",
        password="postgres",
        cursor_factory=RealDictCursor
    )
