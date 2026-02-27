# ！/usr/bin/env python
# -*- coding:utf8 -*-
# author:yangyaxin time::11:07
import logging
import random
# from common.log import LoggingInit
from interface.add_lockpsw import AddLockPwd
from interface.add_seedpsw import AddSeedPwd
from interface.get_seedpsw import GetSeedPwd
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
        self.devId = "00124b0029402ca5"
        self.prodTypeId = "ZH-B0109"
        self.add_seed = AddSeedPwd(self.devId, self.prodTypeId)
        self.get_seed = GetSeedPwd(self.devId,self.prodTypeId)
        self.add_pwd = AddLockPwd(self.devId, self.prodTypeId)
        self.modify_pwd = ModifyLockPsw(self.devId, self.prodTypeId)
        self.get_pwd = GetLockPwd(self.devId,self.prodTypeId)
        self.delete_pwd = DeleteLockPsw(self.devId,self.prodTypeId)
        self.freeze_pwd = FreezeLockPwd(self.devId,self.prodTypeId)
        self.unfreeze_pwd = UnFreezeLockPwd(self.devId,self.prodTypeId)
        self.clear_pwd = ClearLockPwd(self.devId,self.prodTypeId)
        self.logging_init = LoggingInit()
        # SecureCRT日志存放路径
        self.dir = r'D:\Work(勿删）\03 项目\log\10.1.2.1-10.1.2.1 (max3)'
        # 日志最新存放路径
        self.log_path = r'D:\Work(勿删）\04 _自动化项目\auto_testplat\智能锁\lock\log\log_file\\'
        self.judge_log = JudgeLog(self.dir, self.log_path)
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
        self.freeze_pass_index = []
        self.unfreeze_fail_index = []
        self.unfreeze_pass_index = []
        self.freeze_fail_index = []
        self.seed_pass = []
        self.seed_fail = []
        # # 创建变量：保存查询密码的总数,列表：存放密码index
        # self.reportTotalNum = []
        # self.notify_list = []
        # sys.stdout = Logger(r'D:\Work(勿删）\04 _自动化项目\auto_testplat\z_touch\log\test_log\ztouch_log.txt', sys.stdout)
        sys.stdout = Logger(os.path.join(self.path, "..", "log", "test_log", "log_1a60.txt"), sys.stdout)
        sys.stderr = Logger(os.path.join(self.path, "..", "log", "test_log", "log_1a60_error.txt"), sys.stderr)

    @allure.epic("测试门锁")
    @allure.feature("日志存储")
    @allure.story("日志")  # pass
    @allure.title("日志")
    @allure.description("日志保存")
    def test_000_log(self):
        self.logging_init.logging_init(self.devId)

    @allure.epic("测试门锁")
    @allure.feature("设置种子")
    @allure.story("添加密码种子")
    @allure.title("添加密码种子成功")
    @allure.description("添加密码种子")
    def test_001_addseed(self):
        # print("start_addseed_test")
        logging.info("start_addseed_test")
        # index = random.randint(0,128)
        # self.add_pwd.payload_addpwd["data"][0]["v"] = index
        # payload["data"][1]["v"] = random.randint(000, 255)
        self.add_seed.payload_addseed["data"][0]["v"] = random.randint(100000, 999999)
        command = self.add_seed.payload_addseed["command"]
        # print("下发命令：",command)
        logging.info("下发命令：%s",command)
        sno = self.add_seed.add_seedpsw()
        result = self.judge_log.judge_result(sno, command)
        if result :
            self.seed_pass.append(self.add_seed.payload_addseed["data"][0]["v"])
        else :
            self.seed_fail.append(self.add_seed.payload_addseed["data"][0]["v"])
        pytest.assume(result)
        # print('成功次数为：', succeed_count)
        # logging.info("test_count:%d")
        # time.sleep(3)
        # print("已添加成功的seed：",self.seed_pass)
        # print("添加失败的seed：",self.seed_fail)
        logging.info("已添加成功的seed：%s",self.seed_pass)
        logging.info("添加失败的seed：%s", self.seed_fail)

    @allure.epic("测试门锁")
    @allure.feature("设置种子")
    @allure.story("查询密码种子")
    @allure.title("查询密码种子成功")
    @allure.description("查询密码种子")
    def test_002_getseed(self):
        # print("start_checkseed_test")
        logging.info("start_checkseed_test")
        # index = random.randint(0,128)
        # for index in range(0, 130):
        for seed in self.seed_pass :
            # self.add_pwd.payload_addpwd["data"][0]["v"] = index
            # payload["data"][1]["v"] = random.randint(000, 255)
            self.get_seed.payload_getseed["data"][0]["v"] = seed
            command = self.get_seed.payload_getseed["command"]
            # print("下发命令：", command)
            logging.info("下发命令：%s", command)
            sno = self.get_seed.get_seedpsw()
            result = self.judge_log.judge_result(sno, command)
            pytest.assume(result)

    @allure.epic("测试门锁")
    @allure.feature("设置密码")
    @allure.story("随机添加密码") #pass
    @allure.title("添加密码成功")
    @allure.description("随机添加三个index密码")
    def test_003_addpassword(self):
        # print("start_addpwd_test")
        logging.info("start_addpwd_test")
        # index = random.randint(0,128)
        for index in range(1,2) :
            self.add_pwd.payload_addpwd["data"][0]["v"] = index
            # payload["data"][1]["v"] = random.randint(000, 255)
            self.add_pwd.payload_addpwd["data"][4]["v"] = random.randint(100000, 99999999)
            command = self.add_pwd.payload_addpwd["command"]
            # print("下发命令：",command)
            logging.info("下发命令：%s",command)
            sno = self.add_pwd.add_lockpsw()
            result = self.judge_log.judge_result(sno, command)
            if result :
                self.add_pass_index[(self.add_pwd.payload_addpwd["data"][0]["v"])] = self.add_pwd.payload_addpwd["data"][4]["v"]
            else :
                self.add_fail_index[(self.add_pwd.payload_addpwd["data"][0]["v"])] = self.add_pwd.payload_addpwd["data"][4]["v"]

            pytest.assume(result)
            # print('成功次数为：', succeed_count)
            # logging.info("test_count:%d")
            # time.sleep(3)
            # print("已添加成功的index：",self.add_pass_index)
            logging.info("已添加成功的index：%s",self.add_pass_index)
            # print("添加失败的index：",self.add_fail_index)
            logging.info("添加失败的index：%s",self.add_fail_index)

    def test_004_lock_index_psw(self):
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

    @allure.epic("测试门锁")
    @allure.feature("修改密码")
    @allure.story("修改密码") #pass
    @allure.title("修改密码成功")
    @allure.description("修改已添加的index密码")
    def test_005_modifypassword(self):
        # print("start_modifypwd_test")
        logging.info("start_modifypwd_test")
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
                    pytest.assume(result)
                    # print('成功次数为：', succeed_count)payload_modifypwd
                    # logging.info("test_count:%d")
                    # time.sleep(3)
                    if result :
                        self.modify_pass_index[(self.modify_pwd.payload_modifypwd["data"][0]["v"])] = \
                        self.modify_pwd.payload_modifypwd["data"][4]["v"]
                        # print("已修改成功的index：", self.modify_pass_index)
                        logging.info("已修改成功的index：%s", self.modify_pass_index)
                    else :
                        self.modify_fail_index[(self.modify_pwd.payload_modifypwd["data"][0]["v"])] = \
                            self.modify_pwd.payload_modifypwd["data"][4]["v"]
                        # print( "ID为 "+i+" 修改密码失败！")
                        logging.info("ID为 "+i+" 修改密码失败！")
                        # print("修改失败的index：", self.modify_fail_index)
                        logging.info("修改失败的index：%s", self.modify_fail_index)

    @allure.epic("测试门锁")
    @allure.feature("设置密码")
    @allure.story("查询密码")
    @allure.title("查询密码成功")
    @allure.description("查询freeze 冻结,effective有效,notActive未生效,invalid无效 四种状态")
    @pytest.mark.parametrize("status",["1","2","3","4"],ids=["freeze","effective","notActive","invalid"])
    def test_006_getpassword(self,status):
        # print("start_getpwd_test")
        logging.info("start_getpwd_test")
        # payload["data"][1]["v"] = random.randint(000, 255)
        self.get_pwd.payload_getpwd["data"][0]["v"] =status
        command = self.get_pwd.payload_getpwd["command"]
        # print("下发命令：", command)
        logging.info("下发命令：%s", command)
        sno = self.get_pwd.get_lockpsw()
        result = self.judge_log.judge_result(sno,command)
        pytest.assume(result)
        # print("已添加成功的index：", self.add_index)

    @allure.epic("测试门锁")
    @allure.feature("设置密码")
    @allure.story("根据ID查询密码")
    @allure.title("根据ID查询密码成功")
    @allure.description("根据ID查询密码成功")
    # @allure.description("查询freeze 冻结,effective有效,notActive未生效,invalid无效 四种状态")
    # @pytest.mark.parametrize("status",["freeze","effectiv","notActive","invalid"],ids=["freeze","effective","notActive","invalid"])
    def test_007_getpassword(self):
        # print("start_checkpwd_test")
        logging.info("start_checkpwd_test")
        # payload["data"][1]["v"] = random.randint(000, 255)
        with open(self.index_pass_path) as obj:
            index = obj.read().split(',')
            # index = list(index)
            # print("打印index：", index, type(index))
            if len(index):
                for i in index[:-1]:
                    # print("*"*22+"修改的index为："+i+"*"*22)
                    logging.info("*"*22+"修改的index为："+i+"*"*22)
                    self.get_pwd.payload_get_indexpwd["data"][0]["v"] = i
                    command = self.get_pwd.payload_get_indexpwd["command"]
                    # print("下发命令：", command)
                    logging.info("下发命令：%s", command)
                    sno = self.get_pwd.get_index_lockpsw()
                    result = self.judge_log.judge_result(sno, command)
                    pytest.assume(result)
                    # print("已添加成功的index：", self.add_index)

    @allure.epic("测试门锁")
    @allure.feature("设置密码")
    @allure.story("冻结密码")   # pass
    @allure.title("冻结密码成功")
    @allure.description("冻结已添加的index密码")
    def test_008_freezepassword(self):
        # print("start_freezepwd_test")
        logging.info("start_freezepwd_test")
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
                    pytest.assume(result)
                    # print('成功次数为：', succeed_count)payload_modifypwd
                    # logging.info("test_count:%d")
                    # time.sleep(3)
                    if result :
                        self.freeze_pass_index.append(i)
                        # print("冻结成功的index：", self.delete_pass_index)
                        logging.info("冻结成功的index：%s", self.freeze_pass_index)

                    else :
                        self.freeze_pass_index.append(i)
                        # print("冻结失败的index：",self.delete_fail_index)
                        logging.info("冻结失败的index：%s",self.freeze_fail_index)

    @allure.epic("测试门锁")
    @allure.feature("设置密码")
    @allure.story("解冻密码")  # pass
    @allure.title("解冻密码成功")
    @allure.description("解冻已添加的index密码")
    def test_009_unfreezepassword(self):
        # print("start_unfreezepwd_test")
        logging.info("start_unfreezepwd_test")
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
                    pytest.assume(result)
                    # print('成功次数为：', succeed_count)payload_modifypwd
                    # logging.info("test_count:%d")
                    # time.sleep(3)
                    if result:
                        self.unfreeze_pass_index.append(i)
                        # print("解冻成功的index：", self.delete_pass_index)
                        logging.info("解冻成功的index：%s", self.unfreeze_pass_index)

                    else:
                        self.unfreeze_pass_index.append(i)
                        # print("解冻失败的index：", self.delete_fail_index)
                        logging.info("解冻失败的index：%s", self.unfreeze_fail_index)

    @allure.epic("测试门锁")
    @allure.feature("删除密码")
    @allure.story("删除密码")   # pass
    @allure.title("删除密码成功")
    @allure.description("删除已添加的index密码")
    def test_010_deletepassword(self):
        # print("start_deletepwd_test")
        logging.info("start_deletepwd_test")
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
                    pytest.assume(result)
                    # print('成功次数为：', succeed_count)payload_modifypwd
                    # logging.info("test_count:%d")
                    # time.sleep(3)
                    if result :
                        self.delete_pass_index.append(i)
                        # print("已删除成功的index：", self.delete_pass_index)
                        logging.info("已删除成功的index：%s", self.delete_pass_index)

                    else :
                        self.delete_fail_index.append(i)
                        # print("删除失败的index：",self.delete_fail_index)
                        logging.info("删除失败的index：%s",self.delete_fail_index)

        # 更新lock_pass_index表格：
        with open(self.index_pass_path, 'w') as obj:
            for i in self.delete_fail_index:
                obj.write(str(i) + ",")

    @allure.epic("测试门锁")
    @allure.feature("删除密码")
    @allure.story("总清密码") #pass
    @allure.title("总清密码成功")
    @allure.description("总清index密码")
    def test_011_clearpassword(self):
        # print("start_clearpwd_test")
        logging.info("start_clearpwd_test")
        # index = random.randint(0,128)
        # for index in range(0,130) :
        # self.add_pwd.payload_addpwd["data"][0]["v"] = index
        # payload["data"][1]["v"] = random.randint(000, 255)
        # self.add_pwd.payload_addpwd["data"][4]["v"] = random.randint(000000, 99999999)
        command = self.clear_pwd.payload_clearpwd["command"]
        # print("下发命令：",command)
        logging.info("下发命令：%s",command)
        sno = self.clear_pwd.clear_lockpsw()
        result = self.judge_log.judge_result(sno, command)
        pytest.assume(result)





if __name__ == '__main__':
    # unittest.main()
    pytest.main(['-vs','test_lock_function.py'])
