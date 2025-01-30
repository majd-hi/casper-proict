name_1 =input("Enter a name: ")#mohamd hihi
index=name_1.index(" ")
print(f"welcom{name_1[:index]}\n welvom at codzella")
print('_'*20)
name=input('enter a name: ')
company_name=input('Enter a company name : ')
birthday=input('enter a birthday : ')
emial=input('enter a email : ') #mohamd@hotmil.cpm
#id = first 3 characters of company name + - + last 2
# characters of name + birth year
index=name.index(" ")
print(f"welcom {name[:index]}\n welcom at {company_name}")
print('_'*20)
print(f" your id id :{company_name[:4]} - {name[-2:]} {birthday} ")
index=emial.index("@")
print(f"your email is : {emial[:index]} @gmail.com ")