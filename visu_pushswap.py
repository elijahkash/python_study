#!/usr/bin/env python3

# visualizer for push-swap project

import random as rand
import time
import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
import ttk
import collections as coll

# TODO: depend from display?
DEFAULT_WIN_SIZE_X = 1000
DEFAULT_WIN_SIZE_Y = 1030
WIN_TITLE = 'visualizer for push-swap'
DEFAULT_RANGE_A = 0
DEFAULT_RANGE_B = 100

STICKY_FULL = {'sticky': (tk.W, tk.E, tk.N, tk.S)}


class PushSwapStacks:
	"""
	describe stacks for push-swap algorith
	"""

	def __init__(self):
		""" initstate: Iterable[_T]=..."""
		self.stack_a = coll.deque()
		self.stack_b = coll.deque()
		self.cmd = {
			'pa': self.pa,
			'pb': self.pa,
			'sa': self.pa,
			'sb': self.pa,
			'ss': self.pa,
			'ra': self.pa,
			'rb': self.pa,
			'rr': self.pa,
			'rra': self.pa,
			'rrb': self.pa,
			'rrr': self.pa
		}

	def new_data(self, initstate):
		self.stack_a.clear()
		self.stack_b.clear()
		self.stack_a.extend(initstate)

	def pa(self):
		if len(self.stack_b):
			self.stack_b.appendleft(self.stack_b.popleft())

	def pb(self):
		if len(self.stack_a):
			self.stack_b.appendlenf(self.stack_a.popleft())

	def ra(self):
		if len(self.stack_a):
			self.stack_a.rotate()

	def rb(self):
		if len(self.stack_b):
			self.stack_b.rotate()

	def rr(self):
		self.ra()
		self.rb()

	def rra(self):
		if len(self.stack_a):
			self.stack_a.rotate(-1)

	def rrb(self):
		if len(self.stack_b):
			self.stack_b.rotate(-1)

	def rrr(self):
		self.rra()
		self.rrb()

	def sa(self):
		self.stack_a[0], self.stack_a[1] = self.stack_a[1], self.stack_a[0]

	def sb(self):
		self.stack_b[0], self.stack_b[1] = self.stack_b[1], self.stack_b[0]

	def ss(self):
		self.sa()
		self.sb()


class GameInfo:
	def __init__(self):
		self.src_data = []
		self.st = PushSwapStacks()
		self.op_list = []
		self.cur_op = 0
		self.speed = 1
		self.op_count = 0
		self.stack_state = 'OK'
		self.use_builtin = tk.IntVar()
		self.use_builtin.set(1)


class VisuPS(ttk.Frame):
	def __init__(self, root):
		super().__init__(master=root, padding="5 2 5 2")
		# root.wm_resizable(False, False)
		root.geometry(f'{DEFAULT_WIN_SIZE_X}x{DEFAULT_WIN_SIZE_Y}+0+0')
		root.title(WIN_TITLE)
		root.columnconfigure(0, weight=1)
		root.rowconfigure(0, weight=1)
		self.root = root
		self.style = ttk.Style()
		self.style.theme_use('aqua')
		self.grid(sticky=(tk.N, tk.W, tk.E, tk.S))
		self.game_info = GameInfo()
		self.__initUI()

	def __initUI(self):
		self.canvas_a = tk.Canvas(self)
		self.canvas_b = tk.Canvas(self)
# TODO: block user unput
		self.cmd_list = scrolledtext.ScrolledText(self, width=5)
		self.menu_frame = ttk.Frame(self)
		self.quit_button = ttk.Button(
			self.menu_frame, text='Quit', command=self.visu_exit
		)
		self.start_button = ttk.Button(
			self.menu_frame, text='Start', command=self.start
		)
		self.speed_down_button = ttk.Button(
			self.menu_frame, text='<<', command=self.temp_pass
		)
		self.speed_pause_button = ttk.Button(
			self.menu_frame, text='▷', command=self.temp_pass
		)
		self.speed_up_button = ttk.Button(
			self.menu_frame, text='>>', command=self.temp_pass
		)
		self.reset_button = ttk.Button(
			self.menu_frame, text='Reset', command=self.temp_pass
		)
		self.generate_new_data_button = ttk.Button(
			self.menu_frame, text='Generate new [a, b)', command=self.temp_pass
		)
		self.entry_range_a = ttk.Entry(self.menu_frame, width=10)
		self.entry_range_a.insert(0, str(DEFAULT_RANGE_A))
		self.entry_range_b = ttk.Entry(self.menu_frame, width=10)
		self.entry_range_b.insert(0, str(DEFAULT_RANGE_B))
		self.entry_range_a_label = ttk.Label(self.menu_frame, text='<- input a')
		self.entry_range_b_label = ttk.Label(self.menu_frame, text='<- input b')
