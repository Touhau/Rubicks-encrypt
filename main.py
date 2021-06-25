import tkinter as tk
from Rubiccrypt import ThreeXThree
from crypt import CryptPrepareAfter, CryptPrepareBefore
from decrypt import DecryptPrepareAfter, DecryptPrepareBefore
from key import RandomKey
from gui import Gui
class Engine(Gui):
    def __init__(self, window):
        super().__init__(window)
        self.generate_key_btn.config(command = lambda *args: self.key_gen())
        self.crypt_bth.config(command = lambda *args: self.crypt())
        self.decrypt_bth.config(command = lambda *args: self.decrypt())
        self.key_field.delete(0, tk.END)
        self.opentext_field.delete(1.0, tk.END)
        self.ready_text_field_hex.delete(1.0, tk.END)
        self.ready_text_field_sym.delete(1.0, tk.END)
    def key_gen(self):
        self.key_field.delete(0, tk.END)
        temp = RandomKey(20)
        self.key_field.insert(0, temp.generateKey())
    def crypt(self):
        self.encodeMessage = self.opentext_field.get(1.0, tk.END)
        finalCryptMesSym, finalCryptMesHex = self.prepareToCrypt(self.encodeMessage, self.key_field.get())
        temp = [str(bin(i))[2:].zfill(8) for i in self.encodeMessage.encode(encoding="koi8-r")]
        temp2 = ''
        for i in range(len(temp)):
            temp2+= str(hex(int(temp[i], 2)))[2:].zfill(2)
        self.opentext_field.delete(1.0, tk.END)
        self.opentext_field.insert(1.0, temp2)
        self.ready_text_field_hex.delete(1.0, tk.END)
        self.ready_text_field_sym.delete(1.0, tk.END)
        self.ready_text_field_sym.insert(1.0, finalCryptMesSym)
        self.ready_text_field_hex.insert(1.0, finalCryptMesHex)
    def decrypt(self):
        self.decodeMessage = self.opentext_field.get(1.0, tk.END)
        finalDecryptMes = self.prepareToDecrypt(self.decodeMessage, self.key_field.get())
        self.ready_text_field_hex.delete(1.0, tk.END)
        self.ready_text_field_sym.delete(1.0, tk.END)
        self.ready_text_field_sym.insert(1.0, finalDecryptMes)
    def prepareToCrypt(self, mes, key, shift = False):
        a = CryptPrepareAfter()
        prepMes = a.check13(mes)
        symbMes, hexMes = self.compileEncrypt(prepMes, key, shift)
        return symbMes, hexMes 
    def compileEncrypt(self, mes, key, shift = False):
        if shift:
            cryptMas = crypt_with_shift(mes, key)
        else:
            cryptMas = [ThreeXThree.crypt(key,i) for i in mes]
        preCryptText = ''
        for i in cryptMas: preCryptText+=i
        r = CryptPrepareBefore()
        return(r.getReverseMixedMessage(preCryptText))
    def prepareToDecrypt(self, hexMes, key, shift = False):
        a = DecryptPrepareAfter()
        prepMas = a.getBitStr(hexMes)
        symbMes = self.compileDecrypt(prepMas, key)
        return symbMes
    def compileDecrypt(self, mes, key, shift = False):
        decryptMas = [ThreeXThree.decrypt(key, i) for i in mes]
        preDecryptText = ''
        for i in decryptMas: preDecryptText+=i
        r = DecryptPrepareBefore()
        return(r.getReverseMixedMessage(preDecryptText))


if __name__ == "__main__":
    q = tk.Tk()
    window = Engine(q)
    window.mainloop()


# Исходное сообщение
# encodeMessage = "Пример сообщения для демонстрации работоспособности текста" 
# decodeMessage = 'c99df5c7c5cbc0da9597cd65cfd9c7cecbc1c5ccd964c6d4806482cfc7d4c3d0c2cbd188d2cbc3d0c3cd71d6d1d1de8865cfd6cfcf7ed4d4546bd4e16ac4f4f67b'

# key = RandomKey(20)
# readyKey = key.generateKey()
# print(readyKey)
# Key = 'okydekgszegntydzkfud'
# # c - шифрование, d - дешифрование
# operation = 'd'


# if operation == "c":
#     finalCryptMesSym, finalCryptMesHex = prepareToCrypt(encodeMessage, Key)
#     print(finalCryptMesSym, ' ', finalCryptMesHex)

# else:
#     finalDecryptMes = prepareToDecrypt(decodeMessage, Key)
#     print(finalDecryptMes)



