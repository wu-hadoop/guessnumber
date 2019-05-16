import random

r=random.randint(1,100)
#print (r)
while True:
  num=input('猜數字')
  num=int(num)
  if num == r:
    	print("bingo")
    	break
  elif num >r:
    	print('太大')
  elif num < r:
        print('太小')	
    	
