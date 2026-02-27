# ！/usr/bin/env python
# -*- coding:utf8 -*-
# author:yangyaxin time::15:58

import logging
import uuid
import json
import requests
from common.sendmethod import RequestConnector
from common.ssh_connect import SshConnect


class ClearLockPwd:

    def __init__(self,devId,prodTypeId):
        self.ssh_connect = SshConnect()
        # 初始化接口请求的参数
        self.devId = devId
        self.prodTypeId = prodTypeId
        # 创建接口请求实例
        self.request_connect = RequestConnector()
        # self.args = ["192.168.18.1", 1022, "zihome", "admin"]
        self.payload_clearpwd_yaoguang = {
            "msgType": "DEVICE_CONTROL",
            "devId": "70b3d50580012bdf",
            "prodTypeId": "ZH-B0104",
            "time": "2019-01-08 13:20:10",
            "sno": "1584000196273",
            "attribute": "lock_password",
            "command": "clear_password",
            "catalog": "",
            "data": [
                {
                    "k": "index",
                    "v": "all"
                }
            ]
        }

        self.payload_clearpwd = {
            "msgType": "DEVICE_CONTROL",
            "devId": "00124b0029402ca5",
            "prodTypeId": "ZH-B0109",
            "time": "2019-01-08 13:20:10",
            "sno": "1582880050342",
            "attribute": "lock_password",
            "command": "clear_password",
            "data": [
                {
                    "k": "type",
                    "v": "1"
                }
            ]
        }

    def clear_lockpsw(self):

        # lock_index[payload["data"][0]["v"]] = payload["data"][4]["v"]
        # print(lock_index)
        self.payload_clearpwd["devId"] = self.devId
        self.payload_clearpwd["prodTypeId"] = self.prodTypeId
        self.payload_clearpwd["sno"] = str(uuid.uuid1())
        sno = self.payload_clearpwd['sno']
        # print("sno:",sno)
        logging.info("sno: %s",sno)
        # payload["data"][0]["v"] = random.randint(000, 255)

        logging.info(self.payload_clearpwd)
        flag = 0
        while flag == 0:
            try :
                # rep = self.request_connect.post_request_qlink(self.payload_clearpwd)
                rep = self.request_connect.post_request_qlink(self.payload_clearpwd)
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


if __name__ == '__main__':
    pass
