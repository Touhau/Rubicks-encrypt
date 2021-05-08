# Подготовка для шифрования:
# 1) Проверка на кратность 13 и добитие если надо
# 2) Перевод в KOI8-R
# 3) Разбитие 1 перстановкой и склеивание
# 4) Получение блоков для шифрования

class CryptPrepareAfter:
    # Проверка на длину
    def check13(self, mes, forState = 0):
        if len(mes)%13 != 0:
            mes+= '~' * (13-(len(mes) % 13))
        if forState == 0:
            return self.getBitArray(mes)
        else:
            return self.getBitArray(mes, 1)
      

    # Получаем массив битовых строк сообщения, на вход идёт изначальное символьное сообщение
    def getBitArray(self, mes, forState = 0):
        nummes = [str(bin(i))[2:].zfill(8) for i in mes.encode(encoding="koi8-r")]
        tempMes = ''
        for i in nummes: tempMes+=i
        if forState == 0:
            return self.getMixedMessage(tempMes, len(tempMes)/8)
        else:
            return tempMes
        

    # Получаем перемешанное сообщение
    def getMixedMessage(self, bitMes, mesLen):
        blockmas = []
        for i in range(8):
            blockmas.append(bitMes[i])
        for i in range(8):
            q = i
            for j in range(int(mesLen)-1):
                blockmas[i]+=bitMes[q+8]
                q+=8
        preparemes = ''
        for i in blockmas: preparemes+= i
        return self.getReadyToCryptBlocks(preparemes, mesLen)

    # Получаем битовые блоки сообщения
    def getReadyToCryptBlocks(self, bitMes, mesLen):
        prepare = []
        mesBitLen = mesLen*8
        for i in range(int(mesBitLen/26)):
            prepare.append(bitMes[0:26])
            bitMes = bitMes[26:]
        return(prepare)

# После шифрования:
# 5) Разбитие 2 перестановкой
# 6) Склеивание в текста
# 7) Перевод в хекс и символьный вид

class CryptPrepareBefore:
    # Обратная перестановка
    def getReverseMixedMessage(self, mes):
        self.bitMesLen = len(mes)
        self.mesLen = int(self.bitMesLen/8)
        bitCont = []
        for i in range(self.mesLen):
            bitCont.append(mes[i])

        for i in range(self.mesLen):
            n = i
            for j in range(7):  
                bitCont[i]+=mes[n+self.mesLen]
                n+=self.mesLen

        finalMes = ''
        for i in bitCont: finalMes+=i
        # print(finalMes)
        return self.getFinalText(finalMes)

    def getFinalText(self, mes):
        preDecodemas = []
        for i in range(int(len(mes)/8)):
            preDecodemas.append(int(mes[0:8],2))
            mes = mes[8:]
        # Получим символы:
        symbolView = bytes(preDecodemas).decode(encoding="koi8-r")
        hexVies = ''
        for i in range(len(preDecodemas)):
            hexVies+= str(hex(preDecodemas[i]))[2:].zfill(2)

        return(symbolView, hexVies)
    

        
            
        
