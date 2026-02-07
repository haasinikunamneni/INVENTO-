import tkinter as tk
import datetime
import time
from time import strftime
from tkinter import messagebox
import ast
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass

class IMS:
    def update(self):
        self.timeStr.set(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        ## Now use the .after method to call this function again in 1sec.
        self.lbl_clock.after(1000,self.update)

    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Invento |  Developed by XII--B | Haasini, Kushal, Hemsai")
        self.root.config(bg="#edcbd2")
        #===title=====
        title=tk.Label(self.root, text="Invento", font=("opensans", 40, "bold"), bg="#e3856b", fg="white", anchor="w", padx=20).place(x=0,y=0,relwidth=1,height=70)

        #===btn_logout===
        def logout():
            self.root.destroy()
            self.root3 = tk.Tk()
            obj3 = Login(self.root3)
            self.root3.mainloop()
        
        btn_logout=tk.Button(self.root, text="Logout", font=("opensans",15,"bold"), bg="#80c4b7", cursor="hand2", command= logout).place(x=1150, y=10, height=30, width=150)

        #===clock====
        self.timeStr = tk.StringVar()
        self.lbl_clock =tk.Label(self.root, textvariable=self.timeStr, text="Welcome to home page", font=("opensans", 15), bg="#80c4b7", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        self.update()

        #====Left Menu==
        leftMenu = tk.Frame(self.root, bd=2, bg="#edcbd2")
        leftMenu.place(x=0, y=100, width=200, height=600)

        lbl_menu = tk.Label(leftMenu, text="Menu", font=("opensans", 20), bg="#e3856b", fg="white").pack(side="top", fill="x")

        def quit():
            self.root.destroy()

        btn_employee = tk.Button(leftMenu, text="Employee", font=("opensans", 20), bg="#80c4b7", bd=3, cursor="hand2", command = self.employee).pack( side="top", fill="x")
        btn_supplier = tk.Button(leftMenu, text="Supplier", font=("opensans", 20), bg="#80c4b7", bd=3, cursor="hand2", command = self.supplier).pack(side="top", fill="x")
        btn_category = tk.Button(leftMenu, text="Category", font=("opensans", 20), bg="#80c4b7", bd=3, cursor="hand2", command = self.category).pack(side="top", fill="x")
        btn_product = tk.Button(leftMenu, text="Product", font=("opensans", 20), bg="#80c4b7", bd=3, cursor="hand2", command = self.product).pack(side="top", fill="x")
        btn_sales = tk.Button(leftMenu, text="Sales", font=("opensans", 20), bg="#80c4b7", bd=3, cursor="hand2").pack(side="top", fill="x")
        btn_exit = tk.Button(leftMenu, text="Exit", font=("opensans", 20), bg="#80c4b7", bd=3, cursor="hand2", command= quit).pack(side="top", fill="x")

        #===content==========

        self.lbl_employee = tk.Label(self.root, text="Total Employee\n[ 0 ]",bd=5, relief="ridge", bg="#ff0000", fg="black", font=("goudy old style", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)

        self.lbl_supplier = tk.Label(self.root, text="Total Supplier\n[ 0 ]", bd=5, relief="ridge", bg="#0000ff", fg="black", font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)

        self.lbl_category = tk.Label(self.root, text="Total Category\n[ 0 ]", bd=5, relief="ridge", bg="#00ff00", fg="black", font=("goudy old style", 20, "bold"))
        self.lbl_category.place(x=1000, y=120, height=150, width=300)

        self.lbl_product = tk.Label(self.root, text="Total Product\n[ 0 ]", bd=5, relief="ridge", bg="#a020f0", fg="black", font=("goudy old style", 20, "bold"))
        self.lbl_product.place(x=300, y=300, height=150, width=300)

        self.lbl_sales = tk.Label(self.root, text="Total sales\n[ 0 ]", bd=5, relief="ridge", bg="#000000", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=650, y=300, height=150, width=300)

        # ===footer====
        lbl_footer = tk.Label(self.root, text="IMS-Invento | Developed by XII--B | Haasini, Kushal, Hemsai\nFor any Technical issue Contact:- 9XXXXXXXXX", font=("opensans", 15), bg="#80c4b7", fg="white").pack(side="bottom", fill="x")
 
#==============================================================
    def employee(self):
        self.new_win = tk.Toplevel(self.root)
        self.new_obj =  employeeClass(self.new_win)
        
    def supplier(self):
        self.new_win = tk.Toplevel(self.root)
        self.new_obj =  supplierClass(self.new_win)

    def category(self):
        self.new_win = tk.Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def product(self):
        self.new_win = tk.Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

class Login:
    def __init__(self,root2):
        self.root2=root2
        self.root2.title('Login')
        self.root2.geometry("925x500+300+200")
        self.root2.configure(bg='#edcbd2')
        def signin():
            username = user.get()
            password = pass1.get()

            file = open('datasheet.txt', 'r')
            d= file.read()
            r = ast.literal_eval(d)
            file.close()
    
            if username in r.keys() and password == r[username]:
                self.root2.destroy()
                root = tk.Tk()
                obj1 = IMS(root)
                root.mainloop()
                


            else:
                messagebox.showerror("Invalid","invalid username and password")

        def signup_command():
            window = tk.Toplevel(self.root2)
            window.title('Sign Up')
            window.geometry('925x500+300+200')
            window.configure(bg = '#edcbd2')
            window.resizable(False, False)
    
            def signup():
                username = user.get()
                password = code.get()
                confirm_password = confirm_code.get()

                if password == confirm_password:
                    try:
                        file = open('datasheet.txt', 'r+')
                        d= file.read()
                        r = ast.literal_eval(d)

                        dict2 = {username : password}
                        r.update(dict2)
                        file.truncate(0)
                        file.close

                        file = open("datasheet.txt", "w")
                        w = file.write(str(r))

                        messagebox.showinfo('Signup', 'Successfully Signed Up')

                    except:
                        file = open('datasheet.txt', 'w')
                        pp = str({'Username':'Password'})
                        file.write(pp)
                        file.close()
                else:
                    messagebox.showerror('Invalid', 'Both Password should match')
    
            def sign():
                window.destroy()

            img = tk.PhotoImage(file='login1.png')
            tk.Label(window, image=img, border=0,bg='#edcbd2').place(x=5, y=0)

            frame = tk.Frame(window, width = 350, height = 350, bg = '#edcbd2')
            frame.place(x=480, y=50)

            heading = tk.Label(frame, text='Sign Up', fg='#80c4b7', bg = '#edcbd2', font = ('goudy old style', 23, 'bold'))
            heading.place(x=100, y=5)
##----------------------------------------------------------
            def on_enter(e):
                user.delete(0,'end')

            def on_leave(e):
                name = user.get()
                if name == "":
                    user.insert(0, 'Username')

            user = tk.Entry(frame, width = 25, fg = 'black', border = 0, bg = '#edcbd2', font= ('goudy old style', 11))
            user.place(x=30, y=70)
            user.insert(0,'Username')
            user.bind('<FocusIn>', on_enter)
            user.bind('<FocusOut>', on_leave)

            tk.Frame(frame, width = 295, height = 2, bg = '#000000').place(x=25, y=97)

            def on_enter(e):
                code.delete(0,'end')

            def on_leave(e):
                name = code.get()
                if name == "":
                    code.insert(0, 'Password')

            code = tk.Entry(frame, width = 25, fg = 'black', border = 0, bg = '#edcbd2', font= ('goudy old style', 11))
            code.place(x=30, y=140)
            code.insert(0,'Password')
            code.bind('<FocusIn>', on_enter)
            code.bind('<FocusOut>', on_leave)

            tk.Frame(frame, width = 295, height = 2, bg = '#000000').place(x=25, y=167)

            def on_enter(e):
                confirm_code.delete(0,'end')

            def on_leave(e):
                name = confirm_code.get()
                if name == "":
                    confirm_code.insert(0, 'Confirm password')

            confirm_code = tk.Entry(frame, width = 25, fg = 'black', border = 0, bg = '#edcbd2', font= ('goudy old style', 11))
            confirm_code.place(x=30, y=210)
            confirm_code.insert(0,'Confirm Password')
            confirm_code.bind('<FocusIn>', on_enter)
            confirm_code.bind('<FocusOut>', on_leave)

            tk.Frame(frame, width = 295, height = 2, bg = '#000000').place(x=25, y=237)


            tk.Button(frame, width=39, pady=7, text ='Sign Up', bg="#80c4b7", fg='#FFFFFF', border=0, command = signup).place(x=25, y=270)
            label = tk.Label(frame, text="I have an account", fg='#000000', bg='#edcbd2', font=('goudy old style', 9))
            label.place(x=90, y=330)

            sign_in= tk.Button(frame, width = 6, text='Sign in', border=0, bg = '#edcbd2', cursor = 'hand2', fg = '#80c4b7', command = signin)
            sign_in.place(x=190, y=330)


            window.mainloop()

#==IMAGE===
        img1 = tk.PhotoImage(file='login.png')
        tk.Label(self.root2, image=img1, border=0, bg='#edcbd2').place(x=50, y=30)

#==FRAME==
        frame = tk.Frame(self.root2, width=350, height=350, bg='#edcbd2')
        frame.place(x=480, y=70)

#===HEADER===
        heading = tk.Label(frame, text ='Sign in', fg = '#000000', bg='#edcbd2', font = ('goudy old style', 20, 'bold'))
        heading.place(x=100, y=5)

#===ENTRY===
        def on_enter(e):
            user.delete(0,'end')

        def on_leave(e):
            name = user.get()
            if name == "":
                user.insert(0, 'Username')


        user = tk.Entry(frame, width = 25, fg = '#000000', border=0, bg = "#edcbd2", font = ('goudy old style', 13))
        user.place(x=30, y=80)
        user.insert(0,'Username')
        user.bind('<FocusIn>', on_enter)
        user.bind('<FocusOut>', on_leave)

        tk.Frame(frame, width = 295, height = 2, bg = '#000000').place(x=25, y=107)

        def on_enter(e):
            pass1.delete(0,'end')

        def on_leave(e):
            name = pass1.get()
            if name == '':
                pass1.insert(0, 'Password')


        pass1= tk.Entry(frame, width = 25, fg = '#000000', border=0, bg = "#edcbd2", font = ('goudy old style', 13))
        pass1.place(x=30, y=150)
        pass1.insert(0,'Password')
        pass1.bind('<FocusIn>', on_enter)
        pass1.bind('<FocusOut>', on_leave)

        tk.Frame(frame, width = 295, height = 2, bg = '#000000').place(x=25, y=177)


#===BUTTON===
        tk.Button(frame, width=39, text ='Sign in', bg="#80c4b7", fg='#FFFFFF', border=0, command = signin).place(x=30, y=194)
        label = tk.Label(frame, text="Don't have an account?", fg='#000000', bg='#edcbd2', font=('goudy old style', 11))
        label.place(x=95, y=234)

        sign_up= tk.Button(frame, width = 6, text='Sign up', border=0, bg = '#edcbd2', cursor = 'hand2', fg = '#80c4b7', command= signup_command)
        sign_up.place(x=250, y=234)



root2 = tk.Tk()

obj2 = Login(root2)

root2.mainloop()
