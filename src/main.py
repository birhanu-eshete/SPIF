import sys
import re
import StringIO
import pyPdf
import os, string, time
from Tkinter import *
import Pmw
#import spif.py
#import phonenumbers
from tkFileDialog   import askopenfilename
# create the root window

class SPIF:
	def __init__(self, parent):

		### 1 -- At the outset, we haven't yet invoked any button handler.
		self.root=parent
		self.filename = ""
		Pmw.initialise()

		self.balloon = Pmw.Balloon(parent)

		

		#Main Menu Bar
		self.menuBar = Pmw.MenuBar(parent, hull_relief=RAISED,  hull_borderwidth=1,balloon=self.balloon)
		self.menuBar.pack(fill=X)
		#File Menu
		self.menuBar.addmenu('File', 'Main Menu')
		self.menuBar.addmenuitem('File', 'command', 'Open File',font=('StingerLight', 14), label='Open',command=self.openFile)
		self.menuBar.addmenuitem('File', 'separator')
		self.menuBar.addmenuitem('File', 'command','Exit the application', label='Exit', command=self.exit)
		#Tool Menu
		self.menuBar.addmenu('Tools', 'Tools Menu')
		self.menuBar.addmenuitem('Tools', 'command','Check', label='Check', command=self.check)
		self.menuBar.addmenuitem('Tools', 'command','Clear Screen', label='Clear Screen', command=self.clear)

		photo = PhotoImage(file = 'logo/logo02.gif')
		label = Label(image=photo,width=800,anchor=E)
		label.image = photo # keep a reference!
		label.place(x=20, y=30)
		label.pack()

		self.fixedFont = Pmw.logicalfont('Fixed')
		self.st = Pmw.ScrolledText(self.root,
			labelpos='n',
			borderframe=1,
			label_text='Check Result',
			usehullsize = 1,
			hull_width = 400,
			hull_height = 300,
			text_wrap='none',
			text_font = self.fixedFont,
			text_padx = 4,text_pady = 4,)
		self.st.configure(text_state = 'normal',)
		self.st.pack(padx = 5, pady = 5, fill = 'both', expand = 1)



		self.messagebar = Pmw.MessageBar(self.root, entry_width=40, entry_relief=GROOVE,
                            labelpos=W, label_text='Status:')
		self.messagebar.pack(side=BOTTOM, fill=X, expand=1, padx=10, pady=10)
		self.messagebar.message("state", "No file loaded.")

		


	
	def openFile(self):
		self.filename = askopenfilename()
		self.messagebar.message("state", "The file ("+self.filename+") loaded sucessfully.")
		print self.filename
	def check(self):
		print self.filename
		if (self.filename == ""):
			self.dialog1 = Pmw.MessageDialog(self.root,title = 'No file selected',defaultbutton = 0,message_text = 'There is no file seleceted!')
		else:
			self.messagebar.message("state", "Checking file ("+self.filename+") .......")
			os.system("python spif.py "+self.filename+" > result.txt")
			self.messagebar.message("state", "The file ("+self.filename+") checked.")
			# Prevent users' modifying text and headers
			self.st.configure(text_state = 'normal',)
			self.st.clear()
			# allow users' modifying text and headers
			self.st.appendtext("Scanning results for the file:("+self.filename+")\n")
			self.st.importfile('result.txt');
			#self.st.appendtext(output)	
			self.st.pack(padx = 5, pady = 5, fill = 'both', expand = 1)
			# Prevent users' modifying text and headers
			self.st.configure(text_state = 'disabled',)
	def clear(self):
		self.st.clear()
			
        
	def exit(self):
		self.root.destroy()


		

		



def main():
	root = Tk()
	#modify the window
	root.title("SPIF - Sensitive and Private Information Filter")
	root.geometry("800x600")
	myApp = SPIF(root)
	root.mainloop()
	

# main
if __name__=='__main__':
	main()
	
