# sql_queries.py

SELECT_ALL_FEMALE_BEARS = """
    SELECT
       name,
       age
    FROM bears
    WHERE sex='F'
"""

SELECT_ALL_BEAR_NAMES_ALPHABETICAL = """
    SELECT 
        name
    FROM bears
    ORDER BY name
"""

SELECT_ALL_ALIVE_BEAR_NAMES_AND_AGES_YOUNGEST_TO_OLDEST = """
    SELECT 
       name,
       age
    FROM bears
    WHERE alive=1
    ORDER BY age
"""

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
