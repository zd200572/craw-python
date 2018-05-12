import requests
import os
import time
from bs4 import BeautifulSoup
import lxml
import re
import io
import sys
#import json
#sys.getdefaultencoding('utf8')  

#url = 'http://www.jmrgs.com/showinfo-121-65372-0.html#001'
#url1 = 'http://www.jmrgs.com/showinfo-116-616650-0.html'
fout = open('tongchuangjiaoqi.txt', 'w')
url_li = []

'''
content = requests.get(url).text
soup = BeautifulSoup(content,'lxml')
print(content)
'''
def get_chapter_url():
	with open('xiaoshuo.txt') as f:
		for line in f:
			url_li.append(line.strip().split('" title=')[0].split('<a href="')[-1])
		#print(url_li[:10])
	return url_li


def get_page_url(a,i):
    #print(a)
    if i == 0:
		url  = 'http://www.jmrgs.com' + a
    else:
		url = 'http://www.jmrgs.com' + a.split('0.html')[0] + '%s.html' % i
    #print(url)
    return url


def get_chapter_content(url_li):
    for a in url_li:
        flag = 1
        #print(a)
        i = 0
        while flag == 1 and i <=6:
            url = get_page_url(a,i)
            content = requests.get(url)
            #content.encoding = 'utf-8'
            soup = BeautifulSoup(content.text,'lxml')
            #print(soup)
            s = str(soup.select('div#view_content_txt'))
            s_c = s.encode('latin-1').decode('unicode_escape')
            #print(soup.select('div.view_page'))
            if soup.select('a#next'):
                flag = 0
                #print(soup.select('div.view_page'))
                print(s_c)
                time.sleep(2)
            else:
                i += 1
                print(s_c)
                time.sleep(2)
        #break
    

        #continue
        #break
        #time.sleep(6)
        #i += 1
    	#print(soup)
    	#print(soup.select('div#view_content_txt')) #
        #r1 = re.compile(r'')
        #con = r1.findall(content)
        #print(con)
        # break


    
url_li = get_chapter_url()
#url_li = ['/showinfo-116-616705-6.html']
get_chapter_content(url_li)
fout.close()

#[Finished in 2876.4s with exit code 1]