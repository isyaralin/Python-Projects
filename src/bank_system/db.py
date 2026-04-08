import sqlite3

DB_NAME = "bank.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        address TEXT,
        phone TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_customer(cid, name, address, phone):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO customers VALUES (?, ?, ?, ?)",
                    (cid, name, address, phone))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()


def get_all_customers():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM customers")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_customer(cid):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM customers WHERE id=?", (cid,))
    conn.commit()
    conn.close()


def update_customer(cid, name, address, phone):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE customers
        SET name=?, address=?, phone=?
        WHERE id=?
    """, (name, address, phone, cid))

    conn.commit()
    conn.close()


def search_customer(cid):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM customers WHERE id=?", (cid,))
    row = cur.fetchone()
    conn.close()
    return row
