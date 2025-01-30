import random

winer_num1 = random.randint(1,20) 
winer_num2 = random.randint(1,20) 
winer_num3 = random.randint(1,20) 
winer_num4 = random.randint(1,20) 

num=int(input('enter a num: '))
num1=[winer_num1,winer_num2,winer_num3,winer_num4]
if num in num1:
      print('your win')
else:
      print('your lost')
print('_'*20)
coin_rand=random.randint(1,2)
cion=int(input('enter coin number :\n1.for hed \n2.for tails'))
if coin_rand==cion:
    print('your win')
else:
    print('your lost')

print('-'*20)
dis_random=random.randint(1,6)
dis= int(input('enter a dic betwin 1 to 6 :'))
if dis_random==dis:
        print('your win')
else:
        print('your lost')

