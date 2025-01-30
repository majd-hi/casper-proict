hight=int(input("enter the hight :"))
if hight>200:
 print(f"{hight} cm is consedred  very tall")
elif 180< hight <200:
 print(f"{hight} cm is consedred tall")
elif 160<hight<180:
 (f"{hight} cm is consedred normal")
elif hight<150:
 (f"{hight} cm is consedred short")

 print("_"*20)

 # greeting
print('It is the time to see if we could do better 😃')
print('-'*20)
# getting the number
num = float(input('Enter the number: '))
# getting the guess
guess = input(f'{num} is even or odd? 🤔🤔\n').lower()
# compare the numbers
if (num%2==0 and guess=='even') or (num%2!=0 and guess=='odd'):
  print('Bravoooo!!! 🥳🥳🥳')
else:
 print("No problem, let's try again 😀")

  
  

