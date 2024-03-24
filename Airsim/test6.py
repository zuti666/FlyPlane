# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Software: PyCharm
# @Version: V 0.1
# @Author: 珇逖
# @Contact: 1978192989@qq.com
# @Time: 2022/4/24 22:01
# @File : test6.py
# @Description  #TODO 飞正方形（速度控制无人机）


"""
 文件说明：  速度控制无人机飞正方形
 
"""
"""
 飞正方形（速度控制）
 """
import airsim
import time

"""1 链接AirSim仿真环境"""
client = airsim.MultirotorClient()  # connect to the AirSim simulator

"""2 获取控制权"""
client.enableApiControl(True)       # 获取控制权
"""3 解锁"""
client.armDisarm(True)              # 解锁

"""4 起飞"""
client.takeoffAsync().join()        # 第一阶段：起飞

"""5 飞行状态控制"""
#moveToZAsync(z, velocity) 是高度控制 API，
# 第一个参数是高度，第二个参数是速度。实现的效果是以 1m/s 的速度飞到 3 米高。
# .join() 后缀的意思是程序在这里等待直到任务完成，也就是四旋翼达到 3 米的高度。
# 如果不加.join()后缀，则不用等待任务是否完成，函数直接返回，程序继续往下执行。
"""上升"""
client.moveToZAsync(-2, 1).join()   # 第二阶段：上升到2米高度

"""飞正方形"""
# 飞正方形
#速度控制函数，让四旋翼在z的高度，以vx, vy的速度，飞行duration秒。
# .join()是程序在这里等待任务执行完成。
client.moveByVelocityZAsync(1, 0, -2, 8).join()     # 第三阶段：以1m/s速度向前飞8秒钟
client.moveByVelocityZAsync(0, 1, -2, 8).join()     # 第三阶段：以1m/s速度向右飞8秒钟
client.moveByVelocityZAsync(-1, 0, -2, 8).join()    # 第三阶段：以1m/s速度向后飞8秒钟
client.moveByVelocityZAsync(0, -1, -2, 8).join()    # 第三阶段：以1m/s速度向左飞8秒钟

# 悬停 2 秒钟
#这句指令的功能是让四旋翼在当前位置悬停。
client.hoverAsync().join()          # 第四阶段：悬停6秒钟

time.sleep(6)

"""6 降落"""
client.landAsync().join()           # 第五阶段：降落
"""7 上锁"""
client.armDisarm(False)             # 上锁
"""8 释放控制权"""
client.enableApiControl(False)      # 释放控制权