# TODO: here!
		# self.init_var = tk.IntVar(self.root)
		# self.init_var.set(1)
		self.use_builtin = ttk.Checkbutton(
			self.menu_frame, text='use built-in algo',
			command=self.builtin_click, variable=self.game_info.use_builtin
		)
		self.input_file_name = ttk.Label(
			self.menu_frame, text='Custom push_swap:'
		)
		self.push_swap_file_name = ttk.Entry(
			self.menu_frame, width=30, state=tk.DISABLED
		)
		self.open_file = ttk.Button(
			self.menu_frame, text='choose file ...', command=self.choose_file,
			state=tk.DISABLED
		)
		self.op_num = ttk.Label(
			self.menu_frame,
			text=f'operations count = {self.game_info.op_count}'
		)
		self.stack_state = ttk.Label(self.menu_frame, text=f'stack state:  ')
		self.powered_by = ttk.Label(
			self.menu_frame, text='powered by Ilya Kashnitkiy', anchor=tk.CENTER
		)
		self.git_link = ttk.Label(
			self.menu_frame, text='github.com/elijahkash', anchor=tk.CENTER
		)

		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=20)
		self.columnconfigure(2, weight=20)
		self.columnconfigure(3, weight=1)

		self.canvas_a.grid(column=1, row=0, pady=4, padx=2, **STICKY_FULL)
		self.canvas_b.grid(column=2, row=0, pady=4, padx=2, **STICKY_FULL)
		self.cmd_list.grid(column=3, row=0, pady=4, **STICKY_FULL)
		self.menu_frame.grid(column=0, row=0, pady=4, padx=4, **STICKY_FULL)

		for i in range(0, 3):
			self.menu_frame.columnconfigure(i, weight=1)
		for i in range(0, 90):
			self.menu_frame.rowconfigure(i, weight=1)

		self.quit_button.grid(row=0, columnspan=3, **STICKY_FULL)
		self.start_button.grid(row=1, columnspan=3, **STICKY_FULL)
		self.speed_down_button.grid(row=2, column=0, **STICKY_FULL)
		self.speed_pause_button.grid(row=2, column=1, **STICKY_FULL)
		self.speed_up_button.grid(row=2, column=2, **STICKY_FULL)
		self.reset_button.grid(row=3, columnspan=3, **STICKY_FULL)
		self.generate_new_data_button.grid(row=4, columnspan=3, **STICKY_FULL)
		self.entry_range_a.grid(row=5, column=0)
		self.entry_range_b.grid(row=6, column=0)
		self.entry_range_a_label.grid(row=5, column=2, **STICKY_FULL)
		self.entry_range_b_label.grid(row=6, column=2, **STICKY_FULL)
		self.use_builtin.grid(row=7, columnspan=3, **STICKY_FULL)
		self.input_file_name.grid(row=8, columnspan=3, **STICKY_FULL)
		self.push_swap_file_name.grid(
			in_=self.menu_frame, row=9, columnspan=3, **STICKY_FULL
		)
		self.open_file.grid(row=8, column=2, **STICKY_FULL)
		self.powered_by.grid(row=40, column=0, columnspan=3, **STICKY_FULL)
		self.git_link.grid(row=41, column=0, columnspan=3, **STICKY_FULL)
		self.op_num.grid(row=13, column=0, columnspan=3, **STICKY_FULL)
		self.stack_state.grid(row=14, column=0, columnspan=3, **STICKY_FULL)

	def visu_exit(self):
		tk.Tk.quit(self.root)

	def temp_pass(self):
		print("pass")
		pass

	def choose_file(self):
		tmp = filedialog.askopenfilename()
		self.push_swap_file_name.delete(0, tk.END)
		self.push_swap_file_name.insert(0, tmp)

	def builtin_click(self):
		if self.game_info.use_builtin.get():
			self.open_file.config(state=tk.DISABLED)
			self.push_swap_file_name.config(state=tk.DISABLED)
		else:
			self.open_file.config(state=tk.NORMAL)
			self.push_swap_file_name.config(state=tk.NORMAL)

	def start(self):
		pass


def main():
	rand.seed(time.time())
	visu = VisuPS(tk.Tk())
	visu.root.mainloop()


if __name__ == '__main__':
	exit(main())
