import constant
import random



class RandomKey:
    def __init__(self, keyLenght):
        self.keyLen = keyLenght
        self.keyWord = tuple('relkfgbntudsxpyozi')  
    def generateKey(self, shift = False):
        self.randomKey = ''
        for i in range(self.keyLen):
            self.randomKey+=random.choice(self.keyWord)  
        return self.keyCheck(self.keyLen, shift)
    def keyCheck(self, kL, shift = False):
        counter = 0
        repeatCounter = 0
        for i in range(len(self.randomKey)-1):
            if constant.ConstReverseThreeXThree[self.randomKey[i]] == self.randomKey[i+1]:
                counter+=1
        for i in range(len(self.randomKey)-2):
            if self.randomKey[i] == self.randomKey[i+1] == self.randomKey[i+2]:
                repeatCounter+=1
        if counter >= 1 or repeatCounter >= 1:
            return self.generateKey()
        else:
            return self.randomKey

# m = []
# a = RandomKey(20)
# for i in range(20):
#     m.append(a.generateKey())
# print(len(m))

# a = RandomKey(20)
# m = a.generateKey(True)
# print(len(m), m)


  
