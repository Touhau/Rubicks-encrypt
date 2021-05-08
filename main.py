from Rubiccrypt import ThreeXThree
from crypt import CryptPrepareAfter, CryptPrepareBefore
from decrypt import DecryptPrepareAfter, DecryptPrepareBefore


# Подготовка к шифрованию и полное шифрование
def prepareToCrypt(mes, key):
    a = CryptPrepareAfter()
    prepMes = a.check13(encodeMessage)
    symbMes, hexMes = compileEncrypt(prepMes, key)
    return symbMes, hexMes
# Полное шифрование
def compileEncrypt(mes, key):
    cryptMas = [ThreeXThree.crypt(key,i) for i in mes]
    preCryptText = ''
    for i in cryptMas: preCryptText+=i
    r = CryptPrepareBefore()
    return(r.getReverseMixedMessage(preCryptText))
  
def prepareToDecrypt(hexMes, key):
    a = DecryptPrepareAfter()
    prepMas = a.getBitStr(hexMes)
    symbMes = compileDecrypt(prepMas, key)
    return symbMes

def compileDecrypt(mes, key):
    decryptMas = [ThreeXThree.decrypt(key, i) for i in mes]
    preDecryptText = ''
    for i in decryptMas: preDecryptText+=i
    r = DecryptPrepareBefore()
    return(r.getReverseMixedMessage(preDecryptText))



# Исходное сообщение
encodeMessage = "Аюсолютно рандомное сообщение" 
decodeMessage = '61cd9dcacacccf9595ceda9f97d4cf65dbd6d6f4d4d4c4c7d4caecf66f6bcfd6ccc5886f7e556f'
# Ключ
key = "rktoirtzusrkftrrporb"
# c - шифрование, d - дешифрование
operation = 'd'


if operation == "c":
    finalCryptMesSym, finalCryptMesHex = prepareToCrypt(encodeMessage, key)
    print(finalCryptMesSym, ' ', finalCryptMesHex)
else:
    finalDecryptMes = prepareToDecrypt(decodeMessage, key)
    print(finalDecryptMes)




