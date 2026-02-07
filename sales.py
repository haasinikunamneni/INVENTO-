import tkinter as tk
from tkinter import messagebox
import ast
from tkinter import ttk
import os


class salesClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Sales Managment")
        self.root.config(bg="#edcbd2")
        self.root.focus_force()

        self.bill_list=[]
        self.var_invoive=tk.StringVar()

        title = tk.Label(self.root, text='Manage Customer Bills', font=('goudy old style', 15), bg='#e3856b', fg='white').pack(side='top', fill='x')
        
        lbl_invoive = tk.Label(self.root, text="Invoice No", font=("goudy old style", 12), bg='#edcbd2').place(x=50, y=40)
        txt_invoive = tk.Entry(self.root, textvariable=self.var_invoive, font=("goudy old style", 12), bg='lightyellow').place(x=160, y=40, width=180, height=28)

        btn_Search = tk.Button(self.root, text='Search', command = self.search, font=('goudy old style', 15), bg="#80c4b7", fg='black', cursor = 'hand2').place(x=360, y=40, width=120, height=28)
        btn_Clear = tk.Button(self.root, text='Clear', command = self.clear, font=('goudy old style', 15), bg="#80c4b7", fg='black', cursor = 'hand2').place(x=490, y=40, width=120, height=28)

        sales_Frame = tk.Frame(self.root, bd=3, relief='ridge')
        sales_Frame.place(x=50, y=80, width=200, height=370)

        scrolly = tk.Scrollbar(sales_Frame, orient='vertical')      
        self.Sales_List = tk.Listbox(sales_Frame, font=('goudy old style', 15), bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side='right', fill='y')
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill='both', expand=1)
        self.Sales_List.bind("<ButtonRelease-1>", self.get_data)
        
        bill_Frame = tk.Frame(self.root, bd=3, relief='ridge')
        bill_Frame.place(x=280, y=80, width=410, height=370)

        title = tk.Label(bill_Frame, text='Customer Bill Area', font=('goudy old style', 15), bg='#e3856b', fg='white').pack(side='top', fill='x')
       
    
        scrolly2 = tk.Scrollbar(bill_Frame, orient='vertical')      
        self.Bill_Area = tk.Text(bill_Frame, font=('goudy old style', 15), bg="white", yscrollcommand=scrolly2.set)
        scrolly2.pack(side='right', fill='y')
        scrolly2.config(command=self.Sales_List.yview)
        self.Bill_Area.pack(fill='both', expand=1)

        self.show()
    
    def show(self):
         del self.bill_list[:]
         self.Sales_List.delete(0, 'end')
         for i in os.listdir('bill'):
             if i.split('.')[-1]=='txt':
                 self.Sales_List.insert('end', i)
                 self.bill_list.append(i.split('.')[0])

    def get_data(self,ev):
        row=self.Sales_List.curselection()
        file_name=self.Sales_List.get(row)
        self.Bill_Area.delete('1.0', 'end')
        fp = open(f'bill/{file_name}', 'r')
        for i in fp:
            self.Bill_Area.insert('end', i)
        fp.close()

    def search(self):
        if self.var_invoive.get()=="":
            messagebox.showerror("Error", "Invoice no. should be required", parent=self.root)
        else:
            if self.var_invoive.get() in self.bill_list:
                fp = open(f'bill/{self.var_invoive.get()}.txt', 'r')
                self.Bill_Area.delete('1.0', 'end')
                for i in fp:
                    self.Bill_Area.insert('end', i)
                fp.close()

            else:
                messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)

    def clear(self):
        self.show()
        self.Bill_Area.delete('1.0', 'end')


if __name__ == '__main__':
    root = tk.Tk()
    obj = salesClass(root)
    root.mainloop()