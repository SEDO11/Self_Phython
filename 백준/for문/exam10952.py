run = True

while run:
    string = input().split()
    num1 = int(string[0])
    num2 = int(string[1])
    
    result = num1 + num2
    if(num1 == 0 and num2 == 0):
        run = False
    else:
        print(result)