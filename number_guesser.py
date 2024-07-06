import random
top_of_range=input("Type a number for top range : ")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("please enter a number greater than zero next time :) ")
        quit()
else:
    print("please type a number next time :) ")
    quit()

random_number=random.randint(0,top_of_range)
guesses=0

while True:
    guesses+=1
    user_guess=input("Make a guess : ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
        if user_guess<0:
            print("enter a number greater than zero next time :)")
            quit()
    else:
        print("please enter a number next time")
        continue
    if random_number==user_guess:
        print("right guess")
        break
    elif(user_guess>random_number):
        print("you were above the number")
        continue
    else:
        print("you were below the number")
        continue
print("you got it right in",guesses,"guesses")