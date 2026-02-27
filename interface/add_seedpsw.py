
# ！/usr/bin/env python
# -*- coding:utf8 -*-
# author:yangyaxin time::11:23

import logging
import uuid
import json
import requests
from common.sendmethod import RequestConnector
from common.ssh_connect import SshConnect


class AddSeedPwd:

    def __init__(self,devId,prodTypeId):
        self.ssh_connect = SshConnect()
        # 初始化接口请求的参数
        self.devId = devId
        self.prodTypeId = prodTypeId
        # 创建接口请求实例
        self.request_connect = RequestConnector()
        self.payload_addseed = {
            "msgType":"DEVICE_CONTROL",
            "devId":"70b3d50580012bdf",
            "prodTypeId": "ZH-B0104",
            "time": "2019-01-08 13:20:10",
            "sno": "1583478637033",
            "attribute": "lock_seed",
            "command": "set_seed",
            "data": [
                {
                    "k": "seed",
                    "v": "681234"
                }
                ]
        }


    def add_seedpsw(self):

        # lock_index[payload["data"][0]["v"]] = payload["data"][4]["v"]
        # print(lock_index)
        self.payload_addseed["devId"] = self.devId
        self.payload_addseed["prodTypeId"] = self.prodTypeId
        self.payload_addseed["sno"] = str(uuid.uuid1())
        sno = self.payload_addseed['sno']
        # print("sno:",sno)
        logging.info("sno: %s",sno)
        # payload["data"][0]["v"] = random.randint(000, 255)

        logging.info(self.payload_addseed)
        flag = 0
        while flag == 0:
            try :
                # rep = self.request_connect.post_request_qlink(self.payload_addseed)
                rep = self.request_connect.post_request_qlink(self.payload_addseed)
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
    # add_lockpsw = AddLockPwd()
    # dev = "F108E34401608CF2"
    # add_lockpsw.add_lockpsw(dev,3)