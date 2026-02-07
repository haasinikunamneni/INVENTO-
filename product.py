import tkinter as tk
from tkinter import messagebox
import ast
from tkinter import ttk
import sqlite3


class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Product Managment")
        self.root.config(bg="#edcbd2")
        self.root.focus_force()

        self.var_pid = tk.StringVar()        
        self.var_cat = tk.StringVar()
        self.var_sup = tk.StringVar()
        self.catList = []
        self.supList = []
        self.fetch_cat_sup()
        self.var_name = tk.StringVar()
        self.var_price = tk.StringVar()
        self.var_qty = tk.StringVar()
        self.var_status = tk.StringVar()
        self.var_searchby = tk.StringVar()
        self.var_searchtxt = tk.StringVar()
        
        
        
        product_Frame = tk.Frame(self.root, bd =3, relief="ridge", bg='#edcbd2')
        product_Frame.place(x=10, y=10, width=450, height=480)

        title = tk.Label(product_Frame, text='Manage Product Details', font=('goudy old style', 15), bg='#e3856b', fg='white').pack(side='top', fill='x')
        
        lbl_category = tk.Label(product_Frame, text='Category', font=('goudy old style', 15), bg='#edcbd2').place(x=30, y=60)
        lbl_supplier = tk.Label(product_Frame, text='Supplier', font=('goudy old style', 15), bg='#edcbd2').place(x=30, y=110)
        lbl_prod_name = tk.Label(product_Frame, text='Name', font=('goudy old style', 15), bg='#edcbd2').place(x=30, y=160)
        lbl_price = tk.Label(product_Frame, text='Price', font=('goudy old style', 15), bg='#edcbd2').place(x=30, y=210)
        lbl_quantity = tk.Label(product_Frame, text='Quantity', font=('goudy old style', 15), bg='#edcbd2').place(x=30, y=260)
        lbl_status = tk.Label(product_Frame, text='Status', font=('goudy old style', 15), bg='#edcbd2').place(x=30, y=310)

        SearchFrame = tk.LabelFrame(self.root, text='Search Product', bg='#edcbd2', font=('goudy old style', 12, 'bold'), bd=2, relief='ridge')
        SearchFrame.place(x=480, y=10, width=600, height=80)

        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", 'Category', 'Supplier', 'Name'), state='readonly', justify='center', font=('goudy old style', 15, ))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = tk.Entry(SearchFrame, textvariable=self.var_searchtxt, font=('goudy old style', 15), bg='lightyellow').place(x=200, y=10)
        btn_Search = tk.Button(SearchFrame, text="Search", font=('goudy old style', 15), bg='#80c4b7', cursor = 'hand2', command=self.search).place(x=430, y=9, width=150, height=30)
        
        cmb_cat = ttk.Combobox(product_Frame, textvariable=self.var_cat, values=self.catList, state='readonly', justify='center', font=('goudy old style', 15, ))
        cmb_cat.place(x=150, y=60, width=200)
        cmb_cat.current(0)

        cmb_sup = ttk.Combobox(product_Frame, textvariable=self.var_sup, values=self.supList, state='readonly', justify='center', font=('goudy old style', 15, ))
        cmb_sup.place(x=150, y=110, width=200)
        cmb_sup.current(0)

        txt_name = tk.Entry(product_Frame, textvariable=self.var_name, font=('goudy old style', 15, ), bg = 'lightyellow').place(x=150, y=160, width=200)
        txt_price = tk.Entry(product_Frame, textvariable=self.var_price, font=('goudy old style', 15, ), bg = 'lightyellow').place(x=150, y=210, width=200)
        txt_quantity = tk.Entry(product_Frame, textvariable=self.var_qty, font=('goudy old style', 15, ), bg = 'lightyellow').place(x=150, y=260, width=200)

        cmb_status = ttk.Combobox(product_Frame, textvariable=self.var_status, values=("Select", "Active", "Inactive"), state='readonly', justify='center', font=('goudy old style', 15, ))
        cmb_status.place(x=150, y=310, width=200)
        cmb_status.current(0)

        btn_add = tk.Button(product_Frame, text="Save", font=('goudy old style', 15), bg='#80c4b7', cursor = 'hand2', command=self.add).place(x=10, y=400, width=100, height=40)
        btn_update = tk.Button(product_Frame, text="Update", font=('goudy old style', 15), bg='#80c4b7', cursor = 'hand2', command=self.update).place(x=120, y=400, width=100, height=40)
        btn_delete = tk.Button(product_Frame, text="Delete", font=('goudy old style', 15), bg='#80c4b7', cursor = 'hand2', command=self.delete).place(x=230, y=400, width=100, height=40)
        btn_clear = tk.Button(product_Frame, text="Clear", font=('goudy old style', 15), bg='#80c4b7', cursor = 'hand2', command=self.clear).place(x=340, y=400, width=100, height=40)

        
        prod_frame = tk.Frame(self.root, bd=3, relief = 'ridge')
        prod_frame.place(x=480, y=110, width=600, height=380)

        scrolly=tk.Scrollbar(prod_frame, orient='vertical')
        scrollx=tk.Scrollbar(prod_frame, orient='horizontal')

        self.ProductTable=ttk.Treeview(prod_frame, columns=("pid", "category", 'supplier', 'name', 'price', 'quantity', 'status'), yscrollcommand=scrolly, xscrollcommand=scrollx)
        scrollx.pack(side='bottom', fill='x')
        scrolly.pack(side='right', fill='y')
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        self.ProductTable.heading("pid", text="PRODUCT.ID")
        self.ProductTable.heading("category", text="CATEGORY")
        self.ProductTable.heading("supplier", text="SUPPLIER")
        self.ProductTable.heading("name", text="NAME")
        self.ProductTable.heading("price", text="PRICE")
        self.ProductTable.heading("quantity", text="QUANTITY")
        self.ProductTable.heading("status", text="STATUS")
        
        self.ProductTable["show"]="headings"
        
        self.ProductTable.column("pid", width=100)
        self.ProductTable.column("category", width=100)
        self.ProductTable.column("supplier", width=100) 
        self.ProductTable.column("name", width=100)
        self.ProductTable.column("quantity", width=100)
        self.ProductTable.column("price", width=100)
        self.ProductTable.column("status", width=100)
        
        self.ProductTable.pack(fill='both', expand=True)
        self.ProductTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()
        
        
