number1: int = 2
number2: int = 4
number3: int = 5
number4: int = 3
numberSup: int = 0

if numberSup < number1:
    number1 = numberSup
    if numberSup < number2:
        numberSup = number2
        if numberSup < number3:
            numberSup = number3
            if numberSup < number4:
                numberSup = number4

print(numberSup)
