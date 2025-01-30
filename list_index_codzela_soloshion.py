drinks = [
# hot drinks
['Tea', 'Herbs', 'Hot Cider', 'Coffee', 'Hot Chocolate'],
# soda
['Coke', 'Pepsi', 'Fanta', 'Sprite', 'Mirinda'],
# juices
['Lemonade', 'Orange Juice', 'Mango Juice',
'Strawberry Juice', 'Apple Juice']
]


message_type_drink = f"""
Please, Enter the type of the drink you want to order:
1. Hot Drinks
2. Soda
3. Juices
"""
# get the type of the drink index
order_index_type = int(input(message_type_drink))
# a message to ask the user for the drink
message_drink = f"""
Please, Enter the number of the drink you want to order:
1. {drinks[order_index_type - 1][0]}
2. {drinks[order_index_type - 1][1]}
3. {drinks[order_index_type - 1][2]}
4. {drinks[order_index_type - 1][3]}
5. {drinks[order_index_type - 1][4]}
"""
# get the drink index
order_index = int(input(message_drink))
print('-' * 50)
# get the drink, choose the type then the drink
order = drinks[order_index_type - 1][order_index - 1]
# print the order
print('Thanks for choosing Codezillas Café!')
print(f'Please, Enjoy your time\nWhile we get {order} ready for you.')
