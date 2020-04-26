# coding: utf-8
#
import uiautomator2 as u2
import time

def login(username):
    d.click(0.555, 0.406)
    time.sleep(3)
    try:
        d.xpath('//*[@resource-id="com.seeyon.cmp:id/et_login_username"]/android.widget.ImageView[1]').click()
        time.sleep(3)
    except:pass

    d(text="用户名").send_keys(username)
    time.sleep(3)

    #输入密码

    d.xpath('//*[@resource-id="com.seeyon.cmp:id/et_login_password"]/android.widget.EditText[1]').click()
    time.sleep(3)
    try:
        d.xpath('//*[@resource-id="com.seeyon.cmp:id/et_login_password"]/android.widget.ImageView[1]').click()
        time.sleep(3)
    except:
        pass

    d.xpath('//*[@resource-id="com.seeyon.cmp:id/et_login_password"]/android.widget.EditText[1]').click()
    time.sleep(3)
    d.send_keys('123456')
    time.sleep(3)
    d(resourceId="com.seeyon.cmp:id/btn_login").click()
    time.sleep(3)
    try:
        #跳过手势密码
        d(resourceId="com.seeyon.cmp:id/passBy").click()
        time.sleep(3)
    except:pass

def qiandao():
    #点击消息菜单
    d.xpath(
        '//*[@resource-id="com.seeyon.cmp:id/tabLayout"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').click()
    time.sleep(3)
    #点击签到
    d(resourceId="com.seeyon.cmp:id/msg_tv_name", text="签到").click()
    time.sleep(3)
    d.xpath('//android.widget.ListView/android.view.View[3]/android.view.View[2]/android.view.View[1]')
    time.sleep(3)
    d.xpath(
        '//*[@resource-id="index-container"]/android.view.View[4]/android.view.View[1]/android.view.View[1]').click()
    time.sleep(3)
    d.xpath('//android.widget.ListView/android.view.View[2]/android.view.View[1]').click()
    time.sleep(3)
    d(description="提交").click()
    time.sleep(3)
def exit():
    d(description="返回").click()
    time.sleep(3)
    d(description="消息").click()
    time.sleep(3)
    #点击我的
    d.xpath(
        '//*[@resource-id="com.seeyon.cmp:id/tabLayout"]/android.widget.RelativeLayout[5]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').click()
    time.sleep(3)
    #设置
    d.xpath('//*[@resource-id="setting"]/android.view.View[1]').click()
    time.sleep(3)
    #退出登录
    d(description="退出登录").click()
    time.sleep(3)
    #确认退出
    d(resourceId="com.seeyon.cmp:id/buttonDefaultPositive").click()
    time.sleep(3)
if __name__ == '__main__':
    d = u2.connect()

    users = ['luyanhong','baomeijun']
    for user in users:
        login(user)
        qiandao()
        exit()
