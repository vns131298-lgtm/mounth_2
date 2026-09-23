# SQL - structured query language
# data - данные
#SQLite, PostgreSQL, MSSQL
import sqlite3

def create_table(connection):
    connection.execute("""
    CREATE TABLE IF NOT EXISTS books (
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    """)

def insert_books(connection, name, author, publication_year, genre, number_of_pages, number_of_copies):
    connection.execute("""
    INSERT INTO books (name,
        author,
        publication_year,
        genre,
        number_of_pages,
        number_of_copies
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, author, publication_year, genre, number_of_pages, number_of_copies))

if __name__ == "__main__":
    connection = sqlite3.connect("database.db")
    create_table(connection)

    insert_books(
        connection,
        "1984",
        "Джордж Оруэлл",
        1949,
        "Антиутопия",
        328,
        5
    )

    insert_books(
        connection,
        "Шантарам",
        "Грегори Дэвид Робертс",
        2003,
        "Приключенческий роман",
        936,
        7
    )

    insert_books(
        connection,
        "Тень горы",
        "Грегори Дэвид Робертс",
        2016,
        "Приключенческий роман",
        830,
        6
    )

    insert_books(
        connection,
        "Я - четвертый",
        "Питтакус Лор",
        2014,
        "Научная фантастика",
        416,
        6
    )

    insert_books(
        connection,
        "Мистер Мерседес",
        "Стивен Кинг",
        2014,
        "Триллер",
        437,
        8
    )

    insert_books(
        connection,
        "Сталкер - В зоне тумана",
        "Алексей Гравицкий",
        2009,
        "Боевая фантастика",
        384,
        5
    )

    insert_books(
        connection,
        "Тьма, - и больше ничего",
        "Стивен Кинг",
        2010,
        "Ужасы",
        448,
        9
    )

    insert_books(
        connection,
        "Искусство войны",
        "Сунь-цзы",
        2017,
        "Военная стратегия",
        192,
        6
    )

    insert_books(
        connection,
        "Сила вашего подсознания",
        "Джозеф Мерфи",
        2015,
        "Психология",
        352,
        4
    )

    insert_books(
        connection,
        "Кладбище домашних животных",
        "Стивен Кинг",
        2019,
        "Ужасы",
        480,
        8
    )

    connection.commit()

