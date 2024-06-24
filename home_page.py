import time
from selenium import webdriver
from selenium.webdriver.common.by import By


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


def home_page_first_proxy_button(div_classname):
    """
    :param div_classname: 第一个代理按钮div元素classname
    :return: None
    """
    div_a_list = driver.find_element(By.CLASS_NAME, f'{div_classname}').find_elements(By.TAG_NAME, 'a')
    for _ in div_a_list:
        a_element = _.get_attribute('href')
        _.click()
        time.sleep(2)
        a_element_click_url = driver.current_url
        # print(a_element_click_url, a_element)
        assert (a_element == a_element_click_url)
        time.sleep(2)
        driver.back()


def video_play2(video2_id):
    """
    :param video2_id: 视频播放按钮classname
    :return: None
    """
    # 创建播放按钮和video元素实例
    video_element = driver.find_element(By.ID, f'{video2_id}')
    driver.execute_script("arguments[0].scrollIntoView();", video_element)

    # 验证视频链接
    video_link = video_element.find_element(By.TAG_NAME, "source").get_attribute("src")
    assert (video_link == 'https://www.360proxy.com/360Proxywebsite.mp4')

    # js执行滑动到对应element位置，并点击
    driver.execute_script("arguments[0].scrollIntoView(true);", video_element)
    driver.execute_script("arguments[0].click();", video_element)
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
    driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()

    # 验证登录连接和注册连接
    # login_and_register('vh-h-btn', 'vh-h-btn.blue')
    # 按钮点击验证
    # try_now_click('ix-banner-user')
    # 首页视频播放
    # video_play1('video_logo_play')
    # 首页底部代理按钮连接循环验证
    # home_page_first_proxy_button('ix-banner-proxy')
    # 介绍视频按钮
    video_play2('intruduct-video')
