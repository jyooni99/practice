#클래스 정의                                 [class 클래스명: ]
#인스턴스 생성 > 클래스 이름 적고 괄호 닫기     [인스턴스 = 클래스명()]
#객체에 점(.)을 찍으면 객체 공간에 접근을 의미  [인스턴스.속성 = "값"]
#객체 공간에 있는 변수를 속성이라고 부름, 객체 공간에 있는 변수를 속성이라고 부름
#print(인스턴스.속성)  > 값 출력 
#클래스 내에서 정의된 함수 = 메서드


class account:
    def create(self, name, balance):
        self.name = name
        self.balance = balance
    
    def output(self):
        print(f"이름: {self.name}")
        print(f"잔액: {self.balance}원")


account1 = account()     #빈 객체 공간 생성
account.create(account1,"김철수", 500)  #클래스.메서드(객체명, 인자, 인자)  >> 객체에 값 집어넣기 

account1.output()        #객체.메서드(인자)   >> 파이썬에서 자동으로 클래스.메서드(객체) 형태로 변경해 호출하므로 동일한 값 출력
account.output(account1) #클래스.메서드(객체)  >> 둘 다 동일한 값 출력


#객체.메서드(인자)의 예
#a = [1,2,3]   #list 클래스의 객체 생성
#a.append(4)   #list 클래스의 append 메서드를 a 객체에 대해 호출
#b = "hello"   #문자열 클래스의 객체 생성
#b.upper()     #문자열 클래스의 upper 메서드를 b 객체에 대해 호출 



#생성자  __init__(self)   >> 객체가 생성될 때 파이썬 인터프리터에 의해 자동으로 호출되는 메서드, 객체에 데이터를 넣거나 초기화하는 목적으로 사용
class account_ver2:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def output(self):
        print(f"이름: {self.name}")
        print(f"잔액: {self.balance}원")

account2 = account_ver2("이영희", 1500)   #객체를 생성하면 __init__이 바로 호출되므로 __init__의 인자인 name과 balance를 입력해주어야 객체가 오류없이 생성됨.
account2.output()



class person:
  def __init__(self, name, birth, gender):
    self.name = name
    self.birth = birth
    self.gender = gender
  
  def output(self):
    b_year = self.birth[:4]
    b_month = self.birth[4:6]
    b_day = self.birth[6:8]
    print(f"{b_year}년 {b_month}월 {b_day}일 출생")
    print(f"({self.gender}) {self.name}")

first = person("유종훈", "19860302", "남")
first.output()