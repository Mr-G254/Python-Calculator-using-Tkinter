import tkinter as tk
from tkinter import*
from tkinter import ttk

window=Tk()
window.title('Calculator')
window.geometry('387x460+0+0')
window.resizable(False,False)

img=tk.PhotoImage(file='Icon.png')
window.iconphoto(False,img)

def one():
	if entry.get()=='Invalid        ':
		entry.delete(0,END)

	y=entry.get()
	if y.find('=')==0:
		entry.delete(0,END)

	x=len(entry.get())+1
	entry.insert(x,'1')

def two():
	if entry.get()=='Invalid        ':
		entry.delete(0,END)

	y=entry.get()
	if y.find('=')==0:
		entry.delete(0,END)
		
	x=len(entry.get())+1
	entry.insert(x,'2')

def three():
	if entry.get()=='Invalid        ':
		entry.delete(0,END)

	y=entry.get()
	if y.find('=')==0:
		entry.delete(0,END)
		
	x=len(entry.get())+1
	entry.insert(x,'3')

def four():
	if entry.get()=='Invalid        ':
		entry.delete(0,END)
		
	y=entry.get()
	if y.find('=')==0:
		entry.delete(0,END)

	x=len(entry.get())+1
	entry.insert(x,'4')

def five():
	if entry.get()=='Invalid        ':
		entry.delete(0,END)
		
	y=entry.get()
	if y.find('=')==0:
		entry.delete(0,END)

	x=len(entry.get())+1
	entry.insert(x,'5')

def six():
	if entry.get()=='Invalid        ':
		entry.delete(0,END)
		
	y=entry.get()
	if y.find('=')==0:
		entry.delete(0,END)

	x=len(entry.get())+1
	entry.insert(x,'6')

def seven():
	if entry.get()=='Invalid        ':
		entry.delete(0,END)

	y=entry.get()
	if y.find('=')==0:
		entry.delete(0,END)
		
	x=len(entry.get())+1
	entry.insert(x,'7')

def eight():
	if entry.get()=='Invalid        ':
		entry.delete(0,END)
	
	y=entry.get()
	if y.find('=')==0:
		entry.delete(0,END)

	x=len(entry.get())+1
	entry.insert(x,'8')

def nine():
	if entry.get()=='Invalid        ':
		entry.delete(0,END)
	
	y=entry.get()
	if y.find('=')==0:
		entry.delete(0,END)

	x=len(entry.get())+1
	entry.insert(x,'9')

def zero():
	if entry.get()=='Invalid        ':
		entry.delete(0,END)

	y=entry.get()
	if y.find('=')==0:
		entry.delete(0,END)

	x=len(entry.get())+1
	entry.insert(x,'0')

def add():
	if entry.get()=='Invalid        ':
		entry.delete(0,END)
	
	y=entry.get()
	if y.find('=')==0:
		entry.delete(0)

	x=len(entry.get())+1
	entry.insert(x,'+')

def minus():
	if entry.get()=='Invalid        ':
		entry.delete(0,END)
	
	y=entry.get()
	if y.find('=')==0:
		entry.delete(0)

	x=len(entry.get())+1
	entry.insert(x,'-')

def times():
	if entry.get()=='Invalid        ':
		entry.delete(0,END)
		
	y=entry.get()
	if y.find('=')==0:
		entry.delete(0)

	x=len(entry.get())+1
	entry.insert(x,'*')

def divide():
	if entry.get()=='Invalid        ':
		entry.delete(0,END)
	
	y=entry.get()
	if y.find('=')==0:
		entry.delete(0)

	x=len(entry.get())+1
	entry.insert(x,'/')

def C():
	entry.delete(0,END)

def delete():
	x=entry.get()
	if x.find('=')==0:
		entry.delete(0,END)
	else:
		pass

	if entry.get()=='Invalid        ':
		entry.delete(0,END)
	else:
		y=len(x)-1
		entry.delete(y,END)
		
def equals():

	x=entry.get()
	if x.find('=')==0:
		pass
	else:
		if entry.get():
			try:
				y=eval(x)
				v=round(y,5)
				m=str('=')+str(v)
				entry.delete(0,END)
				entry.insert(0,m)
			except:
				entry.delete(0,END)
				entry.insert(0,'Invalid        ')
		else:
			pass

