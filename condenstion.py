name=input('enter the name : ')
winners = ['mohamed', 'ahmed', 'mahmoud', 'islam',
'hassan', 'israa', 'mariam']
if name in winners:
    print(f'congrajelashion {name} is wener')
else:
    print(f'sorry {name} is not wenner')
print('_'*20)

First_username = 'islam_hesham@codezilla.com'
First_password = 'islam_codezilla'
second_username = 'mohamed_gouda@codezilla.com'
second_password = 'gouda_codezilla'
username=input('enter first user name')
password=input('enter first passord') 
if First_username==username and First_password==password:
    print('you can accsess')
elif second_username==username and second_username==password:
    print('you can accsess')
else:
    print("accses not avelable")

    print("_"*20)
    # lists of countries and their weekends
countries_fri_sat = ['egypt', 'saudi arabia', 'ksa',
'kuwait']
countris_sat_sun = ['australia', 'usa', 'united states',
'united kingdom', 'uk']
county_frday_satardy=input('enterv the country: ')
county_satrday_sunday=input('enterv the country: ')
if county_frday_satardy in countries_fri_sat:
    print(f'fraday and satrday are the wekkend in{county_frday_satardy}')
elif county_satrday_sunday in countris_sat_sun:
 print(f'satrday and sunday  are the wekkend in{county_satrday_sunday}')





