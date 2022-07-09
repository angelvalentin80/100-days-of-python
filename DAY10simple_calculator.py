import os
operations = ["+", "-", "/", "*"]
answer_history = []
def perform_calculation(a = float, b = float, operation = str) -> float:
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "/":
        return a / b
    elif operation == "*":
        return a * b

def print_operations():
    for i in operations:
        print(i)


calculating = True

while calculating:
    
    try:
        first_number = float(input("What's the first number?: "))
        print_operations()
        operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
    except ValueError:
        print("You did not enter a number, please try again.")
        continue
        
    if operation != "+" and operation != "-" and operation != "*" and operation != "/":
        print("You did not enter a valid operation, please try again.")
        continue

    answer = perform_calculation(first_number, second_number, operation)            
    answer_history.append(answer)
    print(f"{first_number} {operation} {second_number} = {answer}")
    
    making_decision = True

    while making_decision:
    
        decision = input(f"Type 'y' to continue calculating with {answer_history[-1]}, type 'n' to start a new calculation, or type 'q' to quit the application: ")
    
        if decision.lower() == 'y':
            try:
                operation = input("Pick an operation: ")
                next_number = float(input("What's the next number?: "))
            except ValueError:
                print("You did not enter a number, please try again.")
                continue
            
            if operation != "+" and operation != "-" and operation != "*" and operation != "/":
                print("You did not enter a valid operation, please try again.")
                continue
            
            updated_answer = perform_calculation(answer_history[-1], next_number, operation)
            print(f"{answer_history[-1]} {operation} {next_number} = {updated_answer}")
            answer_history.append(updated_answer)
            continue
        elif decision.lower() == 'n':
            os.system("clear")
            answer_history = []
            making_decision = False
        elif decision.lower() == 'q':
            making_decision = False
            calculating = False 
        else:
            print("I don't know that command :0")
