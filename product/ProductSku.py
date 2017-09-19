# -*- coding:utf-8 -*-

"""
    Created on 2017-09-17
    @Author : Bruce Lu
    @Desc : Analysis sku data
"""

import os
import json
import itertools
import time
import MysqlConn

resultList = []
sortList =[]
fileList = []


def get_file(filepath):
    for path in os.listdir(filepath):
        file = os.path.join(filepath,path)
        if os.path.isdir(file):
            get_file(file)
        else:
            # print file
            fileList.append(file)
    return fileList


# 获取json对应字段值，并存到list列表
def get_entity(pathList):
    for path in pathList:
        fd = open(path).read()
        content = json.loads(fd)
        entity = content['result']['entity']
        # 使用get方法获取值，可以设置默认替换值，不需要判断key是否存在
        # print entity.get('commentAvgScore', None)
        # keyList.append(entity.keys())
        resultList.append((entity.get('id',None),entity.get('hidden',None),entity.get('updateStamp',None),entity.get('createStamp',None),
                           entity.get('likeNum',None),entity.get('notLikeNum',None),entity.get('collectionNum',None),entity.get('commentNum',None),
                           entity.get('commentContentNum',None),entity.get('allCommentNum',None),entity.get('commentSumScore',None),entity.get('hitNum',None),
                           entity.get('title',None),entity.get('alias',None),entity.get('image',None),entity.get('mid',None),entity.get('vistTime',None),
                           entity.get('radio',None),entity.get('grade',None),entity.get('safety_1_num',None),entity.get('csort',None),
                           entity.get('commentAvgScore',None),entity.get('allowComment',None)))
    return resultList


def get_goods(pathList):
    for path in pathList:
        fd = open(path).read()
        content = json.loads(fd)
        entity = content['result']['entityInfo']['goods']
        resultList.append((entity.get('id', None),
                           entity.get('alias', None),
                           entity.get('approval', None),
                           entity.get('approvalDate', None),
                           entity.get('capacity', None),
                           entity.get('category', None),
                           entity.get('company', None),
                           entity.get('companyEnglish', None),
                           entity.get('country', None),
                           entity.get('cps', None),
                           entity.get('cpsType', None),
                           entity.get('createStamp', None),
                           entity.get('dataType', None),
                           entity.get('dataTypeStr', None),
                           entity.get('image', None),
                           entity.get('imageSrc', None),
                           entity.get('mid', None),
                           entity.get('price', None),
                           entity.get('remark', None),
                           entity.get('sellCapacity', None),
                           entity.get('sellPrice', None),
                           entity.get('title', None),
                           entity.get('updateStamp', None)
                           ))
    return resultList


def get_doyen(pathList):
    for path in pathList:
        fd = open(path).read()
        content = json.loads(fd)
        if content['result']['entityInfo']['goods'].has_key('doyen'):
            entity = content['result']['entityInfo']['goods']['doyen']
            resultList.append((entity.get('id', None),
                               entity.get('doyenComment', None),
                               entity.get('goodsId', None),
                               entity.get('headimgurl', None),
                               entity.get('nickname', None),
                               entity.get('skin', None),
                               entity.get('skinResults', None),
                               entity.get('userDescz', None),
                               entity.get('userId', None)
                                ))
        else:
            continue
    return resultList


def get_goodsext(pathList):
    for path in pathList:
        fd = open(path).read()
        content = json.loads(fd)
        if content['result']['entityInfo']['goods'].has_key('goodsExt'):
            entity = content['result']['entityInfo']['goods']['goodsExt']
            resultList.append((entity.get('id', None),
                               entity.get('allowComment', None),
                               entity.get('cpsType', None),
                               entity.get('defCps', None),
                               entity.get('defExtCps', None),
                               entity.get('gcCps', None),
                               entity.get('goodsId', None),
                               entity.get('mfjCps', None)
                                ))
        else:
            continue
    return resultList


