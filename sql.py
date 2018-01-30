# -*- coding:utf-8 -*-

import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='163',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)



# 保存歌手
def insert_artist(artist_id, artist_name,cat_id):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `artist1` (`name`, `artist_id`, `cat_id`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (artist_name, artist_id, cat_id))
    connection.commit()

#保存专辑
def insert_album(album_id,artist_id):
    with connection.cursor() as cursor:
        # 执行sql语句，插入记录
        sql = 'INSERT INTO album1 (album_id, singer_id) VALUES (%s, %s)'
        cursor.execute(sql, (album_id,artist_id));
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()


#保存歌曲
def insert_music(music_name,album_id,music_id):
    with connection.cursor() as cursor:
        # 执行sql语句，插入记录
        sql = 'INSERT INTO music2 (music_name,album_id,music_id) VALUES (%s, %s, %s)'
        cursor.execute(sql, (music_name,album_id,music_id));
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()

#保存歌曲信息
def insert_music(music_id,comment,hotComment,connection0):
    with connection0.cursor() as cursor:
        # 执行sql语句，插入记录
        sql = 'INSERT INTO content1 (music_id,comment,hotComment) VALUES (%s, %s, %s)'
        cursor.execute(sql, (music_id,comment,hotComment));
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection0.commit()


#保存等你下课的歌曲信息
def insert_with_you(count,date,content,zan,connection0):
    with connection0.cursor() as cursor:
        # 执行sql语句，插入记录
        sql = 'INSERT INTO qingtian (count,date,content,zan) VALUES (%s, %s, %s, %s)'
        cursor.execute(sql, (count,date,content,zan));
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection0.commit()

#获取歌手
def qry_artists():
    with connection.cursor() as cursor:
    # 执行sql语句，进行查询,以去除重复
        #爬数据用
        # sql = 'SELECT href FROM singers1 ORDER BY href' 
        #导出excel用
        sql = 'SELECT distinct * FROM artist1 ORDER BY artist_id' 
        #中间断了服务
        # sql = "SELECT href FROM singers1 WHERE href > '127296'  ORDER BY href "
        # sql = "SELECT href FROM singers1 WHERE href > '127289'  ORDER BY href "
        cursor.execute(sql, ())
        # 获取查询结果
        result = cursor.fetchall()
        # print(result)
        return result

#获取歌手专辑
def qry_album():
	with connection.cursor() as cursor:
	# 执行sql语句，进行查询,以去除重复
		# sql = 'SELECT href FROM singers1 ORDER BY href' 
        # sql = "SELECT album_id FROM album1 ORDER BY album_id "
		sql = "SELECT distinct * FROM album1 ORDER BY album_id "
		# sql = "SELECT href FROM singers1 WHERE href > '127289'  ORDER BY href "
		cursor.execute(sql, ())
		# 获取查询结果
		result = cursor.fetchall()
		# print(result)
		return result

#获取歌曲
def qry_music():
	with connection.cursor() as cursor:
	# 执行sql语句，进行查询,以去除重复
		# sql = 'SELECT href FROM singers1 ORDER BY href' 
        # sql = "SELECT distinct * FROM music2 ORDER BY music_id limit 900000"
		sql = "SELECT distinct * FROM music2 where music_id > '469508814' ORDER BY music_id"
		cursor.execute(sql, ())
		# 获取查询结果
		result = cursor.fetchall()
		# print(result)
		return result
#获取评论
def qry_content():
    with connection.cursor() as cursor:
    # 执行sql语句，进行查询,以去除重复
        # sql = 'SELECT href FROM singers1 ORDER BY href' 
        sql = "SELECT distinct * FROM content1 where music_id > '31260161' ORDER BY music_id "
        # sql = "SELECT href FROM singers1 WHERE href > '127289'  ORDER BY href "
        cursor.execute(sql, ())
        # 获取查询结果
        result = cursor.fetchall()
        # print(result)
        return result

# 获取前一半音乐的 ID
def get_before_music():
    with connection.cursor() as cursor:
        sql = "SELECT `music_id` FROM `music2` where music_id <= '360001' and music_id > '28283187' ORDER BY music_id "
        cursor.execute(sql, ())
        return cursor.fetchall()


# 获取后一半音乐的 ID
def get_after_music():
    with connection.cursor() as cursor:
        sql = "SELECT `music_id` FROM `music2` where music_id <'6' and music_id > '427595864' ORDER BY music_id"
        cursor.execute(sql, ())
        return cursor.fetchall()



def dis_connect():
    connection.close()