id=input( "enter the id:"  )
hourly_rate=float(input('enter hourly rate: '))
total_hours=float(input("enter hours work this month"))
salary=hourly_rate*total_hours
# employees and their ids
juniors = ['1111', '1113', '1115', '1117',
'1119', '1121']
mid_level = ['1311', '1313', '1315', '1317',
'1319', '1321', '1323', '1325']
seniors = ['1519', '1521', '1523', '1525']
if id in juniors:
    salary_with_bouns=salary*3
    print(f"employed id: {id} gets a bouns of a {salary_with_bouns}")
elif id in mid_level:
     salary_with_bouns=salary*6
     print(f"employed id: {id} gets a bouns of a {salary_with_bouns}")
elif id in seniors:
      salary_with_bouns=salary*9
      print(f"employed id: {id} gets a bouns of a {salary_with_bouns}")
else:
     print("not in a employ")










