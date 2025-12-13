expenses = []
while True:

    print("\n------ EXPENSE TRACKER ------")
    print("1. Add Expense!")
    print("2. View Expenses!")
    print("3. Delete Expenses!")
    print("4. Total Expense Calculation!")
    print("5. Category Wise Report:");
    print("6. Exit!")
    
    choise = int(input("Enter a Choise:"));

    match choise:
        case 1:
            Amount = int(input("How much Money: "));
            Category = input("where money is spent? ");
            Discripition = input("Why exact reason? ");
            expense = [Amount,Category,Discripition];
            expenses.append(expense);

            print("Expense Added sucessfully!")
        case 2:
            if(len(expenses) == 0):
                print("No Expenses to display.");
            else:
                print(f"{'-:All Expenses:-':^50}")
                print("-"*50)
                for i in range(len(expenses)):
                    print(f"1.Amount: {expenses[i][0]}, "
                      f"2.Category: {expenses[i][1]}, "
                      f"3.Description: {expenses[i][2]} ");
                print("-"*50)
        case 3:
            delete_choice = int(input("Enter expense number to delete:"))
            if 1 <= delete_choice <= len(expenses):
                deleted = expenses.pop(delete_choice-1);
                print("Expensess Delete Successfully!",deleted);        
            else:
                print("Invalid expense number!")
        case 4:
            sum = 0;
            for i in range (len(expenses)):
                sum+=expenses[i][0];
            print("Total Expensess Amount:",sum);
            print("Total Expensess:",len(expenses)); 
        case 5:
               search_category = input("Enter a search Category:");
               category_total = 0;
               found = False;
               print(f"\n--- Expenses for Category: {search_category} ---")
               for i in range(len(expenses)):
                    if expenses[i][1].lower() == search_category.lower():
                        print(f"Amount: {expenses[i][0]}, "
                              f"Description: {expenses[i][2]}")
                        category_total += expenses[i][0]
                        found = True

               if found:
                    print("Total for this category:", category_total)
               else:
                    print("No expenses found in this category.")

        case 6:
            print("Exiting Expense Tracker.Thank You!")
            break
        case _:
            print("Invalid Choise!! Try Again.");