def dot():
	if entry.get()=='Invalid        ':
		entry.delete(0,END)
		
	y=entry.get()
	if y.find('=')==0:
		entry.delete(0)

	x=len(entry.get())+1
	entry.insert(x,'.')

def sum():
	sumbtn.configure(state='disable')
	weightbtn.configure(state='normal')
	sep=ttk.Separator(frame,orient='horizontal')
	sep.place(x=2,y=432,width=100)

	try:
		sep1.destroy()
	except:
		pass

	try:
		frame2.destroy()
	except:
		pass


def wght():
	def main():
		try:
			if bx.get()=='Gigatonne' and bx2.get()=='Gigatonne':
				x=ntry.get()
				ntry2.configure(text=x)
			elif bx.get()=='Gigatonne' and bx2.get()=='Megatonne':
				x=ntry.get()
				try:
					an=int(x) * 1000
				except:
					an=float(x) * 1000

				ntry2.configure(text=an)
			elif bx.get()=='Gigatonne' and bx2.get()=='Tonne':
				x=ntry.get()
				try:
					an=int(x) * 1000000000
				except:
					an=float(x) * 1000000000

				ntry2.configure(text=an)
			elif bx.get()=='Gigatonne' and bx2.get()=='Kilogram':
				x=ntry.get()
				try:
					an=int(x) * 1000000000000
				except:
					an=float(x) * 1000000000000

				ntry2.configure(text=an)
			elif bx.get()=='Gigatonne' and bx2.get()=='Gram':
				x=ntry.get()
				try:
					an=int(x) * 1000000000000000 
				except:
					an=float(x) * 1000000000000000 

				ntry2.configure(text=an)
			elif bx.get()=='Gigatonne' and bx2.get()=='Milligram':
				x=ntry.get()
				try:
					an=int(x) * 1000000000000000000
				except:
					an=float(x) * 1000000000000000000

				ntry2.configure(text=an)
			if bx.get()=='Megatonne' and bx2.get()=='Gigagatonne':
				x=ntry.get()
				try:
					an=int(x) / 1000
				except:
					an=float(x) * 1000

				ntry2.configure(text=an)
			elif bx.get()=='Megatonne' and bx2.get()=='Megatonne':
				x=ntry.get()
				ntry2.configure(text=x)
			elif bx.get()=='Megatonne' and bx2.get()=='Tonne':
				x=ntry.get()
				try:
					an=int(x) * 1000
				except:
					an=float(x) * 1000

				ntry2.configure(text=an)
			elif bx.get()=='Megatonne' and bx2.get()=='Kilogram':
				x=ntry.get()
				try:
					an=int(x) * 1000000
				except:
					an=float(x) * 1000000

				ntry2.configure(text=an)
			elif bx.get()=='Megatonne' and bx2.get()=='Gram':
				x=ntry.get()
				try:
					an=int(x) * 1000000000
				except:
					an=float(x) * 1000000000

				ntry2.configure(text=an)
			elif bx.get()=='Megatonne' and bx2.get()=='Milligram':
				x=ntry.get()
				try:
					an=int(x) * 1000000000000
				except:
					an=float(x) * 1000000000000

				ntry2.configure(text=an)
			elif bx.get()=='Tonne' and bx2.get()=='Gigatonne':
				x=ntry.get()
				try:
					an=int(x) / 1000000000
				except:
					an=float(x) / 1000000000

				ntry2.configure(text=an)
			elif bx.get()=='Tonne' and bx2.get()=='Megatonne':
				x=ntry.get()
				try:
					an=int(x) / 1000000
				except:
					an=float(x) / 1000000

				ntry2.configure(text=an)
			elif bx.get()=='Tonne' and bx2.get()=='Tonne':
				x=ntry.get()
				ntry2.configure(text=x)
			elif bx.get()=='Tonne' and bx2.get()=='Kilogram':
				x=ntry.get()
				try:
					an=int(x) * 1000
				except:
					an=float(x) * 1000

				ntry2.configure(text=an)
			elif bx.get()=='Tonne' and bx2.get()=='Gram':
				x=ntry.get()
				try:
					an=int(x) * 1000000 
				except:
					an=float(x) * 1000000 

				ntry2.configure(text=an)
			elif bx.get()=='Tonne' and bx2.get()=='Milligram':
				x=ntry.get()
				try:
					an=int(x) * 1000000000
				except:
					an=float(x) * 1000000000

				ntry2.configure(text=an)
			elif bx.get()=='Kilogram' and bx2.get()=='Gigatonne':
				x=ntry.get()
				try:
					an=int(x) / 1000000000000
				except:
					an=float(x) / 1000000000000

				ntry2.configure(text=an)
			elif bx.get()=='Kilogram' and bx2.get()=='Megatonne':
				x=ntry.get()
				try:
					an=int(x) / 1000000000
				except:
					an=float(x) / 1000000000

				ntry2.configure(text=an)
			elif bx.get()=='Kilogram' and bx2.get()=='Tonne':
				x=ntry.get()
				try:
					an=int(x) / 1000000000000
				except:
					an=float(x) / 1000000000000

				ntry2.configure(text=an)
			elif bx.get()=='Kilogram' and bx2.get()=='Kilogram':
				x=ntry.get()
				ntry2.configure(text=x)
			elif bx.get()=='Kilogram' and bx2.get()=='Gram':
				x=ntry.get()
				try:
					an=int(x) * 1000
				except:
					an=float(x) * 1000 

				ntry2.configure(text=an)

			elif bx.get()=='Kilogram' and bx2.get()=='Milligram':
				x=ntry.get()
				try:
					an=int(x) * 1000000
				except:
					an=float(x) * 1000000

				ntry2.configure(text=an)
			elif bx.get()=='Milligram' and bx2.get()=='Gigatonne':
				x=ntry.get()
				try:
					an=int(x) / 1000000000000
				except:
					an=float(x) / 1000000000000

				ntry2.configure(text=an)
			elif bx.get()=='Milligram' and bx2.get()=='Megatonne':
				x=ntry.get()
				try:
					an=int(x) / 1000000000000000
				except:
					an=float(x) / 1000000000000000

				ntry2.configure(text=an)
			elif bx.get()=='Milligram' and bx2.get()=='Tonne':
				x=ntry.get()
				try:
					an=int(x) / 1000000000
				except:
					an=float(x) / 1000000000

				ntry2.configure(text=an)
			elif bx.get()=='Milligram' and bx2.get()=='Kilogram':
				x=ntry.get()
				try:
					an=int(x) / 1000000
				except:
					an=float(x) / 1000000

				ntry2.configure(text=an)
			elif bx.get()=='Milligram' and bx2.get()=='Gram':
				x=ntry.get()
				try:
					an=int(x) / 1000
				except:
					an=float(x) / 1000 

				ntry2.configure(text=an)

			elif bx.get()=='Milligram' and bx2.get()=='Milligram':
				x=ntry.get()
				ntry2.configure(text=x)
			elif bx.get()=='Gram' and bx2.get()=='Gigatonne':
				x=ntry.get()
				try:
					an=int(x) / 1000000000000000
				except:
					an=float(x) / 1000000000000000

				ntry2.configure(text=an)
			elif bx.get()=='Gram' and bx2.get()=='Megatonne':
				x=ntry.get()
				try:
					an=int(x) / 1000000000000
				except:
					an=float(x) / 1000000000000

				ntry2.configure(text=an)
			elif bx.get()=='Gram' and bx2.get()=='Tonne':
				x=ntry.get()
				try:
					an=int(x) / 1000000
				except:
					an=float(x) / 1000000

				ntry2.configure(text=an)
			elif bx.get()=='Gram' and bx2.get()=='Kilogram':
				x=ntry.get()
				try:
					an=int(x) / 1000
				except:
					an=float(x) / 1000

				ntry2.configure(text=an)
			elif bx.get()=='Gram' and bx2.get()=='Gram':
				x=ntry.get()
				ntry2.configure(text=x)

			elif bx.get()=='Gram' and bx2.get()=='Milligram':
				x=ntry.get()
				try:
					an=int(x) * 1000
				except:
					an=float(x) * 1000

				ntry2.configure(text=an)
		except:
			ntry.delete(0,END)

	def ans(event):
		if ntry.get()=='':
			ntry2.configure(text='')
		def main():
			try:
				if bx.get()=='Gigatonne' and bx2.get()=='Gigatonne':
					x=ntry.get()
					ntry2.configure(text=x)
				elif bx.get()=='Gigatonne' and bx2.get()=='Megatonne':
					x=ntry.get()
					try:
						an=int(x) * 1000
					except:
						an=float(x) * 1000

					ntry2.configure(text=an)
				elif bx.get()=='Gigatonne' and bx2.get()=='Tonne':
					x=ntry.get()
					try:
						an=int(x) * 1000000000
					except:
						an=float(x) * 1000000000

					ntry2.configure(text=an)
				elif bx.get()=='Gigatonne' and bx2.get()=='Kilogram':
					x=ntry.get()
					try:
						an=int(x) * 1000000000000
					except:
						an=float(x) * 1000000000000

					ntry2.configure(text=an)
				elif bx.get()=='Gigatonne' and bx2.get()=='Gram':
					x=ntry.get()
					try:
						an=int(x) * 1000000000000000 
					except:
						an=float(x) * 1000000000000000 

					ntry2.configure(text=an)
				elif bx.get()=='Gigatonne' and bx2.get()=='Milligram':
					x=ntry.get()
					try:
						an=int(x) * 1000000000000000000
					except:
						an=float(x) * 1000000000000000000

					ntry2.configure(text=an)
				if bx.get()=='Megatonne' and bx2.get()=='Gigagatonne':
					x=ntry.get()
					try:
						an=int(x) / 1000
					except:
						an=float(x) * 1000

					ntry2.configure(text=an)
				elif bx.get()=='Megatonne' and bx2.get()=='Megatonne':
					x=ntry.get()
					ntry2.configure(text=x)
				elif bx.get()=='Megatonne' and bx2.get()=='Tonne':
					x=ntry.get()
					try:
						an=int(x) * 1000
					except:
						an=float(x) * 1000

					ntry2.configure(text=an)
				elif bx.get()=='Megatonne' and bx2.get()=='Kilogram':
					x=ntry.get()
					try:
						an=int(x) * 1000000
					except:
						an=float(x) * 1000000

					ntry2.configure(text=an)
				elif bx.get()=='Megatonne' and bx2.get()=='Gram':
					x=ntry.get()
					try:
						an=int(x) * 1000000000
					except:
						an=float(x) * 1000000000

					ntry2.configure(text=an)
				elif bx.get()=='Megatonne' and bx2.get()=='Milligram':
					x=ntry.get()
					try:
						an=int(x) * 1000000000000
					except:
						an=float(x) * 1000000000000

					ntry2.configure(text=an)
				elif bx.get()=='Tonne' and bx2.get()=='Gigatonne':
					x=ntry.get()
					try:
						an=int(x) / 1000000000
					except:
						an=float(x) / 1000000000

					ntry2.configure(text=an)
				elif bx.get()=='Tonne' and bx2.get()=='Megatonne':
					x=ntry.get()
					try:
						an=int(x) / 1000000
					except:
						an=float(x) / 1000000

					ntry2.configure(text=an)
				elif bx.get()=='Tonne' and bx2.get()=='Tonne':
					x=ntry.get()
					ntry2.configure(text=x)
				elif bx.get()=='Tonne' and bx2.get()=='Kilogram':
					x=ntry.get()
					try:
						an=int(x) * 1000
					except:
						an=float(x) * 1000

					ntry2.configure(text=an)
				elif bx.get()=='Tonne' and bx2.get()=='Gram':
					x=ntry.get()
					try:
						an=int(x) * 1000000 
					except:
						an=float(x) * 1000000 

					ntry2.configure(text=an)
				elif bx.get()=='Tonne' and bx2.get()=='Milligram':
					x=ntry.get()
					try:
						an=int(x) * 1000000000
					except:
						an=float(x) * 1000000000

					ntry2.configure(text=an)
				elif bx.get()=='Kilogram' and bx2.get()=='Gigatonne':
					x=ntry.get()
					try:
						an=int(x) / 1000000000000
					except:
						an=float(x) / 1000000000000

					ntry2.configure(text=an)
				elif bx.get()=='Kilogram' and bx2.get()=='Megatonne':
					x=ntry.get()
					try:
						an=int(x) / 1000000000
					except:
						an=float(x) / 1000000000

					ntry2.configure(text=an)
				elif bx.get()=='Kilogram' and bx2.get()=='Tonne':
					x=ntry.get()
					try:
						an=int(x) / 1000000000000
					except:
						an=float(x) / 1000000000000

					ntry2.configure(text=an)
				elif bx.get()=='Kilogram' and bx2.get()=='Kilogram':
					x=ntry.get()
					ntry2.configure(text=x)
				elif bx.get()=='Kilogram' and bx2.get()=='Gram':
					x=ntry.get()
					try:
						an=int(x) * 1000
					except:
						an=float(x) * 1000 

					ntry2.configure(text=an)

				elif bx.get()=='Kilogram' and bx2.get()=='Milligram':
					x=ntry.get()
					try:
						an=int(x) * 1000000
					except:
						an=float(x) * 1000000

					ntry2.configure(text=an)
				elif bx.get()=='Milligram' and bx2.get()=='Gigatonne':
					x=ntry.get()
					try:
						an=int(x) / 1000000000000
					except:
						an=float(x) / 1000000000000

					ntry2.configure(text=an)
				elif bx.get()=='Milligram' and bx2.get()=='Megatonne':
					x=ntry.get()
					try:
						an=int(x) / 1000000000000000
					except:
						an=float(x) / 1000000000000000

					ntry2.configure(text=an)
				elif bx.get()=='Milligram' and bx2.get()=='Tonne':
					x=ntry.get()
					try:
						an=int(x) / 1000000000
					except:
						an=float(x) / 1000000000

					ntry2.configure(text=an)
				elif bx.get()=='Milligram' and bx2.get()=='Kilogram':
					x=ntry.get()
					try:
						an=int(x) / 1000000
					except:
						an=float(x) / 1000000

					ntry2.configure(text=an)
				elif bx.get()=='Milligram' and bx2.get()=='Gram':
					x=ntry.get()
					try:
						an=int(x) / 1000
					except:
						an=float(x) / 1000 

					ntry2.configure(text=an)

				elif bx.get()=='Milligram' and bx2.get()=='Milligram':
					x=ntry.get()
					ntry2.configure(text=x)
				elif bx.get()=='Gram' and bx2.get()=='Gigatonne':
					x=ntry.get()
					try:
						an=int(x) / 1000000000000000
					except:
						an=float(x) / 1000000000000000

					ntry2.configure(text=an)
				elif bx.get()=='Gram' and bx2.get()=='Megatonne':
					x=ntry.get()
					try:
						an=int(x) / 1000000000000
					except:
						an=float(x) / 1000000000000

					ntry2.configure(text=an)
				elif bx.get()=='Gram' and bx2.get()=='Tonne':
					x=ntry.get()
					try:
						an=int(x) / 1000000
					except:
						an=float(x) / 1000000

					ntry2.configure(text=an)
				elif bx.get()=='Gram' and bx2.get()=='Kilogram':
					x=ntry.get()
					try:
						an=int(x) / 1000
					except:
						an=float(x) / 1000

					ntry2.configure(text=an)
				elif bx.get()=='Gram' and bx2.get()=='Gram':
					x=ntry.get()
					ntry2.configure(text=x)

				elif bx.get()=='Gram' and bx2.get()=='Milligram':
					x=ntry.get()
					try:
						an=int(x) * 1000
					except:
						an=float(x) * 1000

					ntry2.configure(text=an)
			except:
				ntry.delete(0,END)

		window.after(100,main)

	def one():
		x=len(ntry.get())+1
		ntry.insert(x,'1')
		window.after(10,main)

	def two():
		x=len(ntry.get())+1
		ntry.insert(x,'2')
		window.after(20,main)

	def three():
		x=len(ntry.get())+1
		ntry.insert(x,'3')
		window.after(10,main)

	def four():
		x=len(ntry.get())+1
		ntry.insert(x,'4')
		window.after(10,main)

	def five():
		x=len(ntry.get())+1
		ntry.insert(x,'5')
		window.after(10,main)

	def six():
		x=len(ntry.get())+1
		ntry.insert(x,'6')
		window.after(10,main)

	def seven():
		x=len(ntry.get())+1
		ntry.insert(x,'7')
		window.after(10,main)

	def eight():
		x=len(ntry.get())+1
		ntry.insert(x,'8')
		window.after(10,main)

	def nine():
		x=len(ntry.get())+1
		ntry.insert(x,'9')
		window.after(10,main)

	def zero():
		x=len(ntry.get())+1
		ntry.insert(x,'0')

	def Dot():
		x=len(ntry.get())+1
		ntry.insert(x,'.')

	def C():
		ntry.delete(0,END)
		ntry2.configure(text='')

	def trial(event):
		if bx.get()=='Gigatonne':
			Units.configure(text='Gt')
		elif bx.get()=='Megatonne':
			Units.configure(text='Mt')
		elif bx.get()=='Tonne':
			Units.configure(text='t')
		elif bx.get()=='Kilogram':
			Units.configure(text='kg')
		elif bx.get()=='Gram':
			Units.configure(text='g')
		elif bx.get()=='Milligram':
			Units.configure(text='mg')

	def trial2(event):
		if bx2.get()=='Gigatonne':
			Units2.configure(text='Gt')
		elif bx2.get()=='Megatonne':
			Units2.configure(text='Mt')
		elif bx2.get()=='Tonne':
			Units2.configure(text='t')
		elif bx2.get()=='Kilogram':
			Units2.configure(text='kg')
		elif bx2.get()=='Gram':
			Units2.configure(text='g')
		elif bx2.get()=='Milligram':
			Units2.configure(text='mg')

	sumbtn.configure(state='normal')
	weightbtn.configure(state='disable')

	try:
		frame3.destroy()
	except:
		pass

	global frame2
	frame2=Frame(window,bg='#3D3C3A',height=434,width=387)
	frame2.place(x=0,y=0)

	global sep1
	sep1=ttk.Separator(frame2,orient='horizontal')
	sep1.place(x=102,y=432,width=100)

	frame2b=Frame(frame2,bg='black',height=229,width=75)
	frame2b.place(x=310,y=201)

	global Units
	Units=Label(frame2,bg='#3D3C3A',font=('Times',20))
	Units.place(x=351,y=10)

	bx=ttk.Combobox(frame2,width=6,state='readonly',font=('Times',15),values=['Gigatonne','Megatonne','Tonne','Kilogram','Gram','Milligram'])
	bx.current([2])
	Units.configure(text='t')
	bx.bind("<<ComboboxSelected>>",trial)
	bx.place(x=10,y=10,width=170,height=30)


	ntry=Entry(frame2,bg='#343232',font=('Times',20),bd=0)
	ntry.bind('<KeyPress>',ans)
	ntry.place(x=200,y=10,width=150,height=30)

	global Units2
	Units2=Label(frame2,bg='#3D3C3A',font=('Times',20))
	Units2.place(x=351,y=110)

	bx2=ttk.Combobox(frame2,width=6,state='readonly',font=('Times',15),values=['Gigatonne','Megatonne','Tonne','Kilogram','Gram','Milligram'])
	bx2.current([3])
	Units2.configure(text='kg')
	bx2.bind("<<ComboboxSelected>>",trial2)
	bx2.place(x=10,y=110,width=170,height=30)

	ntry2=Label(frame2,bg='#343232',font=('Times',20),bd=0,)
	ntry2.place(x=200,y=110,width=150,height=30)

	btn1=Button(frame2,text='1',bg='#343232',bd=0,font=('Times',35),command=one)
	btn1.place(x=2,y=201,height=75,width=75)

	btn2=Button(frame2,text='2',bg='#343232',bd=0,font=('Times',35),command=two)
	btn2.place(x=79,y=201,height=75,width=75)

	btn3=Button(frame2,text='3',bg='#343232',bd=0,font=('Times',35),command=three)
	btn3.place(x=156,y=201,height=75,width=75)

	btn4=Button(frame2,text='4',bg='#343232',bd=0,font=('Times',35),command=four)
	btn4.place(x=2,y=278,height=75,width=75)

	btn5=Button(frame2,text='5',bg='#343232',bd=0,font=('Times',35),command=five)
	btn5.place(x=79,y=278,height=75,width=75)

	btn6=Button(frame2,text='6',bg='#343232',bd=0,font=('Times',35),command=six)
	btn6.place(x=156,y=278,height=75,width=75)

	btn7=Button(frame2,text='7',bg='#343232',bd=0,font=('Times',35),command=seven)
	btn7.place(x=2,y=355,height=75,width=75)

	btn8=Button(frame2,text='8',bg='#343232',bd=0,font=('Times',35),command=eight)
	btn8.place(x=79,y=355,height=75,width=75)

	btn9=Button(frame2,text='9',bg='#343232',bd=0,font=('Times',35),command=nine)
	btn9.place(x=156,y=355,height=75,width=75)

	btn0=Button(frame2,text='0',bg='#343232',bd=0,font=('Times',35),command=zero)
	btn0.place(x=233,y=355,height=75,width=75)

	dotbtn=Button(frame2,text='.',bg='#343232',bd=0,font=('Times',25),command=Dot)
	dotbtn.place(x=233,y=278,height=75,width=75)

	cbtn=Button(frame2,text='C',bg='#343232',bd=0,font=('Times',25),command=C)
	cbtn.place(x=233,y=201,height=75,width=75)

