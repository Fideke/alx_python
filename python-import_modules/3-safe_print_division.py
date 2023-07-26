def safe_print_division(a, b):
    try:
        result = a /b 
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
        return None
    finally:
        print("inside result: {}".format(result))
        return result


