import random
import time

OPERATORS=["+","-","*"]
MIN_OPERAND=3
MAX_OPERAND=6
TOTAL_PROBLEMS=5

def generate_problem():
    left=random.randint(MIN_OPERAND,MAX_OPERAND)
    right=random.randint(MIN_OPERAND,MAX_OPERAND)
    operator=random.choice(OPERATORS)
    expr=str(left)+" "+operator+" "+str(right)
    answer=eval(expr)

    return expr,answer
wrong=0
input("press enter to start !")
print("------------------------------------")
start_time=time.time()
for i in range(TOTAL_PROBLEMS):
    expr,answer=generate_problem()
    while True:
        guess=input("Problem no"+" "+str(i+1)+">>     "+expr+" = ")
        if guess==str(answer):
            break
        wrong+=1
end_time=time.time()
total_time=(end_time-start_time)
total_time=round(total_time,2)

print("------------------------------------")
print("good job! you finished in ",str(total_time),"seconds")
print("no of wrong attempts : ",wrong)

