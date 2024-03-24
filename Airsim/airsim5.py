# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Software: PyCharm
# @Version: V 0.1
# @Author: 珇逖
# @Contact: 1978192989@qq.com
# @Time: 2022/4/24 20:02
# @File : airsim5.py
# @Description  #TODO 位置控制无人机飞行


"""
 文件说明： 位置控制无人机飞行
 
"""
"""
square flight
"""
import airsim
import time

"""1 链接AirSim仿真环境"""
# connect to the AirSim simulator
client = airsim.MultirotorClient()

"""2 获取控制权"""
client.enableApiControl(True)  # get control

"""3 解锁"""
client.armDisarm(True)  # unlock

"""4 起飞"""
client.takeoffAsync().join()  # takeoff

"""5 飞行状态控制"""
"""上升"""
# square flight
#moveToZAsync(z, velocity) 是高度控制 API，
# 第一个参数是高度，第二个参数是速度。实现的效果是以 1m/s 的速度飞到 3 米高。
# .join() 后缀的意思是程序在这里等待直到任务完成，也就是四旋翼达到 3 米的高度。
# 如果不加.join()后缀，则不用等待任务是否完成，函数直接返回，程序继续往下执行。
client.moveToZAsync(-3, 1).join()  # 上升到3m高度
#moveToPositionAsync(x, y, z, velocity) 是水平位置控制 API，
# x,y,z是全局坐标位置，velocity是速度。
# 实现的效果是以 1m/s 的速度飞到 (5, 0) 点，3m 高的位置。
# .join() 后缀的意思是程序在这里等待直到任务完成，也就是四旋翼到达目标位置点，同时到达设置的高度。
# 如果不加 .join() 后缀，则不用等待任务是否完成，函数直接返回，程序继续往下执行。
client.moveToPositionAsync(5, 0, -3, 1).join()  # 飞到（5,0）点坐标
client.moveToPositionAsync(5, 5, -3, 1).join()  # 飞到（5,5）点坐标
client.moveToPositionAsync(0, 5, -3, 1).join()  # 飞到（0,5）点坐标
client.moveToPositionAsync(0, 0, -3, 1).join()  # 回到（0,0）点坐标

"""6 降落"""
client.landAsync().join()  # land
"""7 上锁"""
client.armDisarm(False)  # lock
"""8 释放控制权"""
client.enableApiControl(False)  # release control