#LazyDoll.Python    V.BETA1.0.0

### 框架简介
> LazyDoll 是一个 App \ Web 应用程序的自动化测试框架 （未来将支持接口自动化）
>
> 对平台的支持采用模组化设计，高度统一的接口使所有模组间的运行逻辑一致
>
> 使用者仅需要关注测试业务的设计而不需要去理解不同模组的代码逻辑
>
> LazyDoll 模组核心封装中提供了以下功能
>
>> * DriverHandle
>>>     Driver 的注册机， 职责于生产相应模组的 Driver
>>>     并且管理全部 Driver 的生命周期
>>
>> * Puppeteer
>>>     元素组件构建类，它负责动态解析元素结构体并将其封装成元素组件
>>>     元素组件细化为三个模块
>>>        app : 负责设备操作，如模拟按下物理键、打开新窗口\应用等
>>>       view : 负责视图操作，如滑动屏幕、浏览器切换标签页等
>>>     module : 负责元素操作，如点击、输入、获取元素属性等
>>
>> * WindowsGui
>>>     提供一个快捷启动测试文件的可视化界面
>>

### 运行环境
> * Python 3.6 +
> * 依赖库 :
>>     PyYAML
>>     selenium
>>     appium
>>     Appium-Pyhon-Client
>>     allure-pytest
>>     allure-python-commons
>>     dearpygui
>
> * App 应用程序测试依赖 :
>>     JDK
>>     Android SDK
>>     Node.js
>>     Appium-desktop
>
> * Wep 应用程序测试依赖 :
>>     ChromeDriver : 根据谷歌浏览器版本下载相应的 ChromeDriver 驱动

### 开始:: 第一个测试项目

> * 复制 demos 中的一个项目模板 或 手动创建结构一致的目录 :
>>     testing_app              -> 测试项目目录
>>     | cases                  -> 测试文件目录
>>     | | __init__.py
>>     | configure              -> 配置文件目录
>>     | logs                   -> 日志文件目录
>>     | modes                  -> 元素模型目录
>>     | | __init__.py
>>     | reports                -> 测试报告目录
>>     | __init__.py
>>     | running.py             -> 快速启动测试文件的GUI可视化窗口
>
> * 构建元素模型
>>>     一个应用程序(app/web)由若干个页面组成 
>>>     项目中我们需要以 "页面" 为单位，为其建立元素模型
>>>     元素模型将包含该页面业务所需的所有可视化、可操作的元素
>>>     
>>>     这个过程将由 Puppeteer 类
>>>     我们只需要构建 ElementStructure 结构体，并交给 Puppeteer 类
>
>>> 代码示例
>>>```python
>>># modes/baidu/.mode_bd_home.py
>>>
>>>from core.const import Const
>>>from core.testingkit.web.puppeteer import Puppeteer
>>>from core.common.element_structure import ElementStructure
>>>
>>>class ModeBdHome(object):
>>>
>>>    modeName = '百度页面模型'
>>>    _puppeteerCore = None
>>>
>>>    # 元素模型初始化需要接收一个 RegisteredDriver 对象
>>>    def __init__(self, registered_driver):
>>>        self._puppeteerCore = Puppeteer(registered_driver)
>>>
>>>    # 构建 app 模组
>>>    @property
>>>    def app(self):
>>>        return self._puppeteerCore.app()
>>>
>>>    # 构建 view 模组
>>>    @property
>>>    def view(self):
>>>        return self._puppeteerCore.view()
>>>
>>>    # 构建 module 模组:: 百度搜索框
>>>    @property
>>>    def home_search(self):
>>>        return self._puppeteerCore.module(ElementStructure(
>>>            {
>>>                Const.ELEMENT_BY: 'xpath',
>>>                Const.ELEMENT_EL: '//input[@id="kw"]',
>>>                Const.ELEMENT_PAGE_NAME: self.modeName,
>>>                Const.ELEMENT_ELEMENT_NAME: '搜索框',
>>>            }))
>>>
>>>    # 构建 module 模组:: 搜索按钮
>>>    @property
>>>    def home_search_confirm(self):
>>>        return self._puppeteerCore.module(ElementStructure(
>>>            {
>>>                Const.ELEMENT_BY: 'xpath',
>>>                Const.ELEMENT_EL: '//input[@id="su"]',
>>>                Const.ELEMENT_PAGE_NAME: self.modeName,
>>>                Const.ELEMENT_ELEMENT_NAME: '搜索框.百度一下',
>>>            }))
>>>```
> * 编写 Case 测试业务
>>> 代码示例 :: PyTest 测试框架
>>>```python
>>># cases/test_01_case_search.py
>>>
>>>import allure
>>>
>>>from core.common.log import Log
>>>from core.testingkit.web.driverhandle import DriverHandle
>>>from demos.testing_web.modes.baidu.mode_bd_home import ModeBdHome
>>>
>>>class Test01CaseSearch(object):
>>>
>>>    Log = Log()
>>>
>>>    # DriverHandle 实例
>>>    DriverHandle = DriverHandle()
>>>    # RegisteredDriver 实例
>>>    RegisteredDriver = DriverHandle.get_driver_chrome()
>>>
>>>    # 元素模型
>>>    ModeBdHome = ModeBdHome(RegisteredDriver)
>>>
>>>    @classmethod
>>>    def setup_class(cls):
>>>        pass
>>>
>>>    @classmethod
>>>    def teardown_class(cls):
>>>        pass
>>>
>>>    def setup_method(self):
>>>        pass
>>>
>>>    def teardown_method(self):
>>>        pass
>>>
>>>    @allure.severity('Blocker')
>>>    @allure.story('第一个测试用例:: 输入URL并点击搜索按钮')
>>>    def test_001_search(self):
>>>        try:
>>>            # 调用元素模型组件操作函数
>>>            self.ModeBdHome.home_search.send_key('搜索内容')
>>>            self.ModeBdHome.home_search_confirm.tap()
>>>            assert True
>>>        except Exception as err:
>>>            self.Log.error(f'用例执行失败: 第一个测试用例:: 输入URL并点击搜索按钮: {err}')
>>>            assert False
>>>```
> * 运行测试并生成测试报告
>> * 方式1 : IDE直接运行 PyTest 文件 (该方法不会生成测试报告)
>> * 方式2 : IDE 中运行项目根目录下的 running.py 文件启动可视化GUI
>>>> 1. 选择需要运行的文件名称
>>>> 2. 点击 Running Testing 开始执行