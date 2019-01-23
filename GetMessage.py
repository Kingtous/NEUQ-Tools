from selenium import webdriver

#query_class='python'
print('请输入你的信息')
username=input('学号：')
passwd=input('密码：')

browser=webdriver.Chrome()

try:
    url='http://jwxt.neuq.edu.cn/jwglxt'
    browser.get(url)
except:
    pass

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
            if(tipsFlag.text=='用户名或密码不正确，请重新输入！' or tipsFlag.text=='验证码输入错误！'):
                raise Exception
            else:
                raise RuntimeError
    except RuntimeError:
        print('登录失败，请重试')
    except Exception:
        print('登录失败')
        print('请重新输入你的信息')
        username = input('学号：')
        passwd = input('密码：')

browser.implicitly_wait(50)


'''
选课代码
#Select Classes
#browser.get('http://jwxt.neuq.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su='+username)
#browser.switch_to.window(browser.window_handles[1])

browser.find_element_by_xpath('//*[@id="cdNav"]/ul/li[3]').click()
browser.find_element_by_xpath('//*[@id="cdNav"]/ul/li[3]/ul/li[3]/a').click()

#input class name
browser.switch_to.window(browser.window_handles[1])
browser.implicitly_wait(50)
browser.find_element_by_xpath('//*[@id="searchBox"]/div/div[1]/div/div/div/div/input').send_keys(query_class)

#press query button
browser.implicitly_wait(50)
browser.find_element_by_xpath('//*[@id="searchBox"]/div/div[1]/div/div/div/div/span/button[1]').click()
'''

#通过主界面点击成绩查询
browser.find_element_by_xpath('//*[@id="cdNav"]/ul/li[4]').click()
browser.find_element_by_xpath('//*[@id="cdNav"]/ul/li[4]/ul/li[12]').click()

#查询
browser.switch_to.window(browser.window_handles[1])
browser.find_element_by_xpath('//*[@id="search_go"]').click()


