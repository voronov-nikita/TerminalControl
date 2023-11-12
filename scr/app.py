import argparse

def calculator(operation, operands):
    if operation == 'ssh':
        print("SSH")
        return 
    elif operation == 'subtract':
        result = operands[0]
        for operand in operands[1:]:
            result -= operand
        return result
    elif operation == 'multiply':
        result = 1
        for operand in operands:
            result *= operand
        return result
    elif operation == 'divide':
        result = operands[0]
        for operand in operands[1:]:
            if operand != 0:
                result /= operand
            else:
                raise ValueError("Division by zero is not allowed.")
        return result
    else:
        raise ValueError("Unsupported operation")

def main():
    parser = argparse.ArgumentParser(description='Simple Calculator')

    # Добавление позиционного аргумента для операции
    parser.add_argument('operation', choices=['ssh', 'subtract', 'multiply', 'divide'], help='Operation to perform')

    # Добавление аргумента для операндов (может быть несколько)
    parser.add_argument('operands', type=float, nargs='+', help='Operands for the operation')

    # Разбор аргументов
    args = parser.parse_args()

    # Вызов калькулятора с переданными аргументами
    try:
        result = calculator(args.operation, args.operands)
        if result is not None:
            print(f"Result of {args.operation}:", result)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
