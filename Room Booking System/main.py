from tkinter import *
import check_in_ui
import check_out
import get_info
import customer_info
import os 
 
 
class Hotel:
    def __init__(self, root):
        self.root = root
        pad = 3 
         
        self.root.title("Bon Voyage!")
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad)) 
        root.configure(bg="pink") 
        # create mainframe to add message 
        top = Frame(self.root)
        top.pack(side="top") 
 
        # create frame to add buttons
        bottom = Frame(self.root)
        bottom.pack(side="top")
        # display message 
        self.label = Label(top, font=('arial', 50, 'bold'), text="WELCOME", fg="red", anchor="center",bg="pink")
        self.label.grid(row=0, column=3) 
 
        # create check in button 
        self.check_in_button = Button(bottom, text="CHECK IN", font=('', 20), bg="#15d3ba", relief=RIDGE, height=2, 
                                      width=50, 
                                      fg="black", anchor="center", 
                                      command=check_in_ui.check_in_ui_fun)
        # call check_in_ui_fun from check_in_ui.py file 
        self.check_in_button.grid(row=0, column=2, padx=10, pady=10) 
 
        # create check out button 
        self.check_out_button = Button(bottom, text="CHECK OUT", font=('', 20), bg="#15d3ba", relief=RIDGE, height=2, 
                                       width=50, fg="black", anchor="center", 
                                       command=check_out.check_out_ui)
        # call check_out_ui function from check_out.py file 
        self.check_out_button.grid(row=1, column=2, padx=10, pady=10) 
 
        # create show list button 
        self.room_info_button = Button(bottom, text="INFORMATION OF ROOMS", font=('', 20), bg="#15d3ba", relief=RIDGE, 
                                       height=2, 
                                       width=50, fg="black", anchor="center", 
                                       command=get_info.get_info_ui)
        # call get_info_ui function from get_info.py file 
        self.room_info_button.grid(row=2, column=2, padx=10, pady=10) 
 
        # create get information of all the guest 
        self.get_info_button = Button(bottom, text="INFORMATION OF ALL GUEST", font=('', 20), bg="#15d3ba", 
                                      relief=RIDGE, 
                                      height=2, width=50, fg="black", anchor="center",
                                      command=customer_info.customer_info_ui)
        # call customer_info_ui function from customer_info.py file
        self.get_info_button.grid(row=3, column=2, padx=10, pady=10) 
 
         
 
        # button to exit the program 
        self.exit_button = Button(bottom, text="EXIT", font=('', 20), bg="#15d3ba", relief=RIDGE, height=2, width=50, 
                                  fg="black", 
                                  anchor="center", command=quit) 
        self.exit_button.grid(row=4, column=2, padx=10, pady=10) 
 
        self.label1 = Label(bottom, font=('arial', 30, 'bold'), text="About Us: Project On Room Booking System", fg="purple", anchor="center") 
        self.label1.grid(row=5, column=2) 
        self.label2 = Label(bottom, font=('arial', 20, 'bold'), text="Since nobody got to travel in 2020;)So Bon Voyage!(Happy Journey!)", fg="black", anchor="center")
        self.label2.grid(row=6, column=2) 
 
 
def home_ui():
    root = Tk() 
    application = Hotel(root)
    root.mainloop() 
 
 
if __name__ == '__main__': 
    home_ui() 
 
