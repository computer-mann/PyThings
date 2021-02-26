import random

guess=0;
randNumber=1

while(guess != randNumber ):
    randNumber=random.randint(1,20)
    guess=int(input('Guess the number: '))

print('You got that right.')
     
     
