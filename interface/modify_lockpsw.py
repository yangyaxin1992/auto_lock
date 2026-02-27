# ！/usr/bin/env python
# -*- coding:utf8 -*-
# author:yangyaxin time::14:56

import logging
import uuid
import random
import json
import requests
import time
from common.sendmethod import RequestConnector
from common.ssh_connect import SshConnect

class ModifyLockPsw:

    def __init__(self,devId,prodTypeId):
        self.ssh_connect = SshConnect()
        # 初始化接口请求的参数
        self.devId = devId
        self.prodTypeId = prodTypeId
        # 创建接口请求实例
        self.request_connect = RequestConnector()
        # self.args = ["192.168.18.1", 1022, "zihome", "admin"]
        self.payload_modifypwd = {
            "msgType": "DEVICE_CONTROL",
            "devId": "70b3d50580012bdf",
            "prodTypeId": "ZH-B0104",
            "time": "2019-01-08 13:20:10",
            "sno": "1582880050342",
            "attribute": "lock_password",
            "command": "reset_password",
            "data": [
                {
                    "k": "index",
                    "v": "14"
                },
                {
                    "k": "status",
                    "v": "2"
                },
                {
                    "k": "starttime",
                    "v": "1655695238"
                },
                {
                    "k": "deadline",
                    "v": "2028873811"
                },
                {
                    "k": "content",
                    "v":"56778788"
                }
            ]
        }

    def modify_lockpsw(self):
        self.payload_modifypwd["devId"] = self.devId
        self.payload_modifypwd["prodTypeId"] = self.prodTypeId
        self.payload_modifypwd["sno"] = str(uuid.uuid1())
        sno = self.payload_modifypwd['sno']
        # print("sno:", sno)
        logging.info("sno: %s", sno)
        flag = 0
        while flag == 0:
            try :
                # rep = self.request_connect.post_request_qlink(self.payload_modifypwd)
                rep = self.request_connect.post_request_qlink(self.payload_modifypwd)
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


# if __name__ == '__main__':
#     devId = ""
#     prodTypeId =""
#     modify = ModifyLockPsw(devId,prodTypeId)
