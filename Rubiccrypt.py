# Модуль шифрования и дешифрования, на вход принимаются 3 параметра: 
# 1) Тип шифрования: 3 х 3, 4 х 4 итд, 
# 2) Ключ (str)
# 3) Подготовленный битовый блок текста (str)
# На выходе получается 1 битовый блок шифротекста или изначального текста
import constant 

class ThreeXThree:
    @staticmethod
    def crypt(key, openText):
        for i in key:
            roundText = ""
            for j in range(len(openText)):
                roundText+= openText[constant.ConstPermutThreeXThree[i][j]-1]
            openText = roundText
        cryptoText = openText
        return cryptoText
    @staticmethod
    def decrypt(key, cryptoText):
        reverseKey = ThreeXThree.getReverseKey(key)
        return ThreeXThree.crypt(reverseKey, cryptoText)
    @staticmethod
    def getReverseKey(key):
        backKey = ''
        for i in range(len(key)): backKey+=constant.ConstReverseThreeXThree[key[i]]
        revKey = ""
        for i in reversed(backKey): revKey+= i
        return revKey
 
# ley = 'srtlxbtdykgetbedzntr'

# # a = ThreeXThree.crypt(ley, 'У1лукоморья1дуб1зелёный1Зл')
# b = ThreeXThree.decrypt(ley, 'к1мЗУьёоб1рлдул1зеулйын1оя')


