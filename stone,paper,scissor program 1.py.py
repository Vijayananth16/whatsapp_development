
import random
user_choice=int(input("enter number between 0 to 2 ,0=rock,1=paper,2=scissor:"))
comp_choice=random.randint(0,2)
print("computer choice")
if user_choice<3:
 if user_choice==2 and comp_choice==0:
    print("you lose")
 elif user_choice==0 and comp_choice==2:
    print("you win")
 elif user_choice > comp_choice:
    print("you win")
 elif comp_choice > user_choice:
    print("you lose")
 elif user_choice==comp_choice:
    print("match draw")
else:
    print("you enter wrong number")
wait for next code
