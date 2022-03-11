import json
import sys
import requests
import os
import logging
import datetime
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
cookie = os.environ["COOKIE"]
uid = os.environ["UID"]
get_url = "https://hk4e-api.mihoyo.com/event/birthdaystar/account/index?lang=zh-cn&uid=%s&region=cn_gf01&activity_id=20220301153521" % uid
url = "https://hk4e-api.mihoyo.com/event/birthdaystar/account/post_my_draw?lang=zh-cn&uid=%s&region=cn_gf01&activity_id=20220301153521" % uid
calendar = "https://hk4e-api.mihoyo.com/event/birthdaystar/account/calendar?lang=zh-cn&uid=140309417&region=cn_gf01&activity_id=20220301153521&year=2023"
r = requests.Session()
r.headers["Cookie"] = cookie
r.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"


def re(r):
    g = r.get(get_url).json()
    logging.info(f"Index: {g}")
    r = g["data"]['role']
    for i in r:
        if i["is_partake"] == False:
            t = requests.post(url, str({"role_id": int(i['role_id'])}).replace("'", '"'), 
                headers={"Cookie": cookie,
                         "Content-Type": "application/json;charset=UTF-8",
                         "Referer": "https://webstatic.mihoyo.com/"})
            logging.info(f"Received: {t.text}")
            logging.debug(f"成功领取{i['name']}的画册")

if "--forced-indexed" in sys.argv:
    re(r)
else:
    t = datetime.date.today()
    m = t.month
    d = 14
    b = f"{m}/{d}"
    if "--use-locals" in sys.argv:
        with open("calendar.json",encoding="UTF-8") as f:
            c=json.loads(f.read())
    else:
        c = r.get(calendar).json()

    logging.info(f"Calendar: {c}\n")
    for i in c["data"]["calendar_role_infos"][str(m)]["calendar_role"]:
        if i["role_birthday"] == b:
            logging.debug(f"今日是{i['name']}的生日")
            re(r)


logging.debug("Run finished")
