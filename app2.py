# 서비스를 빨리 구현해야 하는 상황 -> flask

from flask import Flask, request, render_template
import sqlite3

# flask 가동
app = Flask(__name__)

# sqlite 연결 mysql, mongodb
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# db 만들기, 데이터베이스 테이블 생성
def create_table():
    print("DB 생성중 ...")
    conn = get_db_connection()
    cursor = conn.cursor() # 커서, 

    # 쿼리문 작성
    sql = f"CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)"
    cursor.execute(sql) # 쿼리문 실행
    conn.commit() # 쿼리 반영하기
    conn.close() # 닫아주기 


# add_book
def add_book(title, author):
    conn = get_db_connection()
    cursor = conn.cursor() # 커서
    title, author = str(title), str(author)
    sql = f"INSERT INTO books (title, author) VALUES ('{title}', '{author}')"
    print(sql)
    cursor.execute(sql) # 쿼리문 실행
    conn.commit()
    conn.close()
    

@app.route('/', methods = ['GET', 'POST'])
def main():
    create_table()
    if request.method == 'POST':
        print("유저로부터 POST 요청 받는 중 ...")
        title = request.form['title']
        author = request.form['author']
        add_book(title, author)

    return render_template('index.html') # render 그려주기 

if __name__ == "__main__":
    app.run()
