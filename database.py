import os
import json
import sqlite3

# Delete Database if exists:
if os.path.exists("./users.db"):
    os.remove("./users.db")

# Create Table:
with sqlite3.connect(database="./users.db") as conn:
    cursor = conn.cursor()
    command = """
    CREATE TABLE USERS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        email EMAIL,
        dob DATE
    );
    """
    cursor.execute(command)
    conn.commit()


# Make Entries:
with sqlite3.connect(database="./users.db") as conn:
    cursor = conn.cursor()
    command = """
    INSERT INTO USERS (first_name, last_name, email, dob) VALUES
        ('Bhushan', 'Songire', 'bhushan_songire@gmail.com', '2004-01-01'),
        ('Vikram', 'Sharma', 'vikram.sharma@hotmail.com', '1992-06-15'),
        ('Priya', 'Patel', 'priya.patel@outlook.com', '1995-03-22'),
        ('Arjun', 'Gupta', 'arjun_gupta@yahoo.com', '1988-11-30'),
        ('Divya', 'Agarwal', 'divya.agarwal@protonmail.com', '1997-09-18'),
        ('Rahul', 'Singh', 'rahul.singh@zoho.com', '1994-04-05'),
        ('Anjali', 'Mishra', 'anjali_mishra@rediffmail.com', '1990-12-27'),
        ('Karan', 'Desai', 'karan.desai@gmail.com', '1993-08-10'),
        ('Neha', 'Joshi', 'neha.joshi@icloud.com', '1996-02-14'),
        ('Amit', 'Verma', 'amit_verma@outlook.in', '1991-07-23');
    """
    cursor.execute(command)
    conn.commit()


# Fetch and print all entries:
with sqlite3.connect(database="./users.db") as conn:
    cursor = conn.cursor()
    command = "SELECT * FROM USERS;"
    cursor.execute(command)
    entries = cursor.fetchall()

    users = {}
    for entry in entries:
        users[entry[0]] = {
            "first_name": entry[1],
            "last_name": entry[2],
            "email": entry[3],
            "dob": entry[4]
        }

    print("All entries in USERS table:")
    print(json.dumps(users, indent=4))
