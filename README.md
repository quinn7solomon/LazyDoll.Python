#LazyDoll.Python

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
>> * Appium-desktop : Appium Server 客户端
>
> * Wep 应用程序测试依赖 :
>> * Appium-desktop : Appium Server 客户端