from numberValidator import numberValidator
def factorial(num):
    if num==1:print(1)
    else:
        temp=num
        a=1
        while num>=1:
            a*=num
            num-=1
        try:print("Factorial of %g is %g"%(temp,a))
        except:print("Factorial of %g is %g"%(temp,float(a)))
if __name__=="__main__":
    while True:
        '''line=input('Enter a Number for Factorial Calculation: ')
        #try:
            num=int(line)
        except ValueError:
            try:num=float(line)
            except ValueError:
                print('integers only')
                continue'''
        factorial(numberValidator())
        q=input('Try Again?y/n ')
        if q=='n':break
    dash='-'*27
    print(dash,'THANK YOU',dash)
    input()
