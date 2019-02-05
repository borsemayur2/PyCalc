from numberValidator import numberValidator
def primer(y):
        x = y // 2 # For some y > 1
        while x > 1:
            if y % x == 0: # Remainder
                print(y, 'has factor', x)
                break # Skip else
            x -= 1
        else: # Normal exit
            print(y, 'is prime')
    
        
if __name__=="__main__":
        while True:
            
                primer(numberValidator())
                c=input('\ntry again? y/n : ')
                if c=='n':break

