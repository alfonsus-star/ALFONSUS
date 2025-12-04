import datetime
import sys

try:
    import tkinter as tk
    from tkinter import messagebox, ttk
    TK_AVAILABLE = True
except ModuleNotFoundError:
    TK_AVAILABLE = False

class RentalPS:
    def __init__(self):
        self.harga_ps = {
            "PS3": 5000,
            "PS4": 8000,
            "PS5": 12000
        }
        self.riwayat = []

    def buat_struk(self, nama, jenis, lama):
        total = lama * self.harga_ps[jenis]
        waktu = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        struk = (
            f"======= STRUK RENTAL PS =======\n"
            f"Waktu        : {waktu}\n"
            f"Nama Penyewa : {nama}\n"
            f"Jenis PS     : {jenis}\n"
            f"Lama Sewa    : {lama} jam\n"
            f"Total Bayar  : Rp {total:,}\n"
            f"================================\n"
        )
        return struk

    def tambah_riwayat(self, struk):
        self.riwayat.append(struk)

    def get_riwayat(self):
        return self.riwayat

    def simpan_ke_file(self, filename="riwayat_rental.txt"):
        with open(filename, "w", encoding="utf-8") as file:
            for data in self.riwayat:
                file.write(data + "\n")

rental = RentalPS()

def cli_sewa_ps():
    print("\n--- Form Sewa PS (CLI) ---")
    nama = input("Masukkan nama penyewa : ").strip()
    print("\nPilih jenis PS:")
    print("1. PS3 (Rp 5.000 / jam)")
    print("2. PS4 (Rp 8.000 / jam)")
    print("3. PS5 (Rp 12.000 / jam)")

    pilihan = input("Masukkan pilihan (1/2/3): ").strip()
    jenis_map = {"1": "PS3", "2": "PS4", "3": "PS5"}

    if pilihan not in jenis_map:
        print("Pilihan tidak tersedia!")
        return

    jenis = jenis_map[pilihan]

    try:
        lama = int(input("Lama sewa (jam): ").strip())
    except ValueError:
        print("Input harus angka!")
        return

    struk = rental.buat_struk(nama, jenis, lama)
    print(struk)
    rental.tambah_riwayat(struk)

def cli_tampilkan_riwayat():
    print("\n========= RIWAYAT TRANSAKSI =========")
    
    riwayat = rental.get_riwayat()
    if not riwayat:
        print("Belum ada transaksi.")
        return

    for i, struk in enumerate(riwayat, start=1):
        print(f"\n--- Transaksi {i} ---")
        print(struk)   

def cli_simpan_ke_file():
    if not rental.get_riwayat():
        print("Belum ada transaksi untuk disimpan!")
        return

    try:
        rental.simpan_ke_file()
        print("Riwayat berhasil disimpan ke 'riwayat_rental.txt'")
    except Exception as e:
        print(f"Gagal menyimpan file: {e}")


def run_cli():
    while True:
        print("\n===========================")
        print("RENTAL PLAYSTATION")
        print("===========================")
        print("1. Sewa PS")
        print("2. Lihat Riwayat Transaksi")
        print("3. Simpan Riwayat ke File")
        print("4. Keluar")
        print("===========================")

        menu = input("Pilih menu: ").strip()

        if menu == "1":
            cli_sewa_ps()
        elif menu == "2":
            cli_tampilkan_riwayat()
        elif menu == "3":
            cli_simpan_ke_file()
        elif menu == "4":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if TK_AVAILABLE:

    def gui_sewa_ps():
        nama = entry_nama.get().strip()
        jenis = combo_ps.get().strip()
        lama_text = entry_lama.get().strip()

        if not nama or not jenis or not lama_text:
            messagebox.showerror("Error", "Semua harus diisi!")
            return

        try:
            lama = int(lama_text)
        except ValueError:
            messagebox.showerror("Error", "Lama sewa harus berupa angka!")
            return

        struk = rental.buat_struk(nama, jenis, lama)
        rental.tambah_riwayat(struk)

        textbox_output.delete(1.0, tk.END)
        textbox_output.insert(tk.END, struk)


def gui_tampilkan_riwayat():
    riwayat = rental.get_riwayat()
    
    if not riwayat:
        messagebox.showinfo("Info", "Belum ada transaksi.")
        return

    textbox_output.delete(1.0, tk.END)

    for i, struk in enumerate(riwayat, start=1):
        textbox_output.insert(tk.END, f"--- Transaksi {i} ---\n")
        textbox_output.insert(tk.END, struk + "\n") 

        
    def gui_simpan_ke_file():
        try:
            rental.simpan_ke_file()
            messagebox.showinfo("Sukses", "Riwayat berhasil disimpan ke 'riwayat_rental.txt'")
        except Exception as e:
            messagebox.showerror("Gagal", f"Terjadi kesalahan: {e}")

