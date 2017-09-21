# create the sqlite3 database and populate it with basic database

## load libraries
import sqlite3

# create new database
with sqlite3.connect("blog.db") as connection:

    # establish a cursor
    c = connection.cursor()

    # create the table, drop if it already exists
    c.execute('DROP TABLE IF EXISTS posts')
    c.execute('CREATE TABLE posts (title text, post text)')

    # insert dummy records
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
    c.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
    c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')
