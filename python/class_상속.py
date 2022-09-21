#상속 >> 기존의 클래스에서 구현된 메서드와 속성값을 새로운 클래스에서 그대로 사용할 수 있도록 하는 것

class bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"{self.name}님의 통장이 개설되었습니다. (통장 잔액: {self.balance}원)")
  
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}원이 입급되었습니다.  (통장잔액: {self.balance})")
  
    def withdraw(self, amount):
        if self.balance < amount:
            print("잔액이 부족합니다.  (통장잔액:",self.balance,"원)")
        else:
            self.balance -= amount
            print(f"{amount}원이 출금되었습니다.   (통장잔액:{self.balance}원)")

    def remit(self, other, amount):
        if self.balance < amount:
            print("잔액이 부족합니다.  (통장잔액:",self.balance,"원)")
        else:
            self.balance -= amount
            other.balance += amount
            print(f"{other.name}에게 {amount}원을 입금하였습니다.")
            print(f"통장잔액: {self.balance}")


account_1 = bank("이영희", 10000)
account_1.deposit(10000)


class minus_bank(bank):  
    def withdraw(self, amount): # 잔액보다 출금금액이 커도 출금 가능하게 수정
        self.balance -= amount
        print(f"{amount}원이 출금되었습니다.   (통장잔액:{self.balance}원)")

account_2 = minus_bank("홍길동", 10000)
account_2.withdraw(20000)