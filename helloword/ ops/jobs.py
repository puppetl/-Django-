#  分析日志,发送邮件(定时任务)

import os
from helloword import settings
import logging
import smtplib
from email.mime.text import MIMEText
logger = logging.getLogger('')
log_file = 'statistics.log'
def log_analyse():
    log_file_path = os.path.join(settings.BASE_DIR,log_file)
    if not os.path.exists(log_file_path):  # 判断路径是否存在
        print('日志不存在')  # log一下,print都行,需要log的话,需要加一个log实例
        return
    result = {}
    with open(log_file_path,'r',encoding='utf8') as f:
        for line in f:
            line = line.strip()
            line_dict = eval(line)
            print(13131313,line_dict)  # 测试数据字典
            # 记录数据
            # xxx接口1    平均耗时    最高耗时    最低耗时    出现次数
            # xxx接口2    平均耗时    最高耗时    最低耗时    出现次数

            # 如果path存在,count+1
            # 如果path不存在,count==1
            # result[count] = '记录接口访问次数',
            # result[min] = '最少',
            # result[max] ='最多',
            # result[avg] ='总耗时/次数'
            key = line_dict['path']
            if key in result:
                result[key][0] += 1  # 第0位标识次数
                if line_dict['used_time'] < result[key][1]:
                    result[key][1] = line_dict['used_time']
                if line_dict['used_time'] > result[key][1]:
                    result[key][2] = line_dict['used_time']
                result[key][3] += line_dict['used_time']
            # 第一次
            else:
                result[key] = ['次数', '最小值', '最大值', '总时间']
                result[key][0] = 1
                result[key][1] = line_dict['used_time']
                result[key][2] = line_dict['used_time']
                result[key][3] = line_dict['used_time']
        return result

def analyse():
    res = log_analyse()
    for key in res:
        res[key].append(res[key][3] / res[key][0])
    return res


def send_email():
    msg = MIMEText(repr(analyse()), "plain", "utf-8")
    # 发件人
    msg['FROM'] = "刘家昌"
    # 主题
    msg['Subject'] = "【端口统计刘家昌】"
    # 接收人
    receivers = ['1977681614@qq.com']  # list,可添加多个联系人
    # 不加密or加密
    # server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server = smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.set_debuglevel(1)
    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    server.sendmail(settings.EMAIL_FROM, receivers, msg.as_string())
    server.close()



if __name__ == '__main__':

    # log_analyse()
    # analyse()
    send_email()
