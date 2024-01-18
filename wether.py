from urllib.request import urlopen
import json

from geopy.geocoders import Nominatim

url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst" + \
    "?serviceKey=V8YwjBTSxcGvHh6or3ppvBEGZP66lmlHx7NB%2BsfMOA1E5d2Qdjan7drVXpwmjMiQaonO0x6msCgNTrwb2dIFiQ%3D%3D" + \
    "&numOfRows=60&pageNo=1" + \
    "&base_date=20240117&base_time=1630&nx=61&ny=125&dataType=JSON"
answer = urlopen(url).read()
data = json.loads(answer)
print(data)
rain = dict()
temper = dict()
for item in data["response"]["body"]["items"]["item"]:
    if item["category"] == "RN1":
        rain[item["fcstTime"]] = item["fcstValue"]
    if item["category"] == "T1H":
        temper[item["fcstTime"]] = item["fcstValue"]
for k, v in rain.items():
    print("{}시에 예상 강수량 {}".format(k, v))
for k, v in temper.items():
    print("{}시에 예상 온도 {}".format(k, v))



geo_local = Nominatim(user_agent='South Korea')
geo = geo_local.geocode('서울시')
x_y = [geo.latitude, geo.longitude]
print(x_y)