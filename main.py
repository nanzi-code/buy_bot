from selenium import webdriver

##  在商品页面，将商品加入购物车
def get_oreder(brower):
    """
    in:商品链接webdriver对象
    out:num 1:加入购物车成功 0:加入购物车失败
    """
    order_button = "加入购物车"
    if(brower.find_element_by_link_text(order_button)):
        return 0
    try:
        brower.find_element_by_link_text(order_button).click()
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
    url = ""
    brower = webdriver.Chrome()
    brower.maximize_window()
    while(get_oreder(brower)):
        pass
    buy(brower)

