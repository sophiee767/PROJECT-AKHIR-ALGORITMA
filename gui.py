import tkinter as tk
from tkinter import messagebox

from crud import *
from search_sort import *
from structures import *


class TaskGUI:

    def __init__(self, root):

        self.root = root

        root.title("Sistem Manajemen Tugas")
        root.geometry("700x500")

        tk.Label(
            root,
            text="SISTEM MANAJEMEN TUGAS",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        frame_input = tk.Frame(root)
        frame_input.pack(pady=5)

        tk.Label(
            frame_input,
            text="Nama Tugas:"
        ).pack(side=tk.LEFT)

        self.entry_nama = tk.Entry(
            frame_input,
            width=30
        )
        self.entry_nama.pack(side=tk.LEFT, padx=5)

        tk.Label(
            root,
            text="Prioritas"
        ).pack()

        self.prioritas = tk.StringVar()
        self.prioritas.set("Easy")

        frame_prioritas = tk.Frame(root)
        frame_prioritas.pack()

        tk.Radiobutton(
            frame_prioritas,
            text="Easy",
            variable=self.prioritas,
            value="Easy"
        ).pack(side=tk.LEFT)

        tk.Radiobutton(
            frame_prioritas,
            text="Medium",
            variable=self.prioritas,
            value="Medium"
        ).pack(side=tk.LEFT)

        tk.Radiobutton(
            frame_prioritas,
            text="Hard",
            variable=self.prioritas,
            value="Hard"
        ).pack(side=tk.LEFT)

        frame_button = tk.Frame(root)
        frame_button.pack(pady=10)

        tk.Button(
            frame_button,
            text="Tambah Tugas",
            command=self.tambah,
            width=15
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            frame_button,
            text="Hapus Tugas",
            command=self.hapus,
            width=15
        ).pack(side=tk.LEFT, padx=5)

        frame_search = tk.Frame(root)
        frame_search.pack(pady=10)

        tk.Label(
            frame_search,
            text="Cari:"
        ).pack(side=tk.LEFT)

        self.entry_cari = tk.Entry(
            frame_search,
            width=20
        )
        self.entry_cari.pack(side=tk.LEFT, padx=5)

        tk.Button(
            frame_search,
            text="Cari",
            command=self.cari
        ).pack(side=tk.LEFT)

        tk.Button(
            frame_search,
            text="Tandai Selesai",
            command=self.tandai_selesai
        ).pack(side=tk.LEFT, padx=5)

      
        tk.Button(
            root,
            text="Urutkan Prioritas",
            command=self.sort_data,
            width=20
        ).pack(pady=5)

        
        self.listbox = tk.Listbox(
            root,
            width=80,
            height=15
        )

        self.listbox.pack(pady=10)

        self.refresh()

    def refresh(self):

        self.listbox.delete(0, tk.END)

        for i, task in enumerate(tasks):

            self.listbox.insert(
                tk.END,
                f"{i+1}. "
                f"{task['nama']} | "
                f"{task['prioritas']} | "
                f"{task['status']}"
            )

    def tambah(self):

        nama = self.entry_nama.get()

        if nama == "":
            messagebox.showwarning(
                "Peringatan",
                "Nama tugas tidak boleh kosong"
            )
            return

        task = {
            "nama": nama,
            "prioritas": self.prioritas.get(),
            "status": "Belum Selesai"
        }

        tambah_tugas(task)

        task_queue.append(task)

        self.entry_nama.delete(0, tk.END)

        self.refresh()

    def hapus(self):

        try:

            index = self.listbox.curselection()[0]

            deleted_task = hapus_tugas(index)

            deleted_stack.append(deleted_task)

            self.refresh()

        except:

            messagebox.showerror(
                "Error",
                "Pilih tugas terlebih dahulu"
            )

    def cari(self):

        keyword = self.entry_cari.get()

        hasil = cari_tugas(keyword)

        self.listbox.delete(0, tk.END)

        for task in hasil:

            self.listbox.insert(
                tk.END,
                f"{task['nama']} | "
                f"{task['prioritas']} | "
                f"{task['status']}"
            )

    def tandai_selesai(self):

        keyword = self.entry_cari.get()

        for task in tasks:

            if keyword.lower() == task["nama"].lower():

                task["status"] = "Selesai"

                history.add(task["nama"])

                self.refresh()

                messagebox.showinfo(
                    "Berhasil",
                    "Tugas telah diselesaikan"
                )

                return

        messagebox.showerror(
            "Error",
            "Tugas tidak ditemukan"
        )

    def sort_data(self):

        bubble_sort()

        self.refresh()


