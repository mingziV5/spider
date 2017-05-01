#!/usr/bin/python
#-*- coding: utf-8 -*-
import requests
from pyquery import PyQuery as pq

job_name = raw_input('输入要爬的职位: ')
url = 'http://www.zhipin.com/job_detail/?query=%s&scity=101210100' %job_name
headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;",
        "Accept-Encoding":"gzip",
        "Accept-Language":"zh-CN,zh;q=0.8",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
        }

res = requests.get(url=url,headers = headers)
python_query = pq(res.text)

boss_list = []
for job_primary in python_query('.job-primary'):
    job_name = pq(job_primary).find('[class="info-primary"]').find('[class="name"]').html().split()[0]
    salary = pq(job_primary).find('[class="info-primary"]').find('[class="red"]').html()
    company = pq(job_primary).find('[class="company-text"]').find('[class="name"]').html().split()[0]
#    with open('spider.txt','a') as f:
#        file_str = job_name + " " + salary + " " + company + '\n'
#        print repr(file_str)
#        f.write(file_str.encode('utf-8'))

    boss_dict = {u'职位':job_name,u'薪水':salary,u'公司名称':company}
#    print boss_dict
    boss_list.append(boss_dict)
#print boss_list

with open('spider.txt','w') as f:
    item_str = ''
    for item in boss_list:
        item_str += '职位' + ':' + item[u'职位'].encode('utf-8') + '薪水' + ':' + item[u'薪水'].encode('utf-8') + '公司名称' + ':' + item[u'公司名称'].encode('utf-8') + '\n'
    f.write(item_str)
#print python_query
