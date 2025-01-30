input_1=input('enter your input: ')
if input_1.isnumeric():
    print(f"{input_1} you enter number")
elif input_1.isalpha():
    print(f"{input_1} you enter letter")
elif input_1.isalnum():
    print(" there amix betwin number and letter ")

print('_'*20)
number=float(input('enter the number :')) #20
sec_number=float(input('enter the second number : '))#6
opretor=input("enter the opretor: ")#+
if opretor=="+":
        rseolt=number+sec_number
        print(rseolt)
elif opretor=="-":
        rseolt=number-sec_number
        print(rseolt)
elif opretor=="/":
        rseolt=number/sec_number
        print(rseolt)
elif opretor=="*":
        rseolt=number*sec_number
        print(rseolt)
else:
      print('plese enter avalid input')

print('_'*20)

print("plese enter number betwin 0 and 100")
arabic_scor=float(input('enter  arabic scor : '))
english_scor=float(input('enter  english scor : '))
Math_scor=float(input('enter  Math scor : '))
logic_scor=float(input('enter  logic scor : '))
avg_grade=(arabic_scor+english_scor+Math_scor+logic_scor)/4
if avg_grade>90:
      print(f"your scor is {avg_grade} \n your grade is A ")
elif    80<avg_grade<90:
      print(f"your scor is {avg_grade} \n your grade is A-- ")
elif 75<avg_grade<80:
      print(f"your scor is {avg_grade} \n your grade is B ")
elif 60<avg_grade<74:
      print(f"your scor is {avg_grade} \n your grade is C ")




