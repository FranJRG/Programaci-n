'''
number=(int(input("Introduce un número: ")))
def computeFactorial(number):
  if number<0:
    return None
  elif number==0:
    return 1
  else:
    fact=1
    while (number > 1):
      fact*=number
      number-=1
    return fact
print(computeFactorial(number))

print("------------------")

year= int(input("Choose a year: "))
def is_leap_year(year):
    res = False
    if year%4==0 and (year%100!=0 or year%400==0):
        res=True
    
    return res
print("Esta todo bien")

print("------------------")

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

def computeDaysInMonth(year, month):
    liste_days = [31,30,28,29]
    for i in range (len(liste_days)):
        if (month==11 or month==4 or month==7 or month==9) and (year>=400):
            return liste_days[1]
        elif (month==1 or month==3 or month==5 or month==6 or month==8 or month==10 or month==12) and (year>=400):
            return liste_days[0]
        elif (month==2) and (year == is_leap_year(year) or year>=400):
            return liste_days[3]
        elif (month==2) and (year != is_leap_year(year) or year>=400):
            return liste_days[2]
print(computeDaysInMonth(year, month))

print("--------------------")

def getDayOfWeek(d, m, y):
    mensaje=""
    a=(14-m)//12
    y=y-a
    m=m+12*a-2
    d=(d + y + y//4 - y//100 + y//400 + (31*m)//12) %7
    if d==0:
        mensaje+="Sunday"
    elif d==1:
        mensaje+="Monday"
    elif d==2:
        mensaje+="Thursday"
    elif d==3:
        mensaje+="Wednesday"
    elif d==4:
        mensaje+="Tuesday"
    elif d==5:
        mensaje+="Friday"
    elif d==6:
        mensaje+="Saturday"
    return mensaje
print(getDayOfWeek(7, 7, 2007))

print("------------------")

#-b+-raiz(b2 -4*a*c)/2*a
def solveSecondOrderEquation(number1, number2, number):
  raiz_aux = (-number**2)+(-4*number1*number)
  raiz = raiz_aux**(1/2)
  sol1 = (-number2+raiz)/(2*number1)
  sol2 = (-number2-raiz)/(2*number1)
  return (sol1, sol2)
print(solveSecondOrderEquation(2, -7, 3))

print("--------------------")

number1 =int(input("Dime el primer numero: "))
number2 = int(input("Dime el segundo numero: "))

def powerIt(number1, number2):
    if number1>0 and number2>0:
        return(number1**number2)
    elif number1>=0 and number2==0:
        return(number1**0)
print(powerIt(number1, number2))

print("----------------------")

num=int(input("Give me one number: "))

def isPrime(num):
    while num>0:
        if num%2 !=0:
            return True
        elif num<=0:
            return None
        elif num==2:
            return True
        else:
            return False
print(isPrime(num))

print("------------------------")

num = int(input("Give me one number: "))
list=[]
def getPrimeDivisors(num, list):
    list_prime = [2,3,5,7,11,13,17,19,23,29,32,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    for i in range (len(list_prime)):
        if num % list_prime[i] == 0:
            if isPrime (list_prime[i]):
                list.append(list_prime[i])
            elif num<0:
                list = None
    return list
print(getPrimeDivisors(num, list))

print("-----------------------")

num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))

def isFriendNumber (num1, num2):
    sum1=0
    sum2=0
    for i in range(1,num1):
        if num1%i==0:
            sum1+=i
    for i in range(1, num2):
        if num1%i==0:
            sum2+=i
    if sum1==num2 or sum2==num1:
        return True
    else:
        return False
print(isFriendNumber (num1, num2))

print("-----------------------")
'''
def conditions(values):
    values=str(values)
  
    values_s="1234567890.-ABCDEF"
    comprobacion=True
  
    for i in range(len(values)):
        cont_1=0
        cont_2=0
        if values[i]==".":
            cont_1+=1
        elif values[i]=="-":
            cont_2+=1
  
    if cont_1>1 and "."==values[0] and "."==values[-1]:
        comprobacion=False
    elif cont_2>1 and "-"!=values[0]:
        comprobacion=False
    elif "-"==values[0] and "."==values[1]:
        comprobacion=False
    for i in range(len(values)):
        if values[i] not in values_s:
            comprobacion=False
      
    return comprobacion  



def getNumberOfDigitsDecimal(num):
    if conditions(num)==True:
        string=str(num)
        string_n="1234567890-."
        cont=0
        validacion=True
        for i in range(len(string)):
            if string[i] in string_n:
                cont+=1
                validacion=cont
        for i in range(len(string)):
            if num[i] not in string_n:
                validacion=None
        return validacion

def getNumberHexadecimal(num):
    if conditions(num)==True:
        string=str(num)
        string_n="1234567890-.ABCDEF"
        cont=0
        for i in range(len(string)):
            if string[i] in string_n:
                cont+=1
                validacion=cont
        for i in range(len(string)):
            if num[i] not in string_n:
                validacion=None
        return validacion


def getNumberOctaldecimal(num):
    if conditions(num)==True:
        string=str(num)
        string_n="01234567-."
        cont=0
        validacion=True
        for i in range(len(string)):
            if string[i] in string_n:
                cont+=1
                validacion=cont
        for i in range(len(string)):
            if num[i] not in string_n:
                validacion=None
        return validacion

def getNumberOfDigitsBinario(num):
    if conditions(num)==True:
        string=str(num)
        string_n="01-."
        cont=0
        validacion=True
        for i in range(len(string)):
            if string[i] in string_n:
                cont+=1
                validacion=cont
        for i in range(len(string)):
            if num[i] not in string_n:
                validacion=None
        return validacion
    
print(getNumberOfDigitsDecimal("5401"))
print(getNumberHexadecimal("89234C"))
print(getNumberOctaldecimal("-25487"))
print(getNumberOfDigitsBinario("11010"))

