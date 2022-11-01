import pymysql 

# conn = pymysql.connect(host='localhost', user='root', password='kh0103', db='developer', charset='utf8') 

db = pymysql.connect(host='localhost', user='root', password='kh0103', db='free_board', charset='utf8')
cur = db.cursor() 

sql = "SELECT * from board"
cur.execute(sql)

data_list = cur.fetchall()
