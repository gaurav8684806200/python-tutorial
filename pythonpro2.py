expenses = []
def add_expenses():
    description  = input("enter expenses description:")
    try:
        amount = float(input("enter expenses amount :"))
        expenses.append({"description": description, "amount": amount})
        print(f"expenses '{description}' of amount ${amount}added.")
    except ValueError:
        print("Invalid amount ! plese enter a number.")


def view_expenses():
    if not expenses:
        print("No expenses record yet .") 
    else:
        print("\nYour expenses :")
        print(f"{expenses['description']}:${expenses['amount']}")

def calculate_total():
    total = sum(expenses['amount']for expenses in expenses)
    print(f"\nTotal Expensis: ${total}")

def main():
    while True:
        print("\nExpenses Tracker Menu:")   
        print("1. Add Expenses")   
        print("2. view Expenses")
        print("3. Calculate Total")
        print("4.Exit")

        choice = input("Choose an option (1-4):") 


        if choice == "1":
            add_expenses()
        elif choice == "2":
            view_expenses()
        elif choice =="3":
            calculate_total
        elif choice == "4":
            print("thank you for using the Expenses tracker!")
            break
        else:
            print("invalid choice! please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
            
