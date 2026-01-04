# Expanse Tracker  Project 

expenses =[] # list of expenses 
print("Welcome To Expense Tracker ! ") 

while True:
    print("===MENU===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice :"))

#Add expense ( choice 1)
    if(choice==1):
        date = input("Enter the Date :")
        category = input("Enter the Category(like Food , Travel Etc) :")
        description = input("Enter Description :")
        amount = float(input("Enter the Expenses :"))

        expense = {
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expenses.append(expense)
        print("Expense Added Successfully! ")

# View all expenses
    elif(choice==2):
        if(len(expenses)==0):
            print("No Expenses Added Yet!")
        else:
            print(" === This is Your Expenses!")
            count = 1
            for eachExpense in expenses:
                print(f' Expense NO. - {count}-> {eachExpense["date"]},{eachExpense["category"]},{eachExpense["description"]},{eachExpense["amount"]}')
                count = count + 1
# Total Expending 
    elif(choice == 3):
        total = 0
        for eachExpense in expenses:
            total = total + eachExpense["amount"]
        
        print("\n Total Expense = ",total)
    
# Exit 
   
    elif(choice ==4):
        print(" Thank You !")
        break

    else:
        print("Invalid Choice Try Again! !")






    


   
    


