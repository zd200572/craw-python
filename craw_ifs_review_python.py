import requests
import re
import time

fout = open('ifs.csv', 'w')


for i in range(79, 1001):
	j_name = []
	ifs = []
	dict = {}
	url = 'http://www.letpub.com.cn/index.php?page=journalapp&fieldtag=&firstletter=&currentpage=%s' % i
	content = requests.get(url).text
	#print(content)
	re1 = re.compile(r'<a style="color:#0099FF; font-size:12px; font-weight:bold; .*?;" .*?&page=journalapp&view=detail" target="_blank">.*?</a><br><br>')
	re2 = re.compile(r'<td style="border:1px #DDD solid; border-collapse:collapse; text-align:left; padding:8px 8px 8px 8px;">\d+\.\d+</td>')
	#re3 = re.compile(r'')
	journal_name = re1.findall(content)

	
	for a in journal_name:
		name = a.split('</a>')[0].split('>')[1]
		j_name.append(name)
		dict[name] = ''
	iF = re2.findall(content)
	for a in iF:
		ifa = a.split('</td>')[0].split('>')[1]
		#if ifa != '0.000':
		ifs.append(ifa)
	print(ifs)

	j = 0
	print(len(dict))
	for c in dict.keys():
		#print(c)

		if j < len(dict):
			dict[c] = ifs[j]
			j += 1
		fout.write(str(c) + ',' + str(dict[c]) + '\n')
	time.sleep(6)
	#break
fout.close()



