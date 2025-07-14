import time
balance = 10000
def show_menu():
    print("1.Check Balance")
    print("2.Deposit Balance")
    print("3.Withdraw Balance")
    print("4.Exit")
    print("5.Last Transaction")

def check():
    global balance
    print(f"Balance = {balance}")

def Last():
    with open('atm2.txt', 'r') as f:
        contents = f.read()
        print(contents)

def deposit():
    amount = int(input("Enter The Amount:"))
    global balance
    if amount > 0:
        amount2 = balance
        amount2+=amount
        print(f"Balance Deposited New Balance = {amount2}")
        with open('atm2.txt','a') as f:
            records = f"deposited {amount}"
            new_balance = f"New Balance = {amount2}"
            today = time.strftime("%d-%m-%y at %H-%M-%S")
            records_all = f"Money {records} {new_balance} on {today}"
            f.write(f"{records_all}+\n")

    else:
        print("Enter Amount Greater Than Zero")
def withdraw():
    amount = int(input("Enter The Amount:"))
    global balance
    amount2 = balance
    if amount > balance:
        print("Insufficient Funds")
    else:
        amount2-=amount
        print(f"Balance Withdraw Successful New Balance = {amount2}")
        with open('atm2.txt','a') as f:
            records = f"Withdraw {amount}"
            new_balance = f"New Balance = {amount2}"
            today = time.strftime("%d-%m-%y At %H-%M-%S")
            records_all = f"Money {records} {new_balance} on {today}"
            f.write(f"{records_all}+\n")

def main():
    while True:
        show_menu()
        choice = int(input("Enter The Choice:"))
        match choice:
            case 1:
               check()
               break
            case 2:
                deposit()
                break
            case 3:
                withdraw()
                break
            case 4:
                print("Thanks For Visiting Python Atm")
                break
            case 5:
                Last()
                break
            case _:
                print("Enter The Valid Choice")
                break
if __name__ == "__main__":
    main()