#=======================================================================================================================
    def fetch_cat_sup(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT name from category")
            cat=cur.fetchall()
            self.catList.append("Empty")
            if len(cat)>0:
                del self.catList[:]
                self.catList.append("Select")
                for i in cat:
                    self.catList.append(i[0])

            cur.execute("SELECT name from supplier")
            sup=cur.fetchall()
            self.supList.append("Empty")
            if len(sup)>0:
                del self.supList[:]
                self.supList.append("Select")
                for j in sup:
                    self.supList.append(j[0])

        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}") 
    
    
    
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_sup.get()=="Select" or self.var_name.get()=="":
                   messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                 cur.execute("SELECT * from product where name=?",(self.var_name.get(),))
                 row = cur.fetchone()
                 if row!=None:
                    messagebox.showerror("Error", "Product is already present", parent=self.root)
                 else:
                    cur.execute("Insert into product(category, supplier, name, price, quantity, status) values(?,?,?,?,?,?)",(
                         self.var_cat.get(),
                         self.var_sup.get(),
                         self.var_name.get(),
                         self.var_price.get(),
                         self.var_qty.get(),
                         self.var_status.get(),
                    ))
                      
                    con.commit()
                    messagebox.showinfo("Success", "product Added Succesfully", parent=self.root)
                    self.show()
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")   


    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * from product")
            rows=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('','end',values=row)

            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
         
    def get_data(self,ev):
        f=self.ProductTable.focus()
        content = (self.ProductTable.item(f))
        row = content['values']
        self.var_pid.set(row[0]),        
        self.var_cat.set(row[1]),
        self.var_sup.set(row[2]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_qty.set(row[5]),
        self.var_status.set(row[6]),


    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get()=="":
                   messagebox.showerror("Error","Please select product from list",parent=self.root)
            else:
                 cur.execute("SELECT * from product where pid=?", (self.var_pid.get(), ))
                 row = cur.fetchone()
                 if row==None:
                    messagebox.showerror("Error", "Invalid Product", parent=self.root)
                 else:
                    cur.execute("Update product set category=?, supplier=?, name=?, price=?, quantity=?, status=? where pid=?",(
                         self.var_cat.get(),
                         self.var_sup.get(),
                         self.var_name.get(),
                         self.var_price.get(),
                         self.var_qty.get(),
                         self.var_status.get(),
                         self.var_pid.get()
                    ))
                      
                    con.commit()
                    messagebox.showinfo("Success", "Product Updated Succesfully", parent=self.root)
                    self.show()
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
        self.root.focus_force()

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get()=="":
                   messagebox.showerror("Error","Product must be chosen",parent=self.root)
            else:
                 cur.execute("SELECT * from product where pid=?",(self.var_pid.get(),))
                 row = cur.fetchone()
                 if row==None:
                    messagebox.showerror("Error", "Invalid Product", parent=self.root)
                 else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("DELETE from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showerror("Delete", "Product Deleted Successfully", parent=self.root)
                        self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
        self.root.focus_force()

    def clear(self):
        self.var_cat.set("Select"),
        self.var_sup.set("Select"),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_status.set("Select"),
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
                cur.execute("SELECT * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('','end',values=row)
                else:
                    messagebox.showerror("Error", "No Record Found")
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
        self.root.focus_force()


if __name__ == '__main__':
        root = tk.Tk()
        obj = productClass(root)
        root.mainloop