cairo = ['ali', 'mohamd', 'alii']
dobi = ['esa', 'ahmed', 'tizi']
egypt = ['hhhh', 'kaml', 'kmall']
name = input('Enter your name: ')

if name in cairo:
    office = 'cairo'
elif name in dobi:
    office = 'dobi'
elif name in egypt:
    office = 'egypt'
else:
    office = False
    print("Office not found")

if office:
    print(f"Name: {name}, Office: {office}")