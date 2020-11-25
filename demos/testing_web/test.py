
from core.testingKit_web.puppeteer import Puppeteer

from demos.testing_web.modes.baidu.mode_home import ModeHome


PuppeteerObj = Puppeteer.get_driver_chrome()

mode_home = ModeHome(PuppeteerObj)

mode_home.app.goto_url('http:\\www.baidu.com')
mode_home.home_search.send('123')
mode_home.home_search_confirm.tap()

