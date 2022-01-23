# pass generator using Tkinter

from tkinter import *
from random import randint

root = Tk()



# window title

root.title('Password Generator')

# window size
root.geometry("600x400")

# Generate Random Strong Password
def new_rand():
	# Clear Our Entry Box
	return_entry.delete(0, END)

	# Get PW Length and convert to integer
	try:
		length = int(my_entry.get())

	except:

		error_msg.config(text="Warning: Invalid input. Input should only contain digits!")



	# create a variable to hold our password
	my_password = ''

	# Loop through password length
	for x in range(length):
		my_password += chr(randint(33,126))

	# Output password to the screen
	return_entry.insert(0, my_password)


# Copy to clipboard
def clipper():
	# Clear the clipboard
	root.clipboard_clear()
	# Copy to clipboard
	root.clipboard_append(pw_entry.get())

# Label
prompt = Label(text="How many characters will the passord contain?", font=("Calibre", 15)).pack(pady=20)



# Entry Box for user to enter nr of char
my_entry = Entry(root, font=("Calibre", 20))
my_entry.pack(pady=20, padx=20)

# box for returned pass
return_entry = Entry(root, text="", font=("Calibre", 20), bd=0, bg="systembuttonface")
return_entry.pack(pady=20)

# frame for the buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

# Buttons
my_button = Button(my_frame, text="Generate Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

copy_button = Button(my_frame, text="Copy To Clipboad", command=clipper)
copy_button.grid(row=0, column=1, padx=10)

# quit button

quit = Button(my_frame, text="Quit", command=root.destroy)
quit.grid(row=0, column=2, padx=10)

#error message

error_msg = Label(root, text="",font=("Calibre", 10), bd=0, bg="systembuttonface")
error_msg.pack(pady=10)


root.mainloop()

