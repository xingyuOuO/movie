import sqlite3

def connect_db():
    return sqlite3.connect("movies.db")

def create_table():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                director TEXT NOT NULL,
                genre TEXT NOT NULL,
                year INTEGER NOT NULL,
                rating REAL CHECK(rating >= 1.0 AND rating <= 10.0)
            )
        ''')
        conn.commit()

def add_movie(title, director, genre, year, rating):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO movies (title, director, genre, year, rating)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, director, genre, year, rating))
        conn.commit()

def list_movies():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM movies")
        return cursor.fetchall()

def update_movie(title, new_rating):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE movies
            SET rating = ?
            WHERE title = ?
        ''', (new_rating, title))
        conn.commit()

def delete_movie(title):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM movies
            WHERE title = ?
        ''', (title,))
        conn.commit()

# 使用範例
create_table()  # 建立表格
add_movie("Inception", "Christopher Nolan", "Sci-Fi", 2010, 8.8)  # 新增電影
add_movie("Interstellar", "Christopher Nolan", "Sci-Fi", 2014, 8.6)  # 新增電影

# 查詢並顯示所有電影
print("所有電影：")
for movie in list_movies():
    print(movie)

# 更新電影評分
update_movie("Inception", 9.0)

# 刪除電影
delete_movie("Interstellar")

# 查詢並顯示所有電影
print("更新後的電影清單：")
for movie in list_movies():
    print(movie)
