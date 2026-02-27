# ！/usr/bin/env python
# -*- coding:utf8 -*-
# author:yangyaxin time::11:08
import requests

from common.sendmethod import RequestConnector
import uuid
import logging
import json
import time
from common.ssh_connect import SshConnect
# from log.judge_log import JudgeLog

class DeleteLockPsw:
    def __init__(self,devId,prodTypeId):
        self.ssh_connect = SshConnect()
        # 初始化接口请求的参数
        self.devId = devId
        self.prodTypeId = prodTypeId
        # 创建接口请求实例
        self.request_connect = RequestConnector()
        self.payload_deletepwd = {
            "msgType":"DEVICE_CONTROL",
            "devId": "70b3d50580012bdf",
            "prodTypeId": "ZH-B0104",
            "time": "2019-01-08 13:20:10",
            "sno": "1582963479787",
            "attribute": "lock_password",
            "command": "delete_password",
            "data": [
         {
                    "k": "index",
                    "v": "8"
                }

            ]
        }


    def delete_lock_psw(self):
        self.payload_deletepwd["devId"] = self.devId
        self.payload_deletepwd["prodTypeId"] = self.prodTypeId
        self.payload_deletepwd["sno"] = str(uuid.uuid1())
        sno = self.payload_deletepwd['sno']
        # print("sno:", sno)
        logging.info("sno: %s", sno)
        flag = 0
        while flag == 0:
            try:
                # rep = self.request_connect.post_request_qlink(self.payload_deletepwd)
                rep = self.request_connect.post_request_qlink(self.payload_deletepwd)
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

if __name__ == "__main__":
    delete_index = DeleteLockPsw()
    delete_index.delete_lock_psw()