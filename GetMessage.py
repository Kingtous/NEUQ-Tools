from BasicFunction import *



def GradeQuery(browser):
    #通过主界面点击成绩查询
    browser.find_element_by_xpath('//*[@id="cdNav"]/ul/li[4]').click()
    browser.find_element_by_xpath('//*[@id="cdNav"]/ul/li[4]/ul/li[12]').click()
    #查询
    browser.switch_to.window(browser.window_handles[1])
    browser.find_element_by_xpath('//*[@id="search_go"]').click()


if __name__=='__main__':
   browser=CreateBrowser()
   Login(browser)
   GradeQuery(browser)
