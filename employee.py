import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import *
from tkcalendar import Calendar
import sqlite3


class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x750+220+130")
        self.root.title("Employee Managment")
        self.root.config(bg="#edcbd2")
        self.root.focus_force()
    #All Variable=================================
        self.var_searchby=tk.StringVar()
        self.var_searchtxt=tk.StringVar()
        self.var_emp_id=tk.StringVar()
        self.var_name=tk.StringVar()
        self.var_contact=tk.StringVar()
        self.var_gender=tk.StringVar()
        self.var_doj=tk.StringVar()
        self.var_dob=tk.StringVar()
        self.var_email=tk.StringVar()
        self.var_pass=tk.StringVar()
        self.var_utype=tk.StringVar()
        self.var_salary=tk.StringVar()

    #====Frame====
        SearchFrame = tk.LabelFrame(self.root, text='Search Employee', bg='#edcbd2', font=('goudy old style', 12, 'bold'), bd=2, relief='ridge')
        SearchFrame.place(x=250, y=20, width=600, height=70)

    #====Options====
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", 'Name', 'Email', 'Contact'), state='readonly', justify='center', font=('goudy old style', 15, ))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = tk.Entry(SearchFrame, textvariable=self.var_searchtxt, font=('goudy old style', 15), bg='lightyellow').place(x=200, y=10)
        btn_Search = tk.Button(SearchFrame, text="Search", font=('goudy old style', 15), bg='#80c4b7', cursor = 'hand2', command=self.search).place(x=430, y=9, width=150, height=30)

    #====Title====
        title = tk.Label(self.root, text='Employee Details', font=('goudy old style', 15), bg='#e3856b', fg='white').place(x=50, y=100, width=1000)

    #====content====
        lbl_emp_id = tk.Label(self.root, text='Emp ID', font=('goudy old style', 15), bg='#edcbd2').place(x=50, y=150)
        lbl_gender = tk.Label(self.root, text='Gender', font=('goudy old style', 15), bg='#edcbd2').place(x=350, y=150)
        lbl_contact = tk.Label(self.root, text='Contact', font=('goudy old style', 15), bg='#edcbd2').place(x=750, y=150)

        txt_emp_id = tk.Entry(self.root, textvariable= self.var_emp_id, font=('goudy old style', 15), bg='lightyellow').place(x=150, y=150, width=180)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", 'Male', 'Female', 'Other', 'Prefer not to say'), state='readonly', justify='center', font=('goudy old style', 15, ))
        cmb_gender.place(x=500, y=150, width=180)
        cmb_gender.current(0)
        txt_contact = tk.Entry(self.root, textvariable= self.var_contact, font=('goudy old style', 15), bg='lightyellow').place(x=850, y=150, width=180)

        lbl_name = tk.Label(self.root, text='Name', font=('goudy old style', 15), bg='#edcbd2').place(x=50, y=190)
        lbl_dob = tk.Label(self.root, text='D.O.B', font=('goudy old style', 15), bg='#edcbd2').place(x=350, y=190)
        lbl_doj = tk.Label(self.root, text='D.O.J', font=('goudy old style', 15), bg='#edcbd2').place(x=750, y=190)
        
        def grab_date_dob():
            self.txt_dob.config(text=dat_dob.get_date())
            self.txt_dob.update_idletasks()
        def grab_date_doj():
            self.txt_doj.config(text=dat_doj.get_date())
            self.txt_doj.update_idletasks()
        
        
        txt_name = tk.Entry(self.root, textvariable= self.var_name, font=('goudy old style', 15), bg='lightyellow').place(x=150, y=190, width=180)
        self.txt_dob = tk.Label(self.root, bg='lightyellow', text="")
        self.txt_dob.place(x=500, y=190, width=180)
        dob_btn = tk.Button(self.root, text='Submit', cursor='hand2', command=grab_date_dob)
        dob_btn.place(x=500, y= 410)
        dat_dob = Calendar(self.root, bootstyle='danger')
        dat_dob.place(x=500, y=220, width=220)
        self.txt_doj = tk.Label(self.root, bg='lightyellow', text="")
        self.txt_doj.place(x=850, y=190, width=180)
        dat_doj = Calendar(self.root, bootstyle='danger')
        dat_doj.place(x=850, y=220, width=220)
        doj_btn = tk.Button(self.root, text='Submit', cursor='hand2', command=grab_date_doj)
        doj_btn.place(x=850, y= 410)
        lbl_email = tk.Label(self.root, text='Email', font=('goudy old style', 15), bg='#edcbd2').place(x=50, y=230)
        lbl_password = tk.Label(self.root, text='Password', font=('goudy old style', 15), bg='#edcbd2').place(x=50, y=350)
        lbl_usertype = tk.Label(self.root, text='Usertype', font=('goudy old style', 15), bg='#edcbd2').place(x=50, y=430)
        
        txt_email = tk.Entry(self.root, textvariable= self.var_email, font=('goudy old style', 15), bg='lightyellow').place(x=150, y=230, width=180)
        txt_pass = tk.Entry(self.root, textvariable= self.var_pass, font=('goudy old style', 15), bg='lightyellow').place(x=150, y=350, width=180)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Select", 'Admin', 'Employee'), state='readonly', justify='center', font=('goudy old style', 15, ))
        cmb_utype.place(x=150, y=430, width=180)
        cmb_utype.current(0)

        lbl_address = tk.Label(self.root, text='Address', font=('goudy old style', 15), bg='#edcbd2').place(x=50, y=270)
        lbl_salary = tk.Label(self.root, text='Salary', font=('goudy old style', 15), bg='#edcbd2').place(x=50, y=390)

        self.txt_address = tk.Text(self.root, font=('goudy old style', 15), bg='lightyellow')
        self.txt_address.place(x=150, y=270, width=300, height=60)
        txt_salary = tk.Entry(self.root, textvariable= self.var_salary, font=('goudy old style', 15), bg='lightyellow').place(x=150, y=390, width=180)

    #====button====
        btn_add = tk.Button(self.root, text="Save", font=('goudy old style', 15), bg='#80c4b7', cursor = 'hand2', command=self.add).place(x=500, y=520, width=110, height=28)
        btn_update = tk.Button(self.root, text="Update", font=('goudy old style', 15), bg='#80c4b7', cursor = 'hand2', command=self.update).place(x=620, y=520, width=110, height=28)
        btn_delete = tk.Button(self.root, text="Delete", font=('goudy old style', 15), bg='#80c4b7', cursor = 'hand2', command=self.delete).place(x=740, y=520, width=110, height=28)
        btn_clear = tk.Button(self.root, text="Clear", font=('goudy old style', 15), bg='#80c4b7', cursor = 'hand2', command=self.clear).place(x=860, y=520, width=110, height=28)

    #====Employee Details====
        emp_frame = tk.Frame(self.root, bd=3, relief = 'ridge')
        emp_frame.place(x=0, y=650, relwidth=1, height=150)

        scrolly=tk.Scrollbar(emp_frame, orient='vertical')
        scrollx=tk.Scrollbar(emp_frame, orient='horizontal')

        self.EmployeeTable=ttk.Treeview(emp_frame, columns=("eid", 'name', 'email', 'gender', 'contact', 'dob', 'doj', 'password', 'usertype', 'address', 'salary'), yscrollcommand=scrolly, xscrollcommand=scrollx)
        scrollx.pack(side='bottom', fill='x')
        scrolly.pack(side='right', fill='y')
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("eid", text="EMP ID")
        self.EmployeeTable.heading("name", text="NAME")
        self.EmployeeTable.heading("email", text="EMAIL")
        self.EmployeeTable.heading("gender", text="GENDER")
        self.EmployeeTable.heading("contact", text="CONTACT NO.")
        self.EmployeeTable.heading("dob", text="D.O.B")
        self.EmployeeTable.heading("doj", text="D.O.J")
        self.EmployeeTable.heading("password", text="PASSWORD")
        self.EmployeeTable.heading("usertype", text="USERTYPE")
        self.EmployeeTable.heading("address", text="ADDRESS")
        self.EmployeeTable.heading("salary", text="SALARY")
        
        self.EmployeeTable["show"]="headings"
        
        self.EmployeeTable.column("eid", width=90)
        self.EmployeeTable.column("name", width=100) 
        self.EmployeeTable.column("email", width=100)
        self.EmployeeTable.column("gender", width=100)
        self.EmployeeTable.column("contact", width=100)
        self.EmployeeTable.column("dob", width=100)
        self.EmployeeTable.column("doj", width=100)
        self.EmployeeTable.column("password", width=100)
        self.EmployeeTable.column("usertype", width=100)
        self.EmployeeTable.column("salary", width=100)
        
        self.EmployeeTable.pack(fill='both', expand=True)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
