# Подготовка для дешифрования:
# 1) Перевод в битовую строку из хекса
# 2) Разбитие 1 перстановкой и склеивание
# 3) Получение блоков для дешифрования

class DecryptPrepareAfter:
    # Получаем массив хексов который преобразуем в одну строку
    def getBitStr(self, hexMas):
        lenMes = int(len(hexMas)/2)
        decrMesStr = ''
        for i in range(int(len(hexMas)/2)):
            decrMesStr+= str(bin(int(hexMas[0:2],16)))[2:].zfill(8)
            hexMas = hexMas[2:]
        return self.getMixedMessage(decrMesStr, lenMes)

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

class DecryptPrepareBefore:
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
        return self.getFinalText(finalMes)

    def getFinalText(self, mes):
        preDecodemas = []
        for i in range(int(len(mes)/8)):
            preDecodemas.append(int(mes[0:8],2))
            mes = mes[8:]
        # Получим символы:
        symbolView = bytes(preDecodemas).decode(encoding="koi8-r").replace('~','')
        # hexVies = [hex(i) for i in preDecodemas]
        return(symbolView)
    