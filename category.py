import tkinter as tk
from tkinter import messagebox
import ast
from tkinter import ttk
import sqlite3



class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Category Managment")
        self.root.config(bg="#edcbd2")
        self.root.focus_force()
    #All Variable================================  
        self.var_category=tk.StringVar()
        self.var_name = tk.StringVar()
    #====Title====
        title = tk.Label(self.root, text='Category', font=('goudy old style', 15), bg='#e3856b', fg='white').place(x=50, y=10, width=1000)

    #====content====
        lbl_category = tk.Label(self.root, text='Add Category:', font=('goudy old style', 15), bg='#edcbd2').place(x=50, y=50)
        txt_catergory = tk.Entry(self.root, textvariable= self.var_name, font=('goudy old style', 15), bg='lightyellow').place(x=50, y=80, width=180)
        btn_add = tk.Button(self.root, text="Add", font=('goudy old style', 15), bg='#80c4b7', cursor = 'hand2', command=self.add).place(x=240, y=80, width=150, height=25)
        btn_delete = tk.Button(self.root, text="Delete", font=('goudy old style', 15), bg='#80c4b7', cursor='hand2', command=self.delete).place(x=420, y=80, width=150, height=25)

    #====Category Details====
        cat_frame = tk.Frame(self.root, bd=3, relief = 'ridge')
        cat_frame.place(x=0, y=120, relwidth=1, height=380)

        scrolly=tk.Scrollbar(cat_frame, orient='vertical')
        scrollx=tk.Scrollbar(cat_frame, orient='horizontal')

        self.CategoryTable=ttk.Treeview(cat_frame, columns=("C.Id", "Category"), yscrollcommand=scrolly, xscrollcommand=scrollx)
        scrollx.pack(side='bottom', fill='x')
        scrolly.pack(side='right', fill='y')
        scrollx.config(command=self.CategoryTable.xview)
        scrolly.config(command=self.CategoryTable.yview)
        self.CategoryTable.heading("C.Id", text="CATEGORY_ID")
        self.CategoryTable.heading("Category", text="CATEGORY")
        
        self.CategoryTable["show"]="headings"
        
        self.CategoryTable.column("C.Id", width=90)
        self.CategoryTable.column("Category", width=100) 
        
        self.CategoryTable.pack(fill='both', expand=True)
        self.CategoryTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_name.get()=="":
                   messagebox.showerror("Error","Category Name must be required", parent=self.root)
            else:
                 cur.execute("SELECT * from category where name=?",(self.var_name.get(),))
                 row = cur.fetchone()
                 if row!=None:
                    messagebox.showerror("Error", "This Category is already present",parent=self.root)
                 else:
                    cur.execute("Insert into category (name) values(?)",(self.var_name.get(),))
                      
                    con.commit()
                    messagebox.showinfo("Success", "Category  Added Succesfully", parent=self.root)
                    self.show()
            
        except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}")
           
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * from category")
            rows=cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert('','end',values=row)

            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")


    def get_data(self,ev):
        f=self.CategoryTable.focus()
        content = (self.CategoryTable.item(f))
        row = content['values']
        self.var_category.set(row[0]),
        self.var_name.set(row[1])

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_name.get()=="":
                   messagebox.showerror("Error","Category name must be required",parent=self.root)
            else:
                 cur.execute("SELECT * from category where name=?",(self.var_name.get(),))
                 row = cur.fetchone()
                 if row==None:
                    messagebox.showerror("Error", "Invalid CAtegory", parent=self.root)
                 else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("DELETE from category where name=?",(self.var_name.get(),))
                        con.commit()
                        messagebox.showerror("Delete", "Category Deleted Successfully", parent=self.root)
                        self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
        self.root.focus_force()

    def clear(self):
        self.var_category.set(""),
        self.var_name.set(""),
        self.show()
        self.root.focus_force()


if __name__ == '__main__':
        root = tk.Tk()
        obj = categoryClass(root)
        root.mainloop