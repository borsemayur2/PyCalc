def numberValidator():
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
        else:print('enter valid number.')
