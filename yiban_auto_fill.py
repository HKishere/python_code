import uiautomator2 as ut2
import time
d = ut2.connect('192.168.1.101')
if (d.info.get('screenOn') == False):
    print("屏幕关闭,打开屏幕")
    d.screen_on()
print("屏幕已开启")
if d(resourceId="com.smartisanos.keyguard:id/kg_music_layer").exists:
    d.swipe(0.547, 0.900, 0.536, 0.119,0.4)
    d(resourceId="com.smartisanos.keyguard:id/easy_password_keyboard_1").click()
    d(resourceId="com.smartisanos.keyguard:id/easy_password_keyboard_5").click()
    d(resourceId="com.smartisanos.keyguard:id/easy_password_keyboard_8").click()
    d(resourceId="com.smartisanos.keyguard:id/easy_password_keyboard_3").click()
    print("解锁屏幕")
else:
    print("不需要解锁")
#d.press("back")
d.press("home")
time.sleep(0.5)
d.press("home")
time.sleep(0.2)
d.press("home")
sess = d.session("com.yiban.app")
print("进入易班")
time.sleep(10)
if d(resourceId="com.yiban.app:id/page_download_content").exists:
    d(resourceId="com.yiban.app:id/page_download_cancel").click()
d(resourceId="com.yiban.app:id/tv_name", text="信息上报").click()
time.sleep(12)
print()
while (d(resourceId="com.yiban.app:id/widget_custom_titlebar_center_title").get_text() != "我向大家报平安"):
    d(resourceId="com.yiban.app:id/widget_custom_titlebar_left_item").click()
    d(resourceId="com.yiban.app:id/tv_name", text="信息上报").click()
    time.sleep(12)
print("进入填写页面")
time.sleep(2)
d.click(0.456, 0.557)
d.click(0.456, 0.557)
time.sleep(1)
d.swipe(0.547, 0.317, 0.536, 0.119,0.2)
d.set_fastinput_ime(True)
d.click(0.382, 0.822)
d.send_keys("黄祚恺")
d.click(0.412, 0.068)
#选辅导员
d.swipe(0.547, 0.900, 0.536, 0.119,0.4)
d.click(0.29, 0.17)
time.sleep(1)
d.swipe(0.378, 0.922, 0.364, 0.733,0.2)
d.swipe(0.73, 0.824, 0.72, 0.857,0.2)
time.sleep(1)
d.swipe(0.729, 0.88, 0.726, 0.629,0.2)
d.click(0.937, 0.675)
#填下一个(是否无变化)
d.swipe(0.468, 0.914, 0.472, 0.545,0.3)
time.sleep(1)
d.click(0.444, 0.654)
time.sleep(1)
d.click(0.94, 0.738)
time.sleep(1)
#点击承诺书
d.click(0.108, 0.719)
time.sleep(1)
d.click(0.534, 0.329)
time.sleep(1)
d.click(0.513, 0.807)
print("填写完成")