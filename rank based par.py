from tkinter import *



def getPercentile() :

	
	students= int(total_participantField.get())
	
	rank = int(rankField.get())

	
	result = round((students - rank) / students * 100,3);

	
	percentileField.insert(10, str(result)) 
	
	

def Clear():
	
	
	rankField.delete(0, END)
	
	total_participantField.delete(0, END)
	
	percentileField.delete(0, END)
	


if __name__ == "__main__" :

	
	gui = Tk() 
	

	gui.configure(background = "light green") 
	
	
	gui.title("Rank Based- Percentile Calculator") 
	
	
	gui.geometry("650x200") 

	
	rank = Label(gui, text = "Rank", bg = "blue")

	
	andl = Label(gui, text = "And", bg = "blue")
	
	
	total_participant = Label(gui, 
							text = "Total Participants", 
							bg = "blue") 

	 
	find = Button(gui, text = "Find Percentile", 
				fg = "Black", bg = "pink",
				command = getPercentile)
	
	
	percentile = Label(gui, text = "Percentile", bg = "blue") 

	
	 
	clear = Button(gui, text = "Clear",
				fg = "Black", bg = "pink",
				command = Clear) 

	

	
	rank.grid(row = 1, column = 1,padx = 10)

	andl.grid(row = 1, column = 4)
				
	total_participant.grid(row = 1, column = 6, padx = 10)

	 
	find.grid(row = 3, column = 4,pady = 10)
	
	percentile.grid(row = 4, column = 3,padx = 10)
	
	clear.grid(row = 5, column = 4,pady = 10)

	
	rankField = Entry(gui)
	
	total_participantField = Entry(gui)
	
	percentileField = Entry(gui)

 
	rankField.grid(row = 1, column = 2)
	
	total_participantField.grid(row = 1, column = 7)
	
	percentileField.grid(row = 4, column = 4)
	
	
	gui.mainloop() 
