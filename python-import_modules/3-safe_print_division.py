def safe_print_division(a, b):

    try:
        result = a /b 
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed", end="\n")
        return None
    finally:
        print("inside result: {}".format(result), end="\n")
    return result


