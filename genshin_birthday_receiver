import requests,os
cookie=os.environ["COOKIE"]
uid=os.environ["UID"]
get_url="https://hk4e-api.mihoyo.com/event/birthdaystar/account/index?lang=zh-cn&uid=%s&region=cn_gf01&activity_id=20220301153521"%uid
url="https://hk4e-api.mihoyo.com/event/birthdaystar/account/post_my_draw?lang=zh-cn&uid=%s&region=cn_gf01&activity_id=20220301153521"%uid
g=requests.get(get_url,headers={"Cookie":cookie}).json()
print(g)
r=g["data"]['role']
for i in r:
    if i["is_partake"]==True:
        t=requests.post(url,str({"role_id":int(i['role_id'])}).replace("'",'"'),headers=
        {"Cookie":cookie,
        "Content-Type": "application/json;charset=UTF-8",
        "Referer":"https://webstatic.mihoyo.com/"})
        print(t.text)
        print(f"成功领取{i['name']}的画册")


print("Run finished")
