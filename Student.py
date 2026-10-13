from tkinter import *
from tkinter import ttk
import pymysql

class Student:
        def __init__(self,root):
                self.root=root
                self.root.title("Student Management System")
                self.root.geometry("1350x700+0+0")

                title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
                title.pack(side=TOP, fill=X)


        #===== All Variables================
                self.roll_no=StringVar()
                self.name=StringVar()
                self.email=StringVar()
                self.gender=StringVar()
                self.contact=StringVar()
                self.dob=StringVar()
                self.address=StringVar()

                self.search_by=StringVar()
                self.search_txt=StringVar()

        #===== Manage Frame=============

                Management_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
                Management_Frame.place(x=20,y=100,width=450,height=560)

                m_title=Label(Management_Frame,text="Manage Students",bg="crimson",fg="white",font=("times new roman",30,"bold"))
                m_title.grid(row=0,columnspan=2,pady=20)

                lbl_roll=Label(Management_Frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
                lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

                txt_roll=Entry(Management_Frame,textvariable=self.roll_no,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

                lbl_name=Label(Management_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
                lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")        

                txt_name=Entry(Management_Frame,textvariable=self.name,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

                lbl_email=Label(Management_Frame,text="Email",bg="crimson",fg="white",font=("times new roman",20,"bold"))
                lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

                txt_email=Entry(Management_Frame,textvariable=self.email,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

                lbl_gender=Label(Management_Frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
                lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w") 

                combo_gender=ttk.Combobox(Management_Frame,textvariable=self.gender,font=("times new roman",13,"bold"),state='readonly')     
                combo_gender['values']=("Male","Female","Other")
                combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")

                lbl_contact=Label(Management_Frame,text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold"))
                lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

                txt_contact=Entry(Management_Frame,textvariable=self.contact,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

                lbl_dob=Label(Management_Frame,text="D.O.B",bg="crimson",fg="white",font=("times new roman",20,"bold"))
                lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w") 

                txt_dob=Entry(Management_Frame,textvariable=self.dob,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

                lbl_address=Label(Management_Frame,text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold"))
                lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

                self.txt_address=Text(Management_Frame,width=30,height=4,font=("",10))
                self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")
        #======== Button Frame===============
                btn_Frame=Frame(Management_Frame,bd=4,relief=RIDGE,bg="crimson")
                btn_Frame.place(x=15,y=500,width=410)

                Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
                Updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
                Deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
                Clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        #===== Detail Frame===============
                Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
                Detail_Frame.place(x=500,y=100,width=750,height=560)

                lbl_search=Label(Detail_Frame,text="Search By",bg="crimson",fg="white",font=("times new roman",20,"bold"))
                lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

                combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
                combo_search['values']=("Name","Roll_no","Contact")
                combo_search.grid(row=0,column=1,pady=10,padx=20,sticky="w")

                txt_search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
                txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

                searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
                showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)  
        #======== Table Frame================
                Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
                Table_Frame.place(x=10,y=70,width=720,height=480)

                scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
                scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
                self.student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM,fill=X)       
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_x.config(command=self.student_table.xview)
                scroll_y.config(command=self.student_table.yview)
                self.student_table.heading("roll",text="Roll No.")
                self.student_table.heading("name",text="Name")
                self.student_table.heading("email",text="Email")
                self.student_table.heading("gender",text="Gender")
                self.student_table.heading("contact",text="Contact")
                self.student_table.heading("dob",text="D.O.B")
                self.student_table.heading("address",text="Address")
                self.student_table['show']='headings'
                self.student_table.column("roll",width=100)
                self.student_table.column("name",width=100)
                self.student_table.column("email",width=100)
                self.student_table.column("gender",width=100)
                self.student_table.column("contact",width=100)
                self.student_table.column("dob",width=100)
                self.student_table.column("address",width=100)
                self.student_table.pack(fill=BOTH,expand=1)
                self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
                self.fetch_data()
        def add_students(self):
                con=pymysql.connect(host="localhost",user="root",password="",database="stm")
                cur=con.cursor()
                cur.execute("INSERT INTO students VALUES (%s,%s,%s,%s,%s,%s,%s)",(
                    self.roll_no.get(),
                    self.name.get(),
                    self.email.get(),
                    self.gender.get(),
                    self.contact.get(),
                    self.dob.get(),
                    self.txt_address.get('1.0', END)
                ))
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
        def fetch_data(self):
                con=pymysql.connect(host="localhost",user="root",password="",database="stm")
                cur=con.cursor()
                cur.execute("SELECT * FROM students")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert('',END,values=row)
                con.commit()
                con.close()
        def clear(self):
                self.roll_no.set("")
                self.name.set("")
                self.email.set("")
                self.gender.set("")
                self.contact.set("")
                self.dob.set("")
                self.txt_address.delete("1.0",END)
        def get_cursor(self,ev):
                cursor_row=self.student_table.focus()
                contents=self.student_table.item(cursor_row)
                row=contents['values']
                self.roll_no.set(row[0])
                self.name.set(row[1])
                self.email.set(row[2])
                self.gender.set(row[3])
                self.contact.set(row[4])
                self.dob.set(row[5])
                self.txt_address.delete("1.0",END)
                self.txt_address.insert(END,row[6]) 
        def update_data(self):
                con=pymysql.connect(host="localhost",user="root",password="",database="stm")
                cur=con.cursor()

                cur.execute("UPDATE students SET name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s WHERE roll_no=%s",(
                        self.name.get(),
                        self.email.get(),
                        self.gender.get(),
                        self.contact.get(),
                        self.dob.get(),
                        self.txt_address.get('1.0', END),
                        self.roll_no.get()
                ))

                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
        def delete_data(self):
                con=pymysql.connect(host="localhost",user="root",password="",database="stm")                    
                cur=con.cursor()
                cur.execute("DELETE FROM students WHERE roll_no=%s",self.roll_no.get())
                con.commit()
                con.close()
                self.fetch_data()
                self.clear()
        def search_data(self):
                con=pymysql.connect(host="localhost",user="root",password="",database="stm")
                cur=con.cursor()  
                                                                      
                cur.execute("SELECT * FROM students WHERE "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert('',END,values=row)
                con.commit()
                con.close()     
        
              
root = Tk()             
ob=Student(root)
root.mainloop()