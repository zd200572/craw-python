# coding: gb18030
import requests
import re
import time

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') 
fout = open('book250.txt', 'w')

j = 1
re1 = re.compile(r'class="">\
                            <span class="title">.*?</span>')
re2 = re.compile(r'<span class="rating_num" property="v:average">.*?</span>')

for i in range(10):
	book_name = []
	book_info = []
	book_name1 = []
	book_info1 = []
	url = 'https://movie.douban.com/top250?start=%s&filter=' % (i*25)
	#print(url, '\n')
	#continue
	content = requests.get(url).text
	book_name = re1.findall(content)
	book_info = re2.findall(content)
	#print(book_name,'\n')
	#break

	for a in book_name:
		#print(a, '\n\n')
		#print(a.split('title="')[1].split('"\n')[0])
		book_name1.append(a.split('<span class="title">')[1].split('</span>')[0])
	#print(len(book_name1))
	#break
	for b in book_info:
		book_info1.append(b.split('>')[1].split('</s')[0])
		#print(b)

	for i in range(len(book_name1)):
		print(j,'\t',str(book_name1[i]) + '\t' + str(book_info1[i]))
		fout.write(str(j)+ '\t' + str(book_name1[i]) + '\t' + str(book_info1[i]) + '\n')
		#break
		j += 1
	#break
	time.sleep(30)
fout.close()