def get_composition(pathList):
    for path in pathList:
        fd = open(path).read()
        content = json.loads(fd)
        if content['result']['entityInfo'].has_key('composition'):
            entitys = content['result']['entityInfo']['composition']
            for entity in entitys:
                resultList.append((entity.get('id', None),entity.get('acneRisk', None),
                                   entity.get('active', None),entity.get('cas', None),
                                   entity.get('cmEnglish', None),entity.get('cmTitle', None),
                                   entity.get('createStamp', None),entity.get('curUsedName', None),
                                   entity.get('efficacy', None),entity.get('english', None),
                                   entity.get('frequency', None),entity.get('mPid', None),
                                   entity.get('mid', None), entity.get('otherTitle', None),
                                   entity.get('pid', None),entity.get('remark', None),
                                   entity.get('safety', None),entity.get('shenyong', None),
                                   entity.get('srcId', None),entity.get('title', None),
                                   entity.get('updateStamp', None),entity.get('used', None),
                                   entity.get('usedNum', None),entity.get('usedTitle', None),
                                   entity.get('drnt', None), entity.get('drnw', None),
                                   entity.get('drpt', None), entity.get('drpw', None),
                                   entity.get('dsnt', None),entity.get('dsnw', None),
                                   entity.get('dspt', None),entity.get('dspw', None),
                                   entity.get('ornt', None),entity.get('ornw', None),
                                   entity.get('orpt', None),entity.get('orpw', None),
                                   entity.get('osnt', None),entity.get('osnw', None),
                                   entity.get('ospt', None),entity.get('ospw', None)
                                   ))
        else:
            continue
    resultList.sort()
    it =itertools.groupby(resultList)
    for k,g in it:
        sortList.append(k)
    return sortList


def get_compo_used(pathList):
    for path in pathList:
        fd = open(path).read()
        content = json.loads(fd)
        if content['result']['entityInfo'].has_key('composition'):
            entitys = content['result']['entityInfo']['composition']
            for entity in entitys:
                if entity.has_key('useds'):
                    for useds in entity['useds']:
                        resultList.append((useds.get('id', None), useds.get('title', None)))
                else:
                    continue
        else:
            continue
    resultList.sort()
    it =itertools.groupby(resultList)
    for k,g in it:
        sortList.append(k)
    return sortList


def get_effect(pathList):
    for path in pathList:
        fd = open(path).read()
        content = json.loads(fd)
        if content['result']['entityInfo'].has_key('effect'):
            entitys = content['result']['entityInfo']['effect']
            for entity in entitys:
                if len(entity.get('compositionIds', None)):
                    composid = len(entity.get('compositionIds', None))
                else:
                    composid = None
                resultList.append((entity.get('id', None),content['result']['entity'].get('id', None),
                                   entity.get('name', None),entity.get('num', None),
                                   entity.get('unit', None),entity.get('compareName', None),
                                   composid,
                                   entity.get('desc', None),entity.get('displayCompare', None),
                                   entity.get('displayCompareName', None),entity.get('displayCompareSort', None),
                                   entity.get('displayName', None),entity.get('displayType', None),
                                   entity.get('effectId', None),entity.get('effectPid', None),
                                   entity.get('effectPidName', None)
                                   ))
        else:
            continue
    return resultList


def get_safety(pathList):
    for path in pathList:
        fd = open(path).read()
        content = json.loads(fd)
        if content['result']['entityInfo'].has_key('safety'):
            entitys = content['result']['entityInfo']['safety']
            for entity in entitys:
                if len(entity.get('compositionIds', None)):
                    composid = len(entity.get('compositionIds', None))
                else:
                    composid = None
                resultList.append((entity.get('id', None),content['result']['entity'].get('id', None),
                                   entity.get('name', None),entity.get('num', None),
                                   entity.get('unit', None),composid,entity.get('desc', None),
                                   entity.get('displayName', None),entity.get('percentEssence', None),
                                   entity.get('percentPregnant', None),entity.get('percentPreservative', None),
                                   entity.get('percentRisk', None),entity.get('percentSafety', None)
                                   ))
        else:
            continue
    return resultList

