# encoding: utf-8
'''
- 文件名：makedatatofile.py
- 作者：  杰出的城市农夫一代
- 时间：  2016年10月25日15:50:00
- 作用：  批量生成100000条数据,文本文件
- TODO：  暂时没有
- 耗时：  -
'''
import datetime
starttime = datetime.datetime.now()

f = open('../output/test.dat', 'w')
string='430382!g_userid:8888,g_userpwd:=,g_userway:2,g_stationaddr:MAC[],g_sysid:8,g_menuid:12,g_funcid:430382,g_checksno:0,g_chkuserid:,g_confirmaction:0,g_confirmlevel:0,contractno:TT2013042310000051,applicationno:TT2013042110000000,distributorcode:225,businesscode:022,fundcode:420006,isforcedeal:1,applicationamount:30000,buyflag:1,'

for i in range(0,10000):
	f.write(string+'\n')
	i += i

f.close()

endtime = datetime.datetime.now()
#打印耗时
print (endtime - starttime)