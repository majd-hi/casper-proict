#a list of pizzas
pizzas = [
'Margherita'
,
'Pepperoni'
,
'Super Supreme'
,
'Hawaiian'
,
'Meat Lovers'
,
'Cheese Lovers'
]
print(f"1.{pizzas[0]}\n2.{pizzas[1]}\n3.{pizzas[2]}\n4.{pizzas[2]}\n5.{pizzas[3]}\n6.{pizzas[4]}\n7.{pizzas[5]}")
show_piza=int(input('plese enter the nomber of piza do you want: '))
num_of_pizza=input('enter the number of pizza : ')
print("THAMKS FOR CHOSING GODZELA RESTURENR\n enjoy your food ")
print(f'while we get {num_of_pizza} {pizzas[show_piza]} redy for you')

print('_'*20)

# a list of hot drinks, soda, and juices
drinks = [
# hot drinks
['Tea', 'Herbs', 'Hot Cider', 'Coffee', 'Hot Chocolate'],
# soda
['Coke', 'Pepsi', 'Fanta', 'Sprite', 'Mirinda'],
# juices
['Lemonade', 'Orange Juice', 'Mango Juice',
'Strawberry Juice', 'Apple Juice']
]
typee_drink=int(input(f'plese enter the type of drink of you want :\n1.hot drinks \n2.soda\n3.juices'))
num_drinks=int(input(f'plese enter the number of drink of you want \n{drinks[typee_drink]}'))
print("THAMKS FOR CHOSING GODZELA cafee\n enjoy your drink ")
print(f'while we get {drinks[typee_drink][num_drinks-1]} redy for you')

print('_'*20)
# a list of students’ ids
students = [
# Codezilla school
['1100', '1101', '1102', '1103', '1104',
'1105', '1106', '1107', '1108', '1109'],
# Al Dorra school
['2100', '2101', '2102', '2103', '2104',
'2105', '2106', '2107', '2108', '2109'],
# Mostafa Kamel school
['3100', '3101', '3102', '3103', '3104',
'3105', '3106', '3107', '3108', '3109']
]
students_id=input('Enter students_id: ')
if students_id in students[0]:
  print('the students is in Codezilla school')
elif students_id in students[1]:
  print('the students is in Dorra school')
elif students_id in students[2]:
  print('the students is in Mostafa Kamel school')
else:
  print('the id is not corect??')