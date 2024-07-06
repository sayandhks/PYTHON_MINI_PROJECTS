import random

computer_wins=0
user_wins=0
options= ["r","p","s"]

while True:
    user_input=input(" enter r-rock ,  p-paper , s-scissor and q-quit :) ").lower()
    if user_input=="q":
        break
    if user_input not in options:
        print("pick not valid , r,p,s")

        continue


    random_number=random.randint(0,2)
    #r-0 , p-1 , s-2
    computer_pick=options[random_number]
    print(computer_pick)

    if user_input=="r" and computer_pick=='s':
        print("u won !")
        user_wins+=1
        continue
    elif user_input=="p" and computer_pick=='r':
        print("u won !")
        user_wins+=1
        continue
    elif user_input == "s" and computer_pick == 'p':
        print("u won !")
        user_wins += 1
        continue
    elif user_input==computer_pick:
        print("oops same same..")
        continue
    else:
        print("you lost , computer wins")
        computer_wins+=1
        continue
print("Your score : ",user_wins)
print("Computer score : ",computer_wins)
print("good bye :)")
