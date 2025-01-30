word = input('Enter a word :' ) 
violet = ['a','i','o','u']
chek =  input('Dose the word start with a violetio :\n')

if  word[0] in violet and chek=='yes':
    print(f'bravo  the {word} statr with viol')
elif word[0] not in violet and chek=='no':
    print(f'bravo the {word} not start with viol')
else:
    print("try again")