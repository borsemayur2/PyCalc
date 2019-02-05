from numberValidator import numberValidator
from factorial import factorial
from primer import primer
'''def isValidNumber():
    while True:
        line=(input('Enter Number: '))
        while line:
            if line:
                    try:num=int(line)
                    except:
                        try:num=float(line)
                        except:
                            print('invalid number.try again.')
                            break
                    return num
        else:print('enter valid number.')'''

'''def primer(y):
        x = y // 2 # For some y > 1
        while x > 1:
            if y % x == 0: # Remainder
                print(y, 'has factor', x)
                break # Skip else
            x -= 1
        else: # Normal exit
            print(y, 'is prime')'''
if __name__=="__main__":

    d={1:lambda a,b:print('\t\tADDITION:',a+b),2:lambda a,b:print('\t\tSUBTRACTION:',a-b),3:lambda a,b:print('\t\tMULTIPLICATION:',a*b),\
       4:lambda a,b:print('\t\tDIVISION:',a/b),5:lambda a,b:print('\t\tFLOOR DIVISION:',a//b),\
       6:lambda a,b:print('\t\tMODULUS:',a%b),}

    while True:
        print("!-!-!WELCOME TO PyCalc!-!-!\n")
        a=numberValidator()
        b=numberValidator()
        while True:
            try:
                c=int(input("\n1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n\
5.FLOOR DIVISION\n6.MODULUS\n7.PRIMER\n8.FACTORIAL\n9.RESTART PYCALC\n0.EXIT\n\t\tENTER YOUR CHOICE: "))
                if c==0 or c==9:break
                if c==7 or c==8:
                    for num in [a,b]:
                        if c==7:primer(num)
                        else:factorial(num)
                    continue
                ans=d[c](a,b)
            except:
                print('invalid choice.try again.')
                continue
        if c==0:break
    input('Thank You for using "PyCalc!" ')
