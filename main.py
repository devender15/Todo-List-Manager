from tkinter import *
import tkinter.messagebox as tmsg

def done():
	global lstbox
	global tasks_array

	try:
		# finding the selected element from the listbox
		s = lstbox.curselection()
		idx = s[0]
		val = lstbox.get(idx)
		# if any task is done, then it has to be removed from the task array
		tasks_array.remove(val)
		lstbox.delete(ACTIVE)

	except Exception as e:
		tmsg.showerror("Error!", "List is Empty !")

	# if the complete task-list is deleted then .txt file will also be cleared
	if(len(tasks_array)==0):
		with open("list.txt", "w") as f:
			f.write("")

def exit():
	global root
	root.destroy()

index = 0
def add_task():
	global add_var
	global lstbox
	global index
	global tasks_list
	global tasks_array

	if(not add_var.get()):
		tmsg.showerror("Empty!", "Please write some tasks first !")

	else:	
		# appending the new task in the older array which already has previous unfinished tasks
		tasks_array.append(add_var.get())
	
		with open("list.txt", "w") as f:
			for i in tasks_array:
				f.write(f"{i},")
		
		lstbox.insert(index, f"{add_var.get()}\n")
		index += 1
		add_var.set(" ")


def window():
	global root

	root = Tk()
	root.title("To-do List")
	root.geometry("500x550")
	root.resizable(0,0)


	# creating main frames
	header_frame = Frame(root, bg='yellow', height=120, relief=SUNKEN)
	header_frame.pack(fill=X)

	list_box_frame = Frame(root, bg='green', height=280, relief=SUNKEN)
	list_box_frame.pack(fill=X)

	footer_frame = Frame(root, bg='blue', height=150, relief=SUNKEN)
	footer_frame.pack(fill=X)

	# customizing header frame
	Label(header_frame, text='Todo List', bg='yellow',  font='Corbel 25 bold', pady=15).pack()

	global add_var
	add_var = StringVar()

	Entry(header_frame, textvar=add_var, justify='center', bd=2, font='lucida 20 bold').pack(pady=4)

	Button(header_frame, text='Add', bg='pink', width=20, command=add_task).pack()


	# customizing out list_box frame
	global lstbox
	global tasks_list
	global tasks_array

	# making this empty task-array that will contain all the tasks name  
	tasks_array = []

	# reading list.txt file for making our array to be filled with some data
	with open("list.txt", "r") as f:
		tasks = f.read()
		# making another list that will take elements by separating the content of the list.txt file with a comma
		tasks_list = tasks.split(",")
		tasks_array.extend(tasks_list)

	lstbox = Listbox(list_box_frame, height=20, width=100, justify=CENTER, font='Corbel 10 bold')
	lstbox.pack()

	for task in tasks_list:
		lstbox.insert(0, task)

	# customizing footer_frame
	done_btn = Button(footer_frame, text='Done', bg='green', fg='yellow', font='Corbel 15 bold', width=20, command=done)
	done_btn.grid(column=0, row=0)

	Button(footer_frame, text='Exit', bg='red', fg='white', font='Corbel 15 bold', width=21, command=exit, padx=20).grid(column=2, row=0)
	
	root.mainloop()

if __name__ == '__main__':
	window()