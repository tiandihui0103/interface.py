'''
存放基本配置文件
'''
import time,random;
KEY = '';
TOKEN = '';
class Conf():
    LOGS = [];
    TITLE = 'SINCAI API_V1 接口测试报告';
    PROJECT = 'api_v1';
    DOMAIN = 'pre.123ssc.net/api/';
    EXCUTE_TIME = time.strftime("%Y%m%d%H%M%S",time.localtime());
    DETAIL_REPORT_FILE_DIR = 'C:/Python35/Webx_Report/杏彩接口测试_';
    SUMMART_REPORT_FILE_DIR = 'C:/Python35/Webx_Report/杏彩接口测试_SUMMERR_';
    
