#!/usr/bin/env python3

# select_test.py

import sqlite3
import pytest
from your_module import select_functions  # Import your functions for selecting data

def test_select_all_female_bears(conn):
    # Test the SELECT query for female bears
    female_bears = select_functions.SELECT_ALL_FEMALE_BEARS
    cursor = conn.cursor()
    cursor.execute(female_bears)
    results = cursor.fetchall()
    
    # Assuming results contain name and age columns
    assert len(results) == 1  # Assuming only one female bear in your sample data

def test_select_bears_older_than_five_years(conn):
    # Test the SELECT query for bears older than five years
    older_bears = select_functions.SELECT_BEARS_OLDER_THAN_FIVE_YEARS
    cursor = conn.cursor()
    cursor.execute(older_bears)
    results = cursor.fetchall()
    
    # Assuming results contain name and age columns
    # Add your assertions for this query, e.g., assert len(results) == expected_count

def test_select_alive_bears_ordered_by_name(conn):
    # Test the SELECT query for alive bears ordered by name
    alive_bears = select_functions.SELECT_ALIVE_BEARS_ORDERED_BY_NAME
    cursor = conn.cursor()
    cursor.execute(alive_bears)
    results = cursor.fetchall()
    
    # Assuming results contain name and age columns
    # Add your assertions for this query, e.g., assert results[0][0] == 'Bear1'


