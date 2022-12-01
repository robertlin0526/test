from googlesearch import search
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time


class google_search:
    def __init__(self):
        global link
        global query
        global str1
        global date

        str1 = "test"
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        #date = "2022-04-16"
        
        #query = "新增 例COVID-19確定病例，分別為"
        query2 = "新增 例COVID-19確定病例，分別為 www.cdc.gov.tw/Bulletin/Detail"
        query = ("www.cdc.gov.tw/Bulletin/Detail " + date) 
        
        print("%s" % date)
        #date_str = 

        for k in search(query2, stop=1, pause=2.0): 
            link = k
            print(link[:38])

    def get_covid19_info(self):
        for j in search(query, stop=4, pause=2.0): 
            print(j)
            if j[:38] != link[:38]:
                print(j[:38])
                continue
            response = requests.get(j)
            soup = BeautifulSoup(response.text, "html.parser")
        
            result = soup.find("div", class_="text-right")
            if result == None:
                continue
            str1 = str(result.string[5:])
            print(str1) #print date 
            if str1 == "" or str1 != date:
                continue
            else:
                #print(str(result.string[5:]))
                print(str(result.string[5:]) + ":" + str(soup.title.string[:-13]))
                return (str(result.string[5:]) + ":" + str(soup.title.string[:-13]))
        return -1

    def main(self):
        ret = self.get_covid19_info()
        if ret != -1:
            print("Google Search PASS")
            return ret
        else:
            print("Google Search Failed")
            while(True):
                print("After 10 minutes, the search will be restarted...")
                time.sleep(300)
                retry += 1
                ret = self.get_covid19_info()
                if ret != -1:
                    return ret
                elif retry >= 10:
                    break
                else:
                    continue
gs = google_search()
ret = gs.main()
print(ret)
