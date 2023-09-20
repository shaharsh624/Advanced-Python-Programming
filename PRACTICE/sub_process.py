import sys
my_input = sys.argv

def sum_values(a=int(my_input[1]), b=int(my_input[2])):
    return a+b

if __name__ == "__main__":
    print(sum_values())