import cv2
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import threading
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog

def select_file_path(): #选择视频路径
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    video_path = filedialog.askopenfilename()  # 选择文件

    if video_path:
        print(f"Selected file path: {video_path}")
        return video_path
    else:
        print("No file selected.")

def get_user_input(): # 线程数，建议CPU线程数-1
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    thread_num = simpledialog.askinteger("输入线程", "请输入一个整数作为线程数：(建议设置为CPU线程数-1)")

    if thread_num is not None:
        print(f"User input: {thread_num}")
        return thread_num
    else:
        print("No input provided.")
video_path = select_file_path()
thread_num = get_user_input()
out_path = "VideoTestOut/"  # 输出目录
huaZhi = 1  # 清晰度，最低1，无上限

# -----以下为程序使用变量-----#
video_info = []

num = 0

info = []
'''
图片转换成字符里面的相关大小，
为元组，第一个是resize的宽高，第二个是图片输出的宽高
'''

video = cv2.VideoCapture(video_path)

# 定义一个线程安全的队列来存储待处理的图片
image_queue = []

# 获取视频信息
def getVideoInfo() -> list:
    ret = []

    (major_ver, minor_ver, subminor_ver) = cv2.__version__.split('.')
    if int(major_ver) < 3:
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
    else:
        fps = video.get(cv2.CAP_PROP_FPS)

    ret.append(fps)  # 视频帧数
    ret.append(video.read()[1].shape[0])  # 视频高度
    ret.append(video.read()[1].shape[1])  # 视频宽度
    return ret

# 获取视频所有截图
def outVideoAllCapture():
    # 判断载入视频是否可以打开
    ret = video.isOpened()
    global num
    # 循环读取视频帧
    while ret:
        num = num + 1
        # 进行单张图片的读取,ret的值为True或者Flase,frame表示读入的图片
        ret, frame = video.read()
        if ret:
            cv2.imwrite(out_path + str(num) + '.jpg', frame)
            image_queue.append(out_path + str(num) + '.jpg')  # 将图片路径加入队列
            cv2.waitKey(1)
        else:
            break

# 单张图片转换成字符画
def imageToChar(filename, number):
    # 字符列表
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~            <>i!lI;:,\"^`'. ")
    # 判断图片是否存在
    if os.path.exists(filename):
        # 将图片转化为灰度图像,并重设大小
        img_array = np.array(Image.open(filename).resize(info[0], Image.LANCZOS).convert('L'))  # resize里面 宽, 高 输出宽高/7
        # 创建新的图片对象
        img = Image.new('L', info[1], 255)  # 宽, 高
        draw_object = ImageDraw.Draw(img)
        # 设置字体
        font = ImageFont.truetype('consola.ttf', 10, encoding='unic')
        # 根据灰度值添加对应的字符
        for j in range(info[0][1]):  # 是resize的高
            for k in range(info[0][0]):  # 宽
                x, y = k * 8, j * 8
                index = int(img_array[j][k] / 4)
                draw_object.text((x, y), ascii_char[index], font=font, fill=0)
        # 保存字符图片
        img.save(out_path + str(number) + "g.jpg", 'JPEG')
        cv2.imwrite(out_path + str(number) + "g.jpg", cv2.imread(out_path + str(number) + "g.jpg"),
                    [cv2.IMWRITE_JPEG_QUALITY, 2])
        os.remove(out_path + str(number) + '.jpg')  # 删除原始图片
        print("已成功把第" + str(number) + "帧转换成字符画")

# 工作线程函数
def worker():
    while True:
        if image_queue:
            filename = image_queue.pop(0)
            number = int(os.path.splitext(os.path.basename(filename))[0])
            imageToChar(filename, number)
        else:
            break

def mergeImage():
    print("开始将图片合并成MP4视频")
    # global num
    videoWriter = cv2.VideoWriter(out_path + 'out.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), video_info[0],
                                  info[1])
    for i in range(1, num):
        filename = out_path + str(i) + 'g.jpg'
        if os.path.exists(filename):
            img = cv2.imread(filename=filename)
            cv2.waitKey(100)
            videoWriter.write(img)
    print("完成图片合并成MP4视频")

def deleteImg():
    print("开始删除转换图片")
    global num
    for i in range(1, num):
        os.remove(out_path + str(i) + 'g.jpg')
    print("删除转换图片完毕")

if __name__ == "__main__":
    if not os.path.exists(out_path):  # 如果没有这个输出目录就创建
        os.makedirs(out_path)

    video_info = getVideoInfo()  # 获取视频信息
    info.append((int(video_info[2] * huaZhi / 8), int(video_info[1] * huaZhi / 8)))  # 添加计算设置数值
    info.append((int(video_info[2] * huaZhi / 8) * 8, int(video_info[1] * huaZhi / 8) * 8))  # 添加计算设置数值
    # print(info)

    outVideoAllCapture()  # 截取视频所有帧

    threads = []
    for _ in range(thread_num):  # 创建多个工作线程
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    for t in threads:  # 等待所有工作线程完成
        t.join()

    mergeImage()  # 合并图片成视频
    deleteImg()  # 删除每一帧的字符画

    video.release()