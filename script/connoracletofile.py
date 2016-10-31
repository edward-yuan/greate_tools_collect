# encoding: utf-8
'''
- 文件名：    connoracletofile.py
- 作者：      杰出的城市农夫一代
- 时间：      2016年10月28日14:29:22
- 作用：      从数据库里面查询数据导出到文本里面
- 开发工具：  python 3.4.4,cx_Oracle 5.2.1(模块)
- TODO：      暂时没有
- 耗时：      1900ms
'''
import cx_Oracle
import datetime

starttime = datetime.datetime.now()

SQL = "select t.custno||','||t.certificatetype||','||t.certificateno from ACCT_CUST t where t.invtp='1'"

# connection = cx_Oracle.Connection("kd_sale/1@orcl")
connection = cx_Oracle.connect('kd_sale', '1', '192.168.240.117:1521/RACTEST')

cursor = connection.cursor()

# 连接数据库，执行查询
try:
    cursor.execute(SQL)
    rs = cursor.fetchall()
except cx_Oracle.DatabaseError as exc:
    print(exc)
finally:
    connection.close()

# 开始写文件
f = open('../output/test-etrading.dat', 'w')
f.write('custno,certificatetype,certificateno\n')
for i in rs:
    f.write(i[0] + '\n')

f.close()
endtime = datetime.datetime.now()
# 打印耗时
print(endtime - starttime)
