import requests
import os
import time
from bs4 import BeautifulSoup
import lxml
import re

i = 1
fout = open('gene.txt', 'w')
fout.write('GeneID	基因名称或注释	基因符号	RAP_Locus	MSU_Locus	cDNAs	RefSeq_Locus	Uniprots' + '\n')
dic = {}

def get_page_content(i):
	url = 'http://www.ricedata.cn/gene/accessions_switch.aspx?p=%s&located=true' % i #第1到2888页
	content = requests.get(url).text
	soup = BeautifulSoup(content,'lxml')
	items = soup.select('a') ##
	return items


def get_each_item(items):
	for item in items:
		item1 = str(item).split('>')[1].split('</')[0]
		if 'accessions_switch.aspx?p=' not in str(item):
			if item1.isdigit():
				GeneID = item1
				urls = []
				dic[GeneID] = ''
			elif item1 != '':
				if 'http' in str(item):
					urls.append(str(item).split('http')[1].split('">')[0]) 
			else:
				urls.append('') 
		else:
			continue
		dic[GeneID] = urls
	for a in dic.keys():
		fout.write(str(a) + '\t' + str(dic[a]) + '\n')
		#break
		#print(dic)
		#break
			
	return dic

items = get_page_content(i)
dic = get_each_item(items)
fout.close()