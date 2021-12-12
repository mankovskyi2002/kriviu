import pandas as pd
from colorama import init, Fore, Back, Style

pd.options.display.max_columns = 9
pd.set_option('display.width', 1400)
init(autoreset=True) 

with open('pivo.txt') as fileobject:
    pivos = []
    pivos = fileobject.readlines()
    pivos = [line.rstrip('\n') for line in pivos]

print("\n")
print(Style.BRIGHT + Fore.BLUE + "Пиво:",*pivos,sep="\n")
print("\n")

with open('parameters.txt') as fileparameters:
    parameters = []
    parameters = fileparameters.readlines()
    parameters = [line.rstrip('\n') for line in parameters]

print(Style.BRIGHT + Fore.BLUE + "Параметри:",*parameters,sep="\n")
print("\n")

with open('importance.txt') as fileimportance:
    importance = []
    importance = fileimportance.readlines()
    importance = [line.rstrip('\n') for line in importance]

file1 = open ('1.txt' , 'r')
exp1 = []
exp1 = [ line.split() for line in file1]

file2 = open ('2.txt' , 'r')
exp2 = []
exp2 = [ line.split() for line in file2]

file3 = open ('3.txt' , 'r')
exp3 = []
exp3 = [ line.split() for line in file3]

file4 = open ('4.txt' , 'r')
exp4 = []
exp4 = [ line.split() for line in file4]

def Price (pivo):
    price = float(importance[0]) * (float(exp1[pivo][0])+float(exp2[pivo][0])+float(exp3[pivo][0])+float(exp4[pivo][0]))
    return price

def Scent (pivo):
    scent = float(importance[1]) * (float(exp1[pivo][1])+float(exp2[pivo][1])+float(exp3[pivo][1])+float(exp4[pivo][1]))
    return scent

def Taste (pivo):
    taste = float(importance[2]) * (float(exp1[pivo][2])+float(exp2[pivo][2])+float(exp3[pivo][2])+float(exp4[pivo][2]))
    return taste

def Sort (pivo):
    sort = float(importance[3]) * (float(exp1[pivo][3])+float(exp2[pivo][3])+float(exp3[pivo][3])+float(exp4[pivo][3]))
    return sort

def Flavor (pivo):
    flavor = float(importance[4]) * (float(exp1[pivo][4])+float(exp2[pivo][4])+float(exp3[pivo][4])+float(exp4[pivo][4]))
    return flavor

def Value (pivo):
    value = float(importance[5]) * (float(exp1[pivo][5])+float(exp2[pivo][5])+float(exp3[pivo][5])+float(exp4[pivo][5]))
    return value

def Light (pivo):
    light = float(importance[6]) * (float(exp1[pivo][6])+float(exp2[pivo][6])+float(exp3[pivo][6])+float(exp4[pivo][6]))
    return light

#Croissant
price1 = Price(0)
scent1 = Scent(0)
taste1 = Taste(0)
sort1 = Sort(0)
flavor1 = Flavor(0)

#Kalachi
price2 = Price(1)
scent2 = Scent(1)
taste2 = Taste(1)
sort2 = Sort(1)
flavor2 = Flavor(1)

#Brioche
price3 = Price(2)
scent3 = Scent(2)
taste3 = Taste(2)
sort3 = Sort(2)
flavor3 = Flavor(2)

#Pampushki
price4 = Price(3)
scent4 = Scent(3)
taste4 = Taste(3)
sort4 = Sort(3)
flavor4 = Flavor(3)

#Waffles
price5 = Price(4)
scent5 = Scent(4)
taste5 = Taste(4)
sort5 = Sort(4)
flavor5 = Flavor(4)

#Sum

sum1 = price1 + taste1 + scent1 + flavor1 + sort1
sum2 = price2 + taste2 + scent2 + flavor2 + sort2
sum3 = price3 + taste3 + scent3 + flavor3 + sort3
sum4 = price4 + taste4 + scent4 + flavor4 + sort4
sum5 = price5 + taste5 + scent5 + flavor5 + sort5

parameters.append('')
importance.append('')

df = pd.DataFrame({'№': ['1', '2', '3', '4', '5', 'Сума'],
                   'Параметри': parameters,
                   'Вага': importance,
                   pivos[0]: [price1, scent1, taste1, sort1, flavor1, sum1],
                   pivos[1]: [price2, scent2, taste2, sort2, flavor2, sum2],
                   pivos[2]: [price3, scent3, taste3, sort3, flavor3, sum3],
                   pivos[3]: [price4, scent4, taste4, sort4, flavor4, sum4],
                   pivos[4]: [price5, scent5, taste5, sort5, flavor5, sum5]})

print(Style.BRIGHT + Fore.GREEN + "Результат:")
print(df)
print('\n')

winer = ''
points = ''

if sum1 > sum5 and sum1 > sum3 and sum1 > sum2 and sum1 > sum4:
    winer = pivos[0]
    points = sum1
elif sum2 > sum5 and sum2 > sum3 and sum2 > sum1 and sum2 > sum4:
    winer = pivos[1]
    points = sum2
elif sum3 > sum5 and sum3 > sum2 and sum3 > sum1 and sum3 > sum4:
    winer = pivos[2]
    points = sum3
elif sum4 > sum5 and sum4 > sum2 and sum4 > sum1 and sum4 > sum3:
    winer = pivos[3]
    points = sum4
elif sum5 > sum4 and sum5 > sum2 and sum5 > sum1 and sum5 > sum3:
    winer = pivos[4]
    points = sum5
else:
    print("Щось пішло не так при обличсленнях переможця, або переможець не один!")

print(Fore.YELLOW + "Найкращим варіантом вийшов -",winer, '-', points)
print('\n')