#game(rock,paper,scissor,stone)
import random
for i in range(1,4):

    game=["rock","paper","scissor"]
    user1=input("enter your choice=")
    user1_count=0
    computer_count=0
    computer=random.choice(game)
    print(computer)
    if user1==random.choice(game):
        print("tie")
    elif ((user1 =="rock" and game=="scissor") or (user1=="scissor" and game=="paper") or (user1=="paper" and game=="rock")): 
        print("game won")
        user_win+=1
        print()
    else:
        print("computer wins")
if user1_count>computer_count:
    print("user1 won")
else:
    print("computer won")

  





