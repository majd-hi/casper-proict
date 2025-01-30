num=input("enter the number")
num_div=input("enter the numberf divid by")
result=int(num)/int(num_div)
print(f"the div result {result}")
if int(num)%int(num_div)==0:
    print(f"{num} is dived by {num_div}")
else:
    print('false')
print("-"*20)
f_num=int(input("enter the first number"))
s_num=int(input("enter the second number"))
l_num=int(input("enter the last number"))
if f_num>s_num and f_num>l_num:
        print(f"the big number is{f_num} ")
elif s_num>f_num:
        print(f"the big number is{s_num} ")
else:
        print(f"the big num is {l_num}")
print("_"*20)
amount_of_money=int(input("enter the amount of money"))
print("_"*20)
f_item=int(input("enter the first item: "))   #200
s_item=int(input("enter the second item: "))  #100
l_item=int(input("enter the last item: "))     #80
t_item=(f_item)+(s_item)+(l_item)
result_1=(amount_of_money)-(t_item)
if (amount_of_money) >= (result_1):
    print(f"item have been purshesd\n the reman amount{result_1:.2f}")
else:
    print(f"sory you dont have enogh balance\n you need to add extra {result_1}")
