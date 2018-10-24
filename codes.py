# CREATED FOR TEST 1

import requests
# from multiprocessing import Pool
# import threading

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
        'Cookie': 'WEBTJ-ID=20181024095741-166a3cab1e94-0e9f57b5be06c7-4c312878-1327104-166a3c'
                  'ab1ea455; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1540346262,1540346274,154'
                  '0346279; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1540346616; _ga=GA1.2.211'
                  '2127073.1540346262; user_trace_token=20181024095741-3101862e-d730-11e8-9c2e'
                  '-525400f775ce; LGSID=20181024095753-380cc1dc-d730-11e8-80b9-5254005c3644; P'
                  'RE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fww'
                  'w.baidu.com%2Fs%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D1%26tn%3Dmonl'
                  'ine_3_dg%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rsv_pq%3Dc8'
                  '86a35800065a8f%26rsv_t%3D1c52Cykcc%252B67fRXg6lOyU%252BgEG%252BmI1unxU%252B'
                  '8YXUxG1LorvE0wVrM0v8CK47h42bzTutrX%26rqlang%3Dcn%26rsv_enter%3D1%26rsv_sug'
                  '3%3D11%26rsv_sug1%3D7%26rsv_sug7%3D100%26rsv_sug2%3D0%26inputT%3D1614%26rsv'
                  '_sug4%3D2335; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.ht'
                  'ml%3Futm_source%3Dm_cf_cpt_baidu_pc; LGRID=20181024100338-057c4209-d731-11'
                  'e8-80d1-5254005c3644; LGUID=20181024095741-31018eaa-d730-11e8-9c2e-525400f'
                  '775ce; _gid=GA1.2.19213825.1540346262; JSESSIONID=ABAAABAAADEAAFIC944A2AEA'
                  'E86F13DA7F956535937F918; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-'
                  'CODE=search_code; SEARCH_ID=cdd92faac42f418d8ffa22f80a551d39; isCloseNotice=0',
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?px=default&city=%E5%8C%97%E4%BA%AC',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': None,
        'X-Requested-With': 'XMLHttpRequest'
        }
url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=北京&needAddtionalResult=false'


def setdata(n):
    data = {
        'first': 'true',
        'kd': 'python',
        'pn': n
    }
    return data


def get_page_content(data):
    response = requests.post(url, headers=head, data=data)
    response.encoding = 'utf-8'
    resu = response
    # 不能使用 response.text，否则会报错说 str 无法用 .json
    resujson = resu.json()
    # 将resu进行字典化
    # print(resujson['content']['positionResult']['result'])
    # 查找到result的值，是一个列表
    for item in resujson['content']['positionResult']['result']:
        neededinfo = {
            '职位名称': item['positionName'],
            '工作地点': item['district'],
            '工作工资': item['salary'],
            '工作经验': item['workYear']
        }
        # positionID = item['positionId']
        # 可以获取职位的详细信息，页面是静态网页
        print(neededinfo)
    # print(resu.text)


def main(num):
    get_page_content(setdata(num))


if __name__ == '__main__':
    for i in range(1, 2):  # 可以从第1页到第10页
        get_page_content(setdata(i))
    # *****************
    # 使用多线程--1
    # pool = Pool()
    # pool.map(main, [i for i in range(1, 10)])
    # *****************
    # 使用多线程--2
    # for i in range(1, 5):
    #     th = threading.Thread(target=get_page_content(setdata(i)))
    #     th.start()
