# ！/usr/bin/env python
# -*- coding:utf8 -*-
# author:yangyaxin time::9:43
import logging
import uuid
import random
import json
import requests
import time
from common.sendmethod import RequestConnector
from common.ssh_connect import SshConnect


class GetLockPwd:

    def __init__(self,devId,prodTypeId):
        self.ssh_connect = SshConnect()
        # 初始化接口请求的参数
        self.devId = devId
        self.prodTypeId = prodTypeId
        # 创建接口请求实例
        self.request_connect = RequestConnector()
        self.payload_getpwd = {
            "msgType": "DEVICE_CONTROL",
            "devId": "70b3d50580012bdf",
            "prodTypeId": "ZH-B0104",
            "time": "2019-01-08 13:20:10",
            "sno": "1583468141702",
            "attribute": "lock_password",
            "command": "get_password",
            "data": [
                {
                  "k": "status",
                  "v": "1"
                }
            ]
        }
        self.payload_get_indexpwd = {
            "msgType": "DEVICE_CONTROL",
            "devId": "70b3d5058001ac16",
            "prodTypeId": "ZH-B0104",
            "time": "2019-01-08 13:20:10",
            "sno": "1583468141702",
            "attribute": "lock_password",
            "command": "get_password",
            "data": [
                {
                    "k": "index",
                    "v": "1"
                }
            ]
        }

    # 根据密码状态查看
    def get_lockpsw(self):
        self.payload_getpwd["devId"] = self.devId
        self.payload_getpwd["prodTypeId"] = self.prodTypeId
        self.payload_getpwd["sno"] = str(uuid.uuid1())
        sno = self.payload_getpwd['sno']
        # print("sno:", sno)
        logging.info(self.payload_getpwd)
        flag = 0
        while flag == 0:
            try :
                rep = self.request_connect.post_request_qlink(self.payload_getpwd)
                if rep:
                    logging.info(rep.text)
                    if rep.status_code == 200:
                        msg = json.loads(rep.text)
                        # print("msg", msg)
                        logging.info("msg:%s", msg)
                        if 200 == msg["code"]:
                            flag += 1
                            break
                            # return sno
                        else:
                            flag += 0
                    else:
                        flag += 0
                else:
                    flag += 0
            except requests.exceptions.RequestException:
                flag = 0
        return sno
        # time.sleep(2)
        # print(self.lock_index)
        # return paw_index

    # 根据index查看
    def get_index_lockpsw(self):
        self.payload_get_indexpwd["devId"] = self.devId
        self.payload_get_indexpwd["prodTypeId"] = self.prodTypeId
        self.payload_get_indexpwd["sno"] = str(uuid.uuid1())
        sno = self.payload_get_indexpwd['sno']
        # print("sno:", sno)
        logging.info(self.payload_get_indexpwd)
        flag = 0
        while flag == 0:
            try:
                # rep = self.request_connect.post_request_qlink(self.payload_get_indexpwd)
                rep = self.request_connect.post_request_qlink(self.payload_get_indexpwd)
                if rep:
                    logging.info(rep.text)
                    if rep.status_code == 200:
                        msg = json.loads(rep.text)
                        # print("msg", msg)
                        logging.info("msg: %s", msg)
                        if 200 == msg["code"]:
                            flag += 1
                            break
                            # return sno
                        else:
                            flag += 0
                    else:
                        flag += 0
                else:
                    flag += 0
            except requests.exceptions.RequestException:
                flag = 0
        return sno

    # def lock_index_psw(self):
    #     with open(r"D:\Work(勿删）\04 _自动化项目\auto_testplat\lock\params\lock_index.txt",'w') as obj:
    #         for i in self.lock_index.keys():
    #             obj.write(str(i)+",")
    #
    #     return self.lock_index

if __name__ == '__main__':
    pass