import constant
import random

# Генерация ключа заданной длины с проверкой. 
# # Проверка включает в себя: 
# 1) Проверка на отсутствие рядом стоящих взаимообратных действий
# 2) Проверка на количество уникальных действий (минимум ...)
# 3) Проверка на циклические действия

class RandomKey:
    def __init__(self, keyLenght):
        self.keyLen = keyLenght
        self.keyWord = tuple('relkfgbntudsxpyozi')
        self.generateKey(self.keyLen)
        
    
    def generateKey(self, keyLen):
        self.randomKey = ''
        for i in range(keyLen):
            self.randomKey+=random.choice(self.keyWord)
        
        return self.keyCheck(keyLen)

    def keyCheck(self, kL):
        counter = 0
        repeatCounter = 0
        for i in range(len(self.randomKey)-1):
            if constant.ConstReverseThreeXThree[self.randomKey[i]] == self.randomKey[i+1]:
                counter+=1
            if self.randomKey[i] == self.randomKey[i+1]:
                repeatCounter += 1
        
        
        if counter >= 1 and repeatCounter >= 1:
            print(f'Ключ: {self.randomKey}, ошибок: {counter}, повторений: {repeatCounter}')
            self.generateKey(kL)
        else:
            print(self.randomKey)
        

a = RandomKey(20)



        
