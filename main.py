# slot machine
import random
import time
def spin_row():
    symbols = ['🍒',' 🍉', '🍋', '🔔' ,'⭐']
    
    return [random.choice(symbols)for _ in range(3)]
        

def print_row(row):
    print("*" * 15)
    print(" | ".join(row))
    print("*" * 15)

def get_payout(row,bet):
    if row[0] == row [1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0

def main():
    balance = 100
    print("$$$$$$$$$$$$$$$$$$$$$$$$")
    print("Welcome to python slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("$$$$$$$$$$$$$$$$$$$$$$$$")
    
    
    while balance > 0:
        print(f"Current balance: ${balance}")
        
        
        bet = input("Place your bet amount ")
        
        if not bet.isdigit():
            print("Plaese enter a valid number")
            continue
        bet = int(bet)
        if bet > balance:
            print("INsufficient funds")
            continue
        
        if bet <= 0:
            print("bet must be greater than 0")
            continue
        
        balance -= bet
        
        row = spin_row()
        print ("spinning...")
        time.sleep(2)
        print_row(row)
        
        payout = get_payout(row,bet)
        
        if payout > 0:
            print(f"you won ${payout}")
        else:
            print("Sorry you lost this round")
            
        balance += payout
        
        play_again = input("Do yuo want to spin again?(y/n): ").upper()
        
        if play_again != "Y":
            break
    print("*" * 100)    
    print(f"Game over! Your final balance is: ${balance}")
    print("*" * 100)


if __name__ == "__main__":
    main()
    
    
    