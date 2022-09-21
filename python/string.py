#대문자/소문자
ticket = "Btc-Krw"
upper_ticket = ticket.upper()
print(upper_ticket)  #BTC-KRW

lower_ticket = ticket.lower()
print(lower_ticket)  #btc-krw


#문자열 쪼개기
date = "2022/09/07"
new_date = date.split("/")  #/을 기준으로 문자열 쪼갬
print(new_date[0])  #년 출력(2022)
print(new_date[1])  #월 출력(09)


#문자열 변경
name = "TAKAO"
new_name = name.replace('T','K',1)  #replace(변경전,변경후,횟수) 세 번째에 숫자를 안 적으면 전체를 변경
ox = "oxoxoxoxox"
new_ox = ox.replace("ox","*",3)
print(new_ox) #******oxox로 출력