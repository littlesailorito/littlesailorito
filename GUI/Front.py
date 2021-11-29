from tkinter import *
import Back as bck
from tkinter import messagebox
class Window(object):

    def __init__(self,window):
        self.Database=bck.DataBase()
        self.window = window


        #Window
        self.window.geometry("700x500")
        self.window.resizable(False, False)
        self.window.title("Stock")


        #Tkinters widgets
        
       
        
        self.Add_but = Button(window,text = "Add object to the base", width=25,command = self.Add_func)
        self.Add_but.place(x=500,y=120)

        self.Delete_all_but=Button(window,text="Delete all content", width=25,command=self.Delete_all)
        self.Delete_all_but.place(x=500,y=270)

        self.Send_But=Button(window,text="Choose an option",width = 14)
        self.Send_But.place(x=494,y=360)
                
        self.Remove_but = Button(window,text = "Remove object", width=25, command = self.Remove_func)
        self.Remove_but.place(x=500,y=170)

        
        self.Export_csv_but =Button(window,text = "Export all stock to the csv file",width = 25,command =lambda :self.Database.Writing_into_csv_file)
        if self.Database.View_all():
            self.Export_csv_but.place(x=110,y=40)
        
        
        
            

        #listbox
        self.listbox=Listbox(window,height = 20,width=50)
        self.listbox.place(x=50,y=100)
        


        #entry box
        self.entry_name=Entry(window,justify=CENTER,width=15)
        #self.entry_name.place(x=500,y=300)
        self.entry_quantity=Entry(window,justify=CENTER,width=15)
        #self.entry_quantity.place(x=500,y=320)
        self.entry_price=Entry(window,justify=CENTER,width=15)
        #self.entry_price.place(x=500,y=340)

        
        
        
        #labels
        self.Name_label =Label(window,text="Name",width=10)
        
        self.Quantity_label =Label(window,text="Quantity",width=10)
        
        self.Price_label =Label(window,text="Price",width=10)
        
        


        
    #Functions

        
    
    def Add_func(self):
            self.Send_But.config(text="Add object",command = self.Check_if_all_is_right)
            self.Name_label.place(x=420,y=300)
            self.entry_name.place(x=500,y=300)
            self.Price_label.place(x=420,y=340)
            self.entry_price.place(x=500,y=340)
            self.Quantity_label.place(x=421,y=320)
            self.entry_quantity.place(x=500,y=320)


    def Delete_all(self):

        if not self.Database.View_all():
            messagebox.showerror("Error","The stock is empty")
        else:
            self.Database.Remove_all_content()
            self.Export_csv_but.place_forget()

        

    def Remove_func(self):
        self.Showing_in_listbox()
        if  self.Database.View_all():
            self.Send_But.config(text = "Remove object",command = self.Removing)
            self.Quantity_label.place_forget()
            self.entry_quantity.place_forget()
            self.Name_label.place_forget()
            self.entry_name.place_forget()
            self.entry_price.place_forget()
            self.Price_label.place_forget()


    def Showing_in_listbox(self):
        self.listbox.delete(0,END)
        if not self.Database.View_all():
                
           messagebox.showerror("Error","Stock is empty")

        else:
         for row in self.Database.View_all():
            self.listbox.insert(END,row)


    def Removing(self):
           
        
        if self.listbox.curselection() == ():
            messagebox.showerror("Error", "It hasn\'t been seleected any element to remove") 
        else:
            index = self.listbox.curselection()[0]
            self.selected_tuple=self.listbox.get(index)
            self.Database.Remove_object_from_base(self.selected_tuple[0])
            self.listbox.delete(0,END)
            for row in self.Database.View_all():
                self.listbox.delete(0,'end')
                self.listbox.insert(END,row)
            if  not self.Database.View_all():
                self.Export_csv_but.place_forget()


    def Check_if_all_is_right(self):


        if len(self.entry_name.get()) != 0 and len(self.entry_quantity.get())!=0 and len(self.entry_price.get())!=0:
            self.Database.Add_object_to_base(self.entry_name.get(),int(self.entry_quantity.get()), float(self.entry_price.get()))
            messagebox.showinfo("Information","The object has been correctly added to the database")
            self.entry_name.delete(0,'end')
            self.entry_quantity.delete(0,'end')
            self.entry_price.delete(0,'end')
            self.Showing_in_listbox()
            self.Export_csv_but.place(x=110,y=40)

        else:
            messagebox.showerror("Error","Some of given values are incorrect")


    




window=Tk()


Window(window)


window.mainloop()






