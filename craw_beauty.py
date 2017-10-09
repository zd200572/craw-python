import re
import urllib.request
def gethtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

html = gethtml('http://www.ivrfans.cn/xingge/qingchun')

def getarea(html):
    reg = r'<div class="animalPhoto afterAnimalPhoto clear">([\d\D]*)<div class="page">'
    areare = str(re.compile(reg))
    area = re.search(areare, str(html))
    return area.group()

#print getarea(html)


def getimg(getarea):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist
print(getimg(getarea(html)))

x=0
for imgurl in getimg(getarea(html)):
    urllib.urlretrieve(imgurl, '%s.jpg' % x)
    x +=1
