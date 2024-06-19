from selenium import webdriver
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
    assert (register_button == 'https://center.360proxy.com/Login/Register')


def button_click(button_classname):
    """
    按钮点击验证
    :return:
    """
    # 获取登录连接
    try_now_button = driver.find_element(By.CSS_SELECTOR, f'a.{button_classname}').click()
    try_now_link = driver.current_url
    assert (try_now_link == 'https://center.360proxy.com/Login/Register')

    driver.back()


if __name__ == '__main__':
    # 创建一个 Chrome 浏览器实例
    driver = webdriver.Chrome()

    # 打开 Google 首页
    driver.get("https://www.360proxy.com/zh-tw/")
    driver.maximize_window()
    time.sleep(5)

    # 验证登录连接和注册连接
    login_and_register('vh-h-btn', 'vh-h-btn.blue')
    # 按钮点击验证
    button_click('ix-banner-user')

    # 关闭浏览器
    driver.quit()
