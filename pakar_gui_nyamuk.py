import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pyswip import Prolog

# Inisialisasi prolog
prolog = Prolog()
prolog.consult("pakar_nyamuk.pl")

penyakit = list()
gejala = dict()
index_penyakit = 0
index_gejala = 0
current_penyakit = ""
current_gejala = ""

# Fungsi untuk menampilkan pertanyaan
def tampilkan_pertanyaan(pertanyaan):
    kotak_pertanyaan.configure(state=tk.NORMAL)
    kotak_pertanyaan.delete(1.0, tk.END)
    kotak_pertanyaan.insert(tk.END, pertanyaan)
    kotak_pertanyaan.configure(state=tk.DISABLED)

# Fungsi untuk menampilkan hasil diagnosa
def hasil_diagnosa(penyakit=""):
    if penyakit:
        messagebox.showinfo("Hasil Diagnosa", f"Anda terdeteksi {penyakit}.")
    else:
        messagebox.showinfo("Hasil Diagnosa", "Tidak terdeteksi penyakit.")
    yes_btn.configure(state=tk.DISABLED)
    no_btn.configure(state=tk.DISABLED)
    start_btn.configure(state=tk.NORMAL)

# Fungsi untuk melanjutkan ke pertanyaan berikutnya
def pertanyaan_selanjutnya(ganti_penyakit=False):
    global current_penyakit, current_gejala, index_penyakit, index_gejala

    if ganti_penyakit:
        index_penyakit += 1
        index_gejala = -1

    if index_penyakit >= len(penyakit):
        hasil_diagnosa()
        return

    current_penyakit = penyakit[index_penyakit]
    index_gejala += 1

    if index_gejala >= len(gejala[current_penyakit]):
        hasil_diagnosa(current_penyakit)
        return

    current_gejala = gejala[current_penyakit][index_gejala]

    if list(prolog.query(f"gejala_pos({current_gejala})")):
        pertanyaan_selanjutnya()
        return
    elif list(prolog.query(f"gejala_neg({current_gejala})")):
        pertanyaan_selanjutnya(ganti_penyakit=True)
        return

    pertanyaan = list(prolog.query(f"pertanyaan({current_gejala}, Y)"))[0]["Y"].decode()
    tampilkan_pertanyaan(pertanyaan)

# Fungsi untuk menangani jawaban
def jawaban(jwb):
    if jwb:
        prolog.assertz(f"gejala_pos({current_gejala})")
        pertanyaan_selanjutnya()
    else:
        prolog.assertz(f"gejala_neg({current_gejala})")
        pertanyaan_selanjutnya(ganti_penyakit=True)

# Fungsi untuk memulai diagnosa
def mulai_diagnosa():
    global penyakit, gejala, index_penyakit, index_gejala

    prolog.retractall("gejala_pos(_)")
    prolog.retractall("gejala_neg(_)")

    start_btn.configure(state=tk.DISABLED)
    yes_btn.configure(state=tk.NORMAL)
    no_btn.configure(state=tk.NORMAL)

    penyakit = [p["X"].decode() for p in list(prolog.query("penyakit(X)"))]
    for p in penyakit:
        gejala[p] = [g["X"] for g in list(prolog.query(f"gejala(X, \"{p}\")"))]

    index_penyakit = 0
    index_gejala = -1
    pertanyaan_selanjutnya()

# GUI Tkinter

# Inisialisasi window utama
root = tk.Tk()
root.title("Sistem Pakar Penyakit Akibat Gigitan Nyamuk")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Aplikasi Diagnosa Penyakit Akibat Gigitan Nyamuk", font=("Arial", 18, "bold")).grid(column=0, row=0, columnspan=3, pady=10)
ttk.Label(mainframe, text="Silakan jawab pertanyaan berikut untuk diagnosa.").grid(column=0, row=1, columnspan=3, pady=5)

kotak_pertanyaan = tk.Text(mainframe, height=5, width=50, wrap=tk.WORD, state=tk.DISABLED)
kotak_pertanyaan.grid(column=0, row=2, columnspan=3, pady=10)

button_frame = ttk.Frame(mainframe)
button_frame.grid(column=0, row=3, columnspan=3, pady=10)

# Tombol "Tidak"
no_btn = ttk.Button(button_frame, text="Tidak", state=tk.DISABLED, command=lambda: jawaban(False), width=15)
no_btn.pack(side=tk.LEFT, padx=10)

# Tombol "Ya"
yes_btn = ttk.Button(button_frame, text="Ya", state=tk.DISABLED, command=lambda: jawaban(True), width=15)
yes_btn.pack(side=tk.LEFT, padx=10)

# Tombol "Mulai Diagnosa"
start_btn = ttk.Button(mainframe, text="Mulai Diagnosa", command=mulai_diagnosa, width=20)
start_btn.grid(column=1, row=4, columnspan=1, pady=20, sticky=(tk.W, tk.E))

for widget in mainframe.winfo_children():
    widget.grid_configure(padx=5, pady=5)

root.mainloop()
