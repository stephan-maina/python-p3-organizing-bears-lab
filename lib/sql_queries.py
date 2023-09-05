# test_setup.py

import pytest
import sqlite3

@pytest.fixture(scope="module")
def conn():
    conn = sqlite3.connect(":memory:")  # Create an in-memory SQLite database
    yield conn
    conn.close()


SELECT_OLDEST_BEAR_NAME_AND_AGE = """
    SELECT 
        name,
        age
    FROM bears
    ORDER BY age DESC
    LIMIT 1
"""

SELECT_YOUNGEST_BEAR_NAME_AND_AGE = """
    SELECT 
        name,
        age
    FROM bears
    ORDER BY age
    LIMIT 1
"""