frame=Frame(window,bg='#3D3C3A',height=460,width=387)
frame.place(x=0,y=0)

entry=Entry(frame,bg='#343232',bd=0,font=('Times Bold',40),justify=tk.RIGHT)
entry.place(x=2,y=2,height=120,width=383)

btn1=Button(frame,text='1',bg='#343232',bd=0,font=('Times',35),command=one)
btn1.place(x=2,y=124,height=75,width=75)

btn2=Button(frame,text='2',bg='#343232',bd=0,font=('Times',35),command=two)
btn2.place(x=79,y=124,height=75,width=75)

btn3=Button(frame,text='3',bg='#343232',bd=0,font=('Times',35),command=three)
btn3.place(x=156,y=124,height=75,width=75)

btn4=Button(frame,text='4',bg='#343232',bd=0,font=('Times',35),command=four)
btn4.place(x=2,y=201,height=75,width=75)

btn5=Button(frame,text='5',bg='#343232',bd=0,font=('Times',35),command=five)
btn5.place(x=79,y=201,height=75,width=75)

btn6=Button(frame,text='6',bg='#343232',bd=0,font=('Times',35),command=six)
btn6.place(x=156,y=201,height=75,width=75)

btn7=Button(frame,text='7',bg='#343232',bd=0,font=('Times',35),command=seven)
btn7.place(x=2,y=278,height=75,width=75)

