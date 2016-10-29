# encoding: utf-8
'''
- 文件名：    makedatatofile.py
- 作者：      杰出的城市农夫一代
- 时间：      2016年10月25日15:50:00
- 作用：      批量生成100000条数据,文本文件
- 开发工具：  python 3.4.4
- TODO：      暂时没有
- 耗时：      300ms
'''
import datetime
starttime = datetime.datetime.now()

f = open('../output/test.dat', 'w')


lbm_no='487209'
global_string='g_funcid:'+lbm_no+',g_orgid:0,kcbp:KCBP00,g_confirmaction:0,g_sysid:4,g_userid:8888,g_menuid:0,g_confirmlevel:0,g_userpwd:,g_chkuserid:0,g_userway:2,g_stationaddr:192.168.77.167:2016D86E0798,g_checksno:0,'

#487216
string1='custno:30797194,custno_crm:000003252256,fundcode:161608,detailflag:1'
#430312
string2='custno:30797194,fundcode:,businesscode:,paycenterid:,begindate:20160807,enddate:20160910'
#430313
string3='begindate:20160201,enddate:20160301,channelid:,custno:30797194,businesscode:,status:,paycenterid:,fundcode:'
#430305
string4='custno:30797194,flag:2'
#487207
string5='custno_crm:000003252256,begindate:20150101,enddate:20150401,fundcode:,businesscode:'
#487208
string6='custno_crm:000003252256,begindate:20150101,enddate:20150401,fundcode:'
#487209
string7='custno:30797194,custno_crm:000003252256,detailflag:'

string=string7

exec_string=lbm_no+'!'+global_string+string

for i in range(0,100000):
	f.write(exec_string+'\n')
	i += i

f.close()

endtime = datetime.datetime.now()
#打印耗时
print (endtime - starttime)