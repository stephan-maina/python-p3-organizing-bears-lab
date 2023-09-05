#!/usr/bin/env python3

# conftest.py

import pytest
from your_module import create_tables, insert_data  # Import your functions for creating tables and inserting data

@pytest.fixture(autouse=True)
def setup_database(conn):
    create_tables(conn)
    insert_data(conn)
