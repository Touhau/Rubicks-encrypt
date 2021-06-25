import random
import math
import time

import openpyxl

from Rubiccrypt import ThreeXThree
from crypt import CryptPrepareAfter, CryptPrepareBefore
from decrypt import DecryptPrepareAfter, DecryptPrepareBefore
from key import RandomKey

# Шифротекст в битах
def getBitStr(hexMas):
    decrMesStr = ''
    for i in range(int(len(hexMas)/2)):
        decrMesStr+= str(bin(int(hexMas[0:2],16)))[2:].zfill(8)
        hexMas = hexMas[2:]
    return decrMesStr

def checkChanges(old, new):
    # print(old,'\n',new)
    numberOfChanges = int(old, 2) ^ int(new, 2)
    return len(str(bin(numberOfChanges))[2:].replace('0',''))

def prepareToCrypt(mes, key, State = 0):
    a = CryptPrepareAfter()
    # print(mes)
    if State == 0:
        prepMes = a.check13(mes)
        symbMes, hexMes = compileEncrypt(prepMes, key)
        return symbMes, hexMes
    else:
        return a.check13(mes, 1)
# Полное шифрование
def compileEncrypt(mes, key):
    cryptMas = [ThreeXThree.crypt(key,i) for i in mes]
    preCryptText = ''
    for i in cryptMas: preCryptText+=i
    r = CryptPrepareBefore()
    return(r.getReverseMixedMessage(preCryptText))


message = tuple('qwertyuiopasdfghjklzxcvbnm 1234567890йцукенгшщзхъфывапролджэячсмитьбю')

# counter_row = 1
# for mes in range(1,10000, 50):
#     encodeMessage = ''
#     for char in range(mes):
#         encodeMessage+=random.choice(message)
#     stats_excel = openpyxl.load_workbook(filename = 'rubickcrypt\stats.xlsx')
#     book = stats_excel['Sheet1']
#     for i in range(1, 41):
#         avg_key_length = []
#         for j in range(100):
#             key = RandomKey(i)
#             firstMesBit = prepareToCrypt(encodeMessage, key.generateKey(), 1)
#             finalCryptMesSym, finalCryptMesHex = prepareToCrypt(encodeMessage, key.generateKey())
#             strCryptMes = getBitStr(finalCryptMesHex)
#             changes = checkChanges(firstMesBit, strCryptMes)
#             procent = (changes/len(strCryptMes))*100
#             avg_key_length.append(procent)
#             print(f'Строка: {mes}, длина ключа: {i}, трай ключа: {j}')
#         key_avg_excel = openpyxl.utils.get_column_letter(2+i)+str(counter_row+2)
        # book[key_avg_excel] = round(sum(avg_key_length)/100, 2)
    
    
    # mes_excel_row = "B"+str(counter_row+2)
    # mes_lenght_excel_row = "A"+str(counter_row+2)
    # book[mes_excel_row] = encodeMessage
    # book[mes_lenght_excel_row] = len(encodeMessage)
    # stats_excel.save(filename = 'rubickcrypt\stats.xlsx')
    # counter_row+=1
    
enc_mes1 = 'has0'
enc_mes2 = 'has1'
dop = '123456789qwertyuiopasdfghjkzxcvbnmlйцукенгшщзхъфывапролджэячсмитьбю'
# for w in dop:
#     enc_mes2 = enc_mes3 + w
#     for i in range(1,41):
#         avg_key_length = []
#         for j in range(100):
key = RandomKey(20)
key_read = key.generateKey()
firstMesBit1 = prepareToCrypt(enc_mes1, key_read, 1)
finalCryptMesSym1, finalCryptMesHex1 = prepareToCrypt(enc_mes1, key_read)
strCryptMes1 = getBitStr(finalCryptMesHex1)
# print(finalCryptMesHex1)

firstMesBit2 = prepareToCrypt(enc_mes2, key_read, 1)
finalCryptMesSym2, finalCryptMesHex2 = prepareToCrypt(enc_mes2, key_read)
strCryptMes2 = getBitStr(finalCryptMesHex2)
# print(finalCryptMesHex2)

# chan = checkChanges(firstMesBit1, firstMesBit2)
changes = checkChanges(strCryptMes1, strCryptMes2)
procent = (changes/len(strCryptMes1))*100
# avg_key_length.append(procent)
print(strCryptMes1)
print(strCryptMes2)
print(procent)
print(changes)


# encodeMessage = ''
# encodeMessage = 'й~~~~~~~~~~~~'
# for char in range(10):
#     encodeMessage+=random.choice(message)

# with open('huina.txt', 'w') as po:
#     po.write(encodeMessage)
# k = 0
# counter = 0
# key = RandomKey(1)
# finalCryptMesSym, finalCryptMesHex = prepareToCrypt(encodeMessage, key.generateKey())
# new_encode = finalCryptMesSym
# print(new_encode, encodeMessage)
# e = input()
# while k != 1:
#     finalCryptMesSym1, finalCryptMesHex1 = prepareToCrypt(new_encode, key.generateKey())
#     new_encode = finalCryptMesSym1
#     print(new_encode)
#     if new_encode != encodeMessage:
#         counter+=1
#         print(counter)
#     else:
#         print(counter)
#         k+=1


