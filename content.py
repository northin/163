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
	    'csrf_token': ''
	}

	data = {
	    'params': 'izQBiZ/cU/C1Gz1O8aFZKtDTVCg5+JSytwG4JXN+3AGn9zxhgMeNcdb58dc3PmwJ',
	    'encSecKey': '8a1a4ad84083e59b8dc6ece0f0e783a17f19c92fcdfcf451985b795ebc7be21ba00d740217e3f1336b98464b56ba601a091fd6902fe371aa55319d8c41bf23bf874bfb91b1c697796f5ee1075cfa4ab73e653716299cde421b7edd528b318e511acd223709c3e847aa392aad25a63d5a025a0c2d468de289436f379d419e74ec'
	}
	# data1 = {
	# 	# 'params': 'Ak2s0LoP1GRJYqE3XxJUZVYK9uPEXSTttmAS+8uVLnYRoUt/Xgqdrt/13nr6OYhi75QSTlQ9FcZaWElIwE+oz9qXAu87t2DHj6Auu+2yBJDr+arG+irBbjIvKJGfjgBac+kSm2ePwf4rfuHSKVgQu1cYMdqFVnB+ojBsWopHcexbvLylDIMPulPljAWK6MR8',
	# 	# 'encSecKey': '8c85d1b6f53bfebaf5258d171f3526c06980cbcaf490d759eac82145ee27198297c152dd95e7ea0f08cfb7281588cdab305946e01b9d84f0b49700f9c2eb6eeced8624b16ce378bccd24341b1b5ad3d84ebd707dbbd18a4f01c2a007cd47de32f28ca395c9715afa134ed9ee321caa7f28ec82b94307d75144f6b5b134a9ce1a'
	# 	# 'params': 'FVvQYF/HYOdZIgMw/Ynia1yuIDp3NRa6RZfeNygvFSk5Suh4xIUqKKI+eZdg18TfHEu5OEXHuusspTXBAPqmKkkZLVrwKhDeuMCGL6fgQUFX8fzRJNhY4mm6p0h0ox1np1boJqCgPX5hCeLDz5OHp8Xg83Ro38Ds7Ezl+pSm22P5HiJbZ/WLsGHA5UcZM/e1',
	# 	# 'encSecKey': '2fbc994cd62474cdc955612ca446a198574481b0ec45dd4cf8d71b357a6a01805677711c773ef74c16dbac02f8db5520022eec1cfef0510ea161a4baa5605e5d2a47546cace614ebde932f8f936a498736cad0706c58e9d828c487fc3d4f18e12e3d058d00a84f8b84e7a5ba2f0529d441849d7d9bc95532af0befbe3e10c655'
	# 	# 'params':'mzFWZOFM3+sPn9dlBiOPAS06RPTtYF4BhCcQhxCjChobGBgjNOMhkCb58EvSsBSDa4GxC2E2ZYHPu64hcoKFA1YIPzebuBUjtPpZz6vzZI5coVHRp61N61uCVxmx7Hok8S38LLelkEp9DC39qMi6aALtj865FE972Gq2OoHMUijIwjzj1gCdhjST4MEwS63l',
	# 	# 'encSecKey':'7a18c3c3878480c76687db9438ac93b5385a8542decb08c44bb70c23d46e173b0971821d1e55c3dc89d51e0af56c12f07cccdacb3f3f94ca6e9c0b54fd45d9ec25952740c19c891cc4e2f27f8400b3d9b0c878f3cdc80b5842df9a76406620464863211a7c592bc5badc4b6cb42f0253f28913e89ed06f7a9912c3b88e2e3ec5'
	# 	'params':'0iXjVuFCIA2GP+CyLUigN/pgR9HOryjo1wLHuZ6BBeylAeGoyEigaQcjqxk//fTxBN3PjqJNCJiqGPgGHnBa7RtXAt3N15/rh2b1KBSSWtR+OtP1l6IXLixfQPbMqkKxAXRzyS2hSH6e1J2AB3pB3BiF1zhU/zjxGDTa4Suy3cyydCOMbf9c7Kw5PovF+++p',
	# 	'encSecKey':'644d81ad373fe003a7db09e1f2c1338deebad695b90d2c8ed935cb32a486637d9e202b715994c5e8397acc57c57796779eef91ff4234a8f8b8ab35984ad8f95f2b990247d9d7276a92b829758a6c3c3289eaaa544d8554a1fd98a9d110d5a3274f6c73b9b4d9d5721cba6ae8499fc782c24362359c505bdc615ac716fbc06cd6'
	# }


	second_param = "010001" # 第二个参数
	# 第三个参数
	third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
	# 第四个参数
	forth_param = "0CoJUm6Qyw8W8jud"

	# 获取参数
	def get_params(self,page): # page为传入页数
		iv = "0102030405060708"
		first_key = self.forth_param
		second_key = 16 * 'F'
		if(page == 1): # 如果为第一页
			first_param = '{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}'
			h_encText = self.AES_encrypt(first_param, first_key, iv)
		else:
			offset = str((page-1)*20)
			first_param = '{rid:"", offset:"%s", total:"%s", limit:"20", csrf_token:""}' %(offset,'false')
			h_encText = self.AES_encrypt(first_param, first_key, iv)
		h_encText = self.AES_encrypt(h_encText, second_key, iv)
		return h_encText

	# 获取 encSecKey
	def get_encSecKey(self):
		encSecKey = "174c244eae0cd5fa3bc79d588a2b8d60b3830f468c3972bb99a1c3586e4aa2394ba71e7d123f597d9e41fb7745951367ab91788bf54986cc12f15a899d63ee66595c0cbfc2e22480d92a88906b32a35e046e901d79a659a198adf46981fc05191d24060a8f9220bfc1e1e454b0eac863fb0e80e1545d6f3b701038d589eca4af"
		return encSecKey

	# 解密过程
	def AES_encrypt(self,text, key, iv):
		pad = 16 - len(text) % 16
		text = text + pad * chr(pad)
		encryptor = AES.new(key, AES.MODE_CBC, iv)
		encrypt_text = encryptor.encrypt(text)
		encrypt_text = base64.b64encode(encrypt_text)
		return encrypt_text

	

	#歌词
	data2 = {
		'params':'M5wb4wofFGx31OKa1ZtoF2Szx4YnnJLrn2Ash/CEVorNRevW+x3eGUaTAC6RjX5pbi5XrZ+8+bEUETN16ZTYgYWFxsA/TRHouD0lrtKzXQv2I137g0EIWni2gGBTZEKS',
		'encSecKey':'829afd68bdc46e1e42c918248b7abc30033cdb7e59d30bd90e98abaa556e386e8cd8982eca48be240727f3c7d1b23f167b571b60c36af767108188c3541f801bc00a02edd2f26a1058609a8ea92ad056134b5b0bea8b74dfecc948f84bade1c65320c6a2daa23134ed369ac7513e0f0241473cb9a15979ffcbbed9d0de8c97cc'
	}

	proxies = {'http': 'http://122.193.14.102:80'}
	proxies1= {
		'http:':'http://121.232.147.15:9000',
	# 'https:':'https://144.255.48.197'
	}
	    
	def save_content(self,music_id,flag):
		# encSecKey = self.get_encSecKey();
		# params = self.get_params(1)
		# data = {
		# 	"params": params,
		# 	"encSecKey": encSecKey
		# }
		# print(data)
		# params = {'id': music_id}
		self.headers['Referer'] = 'http://music.163.com/song?id=' + str(music_id)
		# flag =True
		if flag:
			r = requests.post('http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + str(music_id),
		                      headers=self.headers, params=self.params, data=self.data, proxies=self.proxies)
		else:
		    r = requests.post('http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + str(music_id),
		                      headers=self.headers, params=self.params, data=self.data, proxies=self.proxies1)
		# print(r.json())
		print(music_id)
		# print(r.json()["total"])
		return r.json()

if __name__ == '__main__':
	my_music = Content()
	def save_comments(musics, flag, connection0):
		for i in musics:
			try:
				comments = my_music.save_content(i["music_id"],flag)
				# comments = my_music.save_content()
				# print(comments)
				if comments["total"] > 0 :
					hotList = []
					for j in comments['hotComments']:
						hotList.append(j["content"])
					sql.insert_music(i["music_id"], comments['total'], ':'.join(hotList), connection0)

			except Exception as e:
				# 打印错误日志
				print("error:"+str(i) + ': ' + str(e))
				# print(str(e))
				time.sleep(5)
	# music_before = sql.get_before_music()
	# music_after = sql.get_after_music()

	# # # pymysql 链接不是线程安全的
	connection1 = pymysql.connect(host='localhost',
	                              user='root',
	                              password='root',
	                              db='163',
	                              charset='utf8mb4',
	                              cursorclass=pymysql.cursors.DictCursor)

	save_comments([{'music_id':531051217}],True,connection1)
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