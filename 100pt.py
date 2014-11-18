#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.



from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="green")
enemy1 = drawpad.create_rectangle(50,100,70,120, fill='red')
enemy2 = drawpad.create_rectangle(390,250,410,270, fill='red')
enemy3 = drawpad.create_rectangle(780,400,800,420, fill='red')

# Create your "enemies" here, before the class
direction = 5
direction2 = 7
direction3 = -9

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=1)
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    drawpad.pack(side=BOTTOM)
       	    
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text='down', background='green')
       	    self.down.grid(row=2,column=1)
       	    self.down.bind('<Button-1>', self.downClicked)
       	    
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text='left', background='yellow')
       	    self.left.grid(row=1,column=0)
       	    self.left.bind('<Button-1>', self.leftClicked)
       	    
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text='right', background='yellow')
       	    self.right.grid(row=1,column=2)
	    self.right.bind('<Button-1>', self.rightClicked)
	    self.animate()
	
	    
	    	
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	   
	def downClicked(self, event):
	    global oval
	    global player
	    drawpad.move(player,0,20)
	    
	def leftClicked(self, event):
	    global oval
	    global player
	    drawpad.move(player,-20,0)
	    
	def rightClicked(self, event):
	    global oval
	    global player
	    drawpad.move(player, 20, 0)
	    
	def animate(self):
	    global drawpad
	    global player
	    global enemy1
	    global enemy2
	    global enemy3
	    global direction
	    global direction2
	    global direction3
	    
	    x1,y1,x2,y2 = drawpad.coords(enemy1)
	    if x2 > drawpad.winfo_width():
	        direction = -800
	    elif x1 < 0:
	        direction = 5
	        
	    x1,y1,x2,y2 = drawpad.coords(enemy2)
	    if x2 > drawpad.winfo_width():
	        direction2 = -800
	    elif x1 < 0:
	        direction2 = 7
	        
            x1,y1,x2,y2 = drawpad.coords(enemy3)
	    if x1 < 0:
	        direction3 = 800

	    elif x2 > drawpad.winfo_width():
	        direction3 = -9
	    
	    drawpad.move(enemy1,direction,0)
	    drawpad.move(enemy2,direction2,0)
	    drawpad.move(enemy3,direction3,0)
	    
	    
	    
            drawpad.after(10, self.animate)	

		
app = MyApp(root)
root.mainloop()