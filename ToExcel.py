# -*- coding:utf-8 -*-
import sql
import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')
import xlwt
import xlsxwriter

artList = sql.qry_content();

workbook = xlsxwriter.Workbook('./content2.xlsx')
# sheet = workbook.add_sheet('table_message',cell_overwrite_ok=True)
sheet = workbook.add_worksheet()
#excel 标题
titleList = [u'歌曲id',u'评论数',u'热评内容'] 
#数据库标题
titleListEn = ['music_id','comment','hotComment']
for i in range(0,len(titleList)):
	sheet.write(0,i,titleList[i])

# artList = artList[0:1]
row = 1
col = 0
for row in range(1,len(artList)+1):
	for col in range(0,len(titleList)):
		# print(artList[row-1][titleListEn[col]])
		sheet.write(row,col,u'%s'%artList[row-1][titleListEn[col]]);
		# sheet.write(row,col,u'%s'%'sss');
workbook.close()
# workbook.save(r'./album.xlsx');

















