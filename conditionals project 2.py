hight=int(input('enter the hight: '))
wight=int(input('enter the wight: '))
bmi=hight/wight
#if   hight>200 and hight>90:
#print("enter valid value")
if 150<=hight<=160 and 45<wight<60:
    print(f"your bmi is{bmi} and you are normal")
elif 161<hight<180 and 61<=wight<=80:
    print(f" your bmi is{bmi} and you are oversize")
    print("_"*20)
    # lists containing the code of items with sales
sales_70 = ['070', '170', '270', '370', '470']
sales_50 = ['050', '150', '250', '350', '450']
sales_30 = ['030', '130', '230', '330', '430']
code_of_item=input('enter the code of item') #070
price_item=int(input('enter the price of item'))#1800
sales1_70=price_item-(price_item*70/100)
sales1_50=price_item-(price_item*50/100)
sales1_30=price_item-(price_item*30/100)
if code_of_item in sales_70:
    print(f'the final price of  cod{code_of_item} is {int(sales1_70)} egb')
elif code_of_item in sales_50:
    print(f'the final price of  cod{code_of_item} is {int(sales1_50)} egb')
elif code_of_item in sales_30:
    
    print(f'the final price of  cod{code_of_item} is {int(sales1_30)} egb')

    print('_'*20)
    print("lets see how we could deal with wather")
degre=int(input('enter the degree in silus : '))

extremely_hot = """When the degree is 40 or more
We could say that the weather is extremely hot 🔥🔥♨
we should avoid direct exposure to The Sun ☀☀
We should also remember to drink a lot of water 💦
"""
very_hot = """When the degree is 30 or more
We could say that the weather is very hot 🔥♨
we should be careful about direct exposure to The Sun ☀
We should also remember to drink a lot of water 💦
"""
moderate = """When the degree is between 20 and 30
We could say that we have moderate or good weather 🌞🌞
We should not go with too heavy nor too light clothes 👕
"""
cold = """When the degree is between 10 and 20
We could say that we have cold weather ❄❄
We should not go with pretty heavy clothes 👕
"""
very_cold = """When the degree is between 0 and 10
We could say that we have very cold weather ❄❄❄
We should go with pretty heavy clothes 👕
"""
extremely_cold = """When the degree is less than 0
We could say that we have extremely cold weather ❄🧊🧊☃
We should avoid getting out as possible 🧊🧊
We should go with really heavy clothes 👕
Never forget your Heavy Jacket 🧥 wheny you are going out 🧊🥶
"""
if degre>=40:
    print(extremely_hot)
elif 30<=degre<40:
    print(very_hot)
elif 20<=degre<=30:
    print(moderate)
elif 10<=degre<20:
    print(cold)
elif  0<=degre<10:
    print(very_cold)
elif degre<0:
    print(extremely_cold)





