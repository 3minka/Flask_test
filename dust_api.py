import requests # 서버에 요청 보내는 라이브러리
import json

def dust_level(data):
    word = ""
    if 0<=data < 10: word="매우 좋음"
    elif 10<=data < 20: word="나쁨"
    elif 20<=data < 30: word="매우 나쁨"
    return word

    

def get_dust_data():
    endpoint_url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc"
    service_path = "/getMsrstnAcctoRltmMesureDnsty"

    API_KEY = "Q+bBtd4d5lmD6aYLVIgrBu+s+Z4Q61dbY/nabbR9gcllovzit2EJeDdm+Rkyx6J782auDB55PmmQdl5BxUa+9A=="
    STATION_NAME = input("지역 구를 입력해주세요. ex)강남구 :: ")
    params = {
        "serviceKey" : API_KEY,
        'returnType' : 'json',
        "numOfRows" : 1, # 시간대별 데이터 
        "pageNo" : 1,
        "stationName" : STATION_NAME,
        "dataTerm" : 'DAILY',
        "ver" : '1.0'
    }
    res = requests.get(f"{endpoint_url}{service_path}", params=params)
    print(res)
    
    if res.status_code == 200:
        print('Data successfully')
        data = json.loads(res.text)
        # print(data)
        items = data['response']['body']['items']

        for item in items:
            dust_level_val = dust_level(int(item['pm10Value'])) # 미세먼지, 초미세먼지는 pm25Value
            print(dust_level_val)
    else:
        print("Request failed {}".format(res.code))
get_dust_data()

