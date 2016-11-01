# encoding:utf-8
'''
- 文件名：    liepin_job.py
- 作者：      杰出的城市农夫一代
- 时间：      2016年10月31日16:08:03
- 作用：      猎聘网职位爬虫,获取信息后生成excel，然后发送邮件
- 开发工具：  python 3.4.4,requests(模块),xlsxwriter(模块)
- TODO：      暂时没有
- 耗时：      37.4s
'''
import requests
import json
import xlsxwriter
'''
https://www.liepin.com/zhaopin/?industries=150&dqs=050090&salary=&jobKind=2&pubTime=1&compkind=&compscale=&industryType=industry_04&searchType=1&clean_condition=&isAnalysis=&init=-1&sortFlag=15&fromSearchBtn=2&headckid=707b3dded436854a&key=IT&ckid=707b3dded436854a&flushckid=1
'''

TAG = ['companyFullName', 'companyShortName', 'positionName',
       'education', 'salary', 'financeStage',
       'companySize', 'industryField', 'companyLabelList'
       ]

TAG_NAME = ['公司名称', '公司简称', '职位名称',
            '所需学历', '工资', '公司资质',
            '公司规模', '所属类别', '公司介绍'
            ]


def read_page(url, page_num, keyword):
    # 读取每一页的信息

    page_headers = {
        'Host': 'www.liepin.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Connection': 'keep-alive'
    }

    if page_num == 1:
        boo = 'true'
    else:
        boo = 'false'

    page_data = {'first': boo,
                 'pn': page_num,
                 'kd': keyword
                 }

    r = requests.post(url, data=page_data, headers=page_headers)

    return r.text


def get_total_page_count(page):
    # 获得总页数
    page_json = json.loads(page)
    total_count = page_json['content']['positionResult']['totalCount']
    page_size = page_json['content']['pageSize']
    return (int(total_count) // int(page_size)) + 1


def read_tag(page):
    # 获得每一页每一个公司的信息
    page_json = json.loads(page)
    result = page_json['content']['positionResult']['result']

    for each in result:
        each_conpany_info = []
        for tag in TAG:
            '''把list拆分成字符串'''
            if not isinstance(each[tag], list):
                each_conpany_info.append(each[tag])
            else:
                each_conpany_info.append(','.join(each[tag]))
        yield each_conpany_info


def save_excel(fin_result, file_name):
    # 保存到excel
    workbook = xlsxwriter.Workbook('../output/{}.xlsx'.format(file_name))
    worksheet = workbook.add_worksheet()

    worksheet.write_row('A1', TAG_NAME)

    for index, conpany_info in enumerate(fin_result):
        worksheet.write_row('A{}'.format(index + 2), conpany_info)

    workbook.close()

if __name__ == '__main__':
    # 查询的数据
    city = '深圳'
    keyword = 'python'

    position_url = 'http://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionalResult=false'.format(
        city)

    main_page_content = read_page(position_url, 1, keyword)

    total_page_count = get_total_page_count(main_page_content)

    fin_result = []

    for i in range(1, total_page_count + 1):
        page = read_page(position_url, str(i), keyword)
        for each_conpany_info in read_tag(page):
            fin_result.append(each_conpany_info)
    save_excel(fin_result, city + keyword)

    print('done!')
