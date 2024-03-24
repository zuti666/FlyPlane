# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Software: PyCharm
# @Version: V 0.1
# @Author: 珇逖
# @Contact: 1978192989@qq.com
# @Time: 2022/5/4 11:41
# @File : airsim-car-0.py
# @Description  #TODO 


"""
 文件说明： 
 
"""
# 使用 python 做AirSim仿真，必须导入 airsim 包。
import airsim

"""1 链接AirSim仿真环境"""
# connect to the AirSim simulator
#与 AirSim 建立连接，并且返回句柄（client），后面的每次操作需要使用这个句柄
client = airsim.CarClient()
#检查通信是否建立成功，并且会在命令行中打印连接情况，这样你就可以判断程序是否和AirSim连接正常
client.confirmConnection()
