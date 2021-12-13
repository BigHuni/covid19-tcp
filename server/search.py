import bs4
from urllib.request import urlopen, Request
from pytz import timezone
from datetime import datetime, timedelta
import os
import sys
import json
import re

def CoronaDataStack():
    jpath = os.getcwd()
    KST = datetime.now(timezone('Asia/Seoul'))
    today = KST.strftime('%Y%m%d')
    hdr = {'User-Agent': 'Mozilla/5.0'}
    url = 'http://ncov.mohw.go.kr/'
    req = Request(url, headers=hdr)
    html = urlopen(req)
    bsObj = bs4.BeautifulSoup(html, "html.parser")
    totalBase = bsObj.find('ul', {'class':'cityinfo'})
    total1 = totalBase.findAll('span', {'class':'num'})
    total = total1[0].text
    total = re.sub('[,]', '', total)
    isol = total1[1].text
    isol = re.sub('[,]', '', isol)
    deisol = total1[2].text
    deisol = re.sub('[,]', '', deisol)
    death = total1[3].text
    death = re.sub('[,]', '', death)
    tenM = total1[4].text
    with open(f"{jpath}/covid19.json", "r") as f:
        DB = json.loads(f.read())

    DB[today] = []
    DB[today].append({
            "total": total,
            "isol": isol,
            "deisol": deisol,
            "death" : death,
            "tenM" : tenM
            })
    with open(f"{jpath}/covid19.json", "w") as f:
        json.dump(DB, f, indent=4)
    print("record success")