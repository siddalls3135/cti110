def main():
    
    user_input()
    
def user_input():
    
    expense = {}
    starting_amount = int(input("Please enter the amount in the account: "))
    
    total_expense = 0
    closing_amount = 0
    cont = 'y'
     
    while cont == 'y':
        key = input("Enter the expense name: ")
        value = int(input("Enter the amount: "))
        
        expense[key] = value
        
        print("Do you want to enter another value?")
        print("Enter y for yes")
        cont = input("Enter n for no: ")
        
        total_expense = total_expense + value
        
       
        
        
    closing_amount = starting_amount - total_expense 
    
    
    print("Starting amount: ", starting_amount)
    
    print(f'{"Expense Calculator":^20}')
    print("--------------------------")
    print(f'{"Expense ":<15}{"Amount":<10}')
    print("--------------------------")
    for key, value in expense.items():
        
        print(f'{key:<15}{value:<10}')
    print("--------------------------")
    print("Closing Amount: $", closing_amount)
    
    
    
    
main()