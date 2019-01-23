#浏览器组件
from selenium import webdriver
#错误类型
from ExceptionKinds import *

def CreateBrowser():

    while True:
        try:
            browser=webdriver.Chrome()
            return browser
        except:
            print('ChromeDriver配置错误或版本不匹配，请尝试输入ChromeDriver的位置：')


def Login(browser):
    url = 'http://jwxt.neuq.edu.cn/jwglxt'
    browser.get(url)
    print('请输入你的信息')
    username=input('学号：')
    passwd=input('密码：')
    #登录
    while True:
        try:
            browser.find_element_by_id('yhm').send_keys(username)
            browser.find_element_by_id('mm').send_keys(passwd)
            #判断是否有验证码
            try:
                CodeRegion=browser.find_element_by_xpath('//*[@id="yzm"]')
                Code=input('请输入验证码：')
                CodeRegion.send_keys(Code)
            except:
                pass

            defaultUrl=browser.current_url
            browser.find_element_by_xpath('//*[@id="dl"]').click()

            #判断页面是否改变
            try:
                browser.find_element_by_xpath('//*[@id="dl"]')
            except:
                print('登录成功')
                break
            tipsFlag=browser.find_element_by_xpath('//*[@id="tips"]')
            if(tipsFlag.is_displayed()):
                #判断是什么错误
                if tipsFlag.text== '用户名或密码不正确，请重新输入！':
                    raise LoginException
                elif tipsFlag.text=='验证码输入错误！':
                    continue
                else:
                    raise RemoteException
        except RemoteException:
            print('服务器错误导致的登录失败，尝试重新登录')
        except LoginException:
            print('密码错误')
            print('请重新输入你的信息')
            username = input('学号：')
            passwd = input('密码：')
