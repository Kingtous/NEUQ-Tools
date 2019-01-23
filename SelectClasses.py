from ExceptionKinds import *
from BasicFunction import *


def Select(Browser,QueryClass):
    #还需要考虑人多的时候被挤出去，重新登录

    #选择自主选课
    browser.find_element_by_xpath('//*[@id="cdNav"]/ul/li[3]').click()
    browser.find_element_by_xpath('//*[@id="cdNav"]/ul/li[3]/ul/li[3]/a').click()

    #输入查询关键字
    browser.switch_to.window(browser.window_handles[1])
    browser.implicitly_wait(50)
    browser.find_element_by_xpath('//*[@id="searchBox"]/div/div[1]/div/div/div/div/input').send_keys(QueryClass)

    #查询
    browser.implicitly_wait(50)
    browser.find_element_by_xpath('//*[@id="searchBox"]/div/div[1]/div/div/div/div/span/button[1]').click()

    #点击选课
    #此处留坑，学校选课系统没开
    pass

if __name__=='__main__':
    QueryClass=input('请输入你要选的科目(只需关键字，但需保证该课程能出现在列表第一个)：')
    browser = CreateBrowser()
    Login(browser)
    Select(browser,QueryClass)
