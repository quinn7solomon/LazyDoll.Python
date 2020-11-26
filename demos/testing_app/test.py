import time

from core.const import Const
from core.common.element_structure import ElementStructure
from core.testingkit.app.driver import Driver
from core.testingkit.app.puppeteer import Puppeteer
from core.const import GlobalVariate

driver_handle = Driver()
driver = driver_handle.get_driver(GlobalVariate.DIR_PATH_CONFIG.joinpath('android_8.1.0.yaml'))
puppeteer = Puppeteer(driver)

a = puppeteer.module(ElementStructure({
    Const.ELEMENT_BY: 'id',
    Const.ELEMENT_EL: 'com.google.android.apps.nexuslauncher:id/all_apps_handle',
    Const.ELEMENT_PAGE_NAME: '系统',
    Const.ELEMENT_ELEMENT_NAME: '向上箭头'
}))

print(a)
a.get_element_len()
a.get_text()
a.in_page()
a.tap()
time.sleep(5)
a.in_page()

print(driver_handle.get_registered_driver_list())
print(driver_handle.get_registered_driver_map_dict())
print(puppeteer)
print(type(puppeteer))

