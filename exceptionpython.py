ItemInCart = 0
# 2 items added to cart
#if ItemInCart != 2:
#    raise Exception("Products cart count not matching")

#if ItemInCart != 2:
#    pass
#assert(ItemInCart == 2)

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except:
    print("somehow i reached this except block cause of failure")

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("Cleaning up resources")