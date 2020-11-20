import os
import time
import shutil

from demos.testing_app.solution_parameter import *


# 测试报告名称
reports_name_prefix = 'LazyDollDemoTestingApp'
reports_name_suffix = time.strftime('%Y%m%d', time.localtime())
reports_name = reports_name_prefix + '-' + reports_name_suffix

# 测试报告输出XML目录 Path
reports_output_xml_path = GLOBAL_DIR_PATH_REPORTS.joinpath(reports_name + 'allureXml')
# 测试报告输出HTML目录 Path
reports_output_html_path = GLOBAL_DIR_PATH_REPORTS.joinpath(reports_name + 'allureHtml')

os.system(f'pytest -v '
          f'{GLOBAL_DIR_PATH_CASES.joinpath("test_01_case_system.py")} '
          f'--alluredir={reports_output_xml_path}')

os.system(
    f'allure generate {reports_output_xml_path} -o {reports_output_html_path} --clean')

shutil.rmtree(reports_output_xml_path, ignore_errors=True)




