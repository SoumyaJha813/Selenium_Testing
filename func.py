print(' hello, world!! ')
other_print= print
other_print('Just a new name')

num1=5
num2= 10
def do_math(num1, num2=7):  #keyword argument
    result= num1+num2
    result = result + 10
    result = result / 1.5
    result = result - num1
    return result
	
print(do_math(6))
print(do_math(45,87))

import operator

print(operator.add(4,5))
print(operator.not_(True))


def other_function(arg1, arg2='a', arg3=None, arg4=True, arg5='hello'):
    print('arg1+arg2: ', str(arg1)+arg5)
    print('arg1', arg1)
    print('arg2', arg2)
    print('arg3', arg3)
    print('arg4', arg4)
    print('arg5', arg5)
    result = arg2 + arg5
    print('arg2+arg4: ', result)
    result= result and arg4
    print('result: ', result)
    return result
	
print(other_function(10,arg4=False))


