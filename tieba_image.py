#-*- coding:utf-8 -*-

from urllib import request
from os import mkdir,chdir
from re import compile,findall

def tieba_image(site,directory):
    """site为贴吧网址，directory为创建目录，两个参数都是字符串"""
    try:
        mkdir('%s' %directory)
        chdir('%s' %directory)
        page = request.urlopen(site)
    except FileExistsError:
        return '该目录已存在'
    except ValueError:
        return "网址格式应为： 'http://xxxx.xxx.xxx'"
    file = str(page.read(),encoding='utf-8')
    page.close()
    pat = compile(r'http://imgsrc.baidu.com/forum/w%3D580/sign=.+?\.jpg')
    lst = findall(pat,file)
    prefix = 'http://imgsrc.baidu.com/forum/pic/item/'
    lst = [prefix + x.split('/')[-1] for x in lst]
    count = 1
    for x in lst:
        request.urlretrieve(x,'%s_%s.jpg' %(directory,count))
        count += 1