if TK_AVAILABLE:

    def gui_sewa_ps():
        nama = entry_nama.get().strip()
        jenis = combo_ps.get().strip()
        lama_text = entry_lama.get().strip()

        if not nama or not jenis or not lama_text:
            messagebox.showerror("Error", "Semua harus diisi!")
            return

        try:
            lama = int(lama_text)
        except ValueError:
            messagebox.showerror("Error", "Lama sewa harus berupa angka!")
            return

        struk = rental.buat_struk(nama, jenis, lama)
        rental.tambah_riwayat(struk)

        textbox_output.delete(1.0, tk.END)
        textbox_output.insert(tk.END, struk)


    def gui_tampilkan_riwayat():
        riwayat = rental.get_riwayat()

        if not riwayat:
            messagebox.showinfo("Info", "Belum ada transaksi.")
            return

        textbox_output.delete(1.0, tk.END)

        for i, struk in enumerate(riwayat, start=1):
            textbox_output.insert(tk.END, f"--- Transaksi {i} ---\n")
            textbox_output.insert(tk.END, struk + "\n")


    def gui_simpan_ke_file():
        try:
            rental.simpan_ke_file()
            messagebox.showinfo("Sukses", "Riwayat berhasil disimpan ke 'riwayat_rental.txt'")
        except Exception as e:
            messagebox.showerror("Gagal", f"Terjadi kesalahan: {e}")


    def build_and_run_gui():
        root = tk.Tk()
        root.title("Program Rental Playstation")
        root.geometry("640x520")

        frame_form = tk.Frame(root)
        frame_form.pack(pady=10, padx=10, anchor="w")

        # Nama Penyewa
        tk.Label(frame_form, text="Nama Penyewa").grid(row=0, column=0, sticky="w", padx=8)
        global entry_nama
        entry_nama = tk.Entry(frame_form, width=40)
        entry_nama.grid(row=0, column=1)

        # Pilih PS
        tk.Label(frame_form, text="Pilih Jenis PS").grid(row=1, column=0, sticky="w", padx=8, pady=10)
        global combo_ps
        combo_ps = ttk.Combobox(frame_form, values=["PS3", "PS4", "PS5"], state="readonly", width=37)
        combo_ps.grid(row=1, column=1)
        combo_ps.current(0)

        # Lama Sewa
        tk.Label(frame_form, text="Lama Sewa (jam)").grid(row=2, column=0, sticky="w", padx=8)
        global entry_lama
        entry_lama = tk.Entry(frame_form, width=40)
        entry_lama.grid(row=2, column=1)

        # Tombol
        frame_button = tk.Frame(root)
        frame_button.pack(pady=10)

        tk.Button(frame_button, text="Sewa PS", width=15, command=gui_sewa_ps).grid(row=0, column=0, padx=5)
        tk.Button(frame_button, text="Lihat Riwayat", width=15, command=gui_tampilkan_riwayat).grid(row=0, column=1, padx=5)
        tk.Button(frame_button, text="Simpan ke File", width=15, command=gui_simpan_ke_file).grid(row=0, column=2, padx=5)

        # Output Box
        global textbox_output
        textbox_output = tk.Text(root, width=80, height=18)
        textbox_output.pack(pady=10, padx=10)

        root.mainloop()


if __name__ == "__main__":
    if TK_AVAILABLE:
        try:
            build_and_run_gui()
        except Exception:
            print("Error GUI, beralih ke CLI.")
            run_cli()
    else:
        print("Tkinter tidak tersedia. Menjalankan CLI.")
        run_cli()

def cli_tampilkan_riwayat():
    print("\n========= RIWAYAT TRANSAKSI =========")
    
    riwayat = rental.get_riwayat()
    if not riwayat:
        print("Belum ada transaksi.")
        return

    for i, struk in enumerate(riwayat, start=1):
        print(f"\n--- Transaksi {i} ---")
        print(struk)   # MENAMPILKAN STRUK ASLI TANPA DIUBAH

def gui_tampilkan_riwayat():
    riwayat = rental.get_riwayat()
    
    if not riwayat:
        messagebox.showinfo("Info", "Belum ada transaksi.")
        return

    textbox_output.delete(1.0, tk.END)

    for i, struk in enumerate(riwayat, start=1):
        textbox_output.insert(tk.END, f"--- Transaksi {i} ---\n")
        textbox_output.insert(tk.END, struk + "\n")  # TAMPILKAN STRUK ASLI

   