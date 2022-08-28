"""

#113p5번 while버전
숫자 = 1

while 숫자 <= 100:
    print(숫자, end='\t')

    if 숫자 % 10 == 0:
          print("")
    숫자 = 숫자 + 1

#113p5번 for 버전

for 십의자리 in range(10):
      for 일의자리 in range(10):
         print((십의자리*10)+일의자리+1, end='\t')
print("")
  """
