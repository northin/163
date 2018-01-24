# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sql
import os
import sys
import time
reload(sys)

sys.setdefaultencoding('utf-8')
class Music(object):
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	    'Accept-Encoding': 'gzip, deflate, sdch',
	    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
	    'Cache-Control': 'no-cache',
	    'Connection': 'keep-alive',
	    'Cookie': '_ntes_nnid=7eced19b27ffae35dad3f8f2bf5885cd,1476521011210; _ntes_nuid=7eced19b27ffae35dad3f8f2bf5885cd; usertrack=c+5+hlgB7TgnsAmACnXtAg==; Province=025; City=025; NTES_PASSPORT=6n9ihXhbWKPi8yAqG.i2kETSCRa.ug06Txh8EMrrRsliVQXFV_orx5HffqhQjuGHkNQrLOIRLLotGohL9s10wcYSPiQfI2wiPacKlJ3nYAXgM; P_INFO=hourui93@163.com|1476523293|1|study|11&12|jis&1476511733&mail163#jis&320100#10#0#0|151889&0|g37_client_check&mailsettings&mail163&study&blog|hourui93@163.com; NTES_SESS=Fa2uk.YZsGoj59AgD6tRjTXGaJ8_1_4YvGfXUkS7C1NwtMe.tG1Vzr255TXM6yj2mKqTZzqFtoEKQrgewi9ZK60ylIqq5puaG6QIaNQ7EK5MTcRgHLOhqttDHfaI_vsBzB4bibfamzx1.fhlpqZh_FcnXUYQFw5F5KIBUmGJg7xdasvGf_EgfICWV; S_INFO=1476597594|1|0&80##|hourui93; NETEASE_AUTH_SOURCE=space; NETEASE_AUTH_USERNAME=hourui93; _ga=GA1.2.1405085820.1476521280; JSESSIONID-WYYY=cbd082d2ce2cffbcd5c085d8bf565a95aee3173ddbbb00bfa270950f93f1d8bb4cb55a56a4049fa8c828373f630c78f4a43d6c3d252c4c44f44b098a9434a7d8fc110670a6e1e9af992c78092936b1e19351435ecff76a181993780035547fa5241a5afb96e8c665182d0d5b911663281967d675ff2658015887a94b3ee1575fa1956a5a%3A1476607977016; _iuqxldmzr_=25; __utma=94650624.1038096298.1476521011.1476595468.1476606177.8; __utmb=94650624.20.10.1476606177; __utmc=94650624; __utmz=94650624.1476521011.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
	    'DNT': '1',
	    'Host': 'music.163.com',
	    'Pragma': 'no-cache',
	    'Referer': 'http://music.163.com/',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
	}

	def writeFile(self,filename,data):
	    file= open(filename,'wb')
	    file.write(data)
	    file.close()
	    print 'File had been writed Succed!'

	def save_music(self,album_id):
		params = {'id': album_id}
		r = requests.get('http://music.163.com/album', headers=self.headers, params=params)

		r.encoding = 'utf-8'
		# self.writeFile(r"./music.txt", r.content)
		# print(r.text[200:30000])
		soup = BeautifulSoup(r.content, 'html.parser')
		body = soup.body

		all_music = body.find('ul', attrs={'class': 'f-hide'}).find_all('a')

		# i["href"] = '/album?id=none'

		for i in all_music: 
			music_id = i["href"].replace('/song?id=', '').strip()
			music_name = i.string
			# name = i.string
			print(music_id,album_id,music_name)

			sql.insert_music(music_name,album_id,music_id)

if __name__ == '__main__':
	my_music = Music()
	albumList = sql.qry_album()
	for i in albumList:
		try:
			my_music.save_music(i["album_id"])
			# my_music.save_music(30938)
			# print(i)
		except Exception as e:
			# 打印错误日志
			print(str(i) + ': ' + str(e))
			# print(str(e))
			time.sleep(5)
		
