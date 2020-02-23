import uiautomator2 as ut2
import os
import subprocess
import time
try:
    d = ut2.connect('127.0.0.1:21513')
    print('模拟器启动,连接成功')
except RuntimeError as reason:
    print('看样子模拟器没启动'+str(reason))
    print('启动模拟器')
    run_simulator = subprocess.Popen(r"E:\Microvirt\MEmu\MEmu.exe MEmu_1")
    time.sleep(5)
    d = ut2.connect('127.0.0.1:21513')
    print('模拟器启动,连接成功')

def Init():
    if (d.info.get('screenOn') == False):
        print("屏幕关闭,打开屏幕")
        d.screen_on()
    print("屏幕已开启")
    #d.press("back")
    d.press("home")
    time.sleep(0.1)
    d.press("home")

def Open_yiban():
    sess = d.session("com.yiban.app")
    print("进入易班")
    time.sleep(10)
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
    d.xpath('//*[@resource-id="form0content"]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View[2]').click()
    d.xpath('//*[@resource-id="form0content"]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View[2]').click()
    d.set_fastinput_ime(True)
    d.xpath('//*[@resource-id="form0content"]/android.view.View[2]/android.view.View[2]/android.view.View[5]/android.view.View[3]/android.view.View[2]').click()
    d.send_keys("黄祚恺")
    d.xpath('//*[@resource-id="com.yiban.app:id/relative"]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]').click()
    d.swipe(0.961, 0.971, 0.974, 0.092, 0.2)
    d.xpath('//*[@text="请输入辅导员"]').click()
    time.sleep(0.7)
    d.swipe(0.385, 0.966, 0.379, 0.820, 0.2)
    d.swipe(0.773, 0.854, 0.773, 0.900, 0.2)
    d.swipe(0.773, 0.854, 0.773, 0.730, 0.2)
    d.xpath('//*[@text="完成"]').click()
    time.sleep(0.7)
    d.xpath('//*[@resource-id="form0content"]/android.view.View[2]/android.view.View[2]/android.view.View[15]/android.view.View[3]/android.view.View[2]').click()
    d.xpath('//*[@text="与湖北人员或湖北返乡人员接触、经停湖北、确诊/疑似接触等三种情况：时间、位置、具体描述等。如没有以上情况则填写“无”。"]').click()
    d.xpath('//*[@resource-id="weuiAgree"]').click()
    time.sleep(1)
    d.click(0.451, 0.208)
    time.sleep(1)
    d.xpath('//*[@resource-id="btn"]').click()
    print("填写完成")

def main():
    clock = time.localtime()
    print("现在时间:%d:%d"%(clock.tm_hour,clock.tm_min))
    Init()
    Open_yiban()
    Auto_Fill()
    print("准备关机")
    os.system('shutdown -s -f -t 59')


if __name__ == "__main__":
    main()
