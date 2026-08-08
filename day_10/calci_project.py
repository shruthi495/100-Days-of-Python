def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        return "division by 0 is not possible"
    return a/b

def calculator():
    print("Welcome to the calculator")
    a=float(input("What's the first number? "))
    while(True):
        print("+\n-\n*\n/")
        op=input("Pick an operation: ")
        b=float(input("What is the next number? "))
        if op=='+':
            res=add(a,b)
        elif op=='-':
            res=sub(a,b)
        elif op=='*':
            res=mul(a,b)
        elif op=='/':
            res= div(a,b)
        else:
            print("Pick a valid operation")

        print(f"{a} {op} {b} = {res}")

        toContinue=input("Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation ")
        if toContinue=='y':
            a=res
        elif toContinue=='n':
            calculator()
            break
        else:
            print("GoodBYE!!!")


calculator()



