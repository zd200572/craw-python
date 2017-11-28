# coding: gb18030
import io
import sys
import requests
import re
import time

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') 
fout = open('book250.txt', 'w')

j = 1
re1 = re.compile(r'<p class="pl">.*?</p>')
re2 = re.compile(r'; title=[\s\S]*?>[\s\S]*?</a>\n\n\n\n')

for i in range(10):
	book_name = []
	book_info = []
	book_name1 = []
	book_info1 = []
	url = 'https://book.douban.com/top250?start=%s' % (i*25)
	#print(url, '\n')
	#continue
	content = requests.get(url).text
	book_name = re2.findall(content)
	book_info = re1.findall(content)
	#print(book_name,'\n')
	

	for a in book_name:
		#print(a, '\n\n')
		#print(a.split('title="')[1].split('"\n')[0])
		book_name1.append(a.split('title="')[1].split('"\n')[0])
	#print(book_name1)
		#break
	for b in book_info:
		book_info1.append(b.split('>')[1].split('</p')[0])
		#print(b)

	for i in range(len(book_name1)):
		print(j,'\t',str(book_name1[i]) + '\t' + str(book_info1[i]))
		#fout.write(str(j)+ str(book_name1[i]) + '\t' + str(book_info1[i]) + '\n')
		#break
		j += 1
	#break
	time.sleep(30)
fout.close()