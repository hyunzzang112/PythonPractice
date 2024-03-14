import math

def add(a,b):
    print(a+b)

def subtract(a,b):
    print(a-b)

def multiply(a,b):
    print(a*b)

def divide(a,b):
    print(a/b)


print("What do you want?")
D=['+','-','*','/','end']
print(D)

C=input()

if C not in D:
    print("Enter Again")
    C=input()
        

elif C in D:
    if C=='+':
        A=float(input())
        print(C)
        B=float(input())
        add(A,B)
        
    elif C=='-':
        A=float(input())
        print(C)
        B=float(input())
        subtract(A,B)
            
    elif C=='*':
        A=float(input())
        print(C)
        B=float(input())
        multiply(A,B)

    elif C=='/':
        A=float(input())
        print(C)
        B=float(input())
        divide(A,B)

    elif C=='^':
        A=float(input())
        print(C)
        B=float(input())
        print(pow(A,B))

    elif C=='end':
        print("END")
            
            

