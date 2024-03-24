# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Software: PyCharm
# @Version: V 0.1
# @Author: 珇逖
# @Contact: 1978192989@qq.com
# @Time: 2022/4/24 19:39
# @File : airsim4.py
# @Description  #TODO 


"""
 文件说明： 控制四旋翼起飞和降落(airsim api)
 
"""
# 使用 python 做AirSim仿真，必须导入 airsim 包。
import airsim

"""1 链接AirSim仿真环境"""
# connect to the AirSim simulator
#与 AirSim 建立连接，并且返回句柄（client），后面的每次操作需要使用这个句柄
client = airsim.MultirotorClient()
#检查通信是否建立成功，并且会在命令行中打印连接情况，这样你就可以判断程序是否和AirSim连接正常
client.confirmConnection()

"""2 获取控制权"""
#get control
#因为安全问题， API 控制默认是不开启的，遥控器有全部的控制权限。
# 所以必须要在程序中使用这个函数来获取控制权。
# 遥控器的操作会抢夺 API 的控制权，同时让 API 获取的控制权失效。
# 使用 isApiControlEnabled 可以检查 API 是否具有控制权。
client.enableApiControl(True)

"""3 解锁"""
# unlock
#但是实际上 AirSim 的开发人员希望在仿真中的代码可以直接移到现实中使用，
# 所以对于现实中的安全问题，还是开发了获取控制权和释放控制权、解锁和上锁等一系列安全操作
client.armDisarm(True)

"""4 起飞"""
# Async methods returns Future. Call join() to wait for task to complete.
#使用这个函数可以让无人机的旋翼启动和停止旋转。
client.takeoffAsync().join()

"""6 降落"""
#如果你想让程序在这里等待任务执行完，则只需要在后面加上.join()。本例子就是让程序在这里等待无人机起飞任务完成，然后再执行降落任务。
#新的任务会打断上一个没有执行完的任务，所以如果takeoff函数没有加 .join()，则最后的表现是无人机还没有起飞就降落了，无人机是不会起飞的。
client.landAsync().join()

"""7 上锁"""
# lock
client.armDisarm(False)

"""8 释放控制权"""
#release control
client.enableApiControl(False)

