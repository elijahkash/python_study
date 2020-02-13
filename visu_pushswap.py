#!/usr/bin/env python3

# visualizer for push-swap project

import random as rand
import time
import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
import ttk
import collections as coll

DEFAULT_WIN_SIZE_X = 1000
DEFAULT_WIN_SIZE_Y = 1000
WIN_TITLE = 'visu'
DEFAULT_RANGE_A = 0
DEFAULT_RANGE_B = 100


class StackPS:
	"""
	describe stacks for push-swap algorith
	"""

	def __init__(self, initstate):
		""" initstate: Iterable[_T]=..."""
		self.stack_a = coll.deque(initstate, len(initstate))
		self.stack_b = coll.deque(maxlen=len(initstate))


class VisuPS(ttk.Frame):
	def __init__(self, root):
		super().__init__(master=root, padding="5 2 5 2")
		root.wm_resizable(False, False)
		root.geometry(f'{DEFAULT_WIN_SIZE_X}x{DEFAULT_WIN_SIZE_Y}+0+0')
		root.title(WIN_TITLE)
		root.columnconfigure(0, weight=1)
		root.rowconfigure(0, weight=1)
		self.root = root
		self.style = ttk.Style()
		self.style.theme_use('aqua')
		self.grid(sticky=(tk.N, tk.W, tk.E, tk.S))
		self.initUI()

	def initUI(self):
		STICKY_FULL = (tk.W, tk.E, tk.N, tk.S)

		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=20)
		self.columnconfigure(2, weight=20)
		self.columnconfigure(3, weight=1)

		self.stack_a = tk.Canvas(self, width=15)
		self.stack_a.grid(column=1, row=0, pady=4, padx=2, sticky=STICKY_FULL)
		self.stack_b = tk.Canvas(self, width=15)
		self.stack_b.grid(column=2, row=0, pady=4, padx=2, sticky=STICKY_FULL)
		self.cmd_list = scrolledtext.ScrolledText(self, width=5)
		self.cmd_list.grid(column=3, row=0, pady=4, sticky=STICKY_FULL)

		self.menu_frame = ttk.Frame(self)
		self.menu_frame.grid(
			column=0, row=0, pady=4, padx=4, sticky=STICKY_FULL)
		for i in range(0, 3):
			self.menu_frame.columnconfigure(i, weight=1)
		self.quit_button = ttk.Button(
			self.menu_frame, text='Quit', command=self.visu_exit)
		self.quit_button.grid(row=0, columnspan=3, sticky=STICKY_FULL)
		self.start_button = ttk.Button(
			self.menu_frame, text='Start', command=self.start)
		self.start_button.grid(row=1, columnspan=3, sticky=STICKY_FULL)
		self.speed_down = ttk.Button(
			self.menu_frame, text='<<', command=self.temp_pass)
		self.speed_down.grid(row=2, column=0, sticky=STICKY_FULL)
		self.speed_pause = ttk.Button(
			self.menu_frame, text='||', command=self.temp_pass)
		self.speed_pause.grid(row=2, column=1, sticky=STICKY_FULL)
		self.speed_up = ttk.Button(
			self.menu_frame, text='>>', command=self.temp_pass)
		self.speed_up.grid(row=2, column=2, sticky=STICKY_FULL)
		self.reset_button = ttk.Button(
			self.menu_frame, text='Reset', command=self.temp_pass)
		self.reset_button.grid(row=3, columnspan=3, sticky=STICKY_FULL)
		self.generate_new_data = ttk.Button(
			self.menu_frame, text='Generate new [a, b)', command=self.temp_pass)
		self.generate_new_data.grid(row=4, columnspan=3, sticky=STICKY_FULL)
		self.input_a = ttk.Entry(self.menu_frame, width=10)
		self.input_a.insert(0, str(DEFAULT_RANGE_A))
		self.input_a.grid(row=5, column=0)
		self.input_b = ttk.Entry(self.menu_frame, width=10)
		self.input_b.insert(0, str(DEFAULT_RANGE_B))
		self.input_b.grid(row=6, column=0)
		self.input_a_label = ttk.Label(self.menu_frame, text='<- input a')
		self.input_a_label.grid(row=5, column=2, sticky=STICKY_FULL)
		self.input_b_label = ttk.Label(self.menu_frame, text='<- input b')
		self.input_b_label.grid(row=6, column=2, sticky=STICKY_FULL)
		self.init_var = tk.IntVar(self.root)
		self.init_var.set(1)
		self.use_builtin = ttk.Checkbutton(
			self.menu_frame, text='use built-in algo',
			command=self.temp_pass, variable=self.init_var)
		self.use_builtin.grid(row=7, columnspan=3, sticky=STICKY_FULL)
		self.input_file_name = ttk.Label(self.menu_frame, text='Custom push_swap:')
		self.input_file_name.grid(row=8, columnspan=3, sticky=STICKY_FULL)
		self.push_swap_file_name = ttk.Entry(self.menu_frame, width=30)
		# self.file = filedialog.askopenfilename()
		self.push_swap_file_name.grid(
			in_=self.menu_frame, row=9, columnspan=3, sticky=STICKY_FULL)

	def visu_exit(self):
		tk.Tk.quit(self.root)

	def temp_pass(self):
		print("pass")
		pass

	def start(self):
		pass


def main():
	rand.seed(time.time())
	root = tk.Tk()
	visu = VisuPS(root)
	visu.root.mainloop()


if __name__ == '__main__':
	exit(main())
