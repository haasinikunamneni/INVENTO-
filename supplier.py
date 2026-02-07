import tkinter as tk
from tkinter import messagebox
import ast
from tkinter import ttk
import sqlite3


class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Supplier Managment")
        self.root.config(bg="#edcbd2")
        self.root.focus_force()
    #All Variable=================================
        self.var_searchby=tk.StringVar()
        self.var_searchtxt=tk.StringVar()
        
        self.var_sup_invoice=tk.StringVar()
        self.var_name=tk.StringVar()
        self.var_contact=tk.StringVar()
        

    #====Frame====
        SearchFrame = tk.LabelFrame(self.root, text='Search Invoice', bg='#edcbd2', font=('goudy old style', 12, 'bold'), bd=2, relief='ridge')
        SearchFrame.place(x=250, y=20, width=600, height=70)

    #====Options====
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", 'Invoice', 'Name', 'Contact'), state='readonly', justify='center', font=('goudy old style', 15, ))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = tk.Entry(SearchFrame, textvariable=self.var_searchtxt, font=('goudy old style', 15), bg='lightyellow').place(x=200, y=10)
        btn_Search = tk.Button(SearchFrame, text="Search", font=('goudy old style', 15), bg='#80c4b7', cursor = 'hand2', command=self.search).place(x=430, y=9, width=150, height=30)

    #====Title====
        title = tk.Label(self.root, text='Supplier Details', font=('goudy old style', 15), bg='#e3856b', fg='white').place(x=50, y=100, width=1000)

    #====content====
        lbl_supplier_invoice = tk.Label(self.root, text='Invoice Number', font=('goudy old style', 15), bg='#edcbd2').place(x=50, y=150)
        txt_supplier_invoive = tk.Entry(self.root, textvariable= self.var_sup_invoice, font=('goudy old style', 15), bg='lightyellow').place(x=200, y=150, width=180)
    

        lbl_name = tk.Label(self.root, text='Name', font=('goudy old style', 15), bg='#edcbd2').place(x=50, y=190)  
        txt_name = tk.Entry(self.root, textvariable= self.var_name, font=('goudy old style', 15), bg='lightyellow').place(x=200, y=190, width=180)

        lbl_contact = tk.Label(self.root, text='Contact', font=('goudy old style', 15), bg='#edcbd2').place(x=50, y=230)
        txt_contact = tk.Entry(self.root, textvariable= self.var_contact, font=('goudy old style', 15), bg='lightyellow').place(x=200, y=230, width=180)

        lbl_description = tk.Label(self.root, text='Description', font=('goudy old style', 15), bg='#edcbd2').place(x=50, y=270)
        self.txt_description = tk.Text(self.root, font=('goudy old style', 15), bg='lightyellow')
        self.txt_description.place(x=200, y=270, width=300, height=60)
    
    #====button====
        btn_add = tk.Button(self.root, text="Save", font=('goudy old style', 15), bg='#80c4b7', cursor = 'hand2', command=self.add).place(x=540, y=305, width=110, height=28)
        btn_update = tk.Button(self.root, text="Update", font=('goudy old style', 15), bg='#80c4b7', cursor = 'hand2', command=self.update).place(x=660, y=305, width=110, height=28)
        btn_delete = tk.Button(self.root, text="Delete", font=('goudy old style', 15), bg='#80c4b7', cursor = 'hand2', command=self.delete).place(x=780, y=305, width=110, height=28)
        btn_clear = tk.Button(self.root, text="Clear", font=('goudy old style', 15), bg='#80c4b7', cursor = 'hand2', command=self.clear).place(x=900, y=305, width=110, height=28)

    #====Supplier Details====
        sup_frame = tk.Frame(self.root, bd=3, relief = 'ridge')
        sup_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly=tk.Scrollbar(sup_frame, orient='vertical')
        scrollx=tk.Scrollbar(sup_frame, orient='horizontal')

        self.SupplierTable=ttk.Treeview(sup_frame, columns=("invoice", 'name', 'contact', 'description'), yscrollcommand=scrolly, xscrollcommand=scrollx)
        scrollx.pack(side='bottom', fill='x')
        scrolly.pack(side='right', fill='y')
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)
        self.SupplierTable.heading("invoice", text="INVOICE")
        self.SupplierTable.heading("name", text="NAME")
        self.SupplierTable.heading("contact", text="CONTACT NO.")
        self.SupplierTable.heading("description", text="DESCRIPTION")
        
        self.SupplierTable["show"]="headings"
        
        self.SupplierTable.column("invoice", width=90)
        self.SupplierTable.column("name", width=100) 
        self.SupplierTable.column("contact", width=100)
        self.SupplierTable.column("description", width=100)
        
        self.SupplierTable.pack(fill='both', expand=True)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
#========================================================================================================
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                   messagebox.showerror("Error","Invoice must be required",parent=self.root)
            else:
                 cur.execute("SELECT * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                 row = cur.fetchone()
                 if row!=None:
                    messagebox.showerror("Error", "This Invoice is already assigned", parent=self.root)
                 else:
                    cur.execute("Insert into Supplier (invoice, name, contact, description) values(?,?,?,?)",(
                         self.var_sup_invoice.get(),
                         self.var_name.get(),
                         self.var_contact.get(),
                         self.txt_description.get('1.0', 'end')
                    ))
                      
                    con.commit()
                    messagebox.showinfo("Success", "Invoice Added Succesfully", parent=self.root)
                    self.show()
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")   


    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * from supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('','end',values=row)

            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
         
    def get_data(self,ev):
        f=self.SupplierTable.focus()
        content = (self.SupplierTable.item(f))
        row = content['values']
        self.var_sup_invoice.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contact.set(row[4]),
        self.txt_description.delete('1.0', 'end'),
        self.txt_description.insert('end', row[9])


    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                   messagebox.showerror("Error","Invoice must be required",parent=self.root)
            else:
                 cur.execute("SELECT * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                 row = cur.fetchone()
                 if row==None:
                    messagebox.showerror("Error", "Invalid Invoice", parent=self.root)
                 else:
                    cur.execute("Update supplier set name=?, description=? where invoice=?",(
                         self.var_name.get(),
                         self.var_contact.get(),
                         self.txt_description.get('1.0', 'end')
                    ))
                      
                    con.commit()
                    messagebox.showinfo("Success", "Invoice Updated Succesfully", parent=self.root)
                    self.show()
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
        self.root.focus_force()

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                   messagebox.showerror("Error","nvoice must be required",parent=self.root)
            else:
                 cur.execute("SELECT * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                 row = cur.fetchone()
                 if row==None:
                    messagebox.showerror("Error", "Invalid Invoice", parent=self.root)
                 else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("DELETE from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showerror("Delete", "Invoice Deleted Successfully", parent=self.root)
                        self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
        self.root.focus_force()

    def clear(self):
        self.var_sup_invoice.set(""),
        self.var_name.set(""),
        self.var_contact.set(""),
        self.txt_description.delete('1.0', 'end'),
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()
        self.root.focus_force()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error", "Select Search By Option", parent=self.root)
            elif self.var_searchby.get()=="":
                messagebox.showerror("Error", "Search imput should be required")
            else:
                cur.execute("SELECT * from supplier where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    for row in rows:
                        self.SupplierTable.insert('','end',values=row)
                else:
                    messagebox.showerror("Error", "No Record Found")
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
        self.root.focus_force()

if __name__ == '__main__':
        root = tk.Tk()
        obj = supplierClass(root)
        root.mainloop