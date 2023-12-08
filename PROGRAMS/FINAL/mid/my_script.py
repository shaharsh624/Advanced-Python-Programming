import sys
import subprocess
my_input = sys.argv
def sqr(a = int(my_input[1])):
    return a * a
if __name__=="__main__":
    print(sqr())