# text = """A computer is a digital electronic machine
# that can be programmed to carry out sequences of
# arithmetic or logical operations automatically"""
# print(len(text))
# withot_space=text.replace(" ","")
# print(len(withot_space))

print("_"*20)

# name=input("enter your name : ")
# birthday=input('enter a birthday day (dd-mm-yy): ')#30-33-1978
# age=int(input("enter a curent age : "))
# index=name.index(" ")
# print(f" hello {name[:index]} welcom at age calcoter ")
# g=birthday[-4:]
# age_calcoter=age-int(g)
# print(f" your age is {age_calcoter}")

print("_"*20)
first_num, operator, second_num = input('Enter The Operation: ').split()
print('-'*20)
# convert to float
first_num = float(first_num)
second_num = float(second_num)
# check the operator and do the operation
if operator=='+':
  operation_name = 'Addition'
  result = first_num + second_num
elif operator=='-':
 operation_name = 'Subtraction'
 result = first_num - second_num
elif operator=='*':
 operation_name = 'Multiplication'
 result = first_num * second_num
elif operator=='/':
 operation_name = 'Division'
 result = first_num / second_num
elif operator=='**':
 operation_name = 'Power'
 result = first_num ** second_num
# print the result
print(f'{operation_name} result is {result:,.2f}')



