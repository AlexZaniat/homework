import tkinter as tk
from tkinter import (messagebox)
import random
import matplotlib.pyplot as plt
from math import prod
def runprogram():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        if a > b:
            messagebox.showerror("Chyba", "Hodnota a musí byť menšia alebo rovná hodnote b.")
            return
        numbers = [random.randint(a, b) for _ in range(60)]
        summ = sum(numbers)
        mutiplication = prod(numbers)
        fixedNumbers = [x + 5 for x in numbers]
        messagebox.showinfo("Výsledky", f"Súčet: {summ}\nSúčin: {mutiplication}")
        plt.figure(figsize=(10, 6))
        plt.plot(fixedNumbers, marker='o', label='Pôvodné hodnoty')
        plt.title("Graf pôvodných hodnôt")
        plt.xlabel("Index")
        plt.ylabel("Hodnota")
        plt.legend()
        plt.grid()
        plt.show()
    except ValueError:
        messagebox.showerror("Chyba", "Prosím, zadajte platné čísla pre a a b.")

okno = tk.Tk()
okno.title("Programovacie techniky")
okno.geometry("400x300")
label_a = tk.Label(okno, text="Zadajte hodnotu a (dolná hranica):")
label_a.pack(pady=5)
entry_a = tk.Entry(okno)
entry_a.pack(pady=5)
label_b = tk.Label(okno, text="Zadajte hodnotu b (horná hranica):")
label_b.pack(pady=5)
entry_b = tk.Entry(okno)
entry_b.pack(pady=5)
legend = tk.Label(okno,
                  text="Programovacie techniky\n"                       "Meno: Aliaksandr\n"
                       "Priezvisko: Varapayeu\n"                       "Zadanie úlohy: Vygenerujte pole 60 náhodných čísiel, "
                       "spočítajte a tiež vynásobte všetky čísla a vypíšte obidve výsledky, "                       "ku každému číslu prirátajte hodnotu 5 a vykreslite graf všetkých neupravených hodnôt.",
                  wraplength=380, justify="left")
legend.pack(pady=10)
button = tk.Button(okno, text="Spustiť program", command=runprogram)
button.pack(pady=20)
okno.mainloop()