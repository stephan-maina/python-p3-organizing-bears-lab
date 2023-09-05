# test_setup.py

import pytest
import sqlite3

@pytest.fixture(scope="module")
def conn():
    conn = sqlite3.connect(":memory:")  # Create an in-memory SQLite database
    yield conn
    conn.close()
