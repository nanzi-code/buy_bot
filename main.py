from selenium import webdriver
import datetime
import time

def login(browser):
  # 打开淘宝登录页，并进行扫码登录
  browser.get("https://item.jd.com/10030769845141.html")
  time.sleep(3)
  if browser.find_element_by_link_text("亲，请登录"):
    browser.find_element_by_link_text("亲，请登录").click()
    print("请在15秒内完成扫码")
    time.sleep(15)
    browser.get("https://cart.taobao.com/cart.htm")
  time.sleep(3)
  
  now = datetime.datetime.now()
  print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))

##  在商品页面，将商品加入购物车
def get_oreder(brower):
    """
    in:商品链接webdriver对象
    out:num 1:加入购物车成功 0:加入购物车失败
    """
    order_button = "加入购物车"
    try:
        brower.find_element(order_button).click()
    except:
        return 0
    return 1

##  在购物车里，下订单函数
def buy(brower):
    """
    in:购物车链接webdriver对象
    out:none
    """
    buy_button = "去结算"
    link = brower.find_element_by_link_text(buy_button)
    link.click()
    brower.get(link)
    brower.find_element_by_link_text("提交订单")

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.binary_location = "C:\Program Files\Google\Chrome\Application/chrome.exe"
    brower = webdriver.Chrome(chrome_options=options)
    num = 0
    login(brower)
    while(num == 0):
        num = get_oreder(brower)
    #buy(brower)

