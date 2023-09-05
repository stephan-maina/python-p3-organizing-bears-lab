import sqlite3
import pytest
from your_module import create_tables

def test_create_tables(conn):
    # Ensure that the tables are created successfully
    create_tables(conn)

    # Verify that the 'bears' table exists
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='bears';")
    table_exists = cursor.fetchone()
    assert table_exists is not None

    # Additional tests related to the schema can be added here

def test_create_duplicate_tables(conn):
    # Test creating the same tables again
    with pytest.raises(sqlite3.OperationalError):
        create_tables(conn)

    # Verify that the original schema is still intact
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='bears';")
    table_exists = cursor.fetchone()
    assert table_exists is not None


