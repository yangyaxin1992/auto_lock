# ！/usr/bin/env python
# -*- coding:utf8 -*-
# author:yangyaxin time::10:59
import datetime
import logging
import random
# from common.log import LoggingInit
from interface.add_lockpsw import AddLockPwd
from interface.modify_lockpsw import ModifyLockPsw
from interface.delete_lockpsw import DeleteLockPsw
from interface.get_lockpsw import GetLockPwd
from interface.freeze_lockpsw import FreezeLockPwd
from interface.unfreeze_lockpsw import UnFreezeLockPwd
from interface.clear_lockpsw import ClearLockPwd
from config.judge_log import JudgeLog
from common.log import Logger,LoggingInit
import pytest
import allure
import os
import sys


@allure.feature("添加密码模块")
class TestLockMethods():
    def setup_class(self):
        # self.gateway = Zgateway()
        # self.args = ["192.168.18.1", 1022, "zihome", "admin"]
        self.devId = "70b3d5058001ac16"
        self.prodTypeId = "ZH-B0104"
        self.add_pwd = AddLockPwd(self.devId, self.prodTypeId)
        self.modify_pwd = ModifyLockPsw(self.devId, self.prodTypeId)
        self.get_pwd = GetLockPwd(self.devId,self.prodTypeId)
        self.delete_pwd = DeleteLockPsw(self.devId,self.prodTypeId)
        self.freeze_pwd = FreezeLockPwd(self.devId,self.prodTypeId)
        self.unfreeze_pwd = UnFreezeLockPwd(self.devId,self.prodTypeId)
        self.clear_pwd = ClearLockPwd(self.devId,self.prodTypeId)
        self.logging_init = LoggingInit()
        # self.endpoint_list = ["1", "2"]
        #SecureCRT日志存放路径
        self.dir = r'D:\Work(勿删）\03 项目\log\10.120.2.1-10.120.2.1(45AE)'
        # 日志最新存放路径
        self.log_path = r'D:\Work(勿删）\04 _自动化项目\auto_testplat\智能锁\lock\log\log_file\\'
        self.judge_log = JudgeLog(self.dir,self.log_path)
        self.path = os.getcwd()
        self.index_pass_path = os.path.join(self.path, "..", "params",  "lock_pass_index.txt")
        self.index_fail_path = os.path.join(self.path, "..", "params",  "lock_fail_index.txt")

        # 创建字典，保存锁的index和密码
        self.add_pass_index = {}
        self.add_fail_index = {}
        self.modify_pass_index = {}
        self.modify_fail_index = {}
        self.delete_pass_index = []
        self.delete_fail_index = []
        # # 创建变量：保存查询密码的总数,列表：存放密码index
        # self.reportTotalNum = []
        # self.notify_list = []
        # sys.stdout = Logger(r'D:\Work(勿删）\04 _自动化项目\auto_testplat\z_touch\log\test_log\ztouch_log.txt', sys.stdout)
        self.count = 1
        current_date = datetime.datetime.now().strftime('%d')
        sys.stdout = Logger(os.path.join(self.path, "..", "log", "test_log","log14.txt"), sys.stdout)
        sys.stderr = Logger(os.path.join(self.path, "..", "log", "test_log", "log14_error.txt"), sys.stderr)

    @allure.story("日志") #pass
    @allure.title("日志")
    @allure.description("日志保存")
    def test_000_log(self):
        self.logging_init.logging_init(self.devId)

    @allure.story("随机添加密码") #pass
    @allure.title("添加密码成功")
    @allure.description("随机添加三个index密码")
    def test_001_addpassword(self):
        # print("start_addpwd_test")
        logging.info("start_addpwd_test")
        # index = random.randint(0,128)
        # print("压力测试添加密码：")
        logging.info("压力测试添加密码：")
        i = 0
        success_count = 0
        fail_count = 0
        while i < self.count:
            i += 1
            for index in range(1,102) :
                self.add_pwd.payload_addpwd["data"][0]["v"] = index
                # payload["data"][1]["v"] = random.randint(000, 255)
                self.add_pwd.payload_addpwd["data"][4]["v"] = random.randint(000000, 99999999)
                command = self.add_pwd.payload_addpwd["command"]
                # print("下发命令：",command)
                logging.info("下发命令：%s",command)
                sno = self.add_pwd.add_lockpsw()
                result = self.judge_log.judge_result(sno, command)
                if result :
                    self.add_pass_index[(self.add_pwd.payload_addpwd["data"][0]["v"])] = self.add_pwd.payload_addpwd["data"][4]["v"]
                    success_count += 1
                    # print("成功次数：", success_count)
                    logging.info("成功次数：%d", success_count)
                else :
                    self.add_fail_index[(self.add_pwd.payload_addpwd["data"][0]["v"])] = self.add_pwd.payload_addpwd["data"][4]["v"]
                    fail_count += 1
                    # print("失败次数：", fail_count)
                    # print("断言失败，请检查结果！", sno)
                    logging.info("失败次数：%d", fail_count)
                    logging.info("%s: 断言失败，请检查结果！", sno)

                # print('成功次数为：', succeed_count)
                # logging.info("test_count:%d")
                # time.sleep(3)
                # print("已添加成功的index：", self.add_pass_index)
                logging.info("已添加成功的index：%s", self.add_pass_index)
                # print("添加失败的index：", self.add_fail_index)
                logging.info("添加失败的index：%s", self.add_fail_index)
        # 统计压力测试丢包率
        self.judge_log.statistics_loss_rate(success_count, fail_count)


    def test_002_lock_index_psw(self):
        # self.index_path = os.path.join(self.path, "..", "params",  "lock_index.txt")
        # print("打印路径:",self.index_pass_path)
        logging.info("打印路径: %s",self.index_pass_path)
        # 添加成功的index
        with open(self.index_pass_path, 'a') as obj:
            for i in self.add_pass_index.keys():
                obj.write(str(i) + ",")
        # 添加失败的index
        with open(self.index_fail_path, 'a') as obj:
            for i in self.add_fail_index.keys():
                obj.write(str(i) + ",")


    @allure.story("压力测试修改密码") #pass
    @allure.title("压力测试修改密码成功")
    @allure.description("压力测试修改已添加的index密码")
    def test_003_modifypassword(self):
        # print("压力测试修改密码：")
        logging.info("压力测试修改密码：")
        j = 0
        success_count = 0
        fail_count = 0
        while j < self.count:
            j += 1
            with open(self.index_pass_path) as obj:
                index = obj.read().split(',')
                # index = list(index)
                # print("打印index：", index, type(index))
                if len(index):
                    for i in index[:-1]:
                        # print("*"*22+"修改的index为："+i+"*"*22)
                        logging.info("*"*22+"修改的index为："+i+"*"*22)
                        self.modify_pwd.payload_modifypwd["data"][0]["v"] = i
                        self.modify_pwd.payload_modifypwd["data"][4]["v"] = random.randint(000000, 99999999)
                        command = self.modify_pwd.payload_modifypwd["command"]
                        # print("下发命令：", command)
                        logging.info("下发命令：%s", command)
                        sno = self.modify_pwd.modify_lockpsw()
                        result = self.judge_log.judge_result(sno, command)
                        if result :
                            self.modify_pass_index[(self.modify_pwd.payload_modifypwd["data"][0]["v"])] = \
                            self.modify_pwd.payload_modifypwd["data"][4]["v"]
                            success_count += 1
                            # print("成功次数：", success_count)
                            logging.info("成功次数：%d", success_count)

                        else :
                            self.modify_fail_index[(self.modify_pwd.payload_modifypwd["data"][0]["v"])] = \
                                self.modify_pwd.payload_modifypwd["data"][4]["v"]
                            # print( "ID为 "+i+" 修改密码失败！")
                            logging.info("ID为 "+i+" 修改密码失败！")
                            fail_count += 1
                            # print("失败次数：", fail_count)
                            logging.info("失败次数：%d", fail_count)
                            # print("断言失败，请检查结果！", sno)
                            logging.info("%s : 断言失败，请检查结果！", sno)

                        # print("已修改成功的index：", self.modify_pass_index)
                        logging.info("已修改成功的index：%s", self.modify_pass_index)
                        # print("修改失败的index：", self.modify_fail_index)
                        logging.info("修改失败的index：%s", self.modify_fail_index)
        # 统计压力测试丢包率
        self.judge_log.statistics_loss_rate(success_count, fail_count)


    @allure.story("根据ID查询密码")
    @allure.title("根据ID查询密码成功")
    # @allure.description("查询freeze 冻结,effective有效,notActive未生效,invalid无效 四种状态")
    # @pytest.mark.parametrize("status",["freeze","effectiv","notActive","invalid"],ids=["freeze","effective","notActive","invalid"])
    def test_005_getpassword(self):
        # print("压力测试查询密码：")
        logging.info("压力测试查询密码：")
        j = 0
        success_count = 0
        fail_count = 0
        while j < self.count:
            j += 1
            with open(self.index_pass_path) as obj:
                index = obj.read().split(',')
                # index = list(index)
                # print("打印index：", index, type(index))
                if len(index):
                    for i in index[:-1]:
                        # print("*" * 22 + "修改的index为：" + i + "*" * 22)
                        logging.info("*" * 22 + "修改的index为：" + i + "*" * 22)
                        self.get_pwd.payload_get_indexpwd["data"][0]["v"] = i
                        command = self.get_pwd.payload_get_indexpwd["command"]
                        # print("下发命令：", command)
                        logging.info("下发命令：%s", command)
                        sno = self.get_pwd.get_lockpsw()
                        result = self.judge_log.judge_result(sno, command)
                        if result :
                            success_count += 1
                            # print("成功次数：", success_count)
                            logging.info("成功次数：%d", success_count)

                        else :
                            fail_count += 1
                            # print("失败次数：", fail_count)
                            logging.info("失败次数：%d", fail_count)
                            # print("断言失败，请检查结果！", sno)
                            logging.info("%s : 断言失败，请检查结果！", sno)
        # 统计压力测试丢包率
        self.judge_log.statistics_loss_rate(success_count, fail_count)

    @allure.story("压力测试冻结密码")   # pass
    @allure.title("压力测试冻结密码成功")
    @allure.description("压力测试冻结已添加的index密码")
    def test_006_freezepassword(self):
        # print("压力测试冻结密码：")
        logging.info("压力测试冻结密码：")
        j = 0
        success_count = 0
        fail_count = 0
        while j < self.count:
            j += 1
            with open(self.index_pass_path) as obj:
                index = obj.read().split(',')
                # index = list(index)
                # print("打印index：", index, type(index))
                if len(index):
                    for i in index[:-1]:
                        # print("*"*22+"冻结的index为："+i+"*"*22)
                        logging.info("*"*22+"冻结的index为："+i+"*"*22)
                        self.freeze_pwd.payload_freezepwd["data"][0]["v"] = i
                        # self.modify_pwd.payload_modifypwd["data"][1]["v"] = random.randint(000000, 99999999)
                        command = self.freeze_pwd.payload_freezepwd["command"]
                        # print("下发命令：", command)
                        logging.info("下发命令：%s", command)
                        sno = self.freeze_pwd.freeze_lockpsw()
                        result = self.judge_log.judge_result(sno, command)
                        # print('成功次数为：', succeed_count)payload_modifypwd
                        # logging.info("test_count:%d")
                        # time.sleep(3)
                        if result :
                            self.delete_pass_index.append(i)
                            success_count += 1
                            # print("成功次数：", success_count)
                            logging.info("成功次数：%d", success_count)
                        else :
                            self.delete_fail_index.append(i)
                            fail_count += 1
                            # print("失败次数：", fail_count)
                            logging.info("失败次数：%s", fail_count)
                            # print("断言失败，请检查结果！", sno)
                            logging.info("%s: 断言失败，请检查结果！", sno)
                        # print("冻结成功的index：", self.delete_pass_index)
                        logging.info("冻结成功的index：%s", self.delete_pass_index)
                        # print("冻结失败的index：", self.delete_fail_index)
                        logging.info("冻结失败的index：%s", self.delete_fail_index)


    @allure.story("压力测试解冻密码")  # pass
    @allure.title("压力测试解冻密码成功")
    @allure.description("压力测试解冻已添加的index密码")
    def test_007_unfreezepassword(self):
        # print("压力测试解冻密码：")
        logging.info("压力测试解冻密码：")
        j = 0
        success_count = 0
        fail_count = 0
        while j < self.count:
            j += 1
            with open(self.index_pass_path) as obj:
                index = obj.read().split(',')
                # index = list(index)
                # print("打印index：", index, type(index))
                if len(index):
                    for i in index[:-1]:
                        # print("*" * 22 + "解冻的index为：" + i + "*" * 22)
                        logging.info("*" * 22 + "解冻的index为：" + i + "*" * 22)
                        self.unfreeze_pwd.payload_unfreezepwd["data"][0]["v"] = i
                        # self.modify_pwd.payload_modifypwd["data"][1]["v"] = random.randint(000000, 99999999)
                        command = self.unfreeze_pwd.payload_unfreezepwd["command"]
                        # print("下发命令：", command)
                        logging.info("下发命令：%s", command)
                        sno = self.unfreeze_pwd.unfreeze_lockpsw()
                        result = self.judge_log.judge_result(sno, command)
                        # print('成功次数为：', succeed_count)payload_modifypwd
                        # logging.info("test_count:%d")
                        # time.sleep(3)
                        if result:
                            self.delete_pass_index.append(i)
                            success_count += 1
                            # print("成功次数：", success_count)
                            logging.info("成功次数：%d", success_count)
                        else:
                            self.delete_fail_index.append(i)
                            fail_count += 1
                            # print("失败次数：", fail_count)
                            logging.info("失败次数：%d", fail_count)
                            # print("断言失败，请检查结果！", sno)
                            logging.info("%s: 断言失败，请检查结果！", sno)
                        # print("解冻成功的index：", self.delete_pass_index)
                        logging.info("解冻成功的index：%s", self.delete_pass_index)
                        # print("解冻失败的index：", self.delete_fail_index)
                        logging.info("解冻失败的index：%s", self.delete_fail_index)


    @allure.story("压力测试删除密码")   # pass
    @allure.title("压力测试删除密码成功")
    @allure.description("压力测试删除已添加的index密码")
    def test_008_deletepassword(self):
        # print("start_deletepwd_test")
        # print("压力测试删除密码：")
        logging.info("压力测试删除密码：")
        j = 0
        success_count = 0
        fail_count = 0
        while j < self.count:
            j += 1
            with open(self.index_pass_path) as obj:
                index = obj.read().split(',')
                # index = list(index)
                # print("打印index：", index, type(index))
                if len(index):
                    for i in index[:-1]:
                        # print("*"*22+"删除的index为："+i+"*"*22)
                        logging.info("*"*22+"删除的index为："+i+"*"*22)
                        self.delete_pwd.payload_deletepwd["data"][0]["v"] = i
                        # self.modify_pwd.payload_modifypwd["data"][1]["v"] = random.randint(000000, 99999999)
                        command = self.delete_pwd.payload_deletepwd["command"]
                        # print("下发命令：", command)
                        logging.info("下发命令：%s", command)
                        sno = self.delete_pwd.delete_lock_psw()
                        result = self.judge_log.judge_result(sno, command)
                        # print('成功次数为：', succeed_count)payload_modifypwd
                        # logging.info("test_count:%d")
                        # time.sleep(3)
                        if result :
                            self.delete_pass_index.append(i)
                            success_count += 1
                            # print("成功次数：", success_count)
                            logging.info("成功次数：%d", success_count)
                        else :
                            self.delete_fail_index.append(i)
                            fail_count += 1
                            # print("失败次数：", fail_count)
                            logging.info("失败次数：%d", fail_count)
                            # print("断言失败，请检查结果！", sno)
                            logging.info("%s:断言失败，请检查结果！", sno)
                        # print("已删除成功的index：", self.delete_pass_index)
                        logging.info("解冻成功的index：%s", self.delete_pass_index)
                        # print("删除失败的index：",self.delete_fail_index)
                        logging.info("解冻失败的index：%s", self.delete_fail_index)

        # 更新lock_pass_index表格：
        with open(self.index_pass_path, 'w') as obj:
            for i in self.delete_fail_index:
                obj.write(str(i) + ",")





if __name__ == '__main__':
    # unittest.main()
    pytest.main(['-v','test_lock_pressure_test.py'])