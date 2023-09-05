# insert_test.py

import sqlite3
import pytest
from your_module import insert_data

def test_insert_data(conn):
    # Ensure that data insertion works as expected
    insert_data(conn)

    # Verify that the data has been inserted correctly by selecting and checking it
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM bears")
    count = cursor.fetchone()[0]
    assert count == 3  # Assuming 3 rows were inserted

    # Additional tests related to data insertion can be added here

def test_insert_duplicate_data(conn):
    # Test inserting duplicate data
    with pytest.raises(sqlite3.IntegrityError):
        # Attempt to insert a bear with the same name (assuming 'name' should be unique)
        conn.execute("INSERT INTO bears (name, age, sex, alive) VALUES (?, ?, ?, ?)", ('Bear1', 5, 'M', 1))

    # Verify that the original data is still intact
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM bears")
    count = cursor.fetchone()[0]
    assert count == 3


