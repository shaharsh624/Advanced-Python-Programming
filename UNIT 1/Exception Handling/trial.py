'''

# IndentationError: expected an indented block
def fun():
return "Hello"

# ZeroDivisionError: division by zer
test = 1/0

# NameError: name 'test' is not defined
y = test

'''


'''
# Multiple except block
try:
   print(1/0)
except ZeroDivisionError:
   print("You cannot divide a value with zero")
except:
   print("Something else went wrong")
'''


'''
# Custom Exception
class CustomExcept(Exception):
    def __init__(self, string):
        self.string = string
        print("Custom Exception:", string)


x = 1
while x <= 3:
    num = int(input("Enter number: "))
    if num == 2:
        # CustomExcept("Cant divide by 2")
        raise CustomExcept("Cant divide by 2")
    elif num == 0:
        raise ZeroDivisionError()
    else:
        print("Done!")
    x += 1
'''