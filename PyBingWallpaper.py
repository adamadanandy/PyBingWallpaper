#! /usr/bin/python3

import win32gui
from urllib.request import urlopen, urlretrieve
from xml.dom import minidom
from PIL import Image
import os


#Variables:
saveDir = 'C:\BingWallPaper\\'
i = 0
while i<1:
    try:
        usock = urlopen('http://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=zh-CN')
    except:
        i = 0
    else:
        i = 1
xmldoc = minidom.parse(usock)
num = 1
#Parsing the XML File
for element in xmldoc.getElementsByTagName('url'):
    url = 'http://www.bing.com' + element.firstChild.nodeValue

    #Get Current Date as fileName for the downloaded Picture
    picPath = saveDir  + 'bingwallpaper' + '%d'%num + '.jpg'
    urlretrieve(url, picPath)
    #Convert Image
    picData = Image.open(picPath)
    picData.save(picPath.replace('jpg','bmp'))
    picPath = picPath.replace('jpg','bmp')
    num = num+1
#Set Wallpaper:
win32gui.SystemParametersInfo(0x0014, picPath, 1+2)
