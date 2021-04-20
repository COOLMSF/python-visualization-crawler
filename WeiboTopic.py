# -*- coding: utf-8 -*-
import requests
import time
import sys
import os

topic_titles = []
 
def get_hot_topic(page):
    topic_list = []
    session = requests.session()
    for i in range(page):
        if i == 0:
            the_url = "https://m.weibo.cn/api/container/getIndex?containerid=100803"
        if i == 1:
            the_url = "https://m.weibo.cn/api/container/getIndex?containerid=100803&since_id=%7B%22page%22:2,%22next_since_id%22:6,%22recommend_since_id%22:[%22%22,%221.8060920078958E15%22,%221.8060920009434E15%22,0]%7D"
        else:
            the_url = "https://m.weibo.cn/api/container/getIndex?containerid=100803&since_id=%7B%22page%22:{},%22next_since_id%22:{},%22recommend_since_id%22:[%22%22,%221.8060912084255E14%22,%221.8060920000515E15%22,0]%7D".format(i+1,6 + 14*(i-2))
        header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
                  'cookie': 'SCF=AtTCtKbsCE8JxtrO0kcD_C4f65Yn1U-tspMXv0bmj_6hIzGSTgr4GYtq3X5qaRmGPY3rS8HrRyz7YQeb51DKXVw.; SUB=_2A25zcABnDeRhGeVJ6lYQ-SrPzj2IHXVQmqAvrDV6PUJbktANLXLZkW1NT-MET2PLWPvDoriPDgqDIvvX8o7fA6UM; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5eGCL6N2RTW9mjY7Y465Lc5JpX5K-hUgL.FoeNeKBp1KB0SK22dJLoIpjLxK.LB.zL1K2LxK-LB.BLBo2LxK.L1-2L1K5t; SUHB=0D-F6txRCGnRJ9; _T_WM=98219736160; XSRF-TOKEN=aee893; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=fid%3D100803%26uicode%3D10000011',
                 }
        try:
            r = session.get(the_url, headers = header)
            res = r.json()
        except requests.exceptions.ConnectionError:
            print("！！！网络连接出错，请检查网络！！！")   
        time.sleep(2)       
        
        for cards in res.get("data").get("cards"):
            #try:
            if cards.get("card_group") is None:
                continue
            for card in cards.get("card_group"):
                #print("***", card.get("title_sub"), card.get("category"), card.get("desc2"))
                title = card.get("title_sub")
                category = card.get("category")
                desc2 = card.get("desc2")
                if "超级话题" in desc2:
                    print("超级话题：", end = "")
                    scheme = card.get("scheme")
                    topic_id = scheme[scheme.index("=") + 1 : scheme.index("=") + 7]
                    topic_url = "https://m.weibo.cn/api/container/getIndex?containerid={}type%".format(topic_id)\
                                 + "3D1%26q%3D%23%E7%8E%8B%E4%BF%8A%E5%87%AF%E4%B8%AD%E9%A4%90%E5%8E%"\
                                 + "85%E7%AC%AC%E4%BA%8C%E5%AD%A3%23%26t%3D10&luicode=10000011&lfid="\
                                 + "100803&page_type=searchall"
                    r2 = session.get(topic_url)
                    res2 = r2.json()
                    desc2 = res2.get("data").get("cardlistInfo").get("cardlist_head_cards")[0].get("head_data").get("midtext").split()
                    desc2.reverse()
                    desc2 = " ".join(desc2)
                # print(title, category, desc2.split())
                topic_titles.append(title)
                cv = []
                for n in desc2.split():
                    if "万" in n:
                        for ch in n:
                            if u'\u4e00' <= ch <= u'\u9fff': #去除中文
                                n = n.replace(ch, "")
                        n = float(n) * 10000
                    elif "亿" in n:
                        for ch in n:
                            if u'\u4e00' <= ch <= u'\u9fff': #去除中文
                                n = n.replace(ch, "")
                        n = float(n) * 100000000
                    else:
                        for ch in n:
                            if u'\u4e00' <= ch <= u'\u9fff': #去除中文
                                n = n.replace(ch, "")
                    cv.append(int(n))
                try:
                    topic_list.append([title, category, cv[0], cv[1]])
                except:
                    continue
            #except:
                #continue
        # time.sleep(2)       
        # print(len(topic_list))
    return topic_list
        
def main():
    topic_list = get_hot_topic(1)

if __name__ == "__main__":
    main()

    for topic_title in topic_titles[0:2]:
        print(topic_title)
