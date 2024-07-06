user_name=input("Type your name : ")
print("Hey",user_name,"welcome to this adventure YOU ARE LOST FIND Way to HOME")
answer=input("you are on end of a dirt road which way dop you want to go (left/right) : ").lower()
if answer=="left":
    answer=input("hey seems like you have reached on a green river bank do you like to swim across or walk around (swim/walk) : ").lower()
    if answer=="swim":
        print(user_name+" you swam across the river and got eaten by crocodile YOU LOSE")
    elif answer=="walk":
        print(user_name+" you walked and walked around the river you got exhausted and died YOU LOSE")
    else:
        print("invalid input no concentration at a crucial time like this YOU LOSE")
elif answer=="right":
    answer = input("hey seems like you have reached a wobbly bridge do you like to cross the bridge or turn back (cross/turn) : ").lower()
    if answer == "cross":
        answer=input(" you crossed the bridge and found a stranger you can eithger talk to him or you can ignore him(talk/ignore) : ").lower()
        if answer=="talk":
            print("you talked to stranger he teleported you to your house using super power ..... you are safe .....YOU WON !")

        elif answer=="ignore":
            print("you ignored him so that you was unable to reach home you are lost YOU LOSE ")
        else:
            print("invalid input no concentration at a crucial time like this YOU LOSE")
    elif answer == "turn":
        print(user_name + " you turned back like a coward  YOU LOSE")
    else:
        print("invalid input no concentration at a crucial time like this YOU LOSE")
