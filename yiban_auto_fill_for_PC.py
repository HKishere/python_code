import uiautomator2 as ut2
import os
import subprocess
import time
try:
    d = ut2.connect('127.0.0.1:62025')
    print('模拟器启动,连接成功')
except RuntimeError as reason:
    print('看样子模拟器没启动'+str(reason))
    print('启动模拟器')
    run_simulator = subprocess.Popen(r"Nox.exe -clone:Nox_1")
    d = ut2.connect('127.0.0.1:62025')
    print('模拟器启动,连接成功')

def Init():
    if (d.info.get('screenOn') == False):
        print("屏幕关闭,打开屏幕")
        d.screen_on()
    print("屏幕已开启")
    if d(resourceId="com.smartisanos.keyguard:id/kg_music_layer").exists:
        d.swipe(0.547, 0.900, 0.536, 0.119,0.4)
        print("解锁屏幕")
    else:
        print("不需要解锁")
    #d.press("back")
    d.press("home")
    time.sleep(0.1)
    d.press("home")

def Open_yiban():
    sess = d.session("com.yiban.app")
    print("进入易班")
    time.sleep(14)
    if d(resourceId="com.yiban.app:id/page_download_content").exists:
        d(resourceId="com.yiban.app:id/page_download_cancel").click()
    d(resourceId="com.yiban.app:id/tv_name", text="信息上报").click()
    time.sleep(5)
    print()
    while (d(resourceId="com.yiban.app:id/widget_custom_titlebar_center_title").get_text() != "我向大家报平安"):
        d(resourceId="com.yiban.app:id/widget_custom_titlebar_left_item").click()
        d(resourceId="com.yiban.app:id/tv_name", text="信息上报").click()
        time.sleep(8)
    print("进入填写页面")

def Auto_Fill():
    time.sleep(2)
    d.click(0.488, 0.5)
    d.click(0.488, 0.5)

    d.click(0.456, 0.917)
    d.set_fastinput_ime(True)
    d.click(0.454, 0.92)
    d.send_keys("黄祚恺")
    #d.set_fastinput_ime(False)

    d.click(0.990, 0.68)
    time.sleep(0.5)
    d.swipe(0.465, 0.590, 0.465, 0.140,0.4)
    time.sleep(0.7)
    d.swipe(0.465, 0.690, 0.465, 0.080,0.4)
    time.sleep(0.7)
    d.click(0.278, 0.289)
    time.sleep(0.7)
    d.swipe(0.385, 0.966, 0.379, 0.780,0.2)
    d.swipe(0.758, 0.851, 0.755, 0.860,0.1)
    time.sleep(0.5)
    d.swipe(0.787, 0.951, 0.787, 0.670,0.2)
    d.click(0.698, 0.572)
    time.sleep(0.7)

    d.swipe(0.965, 0.990, 0.965, 0.500,0.2)
    d.click(0.344, 0.687)
    d.click(0.551, 0.618)
    time.sleep(0.5)
    d.click(0.089, 0.752)
    time.sleep(0.5)
    d.click(0.701, 0.273)
    time.sleep(0.5)
    d.click(0.666, 0.836)
    print("填写完成")

def main():
    clock = time.localtime()
    while (clock.tm_hour != 1):
        print("时候未到")
        clock =time.localtime()
        time.sleep(60)
    Init()
    Open_yiban()
    Auto_Fill()
    print("准备关机")
    os.system('shutdown -s -f -t 59')


if __name__ == "__main__":
    main()