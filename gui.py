import tkinter as tk

class Gui(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        window.title('Шифрование Рубика')
        window.geometry('1230x820')
        window.resizable(False, False)
        window['bg'] = '#ecfceb'

        self.opentext_label = tk.Label(window, text = 'Исходное сообщение', font = 'Arial 14', bg = '#ecfceb')
        self.opentext_field = tk.Text(window, width = 25, height = 35, font = 'Arial 14')
        self.key_label = tk.Label(window, text = 'Ключ шифрования', font = 'Arial 14', bg = '#ecfceb')
        self.key_field = tk.Entry(window, font = 'Arial 14', width = 22)
        self.generate_key_btn = tk.Button(window, text = 'Сгенерировать ключ', font = 'Arial 14', width = 20)
        self.ready_text_label_sym = tk.Label(window, text = 'Готовое сообщение в символьном виде', font = 'Arial 14', bg = '#ecfceb')
        self.ready_text_field_sym = tk.Text(window, width = 25, height = 35, font = 'Arial 14')
        self.crypt_bth = tk.Button(window, text = 'Зашифровать', font = 'Arial 14', width = 20)
        self.decrypt_bth = tk.Button(window, text = 'Расшифровать', font = 'Arial 14', width = 20)
        self.ready_text_label_hex = tk.Label(window, text = 'Готовое сообщение в 16-ном виде', font = 'Arial 14', bg = '#ecfceb')
        self.ready_text_field_hex = tk.Text(window, width = 25, height = 35, font = 'Arial 14')


        self.opentext_label.grid(row = 0, column = 0)
        self.opentext_field.grid(row = 1, column = 0, rowspan = 4, padx = 15)

        self.key_label.grid(row = 0, column = 1)
        self.key_field.grid(row = 1, column = 1)

        self.generate_key_btn.grid(row = 2, column = 1)
        self.crypt_bth.grid(row = 3, column = 1)
        self.decrypt_bth.grid(row = 4, column = 1)

        self.ready_text_label_sym.grid(row = 0, column = 2)
        self.ready_text_field_sym.grid(row = 1, column = 2, rowspan = 4, padx = 15)

        self.ready_text_label_hex.grid(row = 0, column = 3)
        self.ready_text_field_hex.grid(row = 1, column = 3, rowspan = 4, padx = 15)




if __name__ == "__main__":
    q = tk.Tk()
    window = Gui(q)
    window.mainloop()