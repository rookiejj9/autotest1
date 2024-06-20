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


def try_now_click(try_now_classname):
    """
    :param try_now_classname: try_now按钮classname
    :return: None
    """
    # 获取登录连接
    try_now_button = driver.find_element(By.CSS_SELECTOR, f'a.{try_now_classname}').click()
    try_now_link = driver.current_url
    assert (try_now_link == 'https://center.360proxy.com/Login/Register')

    # 返回上一页
    driver.back()


def video_play1(video_classname):
    """
    :param video_classname: 视频播放按钮classname
    :return: None
    """
    # 创建a元素实例,video元素
    video_button = driver.find_element(By.CSS_SELECTOR, f'a.{video_classname}')
    video_element = driver.find_element(By.ID, 'myVideo')

    # 验证视频链接
    video_link = video_element.find_element(By.TAG_NAME, "source").get_attribute("src")
    assert (video_link == 'https://www.360proxy.com/360Proxywebsite.mp4')

    # 点击视频播放按钮
    video_button.click()
    time.sleep(5)
    video_watching_play = driver.execute_script("return arguments[0].paused;", video_element)
    if not video_watching_play:
        assert True
    else:
        assert False

    # 关闭视频播放
    video_close = driver.find_element(By.CLASS_NAME, "video_mark")
    driver.execute_script("arguments[0].style.display='none';", video_close)


if __name__ == '__main__':
    # 设置Chrome选项
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    # 初始化浏览器
    driver = webdriver.Chrome(options=options)

    # 打开 Google 首页
    driver.get("https://www.360proxy.com/zh-tw/")
    driver.maximize_window()
    time.sleep(5)

    # 验证登录连接和注册连接
    login_and_register('vh-h-btn', 'vh-h-btn.blue')
    # 按钮点击验证
    try_now_click('ix-banner-user')
    # 首页视频播放
    video_play1('video_logo_play')
