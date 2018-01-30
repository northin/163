# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from Crypto.Cipher import AES
import base64
import sql
import os
import sys
import time
reload(sys)
import pymysql.cursors
import threading

sys.setdefaultencoding('utf-8')
class Content(object):
	headers = {
		'Accept':'*/*',
		'Accept-Encoding':'gzip, deflate',
		'Accept-Language':'zh-CN,zh;q=0.9',
		'Connection':'keep-alive',
		'Content-Length':'486',
		'Content-Type':'application/x-www-form-urlencoded',
		'Cookie':'_ntes_nnid=754361b04b121e078dee797cdb30e0fd,1486026808627; _ntes_nuid=754361b04b121e078dee797cdb30e0fd; JSESSIONID-WYYY=yfqt9ofhY%5CIYNkXW71TqY5OtSZyjE%2FoswGgtl4dMv3Oa7%5CQ50T%2FVaee%2FMSsCifHE0TGtRMYhSPpr20i%5CRO%2BO%2B9pbbJnrUvGzkibhNqw3Tlgn%5Coil%2FrW7zFZZWSA3K9gD77MPSVH6fnv5hIT8ms70MNB3CxK5r3ecj3tFMlWFbFOZmGw%5C%3A1490677541180; _iuqxldmzr_=32; vjuids=c8ca7976.15a029d006a.0.51373751e63af8; vjlast=1486102528.1490172479.21; __gads=ID=a9eed5e3cae4d252:T=1486102537:S=ALNI_Mb5XX2vlkjsiU5cIy91-ToUDoFxIw; vinfo_n_f_l_n3=411a2def7f75a62e.1.1.1486349441669.1486349607905.1490173828142; P_INFO=m15527594439@163.com|1489375076|1|study|00&99|null&null&null#hub&420100#10#0#0|155439&1|study_client|15527594439@163.com; NTES_CMT_USER_INFO=84794134%7Cm155****4439%7Chttps%3A%2F%2Fsimg.ws.126.net%2Fe%2Fimg5.cache.netease.com%2Ftie%2Fimages%2Fyun%2Fphoto_default_62.png.39x39.100.jpg%7Cfalse%7CbTE1NTI3NTk0NDM5QDE2My5jb20%3D; usertrack=c+5+hljHgU0T1FDmA66MAg==; Province=027; City=027; _ga=GA1.2.1549851014.1489469781; __utma=94650624.1549851014.1489469781.1490664577.1490672820.8; __utmc=94650624; __utmz=94650624.1490661822.6.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; playerid=81568911; __utmb=94650624.23.10.1490672820',
		'Host':'music.163.com',
		'Origin':'http://music.163.com',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}
	params = {
	    'csrf_token': '50d552d668897e5c4971b975cd949c5d'
	}

	second_param = "010001" # 第二个参数
	# 第三个参数
	third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
	# 第四个参数
	forth_param = "0CoJUm6Qyw8W8jud"

	# 获取参数
	def get_params(self,page): # page为传入页数
		iv = "0102030405060708"
		first_key = self.forth_param
		second_key = 'cnNDageFIrjoh2XB'  # 是在网页上断点找的
		if(page == 1): # 如果为第一页
			first_param = '{"rid":"", "offset":"0", "total":"true", "limit":"20", "csrf_token":"50d552d668897e5c4971b975cd949c5d"}'
			h_encText = self.AES_encrypt(first_param, first_key, iv)
		else:
			offset = str((page-1)*20)
			first_param = '{"rid":"", "offset":"%s", "total":"%s", "limit":"20", "csrf_token":"50d552d668897e5c4971b975cd949c5d"}' %(offset,'false')
			h_encText = self.AES_encrypt(first_param, first_key, iv)
		h_encText = self.AES_encrypt(h_encText, second_key, iv)
		return h_encText

	# 获取 encSecKey
	def get_encSecKey(self):
		encSecKey = "595e8b880dc3156ecfc892dafb40a747a6a5ff55c4e98f585633502b3af53fb937e5ac00fb266d7408ca653b53392917cdcc255bcaad951bda6970ff1d65a6def21c49e9f60b54cba7ead21bc58f1b40242cd51a4f68f276a3c5f57e297eac1cc5eda1eb1b434c920e58bf6ff7233bb6f0b3d184e8d4509e22ebf2fa4aae259c"
		# encSecKey = '1a3816ff16ba51af0ac0de52531e7f0f147d0179d335fff888521ab66049f10283d5db9c06e888af2e0e1c193a349a9c2d77ed0c1a26f8332ab05203dba687abefd1d9b32f6eb505063f35958b83c062b0dc1d0d9d87112a3893b3b176819f58b6f46ffcfb20ba0d26bdf2b1a4752f822ced94d18f007de6ce97ed1ae811cd85'
		return encSecKey

	# 解密过程
	def AES_encrypt(self,text, key, iv):
		pad = 16 - len(text) % 16
		text = text + pad * chr(pad)
		encryptor = AES.new(key, AES.MODE_CBC, iv)
		encrypt_text = encryptor.encrypt(text)
		encrypt_text = base64.b64encode(encrypt_text)
		return encrypt_text


	proxies = {'http': 'http://122.193.14.102:80'}
	proxies1= {
		'http:':'http://121.232.147.15:9000',
	# 'https:':'https://144.255.48.197'
	}
	def getData(self,i):
		data = {
			"params": self.get_params(i),
			"encSecKey": self.get_encSecKey()
		} 
		# print(data)  
		return data 
	def save_content(self,music_id,i,flag):
		# print(data)
		# params = {'id': music_id}
		self.headers['Referer'] = 'http://music.163.com/song?id=' + str(music_id)
		# flag =True
		if flag:
			r = requests.post('http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + str(music_id),
		                      headers=self.headers, params=self.params, data=self.getData(i), proxies=self.proxies)
		else:
		    r = requests.post('http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + str(music_id),
		                      headers=self.headers, params=self.params, data=self.getData(i), proxies=self.proxies1)
		# print(r.content)
		# print(music_id)
		# print(r.json()["total"])
		return r.json()

if __name__ == '__main__':
	my_music = Content()
	# # # pymysql 链接不是线程安全的
	connection1 = pymysql.connect(host='localhost',
	                              user='root',
	                              password='root',
	                              db='163',
	                              charset='utf8mb4',
	                              cursorclass=pymysql.cursors.DictCursor)
	def save_comments():
		count = 827841
		for page in range(41394,103948):
			# print(page)
			try:
				#186016  晴天
				#531051217 等你下课
				#29019227 sugar
				#501133611 Look What You Made Me Do
				#436514312 成都
				comments = my_music.save_content('186016',page,True)
				# comments = my_music.save_content()
				print(count)
				if comments["total"] > 0 :
					
					for j in comments['comments']:
						# print j['content'].encode('gbk', 'ignore')
						# hotList.append(j["content"])
						sql.insert_with_you(count,j['time'],j["content"], j['likedCount'],connection1)
						count = count + 1
			except Exception as e:
				# 打印错误日志
				print("error:"+str(page) + ': ' + str(e))
				# print(str(e))
				time.sleep(5)
	# music_before = sql.get_before_music()
	# music_after = sql.get_after_music()

	

	save_comments()
	# connection2 = pymysql.connect(host='localhost',
	#                               user='root',
	#                               password='root',
	#                               db='163',
	#                               charset='utf8mb4',
	#                               cursorclass=pymysql.cursors.DictCursor)

	# t1 = threading.Thread(target=save_comments, args=(music_before, True, connection1))
	# t2 = threading.Thread(target=save_comments, args=(music_after, False, connection2))
	# t1.start()
	# t2.start()