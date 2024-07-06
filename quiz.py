print("Welcome to my computer quiz")

playing=input(" Do you want to play? : ")


if (playing.lower() != 'yes') :
    quit()
print(" Okey lets play :) ")
score=0

answer=input("What does CPU stand for? : ")
if answer.lower()=="central processing unit" :
    print("correct !")
    score+=1
else:
    print("incorrect !")

answer=input("What does GPU stand for? : ")
if answer.lower()=="graphics processing unit" :
    print("correct !")
    score+=1
else:
    print("incorrect !")

answer=input("What does PSU stand for? : ")
if answer.lower()=="power supply unit" :
    print("correct !")
    score+=1
else:
    print("incorrect !")

print("you answered "+str(score)+" questions correct")
print("you got "+str((score/3)*100)+"% correct")




