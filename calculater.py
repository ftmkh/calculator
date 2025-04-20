firstNum = int(input('enter first number :'))
firstOperation = input('enter first operation (+,-,*,/) :')
secondNum = int(input('enter second number :'))
secondOperation = input('enter second operation (+,-,*,/):')
thirdNum =  int(input('enter third number :'))



def operation(a, c, b):
    match (c):
        case '*':
            result = a * b
        case '/':
            result = a / b
        case '+':
            result = a + b
        case '-':
            result = a - b
    return result


match(firstOperation):
    case '*' | '/' :
        result1 = operation(firstNum , firstOperation , secondNum)
        result2 = operation(result1 , secondOperation , thirdNum)
    case '+' | '-' :
        match(secondOperation):
            case '*' | '-':
                result1 = operation(secondNum,secondOperation,thirdNum)
                result2 = operation(firstNum,firstOperation,result1)
            case '+' | '-' :
                result1 = operation(firstNum, firstOperation, secondNum)
                result2 = operation(result1, secondOperation, thirdNum)

print(result2)






