import random


def spin_row():
    symbols=['🍒','🍋','🟩','🍋','🏵️','️❤️‍🩹']
    results=[]
    for symbol in range(3):
        results.append(random.choice(symbols))#return[random.choice(symbols) for _in range(3)]
    return results

def print_row(row):
    print("*******************")
    print(" | ".join(row))
    print("*******************")
def get_payout(row,bet):
      if row[0]==row[1]==row[2]:
        if row[0]=='🍒':
            return bet*3       
        elif row[0]=='🍋':
            return bet*4
        elif row[0]=='🟩':
            return bet*5
        elif row[0]=='🍋':
            return bet*10
        elif row[0]=='❤️‍🩹':
            return bet*20
      return 0





def main():
    balance=100

    print("******************")
    print("welcome to python slots machine")
    print("Symbols:🍒🍋‍🟩🍋🏵️❤️‍🩹")

    print("*********************")

    while balance>0:
        print(f"current balance: ${balance}")

        bet=input("place your bet amount:")

        if not bet.isdigit():
            print("plese enter a valid number")
            continue

        bet=int(bet)

        if bet>balance:
            print("Insufficient funds")
            continue

        if bet<=0:
            print("Bet must be greater than 0")
            continue

        balance-=bet

        row=spin_row()
        print("spinnning..\n")
        print_row(row)

        payout=get_payout(row,bet)

        if payout>0:
            print(f"you won ${payout}")
        else:
            print("sorry you lost this round")

        balance+=payout

        play_again=input("Do you want to spin again(Y/N):").upper()
        if play_again != 'Y':
            break
        print("****************************************")
        print(f"game over!your final balance is ${balance}")
        print("*****************************************")
if __name__=='__main__':
    main()