#========================================================================================================
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get()=="":
                   messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                 cur.execute("SELECT * from employee where eid=?",(self.var_emp_id.get(),))
                 row = cur.fetchone()
                 if row!=None:
                    messagebox.showerror("Error", "This Employee ID is already assigned", parent=self.root)
                 else:
                    cur.execute("Insert into employee (eid, name, email, gender, contact, dob, doj, password, usertype, address, salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                         self.var_emp_id.get(),
                         self.var_name.get(),
                         self.var_email.get(),
                         self.var_gender.get(),
                         self.var_contact.get(),
                         self.txt_doj.cget("text"),
                         self.txt_dob.cget("text"),
                         self.var_pass.get(),
                         self.var_utype.get(),
                         self.txt_address.get('1.0', 'end'),
                         self.var_salary.get()
                    ))
                      
                    con.commit()
                    messagebox.showinfo("Success", "Employee Added Succesfully", parent=self.root)
                    self.show()
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")   


    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('','end',values=row)

            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
         
    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content = (self.EmployeeTable.item(f))
        row = content['values']
        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.txt_dob.config(text=row[5]),
        self.txt_doj.config(text=row[6]),
        self.var_pass.set(row[7]),
        self.var_utype.set(row[8]),
        self.txt_address.delete('1.0', 'end'),
        self.txt_address.insert('end', row[9]),
        self.var_salary.set(row[10])


    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get()=="":
                   messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                 cur.execute("SELECT * from employee where eid=?",(self.var_emp_id.get(),))
                 row = cur.fetchone()
                 if row==None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                 else:
                    cur.execute("Update employee set name=?, email=?, gender=?, contact=?, dob=?, doj=?, password=?, usertype=?, address=?, salary=? where eid=?",(
                         self.var_name.get(),
                         self.var_email.get(),
                         self.var_gender.get(),
                         self.var_contact.get(),
                         self.txt_dob.cget("text"),
                         self.txt_doj.cget("text"),
                         self.var_pass.get(),
                         self.var_utype.get(),
                         self.txt_address.get('1.0', 'end'),
                         self.var_salary.get(),
                         self.var_emp_id.get()
                    ))
                      
                    con.commit()
                    messagebox.showinfo("Success", "Employee Updated Succesfully", parent=self.root)
                    self.show()
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
        self.root.focus_force()

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get()=="":
                   messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                 cur.execute("SELECT * from employee where eid=?",(self.var_emp_id.get(),))
                 row = cur.fetchone()
                 if row==None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                 else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("DELETE from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showerror("Delete", "Employee Deleted Successfully", parent=self.root)
                        self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
        self.root.focus_force()

    def clear(self):
        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_contact.set(""),
        self.txt_dob.config(text=""),
        self.txt_doj.config(text=""),
        self.var_pass.set(""),
        self.var_utype.set("Select"),
        self.txt_address.delete('1.0', 'end'),
        self.var_salary.set("")
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
                cur.execute("SELECT * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('','end',values=row)
                else:
                    messagebox.showerror("Error", "No Record Found")
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
        self.root.focus_force()

if __name__ == '__main__':
        root = tk.Tk()
        obj = employeeClass(root)
        root.mainloop