btn8=Button(frame,text='8',bg='#343232',bd=0,font=('Times',35),command=eight)
btn8.place(x=79,y=278,height=75,width=75)

btn9=Button(frame,text='9',bg='#343232',bd=0,font=('Times',35),command=nine)
btn9.place(x=156,y=278,height=75,width=75)

btn0=Button(frame,text='0',bg='#343232',bd=0,font=('Times',35),command=zero)
btn0.place(x=79,y=355,height=75,width=75)

btnplus=Button(frame,text='+',bg='#343232',bd=0,font=('Times',25),command=add)
btnplus.place(x=2,y=355,height=75,width=75)

btnminus=Button(frame,text='-',bg='#343232',bd=0,font=('Times',25),command=minus)
btnminus.place(x=156,y=355,height=75,width=75)

dellbtn=Button(frame,text='Del',bg='#343232',bd=0,font=('Times',20),command=delete)
dellbtn.place(x=233,y=124,height=75,width=75)

timesbtn=Button(frame,text='x',bg='#343232',bd=0,font=('Times',20),command=times)
timesbtn.place(x=233,y=201,height=113,width=75)

dividebtn=Button(frame,text='/',bg='#343232',bd=0,font=('Times',20),command=divide)
dividebtn.place(x=233,y=316,height=114,width=75)

cbtn=Button(frame,text='C',bg='#343232',bd=0,font=('Times',25),command=C)
cbtn.place(x=310,y=124,height=113,width=75)

eqbtn=Button(frame,text='=',bg='#343232',bd=0,font=('Times',25),command=equals)
eqbtn.place(x=310,y=239,height=113,width=75)

dotbtn=Button(frame,text='.',bg='#343232',bd=0,font=('Times',25),command=dot)
dotbtn.place(x=310,y=355,height=75,width=75)

sep=ttk.Separator(frame,orient='horizontal')
sep.place(x=2,y=432,width=100)

sumbtn=Button(frame,text='Sum',bg='#343232',bd=0,font=('Times',13),fg='#1B1212',state='disable',command=sum)
sumbtn.place(x=2,y=434,height=24,width=100)

weightbtn=Button(frame,text='Weight',bg='#343232',bd=0,font=('Times',13),fg='#1B1212',command=wght)
weightbtn.place(x=102,y=434,height=24,width=100)

label=Label(frame,bg='#343232')
label.place(x=202,y=434,height=24,width=183)

window.mainloop()
