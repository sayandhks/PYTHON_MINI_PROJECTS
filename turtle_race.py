import turtle
import time
import random

WIDTH,HEIGHT=500,500
COLORS=['red','green','blue','orange','yellow','black','purple','pink','brown','cyan']





def get_number_of_racers():
    racers=0
    while True:
        racers=input(" Enter number of racers between (2-10) : ")
        if racers.isdigit():
            racers=int(racers)
        else:
            print("input not numeric...try again")
            continue
        if (2<=racers<=10):
            return racers
        else:
            print("input not in range of(2-10)...try again")
            continue

def init_turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing !")




def create_turtle(colors):
    turtles=[]
    spacingx=WIDTH//(len(colors)+1)
    for i,color in enumerate(colors):
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(((-WIDTH//2)+((i+1)*spacingx)),((-HEIGHT//2)+20))
        racer.pendown()
        turtles.append(racer)
    return turtles



def race(colors):
    turtles = create_turtle(colors)

    while True:
        for racer in turtles:
            distance=random.randrange(1,10)
            racer.forward(distance)
            x,y=racer.pos()
            if y>=((HEIGHT//2)-10):
                    return colors[turtles.index(racer)]





def place_bet(deposit):
    while True:
        print(*colors)
        bet_color=input("place your  bet on any of the above turtles : ")
        if bet_color not in colors:
            print("enter a valid color")
            continue

        else:
            while True:
                bet_amount = input("Enter amount of bet (1-100) : ")
                if bet_amount.isdigit():
                    if int(bet_amount)<=deposit:
                        pass


                        if (0<int(bet_amount)<=100):
                            return bet_color,int(bet_amount)
                        else:
                            print("place a bet between 1-100 ")
                            continue
                    else:
                        print(" oops insufficient balance ")
                        deposit()
                        continue
                else:
                    print("enter a digit")
                    continue

def announce_result(deposit):

    balance=deposit
    if winner == bet_color:
        balance+=(bet_amount*2)
        print("The winner is the turtle with color  : ", winner)
        print("you won the bet you got : ", (bet_amount * 2))
        print("your account balance is :",balance)

    else:
        balance-=bet_amount
        print("The winner is the turtle with color  : ", winner)
        print("you lost :", bet_amount)
        print("your account balance is :", balance)
    return balance

def deposit():
    while True:
        deposit = input("how much did you like to deposit (1-1000) : ")
        if deposit.isdigit():
            if (0 < int(deposit) <= 1000):
                return int(deposit)
            else:
                print("please deposit an amount between 1-1000 ")
                continue
        else:
            print("enter a digit")
            continue

def play_again(balance):
        while True:
            que = input("do you want to play again or quit (p/q) : ")
            if que.lower() == "p":

                if balance == 0:
                    print("you can't play anymore your balance is 0 ")
                    quit()
                else:
                    break
            elif que.lower() == "q":
                print("you can go with : ", balance)
                quit()
            else:
                print("invalid input try again ")
                continue


deposit=deposit()

print("-------select the number of turtles to decide difficulty-------")
racers = get_number_of_racers()
random.shuffle(COLORS)
colors = COLORS[:racers]
while True:
    init_turtle()
    bet_color, bet_amount = place_bet(deposit)
    winner = race(colors)
    balance = announce_result(deposit)
    deposit = balance
    play_again(balance)







