import random
import time
words = [
'have', 'that', 'they', 'with', 'this', 'from', 'which', 'would', 'will',
'there',
'make']
words_random=random.randint(0,len(words)-1)
the_words_index=words[words_random]
word_index=list(the_words_index)
#revers the word
word_index.reverse()
#join the word
word_index_1="".join(word_index)
print(word_index_1)
starttime=time.time()
guse_word=input('enter the word : ')
ansewr_time=time.time()
finish_time=ansewr_time-starttime
print(finish_time)
if guse_word==the_words_index and finish_time<=5:
    print('you win')
else:
    print('you lost')


