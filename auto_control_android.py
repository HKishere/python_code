import uiautomator2 as ut2
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

def Connect_Init():
    if (d.info.get('screenOn') == False):
        print("屏幕关闭,打开屏幕")
        d.screen_on()
    print("屏幕已开启")
    if d(resourceId="com.smartisanos.keyguard:id/kg_music_layer").exists:
        d.swipe(0.547, 0.900, 0.536, 0.119,0.4)
        print("解锁屏幕")
    else:
        print("不需要解锁")
    return d

def XiZi_FaceMask():
    sess = d.session("com.xizi.quan")
    time.sleep(4)
    d.swipe(0.465, 0.390, 0.465, 0.640,0.3)
    d.swipe(0.465, 0.390, 0.465, 0.640,0.3)
    time.sleep(3)
    d(resourceId="com.xizi.quan:id/sign_base_layout").click()
    d.xpath('//*[@resource-id="root"]/android.view.View[1]/android.view.View[1]/android.view.View[1]').click()
    d(text="eRYCoEDqB7rCnYa1DZVMkKZKwrUYLwdcULYLauWAYD1hUcWhQ6UEu69KdbSkc3gG5j0zDQI0UPJj3e9JLQq0YvLL327ceDPkEfKe0yZbrjA0wAAAAASUVORK5CYII=").click()
    d.xpath('//android.widget.Button').click()
    i = 0
    clock = time.localtime()
    while 1:
        #d.click(0.67, 0.903)
        d.xpath('//android.widget.Button').click()
        i = i + 1
        print("点击第%d次" % i)
        if ((clock.tm_hour==7) and (clock.tm_min==55)):
            print("刷新一下")
            d.click(0.947, 0.057)
            time.sleep(0.2)
            d.click(0.148, 0.904)
            time.sleep(0.7)
            d.click(0.075, 0.839)
            d(text="eRYCoEDqB7rCnYa1DZVMkKZKwrUYLwdcULYLauWAYD1hUcWhQ6UEu69KdbSkc3gG5j0zDQI0UPJj3e9JLQq0YvLL327ceDPkEfKe0yZbrjA0wAAAAASUVORK5CYII=").click()
        if ((clock.tm_hour == 8) and (clock.tm_min == 3)):
            sess.close()
            return 

def main():
    Connect_Init()
    XiZi_FaceMask()

if __name__ == "__main__":
    main()
