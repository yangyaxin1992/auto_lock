# ！/usr/bin/env python
# -*- coding:utf8 -*-
# author:yangyaxin time::11:31

import logging
import uuid
import json
import requests
from common.sendmethod import RequestConnector
from common.ssh_connect import SshConnect


class FreezeLockPwd:

    def __init__(self,devId,prodTypeId):
        self.ssh_connect = SshConnect()
        # 初始化接口请求的参数
        self.devId = devId
        self.prodTypeId = prodTypeId
        # 创建接口请求实例
        self.request_connect = RequestConnector()
        # self.args = ["192.168.18.1", 1022, "zihome", "admin"]
        self.payload_freezepwd = {
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
                    "v": "127"
                },
                {
                    "k": "status",
                    "v": "1"
                }
            ]
        }

    def freeze_lockpsw(self):
        # lock_index[payload["data"][0]["v"]] = payload["data"][4]["v"]
        # print(lock_index)
        self.payload_freezepwd["devId"] = self.devId
        self.payload_freezepwd["prodTypeId"] = self.prodTypeId
        self.payload_freezepwd["sno"] = str(uuid.uuid1())
        sno = self.payload_freezepwd['sno']
        # print("sno:", sno)
        logging.info("sno: %s", sno)
        # payload["data"][0]["v"] = random.randint(000, 255)

        logging.info(self.payload_freezepwd)
        flag = 0
        while flag == 0:
            try :
                # rep = self.request_connect.post_request_qlink(self.payload_freezepwd)
                rep = self.request_connect.post_request_qlink(self.payload_freezepwd)
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
