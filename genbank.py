import urllib, re
#抓取mRNA及蛋白质序列
def mRNA(id):
	url = 'http://www.ncbi.nlm.nih.gov/gene/%s' % id
	req = urllib.urlopen(url)
	f = req.read()
	req.close()
	results = re.findall('href = "nuccore/NG_008689.1?report=genbank&from=5001&to=14310"')