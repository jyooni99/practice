import datetime, time

now = datetime.datetime.now()  #오늘 날짜, 시간 출력

after_100 = now + datetime.timedelta(100) # 오늘로부터 100일 뒤
print(after_100)  


#시간 양식에 맞게 출력(strftime) 2022-09-18
print(now.strftime("%Y년 %m월 %d일"))       # 2022년 09월 18일
print(now.strftime("%p %H시 %M분 %S초"))       # AM 03시 04분 22초
print(now.strftime("Today: %a %d %b %y"))  # Today: Sun 18 Sep 22
print(now.strftime("Today:%A %d %B %Y"))   # Today: Sunday 18 September 2022

#  %w = 요일을 10진수로 [일요일(0) ~ 토요일(6)]
#  %l = 시간을 12시간제로 출력
#  %Z = 시간대 이름 (UTC, GMT 등)
#  %j = 연중 일을 십진수로 출력 [001 ~ 366]


#문자열 형식의 시간을 datetime.datetime 타입으로 변경
import datetime

day = "2020-05-04"
result = datetime.datetime.strptime(day, "%Y-%m-%d")
print(result)


#실행 후 5초 뒤 Goodbye 프린트
print("Hello")
time.sleep(5)     #호출 수행을 잠시 멈춤 (5초 sleep)
print("Goodbye")


# 5초 동안 1초 간격으로 현재 시간 출력
for i in range(1,5):
    now = datetime.datetime.now()
    print(now)
    time.sleep(1)
