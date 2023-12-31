import random

def game():
  number=random.randint(1,100)
  attempt=1
  print("Game Started")
  guess=int(input("Guess a number:"))


  while(True):
    if(guess>number):
        print("Not matched!")
        guess=int(input("Guess less than this number:"))
        attempt+=1
    elif(guess<number):
        print("Not matched!")
        guess=int(input("Guess greater than this number:"))
        attempt+=1
    else:
        print("Matched! You won\nYou guessed correct number:-)")
        print(f"You have {attempt} attempts")
        break
S=game()
print(S)
while(True):
 Choice=int(input("Do you want to continue?\nfor Yes enter 1\nfor No enter 0\nEnter your choice:"))
 if(Choice==1):
   print(game())
   continue
 elif(Choice==0):
    print("Thankyou for playing!\nHope you will be back:-)")
    break
 

  
