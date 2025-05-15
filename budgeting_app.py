def get_income(): 
    while True:
        income = input("Enter your monthly income: ").replace(',', '')
        try:
            return float(income)
        except:
            print("Invalid input. Please enter a number.")

def get_expenses():
    expenses = {}
    while True:
        category = input("Enter expense category (or type 'done' to finish): ")
        if category.lower() == 'done':
            break
        amount = input("Enter amount for {category}: ").replace(',', '')
        try:
            amount = float(amount)
            if category in expenses:
                expenses[category] += amount
            else:
                expenses[category] = amount
        except:
            print("Invalid amount. Please try again.")
    return expenses

def calculate(income, expenses):
    total = sum(expenses.values())
    savings = income - total
    return total, savings

def show_summary(income, expenses, total, savings):
    print()
    print("Budget Summary")
    print("--------------")
    print("Income:", income)
    print("Expenses:")
    for item in expenses:
        print(item + ":", expenses[item])
    print("Total Expenses:", total)
    print("Savings:", savings)
    if savings < 0:
        print("Warning: You are over budget.")

def draw_chart(expenses):
    try:
        import matplotlib.pyplot as plt
        labels = list(expenses.keys())
        values = list(expenses.values())

        plt.pie(values, labels=labels)
        plt.title("Expenses")
        plt.show()
    except:
        print("Chart could not be displayed.")

income = get_income()
expenses = get_expenses()
total, savings = calculate(income, expenses)
show_summary(income, expenses, total, savings)
draw_chart(expenses)