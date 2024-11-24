def print_sum(num1, num2):
    if type(num1) != int or type(num2) != int:
        raise Exception("Inputs to print_sum function must be ints")
    print(num1 + num2)


print_sum(5, 6)
try:
    print_sum(1, 'hitori')
except Exception as e: #used the exception raised by print_sum function to annotate with our own text(Something went wrong!)
    print(f'Someting went wrong: {e}')

print_sum(8, 4)
print(" we will never get here")

'''
def print_sum2(num1, num2):
    try:
        print(num1+num2)
    except Exception:
        print("Couldn't add those numbers")

print_sum2(1, 'taki')
print_sum2(4,2)
'''