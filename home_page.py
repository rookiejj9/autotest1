from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def login_and_register(login_a_classname, register_a_classname):
    """
    :param login_a_classname: 首页登录按钮跳转a元素classname
    :param register_a_classname: 首页注册按钮跳转a元素classname
    :return: None
    """
    # 获取登录连接
    login_button = driver.find_element(By.CSS_SELECTOR, f'a.{login_a_classname}').get_attribute('href')
    assert (login_button == 'https://center.360proxy.com/Login/Login')

    register_button = driver.find_element(By.CSS_SELECTOR, f'a.{register_a_classname}').get_attribute('href')
    print(register_button)
    assert (register_button == 'https://center.360proxy.com/Login/Register')


def button_click(button_classname):
    """
    按钮点击验证
    :return:
    """
    # 获取登录连接
    pass


if __name__ == '__main__':
    # 创建一个 Chrome 浏览器实例
    driver = webdriver.Chrome()

    # 打开 Google 首页
    driver.get("https://www.360proxy.com/zh-tw/")
    driver.maximize_window()
    time.sleep(5)

    # 验证登录连接和注册连接
    login_and_register('vh-h-btn', 'vh-h-btn.blue')

    # 关闭浏览器
    driver.quit()
