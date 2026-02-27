# ！/usr/bin/env python
# -*- coding:utf8 -*-
# author:yangyaxin time::10:40
import logging
import os
import re

import json
import time
from common.log import GetLog
import allure

class JudgeLog():
    def __init__(self,dir,path):
        # SecureCRT日志存放路径
        self.dir =dir
        self.path = path
        # self.dir = r'D:\Work(勿删）\03 项目\log'
        # 日志最新存放路径
        # self.path = r'D:\Work(勿删）\04 _自动化项目\auto_testplat\智能锁\lock\log\log_file\\'
        # self.path_new = os.path.join(self.path, "..", "log",  "log_file")

    def log_change_json(self,r):
        # 正则的数据，经过一定规则处理后，数据转换成json格式
        chars = '\n\t'
        for c in chars:
            # 将列表里的元素，去掉\n\t
            r = r.replace(c, '')
        # print(r[-1])
        code_data = json.loads(r)
        # print("转换后的数据：",code_data)
        logging.info("转换后的数据：%s",code_data)
        return code_data

    # 获取开关、模式、风速、温度响应resp
    def get_set_resp(self, command, log_name, sno):
        # print(self.path + log_name)
        logging.info(self.path + log_name)
        # log_path = os.path.join(self.path_new , log_name)
        # print(log_path)
        try:
            with open(self.path + log_name, encoding='utf-8') as obj:
                # with open(r"D:\Work(勿删）\04 _自动化项目\auto_testplat\light\log\log_file\ZGateway_Main_202112231524_019070_001.log",encoding='utf-8') as obj:
                log = obj.read()
                # print("打印log",log)
                # sno = 'bdd39bc9-87fc-11ec-9a30-dc1ba18ce37f'
                # sno = 'dd604b5a-6dfd-11ec-a491-002432a04e89'
                symbol = '.*\n'
                regex_addseed = r'LOG_DEBUG ({.*\n.*"msgType"'+'.*'+'"DEVICE_CONTROL_RESP"' + symbol*4 + '.*"sno"' + '.*' + sno + symbol*2 + '.*"command"' + '.*' + '"set_seed_resp"'+symbol*11+'})'
                regex_getseed = r'LOG_DEBUG ({.*\n.*"msgType"'+'.*'+'"DEVICE_CONTROL_RESP"' + symbol*4 + '.*"sno"' + '.*' + sno + symbol*2 + '.*"command"' + '.*' + '"get_seed_resp"'+symbol*11+'})'
                regex_addpwd = r'LOG_DEBUG ({.*\n.*"msgType"'+'.*'+'"DEVICE_CONTROL_RESP"' + symbol*4 + '.*"sno"' + '.*' + sno + symbol*2 + '.*"command"' + '.*' + '"add_password_resp"'+symbol*11+'})'
                regex_deletepwd = r'LOG_DEBUG ({.*\n.*"msgType"'+'.*'+'"DEVICE_CONTROL_RESP"' + symbol*4 + '.*"sno"' + '.*' + sno + symbol*2 + '.*"command"' + '.*' + '"delete_password_resp"'+symbol*11+'})'
                regex_moditypwd = r'LOG_DEBUG ({.*\n.*"msgType"'+'.*'+'"DEVICE_CONTROL_RESP"' + symbol*4 + '.*"sno"' + '.*' + sno + symbol*2 + '.*"command"' + '.*' + '"reset_password_resp"'+symbol*11+'})'
                # regex_getpwd = r'LOG_DEBUG ({.*\n.*"msgType"'+'.*'+'"DEVICE_CONTROL_RESP"' + symbol*4 + '.*"sno"' + '.*' + sno + symbol*2 + '.*"command"' + '.*' + '"get_password_resp"'+symbol*11+'})'
                # regex_get_index_pwd = r'LOG_DEBUG ({.*\n.*"msgType"'+'.*'+'"DEVICE_CONTROL_RESP"' + symbol*4 + '.*"sno"' + '.*' + sno + symbol*2 + '.*"command"' + '.*' + '"get_password_resp"'+symbol*11+'})'
                regex_clearpwd = r'LOG_DEBUG ({.*\n.*"msgType"'+'.*'+'"DEVICE_CONTROL_RESP"' + symbol*4 + '.*"sno"' + '.*' + sno + symbol*2 + '.*"command"' + '.*' + '"clear_password_resp"'+symbol*11+'})'
                if command == 'set_seed' :
                    r = re.findall(regex_addseed,log)
                elif command == 'get_seed' :
                    r = re.findall(regex_getseed,log)
                elif command == 'add_password':
                    r = re.findall(regex_addpwd, log)
                elif command == 'delete_password':
                    r = re.findall(regex_deletepwd, log)
                elif command == 'reset_password':
                    r = re.findall(regex_moditypwd, log)
                elif command == 'clear_password' :
                    r = re.findall(regex_clearpwd, log)
                # elif command == 'get_password':
                #     r = re.findall(regex_getpwd, log)
                #     regex_notify_password = r'LOG_DEBUG ({.*\n.*"msgType"'+'.*'+'"DEVICE_QUERY_RESP"' + symbol*5 + '.*"attribute"' + '.*' + '"lock_password"' + symbol*1 + '.*"command"' + '.*' + '"notify_password"'+symbol*24+'})'
                #     notify = re.findall(regex_notify_password,log)
                    # 如何解析index？？？
                # r =  re.findall(r'LOG_DEBUG ({\n.*"msgType".*\n.*\n.*\n.*\n.*"sno":	"'+sno+'"'+symbol*13+'})',log)
            # print(r)
            logging.info("解析数据：%s",r)
            # print(len(r))
            if len(r) == 1:
                code_data = self.log_change_json(r[-1])
                # print("解析的resp数据个数：", len(r))
                logging.info("解析的resp数据个数：%d", len(r))
                # print(code_data)
                logging.info(code_data)
                return code_data
            elif len(r) > 1:
                code_data = self.log_change_json(r[-1])
                # print("解析的resp数据个数：",len(r))
                logging.info("解析的resp数据个数：%d",len(r))
                # print(code_data)
                logging.info(code_data)
                return code_data
            else:
                # print("没有获取到指定的数据，测试失败")
                logging.info("没有获取到指定的数据，测试失败")
                return False
        except FileNotFoundError as f:
            # print("文件不存在，请检查文件路径")
            logging.info("文件不存在，请检查文件路径")

    # 查询密码index
    def get_password_resp(self, log_name, sno,reportTotalNum,notify_list):
        print(self.path + log_name)
        # log_path = os.path.join(self.path_new, log_name)
        # print(log_path)
        try:
            with open(self.path + log_name, encoding='utf-8') as obj:
                # with open(r"D:\Work(勿删）\04 _自动化项目\auto_testplat\light\log\log_file\ZGateway_Main_202112231524_019070_001.log",encoding='utf-8') as obj:
                log = obj.read()
                symbol = '.*\n'
                regex_getpwd = r'LOG_DEBUG ({.*\n.*"msgType"'+'.*'+'"DEVICE_CONTROL_RESP"' + symbol*4 + '.*"sno"' + '.*' + sno + symbol*2 + '.*"command"' + '.*' + '"get_password_resp"'+symbol*11+'})'
                #  问题点：从某个特定字符开始读取(从sno开始读取）
                r = re.findall(regex_getpwd, log)
                print("r:",r)
                new_log = log.split(sno,1)[-1]
                regex_notify_password = r'LOG_DEBUG ({.*\n.*"msgType"'+'.*'+'"DEVICE_QUERY_RESP"' + symbol*5 + '.*"attribute"' + '.*' + '"lock_password"' + symbol*1 + '.*"command"' + '.*' + '"notify_password"'+symbol*24+'})'
                notify = re.findall(regex_notify_password,new_log)
                # 如何解析index？？？
                # r =  re.findall(r'LOG_DEBUG ({\n.*"msgType".*\n.*\n.*\n.*\n.*"sno":	"'+sno+'"'+symbol*13+'})',log)
            # print(r)
            logging.info("解析的数据：%s",r)
            # print(len(r))
            if len(r) == 1:
                code_data = self.log_change_json(r[-1])
                # print("resp的数据解析：",code_data)
                logging.info("resp的数据解析：%s",code_data)
                # print("*"*88)
                # print("*" * 22 + ' ' + "开始解析notify的数据" + "*" * 22)
                logging.info("*" * 22 + ' ' + "开始解析notify的数据" + "*" * 22)
                if len(notify) > 0 :
                    for i in notify :
                        notify_data = self.log_change_json(i)
                        # print("notify的数据解析：",notify_data)
                        logging.info("notify的数据解析： %s", notify_data)
                        reportTotalNum.append(notify_data["data"][0]["v"])
                        notify_list.append(notify_data["data"][2]["v"])
                    return code_data
                else :
                    # print("notify没有数据.......")
                    logging.info("notify没有数据.......")
                    return code_data
            elif len(r) > 1:
                code_data = self.log_change_json(r[-1])
                # print(code_data)
                logging.info(code_data)
                if len(notify) > 0:
                    for i in notify :
                        notify_data = self.log_change_json(i)
                        # print(notify_data)
                        logging.info("notify的数据解析： %s",notify_data)
                        reportTotalNum.append(notify_data["data"][0]["v"])
                        notify_list.append(notify_data["data"][2]["v"])
                    return code_data
                else :
                    # print("notify没有数据.......")
                    logging.info("notify没有数据.......")
                    return code_data
            else:
                # print("没有获取到指定的数据，测试失败")
                logging.info("没有获取到指定的数据，测试失败")
                return False
        except FileNotFoundError as f:
            # print("文件不存在，请检查文件路径")
            logging.info("文件不存在，请检查文件路径")

    # def add_password_resp(self,dev,log_name,sno):
    #     # print(self.path + log_name)
    #     with open(r"D:\Work(勿删）\04 _自动化项目\auto_testplat\lock\log\log_file\\"+log_name,encoding='utf-8') as obj:
    #         log = obj.read()
    #         # print(str(log))
    #         # str = f'{sno}'
    #         # sno = '51a3195e-613f-11ec-ab60-dc1ba18ce37f'
    #         #   r =  re.findall(r'LOG_DEBUG {\n\t"msgType":.*\n.*\n.*\n.*\n\t"sno":	"'+sno+'",\n.*\n\t"command":	"add_password_resp",\n\t"data":.*({\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n)}',log)
    #         symbol = '.*\n'
    #         r =  re.findall(r'LOG_DEBUG ({\n.*"msgType":	"DEVICE_CONTROL_RESP".*\n.*"devId":	"'+dev+'".*\n.*\n.*\n.*"sno":	"'+sno+'".*\n.*\n.*"command":	"add_password_resp"'+symbol*11+'})',log)
    #         print(r)
    #         chars = '\n\t'
    #         for c in chars:
    #             r[0] = r[0].replace(c,'')
    #         # r = r[0].split(", ")
    #         # print(r)
    #         code_data = json.loads(r[0])
    #         print(code_data)
    #         count = 0
    #         if code_data['data'][0]['k'] == 'code':
    #             if code_data['data'][0]['v'] == '0':
    #                 count += 1
    #
    #     return count
    #
    #
    # def delete_resp(self,dev,log_name, sno):
    #     with open(r"D:\Work(勿删）\04 _自动化项目\auto_testplat\lock\log\log_file\\" + log_name, encoding='utf-8') as obj:
    #         log = obj.read()
    #         #   r =  re.findall(r'LOG_DEBUG {\n\t"msgType":.*\n.*\n.*\n.*\n\t"sno":	"'+sno+'",\n.*\n\t"command":	"add_password_resp",\n\t"data":.*({\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n)}',log)
    #         symbol = '.*\n'
    #         r = re.findall(r'LOG_DEBUG ({\n.*"msgType":	"DEVICE_CONTROL_RESP".*\n.*"devId":	"'+dev+'".*\n.*\n.*\n.*"sno":	"'+sno+'".*\n.*\n.*"command":	"delete_password_resp"'+symbol * 14+'})',
    #             log)
    #         print(r)
    #         chars = '\n\t'
    #         for c in chars:
    #             r[0] = r[0].replace(c, '')
    #         # r = r[0].split(", ")
    #         # print(r)
    #         code_data = json.loads(r[0])
    #         print(code_data)
    #         count = 0
    #         if code_data['data'][1]['k'] == 'code':
    #             if code_data['data'][1]['v'] == '0':
    #                 count += 1
    #
    #     return count
    #
    # def modify_resp(self, dev,log_name, sno):
    #     with open(r"D:\Work(勿删）\04 _自动化项目\auto_testplat\lock\log\log_file\\" + log_name, encoding='utf-8') as obj:
    #         log = obj.read()
    #
    #         #   r =  re.findall(r'LOG_DEBUG {\n\t"msgType":.*\n.*\n.*\n.*\n\t"sno":	"'+sno+'",\n.*\n\t"command":	"add_password_resp",\n\t"data":.*({\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n)}',log)
    #         symbol = '.*\n'
    #         r = re.findall(r'LOG_DEBUG ({\n.*"msgType":	"DEVICE_CONTROL_RESP".*\n.*"devId":	"'+dev+'".*\n.*\n.*\n.*"sno":	"'+sno+'".*\n.*\n.*"command":	"reset_password_resp"'+symbol * 11+'})',
    #             log)
    #         print(r)
    #         chars = '\n\t'
    #         for c in chars:
    #             r[0] = r[0].replace(c, '')
    #         # r = r[0].split(", ")
    #         # print(r)
    #         code_data = json.loads(r[0])
    #         print(code_data)
    #         count = 0
    #         if code_data['data'][0]['k'] == 'code':
    #             if code_data['data'][0]['v'] == '0':
    #                 count += 1
    #     return count
    #
    # def get_password_resp(self, dev,log_name, sno):
    #     with open(r"D:\Work(勿删）\04 _自动化项目\auto_testplat\lock\log\log_file\\" + log_name, encoding='utf-8') as obj:
    #         log = obj.read()
    #         symbol = '.*\n'
    #         r = re.findall(r'LOG_DEBUG ({\n.*"msgType":	"DEVICE_CONTROL_RESP".*\n.*"devId":	"'+dev+'".*\n.*\n.*\n.*"sno":	"'+sno+'".*\n.*\n.*"command":	"get_password_resp"'+symbol * 11+'})',
    #             log)
    #         print(r)
    #         chars = '\n\t'
    #         for c in chars:
    #             r[0] = r[0].replace(c, '')
    #         code_data = json.loads(r[0])
    #         print(code_data)
    #         # count = 0
    #         if code_data['data'][0]['k'] == 'code':
    #             if code_data['data'][0]['v'] == '0':
    #                 return True
    #
    # def get_password_index(self,dev,log_name, sno):
    #     # 获取查询密码的index
    #     with open(r"D:\Work(勿删）\04 _自动化项目\auto_testplat\lock\log\log_file\\" + log_name, encoding='utf-8') as obj:
    #         log = obj.read()
    #         symbol = '.*\n'
    #         get_log = re.findall(r'"sno":	"'+sno+'".*',log,re.S)  # 获取查询密码后的log日志
    #         # print(get_log)
    #         # 提取index数据
    #         index_log = re.findall(r'LOG_DEBUG ({\n.*"msgType":	"DEVICE_QUERY_RESP".*\n.*"devId":	"'+dev+'"'+symbol*5+'.*"command":	"notify_password"'+symbol*21+'})',get_log[0])
    #         print('index_log',len(index_log),index_log)
    #     #
    #         index_list = []
    #         chars = '\n\t'
    #         for i in range(len(index_log)):
    #             for c in chars:
    #                 index_log[i] = index_log[i].replace(c, '')
    #             # print(index_log[i])
    #             index_list.append(json.loads(index_log[i]))
    #         print("*"*66)
    #         print(index_list)
    #         lock_paw_index = []
    #         total = index_list[0]["data"][0]["v"]
    #         print("锁的密码总数为：",total)
    #         allure.attach(f"锁的密码总数为：{total}", "成功次数", allure.attachment_type.TEXT)
    #         for i in index_list:
    #             reportindex = i["data"][1]["v"]
    #             print("reportIndex:",reportindex,end=' ')
    #             index = i["data"][2]["v"]
    #             lock_paw_index.append(index)
    #             print("index:", index, end=' ')
    #             status = i["data"][5]["v"]
    #             print("status:", status, end=' ')
    #             print()
    #             allure.attach(f"密码index：{index}", f"密码{index}", allure.attachment_type.TEXT)
    #     return lock_paw_index


    def judge_set_resp(self, command, log_name, sno ):
        # 定义列表，存放查询的index总数、index
        reportTotalNum = []
        notify_list = []
        # 查询密码，需要解析日志，提取index
        if command == "get_password" :
            code_data = self.get_password_resp( log_name, sno,reportTotalNum,notify_list)
        else :
            code_data = self.get_set_resp(command, log_name, sno)
        if code_data == False:
            return False
        else:
            if code_data['data'][0]['k'] == 'code':
                if code_data['data'][0]['v'] == '0':
                    # print("操作成功")
                    logging.info("操作成功")
                    if command == 'get_password':
                        if len(reportTotalNum) != 0 and len(notify_list) != 0 :
                            if int(reportTotalNum[0]) == len(notify_list) :
                                # print("查询的index数量与上报的一致")
                                logging.info("查询的index数量与上报的一致")
                                # print("查询index总数为：",reportTotalNum[0],"\n查询的index为：",notify_list)
                                logging.info("查询index总数为：%s", reportTotalNum[0])
                                logging.info("查询的index为：%s", notify_list)
                                return True
                            else :
                                # print("查询的index数量与上报的不一致，请分析日志......")
                                logging.info("查询的index数量与上报的不一致，请分析日志......")
                                # print("查询index总数为：",reportTotalNum[0],"\n查询的index为：", notify_list)
                                logging.info("查询index总数为：%s",reportTotalNum[0])
                                logging.info("查询的index为：%s", notify_list)
                                return False
                        else :
                            # print("查询当前状态的index数量为0，查询的index数量与上报的一致")
                            logging.info("查询当前状态的index数量为0，查询的index数量与上报的一致")
                            return True
                    # elif command == 'clear_password' :
                    #     pass
                    else :
                        return True
                elif code_data['data'][0]['v'] == '1':
                    # print("操作失败：没有找到PasswordID/seed")
                    logging.info("操作失败：没有找到PasswordID/seed")
                    return True
                elif code_data['data'][0]['v'] == '2':
                    # print("操作失败：新增密码内容相似")
                    logging.info("操作失败：新增密码内容相似")
                    return True
                elif code_data['data'][0]['v'] == '3':
                    # print("操作失败：新增密码密码池满")
                    logging.info("操作失败：新增密码密码池满")
                    return True
                elif code_data['data'][0]['v'] == '5':
                    # print("操作失败：命令长度或参数不正确")
                    logging.info("操作失败：命令长度或参数不正确")
                    return False
                elif code_data['data'][0]['v'] == '104':
                    # print("操作失败: 操作超时")
                    logging.info("操作失败: 操作超时")
                    return False
                else:
                    # print("操作失败：resp的code值是：",code_data['data'][0]['v'])
                    logging.info("操作失败：resp的code值是：%s",code_data['data'][0]['v'])
                    return False
            else:
                return False

    def judge_result(self,sno,command):
        # 判断日志结果
        # 获取最新log
        time.sleep(60)
        # print()
        # print("#"*22+"设置"+command+"命令成功"+"#"*22)
        logging.info("#"*22+"设置"+command+"命令成功"+"#"*22)
        get_log = GetLog(self.path)
        log_name = get_log.find_new_file(self.dir)
        # print(log_name)
        logging.info(log_name)
        # judge_log = JudgeLog()
        # 判断响应码
        # print()
        # print("*" * 22 +' ' + "开始判断"+ command + "的resp结果" + "*" * 22)
        logging.info("*" * 22 +' ' + "开始判断"+ command + "的resp结果" + "*" * 22)
        result = self.judge_set_resp(command,log_name,sno)
        # pytest.assume(result)
        # 判断状态改变通知
        if result :
            # print()
            # print("#"*22+' ' + command +"的resp结果判断：pass"+"#"*22)
            logging.info("#"*22+' ' + command +"的resp结果判断：pass"+"#"*22)
            return True
        else:
            # print()
            # print("#" * 22 + command +  "的resp结果判断：fail" + "#" * 22)
            logging.info("#" * 22 + command +  "的resp结果判断：fail" + "#" * 22)
            return False

    def statistics_loss_rate(self,success_count,fail_count):
        # 统计丢包率
        # print("#"*22+"测试结束："+"#"*22)
        logging.info("#"*22+"测试结束："+"#"*22)
        loss = float(fail_count / (success_count + fail_count))
        loss_rate = "%.2f%%" % (loss * 100)
        # print("执行成功次数：", success_count)
        # print("执行失败次数：", fail_count)
        # print("丢包率：", loss_rate)
        logging.info("执行成功次数：%s", success_count)
        logging.info("执行失败次数：%s", fail_count)
        logging.info("丢包率：%s", loss_rate)
        allure.attach(f"执行成功次数：{success_count}", "成功次数", allure.attachment_type.TEXT)
        allure.attach(f"执行失败次数：{fail_count}", "失败次数", allure.attachment_type.TEXT)
        allure.attach(f"控制成功率：{loss_rate}", "成功率", allure.attachment_type.TEXT)

if __name__ == '__main__':
    sno = "1639716295"
    dev = ""
    judge_log = JudgeLog()
    log_name = 'ZGateway_Main_202112201022_031148_000.log'
    # judge_log.add_password_resp(dev,log_name,sno)
