#coding=utf8
import sys
reload(sys)
import requests
import json
from Segment.MySegment import *
sys.setdefaultencoding('utf8')
BasePath = sys.path[0]



if __name__ == "__main__":

    for i in range(1, 10000):

        if i % 1000 == 0:
            print(i)
            print(i/1000)

    # x = raw_input()
    # # http: // 10.168.103.101:8000 / document_solr / document / list.controller?queryString = % E8 % AF % 88 % E9 % AA % 97
    # a = requests.get("http://10.168.103.101:8000/document_solr/document/list.controller",data={'queryString':"饕餮"})
    # print(a)
    # decode_json = json.loads(a.content)
    # print(decode_json)
    # id_list = decode_json['ids']
    # score_list = decode_json['scores']

    # print(id_list[0:10])
    # print(id_list[0:10] - 1)

    # print(decode_json)
    # import numpy as np
    # a = np.array([1,2,3,4,5,5,6,7,8])
    # b = np.array([1,3,5])
    # print(a[b])

    # myseg = MySegment()
    # a = myseg.sen2word("张某酒后驾车，之后逃逸，最后在海淀区被警察逮捕")
    # print(' '.join(a))

    # import os
    # root = BasePath + "/seg_corpus"
    # files = os.listdir(root)
    # for file in files: # 遍历文件夹
    #     print(file)





    #     if not os.path.isdir(file): # 判断是否是文件夹，不是文件夹则打开
            # uniname = unicode(file, 'utf8')
            # json_data = json.load(open(uniname))

        # print(files)
