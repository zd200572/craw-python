#!/usr/bin/env python
# coding=utf-8
# Author: Xu Zhongtian
# Mail: 738502908@qq.com
# Created Time: Tue 15 Nov 2016 08:50:20 AM CST
# Filename: get_file.py
# Last modifed time: Thu Nov 17 10:04:49 2016


import requests
import re 
import os

url = "http://userweb.eng.gla.ac.uk/umer.ijaz/bioinformatics/"

filedir = os.getcwd()
fulldir = str(os.path.join(filedir,"bioinformatics")),#encoding='utf-8')
if not os.path.isdir(fulldir):
    os.makedirs(fulldir)
os.chdir(fulldir)

def get_html(url):
    html = requests.get(url).text
    items = re.findall(r'tr><td valign="top">.*?alt="\[(.*?)\]"></td><td><a href="(.*?)">',html)
    for item in items:
        if item[0] != "DIR":
            file_url = url + item[1]
            file = requests.get(file_url)
            fp = open(item[1],'wb')
            fp.write(file.content)
            fp.close()
        print("Handsome lord, %s has been downloaded" % item[1])

        if item[0] == "DIR":
            if item[1].startswith("/"):
                pass
            else:
                print("\tHandsome lord, We will change into %s" % item[1])
                son_url = url+item[1]
                filedir = os.getcwd()
                folder_name = str(item[1])
                fulldir = unicode(os.path.join(filedir,folder_name),encoding='utf-8')
                if not os.path.isdir(fulldir):
                    os.makedirs(fulldir)
                os.chdir(fulldir)
                get_html(son_url)
                os.chdir("../")
                print("\tHandsome load, we are leaving %s" % item[1])
get_html(url)