from Rubiccrypt import ThreeXThree
from crypt import CryptPrepareAfter, CryptPrepareBefore
from decrypt import DecryptPrepareAfter, DecryptPrepareBefore

# Шифротекст в битах
def getBitStr(hexMas):
    decrMesStr = ''
    for i in range(int(len(hexMas)/2)):
        decrMesStr+= str(bin(int(hexMas[0:2],16)))[2:].zfill(8)
        hexMas = hexMas[2:]
    return decrMesStr

def checkChanges(old, new):
    numberOfChanges = int(old, 2) ^ int(new, 2)
    return len(str(bin(numberOfChanges))[2:].replace('0',''))

def prepareToCrypt(mes, key, State = 0):
    a = CryptPrepareAfter()
    if State == 0:
        prepMes = a.check13(encodeMessage)
        symbMes, hexMes = compileEncrypt(prepMes, key)
        return symbMes, hexMes
    else:
        return a.check13(encodeMessage, 1)
# Полное шифрование
def compileEncrypt(mes, key):
    cryptMas = [ThreeXThree.crypt(key,i) for i in mes]
    preCryptText = ''
    for i in cryptMas: preCryptText+=i
    r = CryptPrepareBefore()
    return(r.getReverseMixedMessage(preCryptText))



encodeMessage = "Малеукамасалам" 
key = "rktoirtzusrkftrrporb"

firstMesBit = prepareToCrypt(encodeMessage, key, 1)
finalCryptMesSym, finalCryptMesHex = prepareToCrypt(encodeMessage, key)

strCryptMes = getBitStr(finalCryptMesHex)
changes = checkChanges(firstMesBit, strCryptMes)
procent = (changes/len(strCryptMes))*100
print(procent)


