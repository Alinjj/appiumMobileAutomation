import time

import pytest
import subprocess
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options


# @pytest.fixture(scope='session', autouse=True)
# def emulator():
#     avd_name = "emulator-5554"
#     emulator_process = subprocess.Popen(["emulator", "-avd", avd_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     time.sleep(20)
#     yield
#     subprocess.call(["adb", "-s", "emulator-5554", "emu", "kill"])
#     emulator_process.terminate()
#     try:
#         emulator_process.wait(timeout=10)
#     except subprocess.TimeoutExpired:
#         emulator_process.kill()

appium_service = AppiumService()


@pytest.fixture(scope='session', autouse=True)
def start_appium_service():
    appium_service.start(args=['--address', '127.0.0.1', '-p', '4723'])
    yield
    appium_service.stop()


@pytest.fixture(scope='function')
def driver():
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='emulator-5554',
        appPackage='com.android.settings',
        appActivity='.Settings',
        language='en',
        locale='US'
    )

    appium_server_url = 'http://localhost:4723'

    options = UiAutomator2Options()
    options.load_capabilities(capabilities)
    driver = webdriver.Remote(appium_server_url, options=options)
    yield driver
    driver.quit()
