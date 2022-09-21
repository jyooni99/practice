import os

#Python 디렉터리 내부의 디렉터리와 파일을 출력
ret_1 = os.listdir("C:/Python")    
print(ret_1)


#현재 디렉터리의 경로 출력 
ret_2 = os.getcwd()
print(ret_2, type(ret_2))


#파일 이름 변경
os.rename("C:/Users/berry/Desktop/practice/python/after.py", "C:/Users/berry/Desktop/practice/python/mymod.py")

