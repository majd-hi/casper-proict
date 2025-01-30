# list of available vegetables
vegetables = ['broccoli', 'eggplant', 'carrot', 'cabbage',
'cucumber', 'potato', 'garlic', 'pepper']
print("welcom at codzeala vegtables ")
vagtibals_1 =input("enter a vigtabls do you want to get : ")
amount =input('enter the amount in kg : ')
if vagtibals_1 in vegetables:
    print(f'we will get you a {amount} kg of {vagtibals_1} very soon')
else:
    join_1=", ".join(vegetables)
    print(f"sorry we only have {join_1}")