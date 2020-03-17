#  分析日志,发送邮件(定时任务)

import os
from helloword import settings
import logging
logger = logging.getLogger('')
log_file = 'statistics.log'
def log_analyse():
    log_file_path = os.path.join(settings.BASE_DIR,log_file)
    if not os.path.exists(log_file_path):  # 判断路径是否存在
        print('日志不存在')  # log一下,print都行,需要log的话,需要加一个log实例

