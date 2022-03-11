import json
import sys
import requests
import os
import logging
import datetime
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
cookie = "_MHYUUID=f649b229-7eff-46f8-ad3c-f88ac117a75e; _ga_5DECE6NN1T=GS1.1.1614046401.3.1.1614046410.0; _ga_FLGX56JEBS=GS1.1.1614342832.6.1.1614343012.0; _ga_WMZDYVPMF8=GS1.1.1623548336.1.1.1623548494.0; _ga_0S6JZDKDXS=GS1.1.1624629175.3.1.1624630115.0; _ga_QH3ZTJN1H1=GS1.1.1630027087.8.1.1630027725.0; _ga_E36KSL9TFE=GS1.1.1630026952.10.1.1630027744.0; _ga_D108ZZQL8P=GS1.1.1630243172.4.1.1630243254.0; _ga_5CED51PLFC=GS1.1.1632050486.5.1.1632050587.0; _ga_H3M17VQB59=GS1.1.1632102894.5.1.1632103003.0; _ga_7STMV3SJ3S=GS1.1.1632103010.2.1.1632103060.0; _ga_Q2VXM5EQKX=GS1.1.1633060792.3.1.1633061058.0; _ga_KJ6J9V9VZQ=GS1.1.1633148874.4.0.1633148878.0; _ga_M6C431156S=GS1.1.1633160364.3.0.1633160412.0; _ga_6ZB57V7XXT=GS1.1.1634297226.1.0.1634297249.0; _ga_YQPW66MJ73=GS1.1.1634306930.1.1.1634306941.0; _ga_CXN1FSHKS4=GS1.1.1634307939.5.1.1634308400.0; _ga_831VBKXN1V=GS1.1.1634965258.5.1.1634965470.0; _ga_XVG5SLNQHV=GS1.1.1635503904.1.1.1635504784.0; ltoken=PAVvTMkryfMoCs8H6ZGz6tCAZr8zepZD53DuUDRV; ltuid=237006471; _ga_4PPV2TWM03=GS1.1.1636270843.3.1.1636271168.0; _ga_87WPJV8929=GS1.1.1636873943.1.1.1636874184.0; _ga_HKTGWLY8PN=GS1.1.1637422216.10.1.1637422302.0; cookie_token=ORD7xK0tgqUhiw59sNGv0rifl3Ffy2iQfwhvpPkH; account_id=237006471; _ga_1JLDNKW30C=GS1.1.1641100953.2.1.1641101041.0; _qddaz=QD.aujth3.p1g1i8.kypaqixl; mi18nLang=zh-cn; _ga_E6T63X3GHE=GS1.1.1643595490.3.1.1643595728.0; _ga_XR5VD06Z8Y=GS1.1.1643860149.8.1.1643860429.0; _ga_Q3LKDGYS1J=GS1.1.1644245007.1.1.1644245159.0; UM_distinctid=17ef25c6ff6bc-06f840e3f2dbb2-5b161c50-1fa400-17ef25c6ffa292; _ga_9TTX3TE5YL=GS1.1.1646106734.10.0.1646106734.0; _ga_QYFFEX7F52=GS1.1.1646125886.2.0.1646125886.0; _ga_7QF7V7R7V6=GS1.1.1646280641.1.1.1646280824.0; _gid=GA1.2.1653338797.1647007050; _ga=GA1.2.529242760.1603800169; _ga_P308KCCFXP=GS1.1.1647007078.2.1.1647007222.0"
uid = 140309417
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
