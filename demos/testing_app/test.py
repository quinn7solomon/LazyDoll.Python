import time

from core.testingKit_app.puppeteer import Puppeteer
from demos.testing_app.solution_parameter import *
from demos.testing_app.modes.mode_chrome import ModeChrome

# Puppeteer 实例
PuppeteerObj = Puppeteer(SOLUTION_DRIVER_CONFIG_PATH)

# 元素模型
ModeChrome = ModeChrome(PuppeteerObj)

ModeChrome.open_app()
ModeChrome.search.tap()
ModeChrome.url_bar.send('www.baidu.com')
ModeChrome.search_result.tap()

PuppeteerObj.quit()

