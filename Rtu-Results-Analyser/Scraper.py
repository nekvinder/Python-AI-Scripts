# results extractor
from bs4 import BeautifulSoup
import requests
import json
import UrlConfig
from contextlib import suppress


def getReultsJson(url, subjectsCount, rnoStart, rnoEnd):
    Records = dict()
    Marks = dict()
    for i in range(rnoStart, rnoEnd+1):
        with suppress(Exception):
            print("Progress: "+str(round((i)*100/(rnoEnd-rnoStart))) + "%")
            r = requests.get(url+str(i).zfill(2))
            data = r.text
            soup = BeautifulSoup(data, features="html.parser")
            table = soup.find_all('table')
            rows = table[0].find_all('tr')
            roll_no = rows[5].find_all('td')[1].find('font').get_text().strip()
            name = rows[6].find_all('td')[1].find('font').get_text().strip()

            rows = table[1].find_all('tr')
            for i in range(1, subjectsCount+1):
                subcode = rows[i].find_all('td')[0].find(
                    'font').get_text().strip()
                subname = rows[i].find_all('td')[1].find(
                    'font').get_text().strip()
                subinternal = rows[i].find_all(
                    'td')[2].find('font').get_text().strip()
                subexternal = rows[i].find_all(
                    'td')[3].find('font').get_text().strip()
                subtotal = rows[i].find_all('td')[4].find(
                    'font').get_text().strip()
                Marks[subcode] = {"Subject Name": subname, 'Internals': subinternal,
                                  'External': subexternal, 'Total': subtotal}
            result = rows[subjectsCount +
                          2].find_all('td')[3].find('font').get_text().strip()
            grandTotal = rows[subjectsCount +
                              2].find_all('td')[1].find('font').get_text().strip()
            Records[roll_no] = {'Student Name': name,
                                'Grand Total': grandTotal, 'Result': result, 'Marks': Marks}

    return json.dumps(Records)


# examName = "my-2nd-sem"
# url = "https://www.rjlive.in/RTU/Show-Result?Examno=3332&key=C9397ED8F9399168690FC5BF85F1301D05C7427F&no=17emtcs0"
# subjectsCount = 11
# rnoFrom=0
# rnoTo=51
# config = UrlConfig.config(UrlConfig.Types.my_1st_sem)
# config = UrlConfig.config(UrlConfig.Types.my_1st_sem_reval)
# config = UrlConfig.config(UrlConfig.Types.my_2nd_sem)
config = UrlConfig.config(UrlConfig.Types.my_2nd_sem_reval)
f = open('rtu-data\\'+config.examName+".json", 'w+')
f.write(getReultsJson(config.url, config.subjectsCount,
                      config.rnoFrom, config.rnoTo))
f.close()
print("Done")
