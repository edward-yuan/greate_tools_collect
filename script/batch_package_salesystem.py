# encoding: utf-8
'''
- 文件名：    batch_package_salesystem.py
- 作者：      杰出的城市农夫一代
- 邮箱：      zhangyuan19870129@gmail.com
- 博客：      http://blog.9ifunds.com
- 时间：      2016-11-15 22:07:04
- 环境：      Windows
- 开发工具：  python 3.4.4,其他
- 作用：      批量打包销售系统
- TODO：      暂时没有
- 耗时：      xxms
'''
import subprocess
import time
import zipfile
import glob

# 需要导出的用户
dmp_user = [['kd_sale', '1'], ['kd_his', '1'], ['kd_com', '1'],
            ['kd_bank', '1'], ['kfcs', '1'], ['kd_app_qhhl', '1']]
# 关联的数据库用户
dmp_tns = ['ffdb', 'orcl']
# 获取日期时间
filetime = time.strftime("%Y%m%d%H%M", time.localtime())
# dmp序列
dmp_list = []
# 应用程序路径
app_path = 'C:\\Users\\edward-local-sueface\\Downloads\\app\wall'

# 执行业务系统数据库备份命令
for i in dmp_user:
    conn_user = i[0] + '/' + i[1] + '@' + dmp_tns[0]
    command = 'exp ' + conn_user + ' file=' + \
        i[0] + '_' + filetime + '.dmp ' + \
        'log=' + i[0] + '_' + filetime + '.log'
    dmp_list.append(i[0] + '_' + filetime + '.dmp')
    print('执行命令: ' + command)
    subprocess.call(command, shell=True)
    print(command)

print(dmp_list)

# 复制app到本地
subprocess.call('xcopy ' + app_path + ' .\\app' + ' /s /e /y /i', shell=True)
dmp_list.append('app')

files = glob.glob('app/*')
f = zipfile.ZipFile('test.zip', 'w', zipfile.ZIP_DEFLATED)

for file in files:
    f.write(file)
f.close()

# 删除复制过来的文件
for i in dmp_list:
    subprocess.call('rd /q /s ' + i, shell=True)
