import tkinter as tk
from tkinter import ttk

class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Program Enkripsi & Dekripsi - Caesar Cipher")
        self.root.geometry("600x500")
        self.root.configure(bg="#FFD1DC")  

        self.shift_value = tk.IntVar(value=3)  # Default nilai pergeseran

        self.tab_control = ttk.Notebook(root)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        
        self.tab_control.add(self.tab1, text='Enkripsi')
        self.tab_control.add(self.tab2, text='Dekripsi')
        self.tab_control.pack(expand=1, fill="both")
        
        self.setup_enkripsi_tab()
        self.setup_dekripsi_tab()

    def setup_enkripsi_tab(self):
        canvas = tk.Canvas(self.tab1, bg="#FFD1DC", highlightthickness=0)
        canvas.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Label(canvas, text="Jumlah Pergeseran:", bg="#FFD1DC", fg="black").place(x=40, y=40)
        shift_spinbox = ttk.Spinbox(canvas, from_=1, to=25, width=5, textvariable=self.shift_value)
        shift_spinbox.place(x=160, y=40)

        tk.Label(canvas, text="Masukkan Plainteks:", bg="#FFD1DC", fg="black").place(x=40, y=100)
        self.plaintext_input = tk.Text(canvas, height=5, width=55, bg="#FFF0F5", fg="black", relief="flat", wrap="word")
        self.plaintext_input.place(x=40, y=130)

        tk.Button(canvas, text="Enkripsi", command=self.encrypt, bg="#FF69B4", fg="white").place(x=260, y=250)

        tk.Label(canvas, text="Hasil Enkripsi (Cipherteks):", bg="#FFD1DC", fg="black").place(x=40, y=310)
        self.cipher_output = tk.Text(canvas, height=5, width=55, bg="#FFF0F5", fg="black", relief="flat", wrap="word")
        self.cipher_output.place(x=40, y=340)

    def setup_dekripsi_tab(self):
        canvas = tk.Canvas(self.tab2, bg="#FFD1DC", highlightthickness=0)
        canvas.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Label(canvas, text="Jumlah Pergeseran:", bg="#FFD1DC", fg="black").place(x=40, y=40)
        shift_spinbox = ttk.Spinbox(canvas, from_=1, to=25, width=5, textvariable=self.shift_value)
        shift_spinbox.place(x=160, y=40)

        tk.Label(canvas, text="Masukkan Cipherteks:", bg="#FFD1DC", fg="black").place(x=40, y=100)
        self.cipher_input = tk.Text(canvas, height=5, width=55, bg="#FFF0F5", fg="black", relief="flat", wrap="word")
        self.cipher_input.place(x=40, y=130)

        tk.Button(canvas, text="Dekripsi", command=self.decrypt, bg="#FF69B4", fg="white").place(x=260, y=250)

        tk.Label(canvas, text="Hasil Dekripsi (Plainteks):", bg="#FFD1DC", fg="black").place(x=40, y=310)
        self.plain_output = tk.Text(canvas, height=5, width=55, bg="#FFF0F5", fg="black", relief="flat", wrap="word")
        self.plain_output.place(x=40, y=340)

    def shift_character(self, char, shift, encrypt=True):
        if not char.isalpha():  # Abaikan karakter non-alfabet
            return char
        ascii_base = 97 if char.islower() else 65
        if not encrypt:
            shift = -shift  # Jika dekripsi, lakukan pergeseran terbalik
        shifted = (ord(char) - ascii_base + shift) % 26
        return chr(shifted + ascii_base)
    
    def process_text(self, text, encrypt=True):
        shift = self.shift_value.get()  # Ambil nilai pergeseran
        result = ''.join(self.shift_character(char, shift, encrypt) for char in text)
        return result

    def encrypt(self):
        plaintext = self.plaintext_input.get("1.0", tk.END).strip()  # Ambil teks dari input
        ciphertext = self.process_text(plaintext, encrypt=True)
        self.cipher_output.delete("1.0", tk.END)  # Kosongkan output sebelumnya
        self.cipher_output.insert("1.0", ciphertext)  # Masukkan hasil enkripsi ke output

    def decrypt(self):
        ciphertext = self.cipher_input.get("1.0", tk.END).strip()  # Ambil teks dari input
        plaintext = self.process_text(ciphertext, encrypt=False)
        self.plain_output.delete("1.0", tk.END)  # Kosongkan output sebelumnya
        self.plain_output.insert("1.0", plaintext)  # Masukkan hasil dekripsi ke output


if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()
