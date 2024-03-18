from appium.webdriver.common.appiumby import AppiumBy


def test_find_battery(driver):
    el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    battery_value_summary = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.RelativeLayout[@resource-id='com.android.settings:id/text_frame'])[5]//android.widget.TextView[@resource-id='android:id/summary']")
    battery_percentage = battery_value_summary.text
    assert battery_percentage == '100%', f'Expected battery percentage to be 100%, but got {battery_percentage}'


