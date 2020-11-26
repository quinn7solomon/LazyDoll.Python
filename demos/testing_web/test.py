
from core.const import Const
from core.common.element_structure import ElementStructure
from core.testingkit.web.driver import Driver

driver_handle = Driver()
driver = driver_handle.get_driver_chrome()

driver.goto_url('http:\\www.baidu.com')
print(driver.find_element(ElementStructure({
    Const.ELEMENT_BY: 'xpath',
    Const.ELEMENT_EL: '//input[@id="kw"]',
    Const.ELEMENT_PAGE_NAME: '百度模型',
    Const.ELEMENT_ELEMENT_NAME: '首页搜索框'
})))

print(driver_handle.get_registered_driver_list())
print(driver_handle.get_registered_driver_map_dict())


