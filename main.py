from cmath import exp
from random import random
from turtle import back
from PIL import Image, ImageTk
import tkinter as tk
from glob import glob
import os
from random import random


class App():
	def __init__(self):
		self.colors = {'dark-brown': "#cb997e", 'brown': "#ddbea9", 'light-brown': "#ffe8d6",
				'light-green': "#b7b7a4", 'green': "#a5a58d", 'dark-green': "#6b705c"}
		
		self.root = tk.Tk()
		self.root.geometry('750x750')
		self.root.resizable(0, 0)
		self.root.title('Mateu - Rock, Paper, Scissors Game')
		
		self.computer_score = 0
		self.user_score = 0
		self.images = glob('images\\*.png')
		self.logos = [ImageTk.PhotoImage(Image.open(self.images[i]).resize((75,75),Image.ANTIALIAS)) for i in range(len(self.images))]
		self.big_logos = [ImageTk.PhotoImage(Image.open(self.images[i]).resize((125,125),Image.ANTIALIAS)) for i in range(len(self.images))]
		self.titles = [os.path.splitext(os.path.basename(self.images[i]))[0].title() for i in range(len(self.images))]
		self.buttons = []

		self.widgets = self.get_widgets()

	def check_result(self, user_choice, computer_choice):
		if user_choice == computer_choice:
			return 'draw'
		elif user_choice == 'Rock' and computer_choice == 'Scissors':
			return 'user'
		elif user_choice == 'Scissors' and computer_choice == 'Rock':
			return 'computer'
		elif user_choice == 'Paper' and computer_choice == 'Rock':
			return 'user'
		elif user_choice == 'Rock' and computer_choice == 'Paper':
			return 'computer'
		elif user_choice == 'Scissors' and computer_choice == 'Paper':
			return 'user'
		elif user_choice == 'Paper' and computer_choice == 'Scissors':
			return 'computer'

	def play(self, value):
		for widget in self.computer_frame.winfo_children():
			if widget._name != '!label':
				widget.destroy()
		
		for widget in self.user_frame.winfo_children():
			if widget._name != '!label':
				widget.destroy()

		random_index = int(random()*len(self.images))
		self.computer_frame = tk.Label(self.computer_frame, background=self.colors['brown'], image=self.big_logos[random_index], text=self.titles[random_index], compound='top')
		self.computer_frame.pack(anchor='center', expand=True)

		self.user_frame = tk.Label(self.user_frame, background=self.colors['brown'], image=self.big_logos[self.titles.index(value)], text=self.titles[self.titles.index(value)], compound='top')
		self.user_frame.pack(anchor='center', expand=True)

		result = self.check_result(user_choice=value, computer_choice=self.titles[random_index])
		if result == 'draw':
			self.bottom_label.config(text="It's a tie, nobody wins")
		elif result == 'computer':
			self.computer_score += 1
			self.computer_label.config(text='Computer: {} points'.format(self.computer_score))
			self.bottom_label.config(text="Computer won :(")
		elif result == 'user':
			self.user_score += 1
			self.user_label.config(text='You: {} points'.format(self.user_score))
			self.bottom_label.config(text='You won! :)')
	
	def get_widgets(self):
		self.contents = tk.Frame(self.root, background=self.colors['light-brown'])
		self.contents.pack(side='top', fill='both', expand=True)
		self.contents.grid_rowconfigure((0,3), weight=1)
		self.contents.grid_columnconfigure((0,2), weight=1)
		self.contents.grid_rowconfigure(2, weight=4)
		
		tk.Label(self.contents, text='Rock Paper Scissors', width=100, height=2, background=self.colors['dark-brown'],
				borderwidth=2, relief='groove', font=('Calibri', 30)).grid(row=0, columnspan=3)


		self.selection_frame = tk.Frame(self.contents, background=self.colors['light-brown'], height=100, borderwidth=2, relief='groove')
		self.selection_frame.grid(row=1, columnspan=3, sticky='nsew')
		self.selection_frame.grid_rowconfigure((0,1), weight=1)
		self.selection_frame.grid_columnconfigure((0,2), weight=1)

		self.user_frame = tk.Frame(self.contents, background=self.colors['light-brown'], height=100, pady=10)
		self.user_frame.grid(row=2, column=0, sticky='nsew')

		self.center_frame = tk.Frame(self.contents, background=self.colors['light-brown'], height=100, pady=10)
		self.center_frame.grid(row=2, column=1, sticky='nsew')

		self.computer_frame = tk.Frame(self.contents, background=self.colors['light-brown'], height=50,pady=10)
		self.computer_frame.grid(row=2, column=2, sticky='nsew')

		tk.Label(self.selection_frame, text='Select one:', width=10, height=1, background=self.colors['brown'], font=('Calibri', 14, 'bold')).grid(row=0, columnspan=3, pady=10)
		self.user_label = tk.Label(self.user_frame, text='You: {} points'.format(self.user_score), width=20, height=2, background=self.colors['brown'], font=('Calibri', 14, 'bold'))
		self.user_label.pack()
		tk.Label(self.center_frame, text='VS', width=10, height=1, background=self.colors['brown'], font=('Calibri', 14, 'bold')).pack(anchor='center', expand=True)
		self.computer_label = tk.Label(self.computer_frame, text='Computer: {} points'.format(self.user_score), width=20, height=2, background=self.colors['brown'], font=('Calibri', 14, 'bold'))
		self.computer_label.pack()

	
		for i in range(len(self.images)):
			self.buttons.append(tk.Button(self.selection_frame, background=self.colors['brown'], text=self.titles[i], image=self.logos[i], compound='top', command=lambda i=i: self.play(self.titles[i])))
			self.buttons[i].grid(row=1, column=i, pady=10)


		self.bottom_label = tk.Label(self.contents, text="Let's Play!", width=100, height=2, background=self.colors['dark-brown'],
				borderwidth=2, relief='groove', font=('Calibri', 30))
		self.bottom_label.grid(row=3, columnspan=3, sticky='w')

root = App().root
root.mainloop()