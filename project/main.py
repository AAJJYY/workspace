import requests
URL ='https://www.weather.go.kr/w/weather/forecast/mid-term.do'
res = requests.get(URL)
from bs4 import BeautifulSoup
soup = BeautifulSoup(res.text, 'html.parser')
#날짜별 오전오후
map = {"location" : "" , "date" : "" , "max" : "" , "min" : "" , "cloud" : "" } 
weather=soup.select('table.table-zebra thead tr')
for i in weather :
    day_1 =i.text.split('\n')
    print(day_1)

# 지역별 강수 확률 및 구름량(?)
region=soup.select('body > div.container > section > div > div.cont-wrap.cmp-midterm > div > div > div.tab-menu-cont > div:nth-child(6) > table > tbody > tr')
for i in region :
    kor=i.text.split('\n')
    print(kor)

# 날짜 배열 
# 최대 최저기온 추출 
day_2=soup.select('body > div.container > section > div > div.cont-wrap.cmp-midterm > div > div > div.tab-menu-cont > div:nth-child(9) > table > thead > tr')
day_final=day_2[0].text.split('\n')
max_min_temp=soup.select('body > div.container > section > div > div.cont-wrap.cmp-midterm > div > div > div.tab-menu-cont > div:nth-child(9) > table > tbody > tr')
temp=[]
for i in range((len(max_min_temp))):
    temp = max_min_temp[i].text.split('\n')[1:-2]
    print(day_final,'\n',temp)


    



#import telegram
# telegram_config={}
# with open('./telegram_config','r') as f:
#     configs = f.readlines()
#     for config in configs :
#         key, value =config.rstrip().split('=')
#         telegram_config[key]=value
# print(telegram_config)
# token = telegram_config['token']
# bot = telegram.Bot(token)
# updates=bot.getUpdates()
# chat_id = updates[-1].message.chat.id
# last_message = updates[-1].message.message_id #마지막 받은 메세지 (.text)
# update_id=bot.getUpdates()[-1].update_id
# last_id = updates[-1].update_id
# 서버에서 텔레그램 메시지 확인, 응답 보내기
# import time

# while True:
    
#     try:
#         # 신규 메시지가 없을 경우 에러가 발생 
#         # list index out of range
#         # 따라서, try - except 문으로 묶어줌
#         new_message = bot.get_updates(offset=last_id)[-1]

#         # 만약 신규 메시지가 오늘날씨면,
#         if new_message.message.text == '오늘날씨':
#             # 관련 메시지 발송
#             bot.send_message(chat_id, '오늘날씨는 화창합니다.')
#         # 만약 신규 메시지가 내일날씨면,
#         elif new_message.message.text == '내일날씨':
#             # 관련 메시지 발송
#             bot.send_message(chat_id, '내일날씨도 화창합니다.')

#         # offset 값 최신화 (update_id) + 1 해줘서 그 다음부터 메시지부터 확인하도록
#         last_id = new_message.update_id + 1
#     except:
#         pass

#     # 텔레그램 서버 부하 줄이기 위해 3초마다 확인
#     time.sleep(3)
