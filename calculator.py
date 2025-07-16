import re

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def parse_input(user_input):
    # Match numbers and operator with or without spaces using regex
    pattern = r'^(-?\d+(?:\.\d+)?)([+\-*/])(-?\d+(?:\.\d+)?)$'
    match = re.match(pattern, user_input.replace(" ", ""))
    if not match:
        return None, None, None
    num1, operator, num2 = match.groups()
    return float(num1), operator, float(num2)

def main():
    print("Simple  Calculator")
    print("Enter input")
    

    while True:
        user_input = input("Enter calculation: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        num1, operator, num2 = parse_input(user_input)

        if operator is None:
            print("Error: Invalid input format. Use format like 5+6 or 5 + 6")
            continue

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("Error: Unsupported operator.")
            continue
        
        print(f"Result: {result}")
        print("Type 'exit' to quit.\n")
if __name__ == "__main__":
    
    main()

