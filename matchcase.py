cairo = ['ali', 'mohamd', 'alii']
dobi = ['esa', 'ahmed', 'tizi']
egypt = ['hhhh', 'kaml', 'kmall']
office=input('enter your office: ').lower()


match office:
 case  'cairo'|'as':
   office1=cairo
 case 'dobi'|'ws':
    office1=dobi
    
 case 'egypt'|'wd':
   office1=egypt
   
 case _:
   print('not found')
if  office1:
     office_str=','.join(office1[:-1])
     print(f'{office_str} and {office1[-1]}')
   

  