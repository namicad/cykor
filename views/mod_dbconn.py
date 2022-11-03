import pymysql 
import sqlite3

#\c root@localhost
#db = pymysql.connect(host='localhost', user='root', password='0000', db='free_board', charset='utf8')
db = sqlite3.connect("./cykor/views/cykor.db", isolation_level=None, check_same_thread=False)
cur = db.cursor() 

def board():
    sql = "SELECT * from board"
    cur.execute(sql)
    data_list = cur.fetchall()

    return data_list


def board_size():
    sql = "SELECT COUNT(0) FROM board"
    cur.execute(sql)
    size = cur.fetchone()

    return size[0]

def board_post(set):
    sql = "INSERT INTO board (title, writer, content) VALUES (?, ?, ?)"
    cur.execute(sql, set)

    return 1

def check_id(set):
    sql = "select * from account where id=?"
    cur.execute(sql,(set[0],))
    if cur.fetchall():
        sql = "select * from account where id=? and pw=?"
        cur.execute(sql, set)

        if cur.fetchall():
            return 2
    
        else :
            return 1

    return 0

def reg(set):
    sql = "INSERT INTO account (id, pw) VALUES (?, ?)"
    cur.execute(sql, set)

    return 1


def board_edit(af_set, be_set):
    sql = "UPDATE board SET title = ?, content = ? WHERE title=? and writer=? and content=?"
    cur.execute(sql, af_set + be_set)

    return 1

def board_delete(set):
    sql = "DELETE from board where title=? and writer=? and content=?"
    cur.execute(sql, set)
    
    return 1