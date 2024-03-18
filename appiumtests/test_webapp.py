import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains


def test_find_battery(driver):
    el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    battery_value_summary = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.RelativeLayout[@resource-id='com.android.settings:id/text_frame'])[5]//android.widget.TextView[@resource-id='android:id/summary']")
    battery_percentage = battery_value_summary.text
    assert battery_percentage == '100%', f'Expected battery percentage to be 100%, but got {battery_percentage}'


def test_check_emulated_device(driver):
    size = driver.get_window_size()
    width,height = size['width'], size['height']
    start_x, start_y, end_x, end_y = width/2, height*0.8, width/2, height*0.2
    driver.swipe(start_x, start_y, end_y, end_x, duration=200)

    # about_emulated_device = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.TextView[@resource-id='android:id/title'])[19]")
    # about_emulated_device_text = about_emulated_device.text
    # assert about_emulated_device_text == 'About emulated device', f'Expected "About emulated device" title, but got {about_emulated_device_text}'
    emulated_device_model = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.TextView[@resource-id='android:id/summary'])[8]")
    assert emulated_device_model.text == 'sdk_gphone_x86_64', f'Expected another emulated device'
