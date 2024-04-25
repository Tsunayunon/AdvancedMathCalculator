import math
import tkinter as tk
from tkinter import messagebox

class Deneme:
    @classmethod
    def islem(cls, a, b=None, c=None):
        if c == "1":
            return f"Sonuç: {a + b}"
        elif c == "2":
            if b == 0:
                return "Bir sayı sıfıra bölünemez"
            else:
                return f"Sonuç: {a / b}"
        elif c == "3":
            return f"Sonuç: {a - b}"
        elif c == "4":
            return f"Sonuç: {a * b}"
        elif c == "5":
            return f"Sonuç: {a ** b}"
        elif c == "6":
            if a < 0:
                return "Negatif sayının karekökü alınamaz"
            else:
                return f"Sonuç: {math.sqrt(a)}"
        elif c == "7":
            return f"Sonuç: {math.sin(math.radians(a))}"
        elif c == "8":
            return f"Sonuç: {math.cos(math.radians(a))}"
        elif c == "9":
            return f"Sonuç: {math.tan(math.radians(a))}"
        elif c == "10":
            return f"Sonuç: {math.log(a) if a > 0 else 'Pozitif sayılar için logaritma hesaplanır'}"
        elif c == "11":
            return f"Sonuç: {math.factorial(a) if a >= 0 else 'Negatif sayının faktöriyeli hesaplanamaz'}"
        elif c == "12":
            return "Bu işlem için ek bilgi gerekli."
        elif c == "13":
            if math.tan(math.radians(a)) == 0:
                return "Kotanjant tanımsız (tanjant 0 oldu)."
            else:
                return f"Sonuç: {1 / math.tan(math.radians(a))}"
        else:
            return "Geçersiz işlem"

def create_gui():
    root = tk.Tk()
    root.title("Matematiksel İşlemler Arayüzü")
    root.geometry("500x400")  # Pencere boyutu

    tk.Label(root, text="Birinci sayı:").pack()
    first_number = tk.Entry(root)
    first_number.pack()

    tk.Label(root, text="İkinci sayı (opsiyonel):").pack()
    second_number = tk.Entry(root)
    second_number.pack()

    operations = {
        "1": "Toplama",
        "2": "Bölme",
        "3": "Çıkarma",
        "4": "Çarpma",
        "5": "Üs alma",
        "6": "Karekök",
        "7": "Sinüs",
        "8": "Kosinüs",
        "9": "Tanjant",
        "10": "Logaritma",
        "11": "Faktöriyel",
        "12": "Kombinasyon",
        "13": "Kotanjant"
    }

    tk.Label(root, text="İşlem seçiniz:").pack()
    operation_var = tk.StringVar(root)
    operation_menu = tk.OptionMenu(root, operation_var, *operations.values())
    operation_menu.pack()

    result_label = tk.Label(root, text="Sonuç burada görünecek...")
    result_label.pack()

    def perform_operation():
        a = float(first_number.get())
        op = next(key for key, value in operations.items() if value == operation_var.get())
        b = second_number.get()
        if b == "":
            b = None
        else:
            b = float(b)
        result = Deneme.islem(a, b, op)
        result_label.config(text=result)

    calculate_button = tk.Button(root, text="Hesapla", command=perform_operation)
    calculate_button.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
