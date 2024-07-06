import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

rows=3
cols=3

symbols_count={ "A":2,"B":4,"C":6,"D":8}
symbol_value={"A":5,"B":4,"C":3,"D":2}

def spin(balance):
    while True:
        lines = get_number_of_lines()
        bet=get_bet()
        total_bet=bet*lines
        if total_bet>balance:
            print(f"you dont have enough to bet.....your current balance is {balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to  >>   ${total_bet}")
    slots = get_slot_machine_spin(rows, cols, symbols_count)
    print(print_slot_machine(slots))
    winnings,winning_lines=check_winnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings}. ")
    print(f"You won on lines ",*winning_lines)
    return winnings-total_bet


def check_winnings(columns,lines,bet,symbol_value):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings+=symbol_value[symbol]*bet
            winning_lines.append(line+1)
    return winnings,winning_lines



def get_slot_machine_spin(rows,cols,symbols_count):
    all_symbols=[]
    for symbol,symbol_count in symbols_count.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns=[]
    for col in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for row in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row])



def deposit():
    while True:
        amount=input("what would you like to deposit in dollar ?  $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("amount must be greater than zero")
        else:
            print("please enter a number ")
    return amount

def get_number_of_lines():
    while True:
        lines=input("enter number of lines to bet on (1-"+str(MAX_LINES)+") ?")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("lines must be between 1 and "+str(MAX_LINES))
        else:
            print(" iNVALID input! ...please enter a number ")
    return lines


def get_bet():
    while True:
        bet = input("what would you like to bet ("+str(MIN_BET)+"-"+str(MAX_BET)+") ....?  $")

        if bet.isdigit():
            bet = int(bet)
            if MIN_BET<=bet<=MAX_BET:
                break
            else:
                print("bet must be between "+str(MIN_BET)+"-"+str(MAX_BET))
        else:
            print("INVALID input! , please enter a number ")
    return bet

def main():
    balance=deposit()
    while True:
        print(f"Current balance is $ {balance}")
        answer=input("press enter to play and q to quit")
        if answer=="q":
            break
        balance+=spin(balance)
    print(f"you left with ${balance}")



main()


