# -*- coding:utf-8 -*-

"""
    Created on 2017-09-17
    @Author : Bruce Lu
    @Desc : Analysis sku data
"""

import os
import json
import time
import itertools

s = os.sep
root = unicode("d:" + s + "桌面" + s + "爬虫" + s , 'utf-8')

keyList = []
checkList = []
dupList = []
finalKey = []
fileList =[]


# 判断字符串是否为json
def is_json(myjson):
    try:
        json.loads(myjson)
    except Exception as e:
        return False
    return True


def get_file(filepath):
    for path in os.listdir(filepath):
        file = os.path.join(filepath,path)
        if os.path.isdir(file):
            get_file(file)
        else:
            fileList.append(file)


# 验证数据使用,确定数据格式
# 获取对应json的key值
def get_keys(filepath):
    for path in filepath:
        fd = open(path).read()
        content = json.loads(fd)
        if content['result']['entityInfo'].has_key('safety'):
            for entity in content['result']['entityInfo']['safety']:
                keys = entity.keys()
                # if entity.has_key('useds'):
                #     for used in entity['useds']:
                #         keys = used.keys()
                keyList.append(keys)
        else:
            continue
        # print keys
    keyList.sort()
    kl = itertools.groupby(keyList)

    for k,g in kl:
        checkList.append(k)

    for key in checkList:
        for k in key:
            dupList.append(k)
    dupList.sort()

    dk = itertools.groupby(dupList)
    for k,g in dk:
        finalKey.append(k)


def get_checkkeys(checkList):
    if os.path.exists(os.path.join(root,'checkkeys.txt')):
        fd = open(os.path.join(root,'checkkeys.txt'),'w')
        for key in checkList:
            fd.write(''.join(key )+'\n')
        fd.close()
    else:
        fd = open(os.path.join(root, 'checkkeys.txt'), 'w')
        for key in checkList:
            fd.write(''.join(key)+'\n')
        fd.close()


get_file(os.path.join(root,'bevol-detial'+s))
get_keys(fileList)
print finalKey
get_checkkeys(finalKey)