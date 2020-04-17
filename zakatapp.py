# file: zakatapp.py

# Aplikasi Zakat Fitrah, Infaq, dan Shodaqoh
# Masjid Mujahidin - Mergosono Malang
#
# by Klinik Python ID
# website: www.klinikpython-online.com
# start : kamis, 16 april 2020
# finish : -
#

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
import tkinter.filedialog as fd
import os
from PIL import ImageTk, Image
import sqlite3 as lite


class ZakatApp:
	def __init__(self, parent):
		self.parent = parent
		
		self.parent.title(":: ZakatApp - Aplikasi Menghitung Zakat Fitrah, Infaq, Shodaqoh ::")
		
		self.tengah_layar(900, 600)
		self.atur_komponen()
		self.atur_database()
		
		self.form_load()
		
	def tengah_layar(self, panjang, lebar):
		setX = (self.parent.winfo_screenwidth()-panjang)/2
		setY = (self.parent.winfo_screenheight()-lebar-80)/2

		self.parent.geometry("%ix%i+%i+%i"%(panjang, lebar, setX, setY))
		
	def atur_komponen(self):
		frame_utama = tk.Frame(self.parent)
		frame_utama.pack(fill='both', expand=1)
		
		objFrameZakat = FrameZakat(frame_utama)
		
	def atur_database(self):
		pass
		
	def form_load(self):
		pass
		
		
class FrameZakat:
	def __init__(self, frame):
		self.frame = frame
		self.frame.config(bg='yellow')
		
class DatabaseZakat:
	def __init__(self, parent):
		self.parent = parent
		
		
class FungsiZakat:
	def __init__(self, parent):
		self.parent = parent
		
		
		
if __name__ == '__main__':
	root = tk.Tk()
	
	app = ZakatApp(root)
	
	root.mainloop()
