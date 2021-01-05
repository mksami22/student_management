from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import pymysql
class Students:
    def __init__(self, root):
        self.root = root
        self.root.title("STUDENT INFORMATION")
        self.root.geometry("1350x700+0+0")
        self.root.iconbitmap('C:/Users/gupta/Desktop/images.ico')
        self.Roll = StringVar()
        self.name = StringVar()
        self.email = StringVar()
        self.pphone =StringVar()
        self.attendance = StringVar()
        self.remark = StringVar()
        self.LastCalled = StringVar()
        self.search_by = StringVar()
        self.search_text = StringVar()

        image_frame=Frame(self.root,bd=4, relief = GROOVE, bg="light sea green")
        image_frame.place(x=2,y=2,width=1270, height=80)
        image = ImageTk.PhotoImage(Image.open('C:/Users/gupta/Desktop/ok.jpg'))
        image_label = Label(image_frame,image=image)
        image_label.image = image
        image_label.place(x=15,y=10)
        title = Label(image_frame, text="MENTORING DETAILS", font=("times now roman", 40, "bold italic"), bg="light sea green", fg="white")
        title.place(x=350,y=0)


        manage_frame = Frame(self.root, bd=4, relief=GROOVE, bg="light sea green")
        manage_frame.place(x=20, y=90, width=450, height=560)
        m_title = Label(manage_frame, text="Manage Students", font=("times now roman", 25, "bold italic"), bg="light sea green" , fg="white")
        m_title.grid(row=0, columnspan=2, pady=20)

        roll_label = Label(manage_frame, text="Roll number", font=("times now roman", 15, "bold italic"),
                           bg="light sea green", fg="white")
        roll_label.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        text_roll = Entry(manage_frame,textvariable = self.Roll, font=("times now roman", 15, "bold italic"))
        text_roll.grid(row=1, column=1, pady=10, padx=20)
        name_label = Label(manage_frame, text="Name", font=("times now roman", 15, "bold italic"),
                           bg="light sea green", fg="white")
        name_label.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        text_name = Entry(manage_frame,textvariable = self.name,font=("times now roman", 15, "bold italic"))
        text_name.grid(row=2, column=1, pady=10, padx=20)
        email_label = Label(manage_frame, text="Email", font=("times now roman", 15, "bold italic"),
                            bg="light sea green", fg="white")
        email_label.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        text_email = Entry(manage_frame,textvariable = self.email ,font=("times now roman", 15, "bold italic"))
        text_email.grid(row=3, column=1, pady=10, padx=20)
        attend_label = Label(manage_frame, text="Attendace ", font=("times now roman", 15, "bold italic"),
                            bg="light sea green", fg="white")
        attend_label.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        attend_entry = Entry(manage_frame,textvariable = self.attendance, font=("times now roman", 15, "bold italic"))
        attend_entry.grid(row=4, column=1, pady=10, padx=20)
        remark_lable = Label(manage_frame, text="Remark ", font=("times now roman", 15, "bold italic"),
                             bg="light sea green", fg="white")
        remark_lable.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        remark_entry = Entry(manage_frame, textvariable=self.remark, font=("times now roman", 15, "bold italic"))
        remark_entry.grid(row=5, column=1, pady=10, padx=20)
        last_label = Label(manage_frame, text="Last called ", font=("times now roman", 15, "bold italic"),
                            bg="light sea green", fg="white")
        last_label.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        last_entry = Entry(manage_frame,textvariable=self.LastCalled, font=("times now roman", 15, "bold italic"))
        last_entry.grid(row=6, column=1, pady=10, padx=20)
        pphone_label = Label(manage_frame, text="Parents Phone", font=("times now roman", 15, "bold italic"),
                             bg="light sea green", fg="white")
        pphone_label.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        pphone_name = Entry(manage_frame, textvariable=self.pphone, font=("times now roman", 15, "bold italic"))
        pphone_name.grid(row=7, column=1, pady=10, padx=20)
        button_frame = Frame(manage_frame, bd=4, relief=RIDGE, bg="light sea green")
        button_frame.place(x=45, y=500, width=350,)
        add_button = Button(button_frame, text="Add", width=10, command=self.Add_student).grid(row=0, column=0)
        update_button = Button(button_frame, text="Update", width=11,command=self.update).grid(row=0, column=1, pady=10)
        delete_button = Button(button_frame, text="Delete", width=11, command=self.delete).grid(row=0, column=2, pady=10)
        clear_button = Button(button_frame, text="clear",width=11, command=self.clear).grid(row=0, column=3, pady=10)

        detail_frame = Frame(self.root, bd=4, relief=GROOVE, bg="light sea green")
        detail_frame.place(x=500, y=90, width=770, height=560)
        search_label = Label(detail_frame, text="SEARCH", font=("times now roman", 15, "bold italic"),
                           bg="light sea green", fg="white")
        search_label.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        combo_search=ttk.Combobox(detail_frame,textvariable=self.search_by,width=10,font=("times now roman", 15, "bold italic"))
        combo_search['values']=("roll", "Name")
        combo_search.grid(row=0, column = 1,padx=20,pady=10)
        text_search = Entry(detail_frame,textvariable=self.search_text, font=("times now roman", 15, "bold italic"))
        text_search.grid(row=0, column=2, pady=10, padx=20)
        search_button = Button(detail_frame, text="Search", width=10,command=self.search).grid(row=0, column=3,padx=10,pady=10)
        show_button = Button(detail_frame, text="Show", width=10, command=self.fetch).grid(row=0, column=4, padx=10, pady=10)


        table_frame=Frame(detail_frame, bd=4, relief=RIDGE, bg="white")
        table_frame.place(x=10,y=70,width=750,height=480)
        scroll_x = Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.Table=ttk.Treeview(table_frame, columns=("roll","name","Email", "Attendance", "Remark","Last called", "Parents Phone"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Table.xview)
        scroll_y.config(command=self.Table.yview)
        self.Table.heading("roll",text="Roll number")
        self.Table.heading("name", text="Name")
        self.Table.heading("Email", text="Email")
        self.Table.heading("Attendance", text="Attendance")
        self.Table.heading("Remark", text="Remark")
        self.Table.heading("Last called", text="Last Called")
        self.Table.heading("Parents Phone", text="Parents Phone")
        self.Table['show']='headings'
        self.Table.column("roll", width=80)
        self.Table.column("name", width=120)
        self.Table.column("Email", width=120)
        self.Table.column("Attendance", width=50)
        self.Table.column("Remark", width=120)
        self.Table.column("Last called", width=120)
        self.Table.column("Parents Phone", width=120)
        self.Table.pack(fill=BOTH,expand=1)
        self.Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch()
    def Add_student(self):
        con=pymysql.connect(host="localhost",user="root",password="",database= "stm")
        cur=con.cursor()
        cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll.get(),
                                                                         self.name.get(),
                                                                         self.email.get(),
                                                                         self.attendance.get(),
                                                                         self.remark.get(),
                                                                         self.LastCalled.get(),
                                                                         self.pphone.get()))
        con.commit()
        self.fetch()
        self.clear()
        con.close()
    def fetch(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from student")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Table.delete(*self.Table.get_children())
            for row in rows:
                self.Table.insert('',END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.Roll.set("")
        self.name.set("")
        self.email.set("")
        self.attendance.set("")
        self.remark.set("")
        self.LastCalled.set("")
        self.pphone.set("")
    def get_cursor(self, ev):
        cursor_row=self.Table.focus()
        content=self.Table.item(cursor_row)
        row=content['values']
        self.Roll.set(row[0])
        self.name.set(row[1])
        self.email.set(row[2])
        self.attendance.set(row[3])
        self.remark.set(row[4])
        self.LastCalled.set(row[5])
        self.pphone.set(row[6])
    def search(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        print("SELECT * FROM student WHERE " + str(self.search_by.get()) + " LIKE '%" + str(self.search_text.get()) + "%'")
        cur.execute(
            "SELECT * FROM student WHERE " + str(self.search_by.get()) + " LIKE '%" + str(self.search_text.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Table.delete(*self.Table.get_children())
            for row in rows:
                self.Table.insert('', END, values=row)
            con.commit()
        con.close()
    def update(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("update student set Name=%s,Email=%s,Attendance=%s,Remark=%s,LastCalled=%s,PPhone=%s where roll=%s",
                                                                  (self.name.get(),
                                                                         self.email.get(),
                                                                         self.attendance.get(),
                                                                         self.remark.get(),
                                                                         self.LastCalled.get(),
                                                                         self.pphone.get(),
                                                                         self.Roll.get()
                                                                        ))
        con.commit()
        self.fetch()
        self.clear()
        con.close()
    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("delete from student where roll=%s",self.Roll.get())
        con.commit()
        con.close()
        self.fetch()
        self.clear()
root = Tk()
obj = Students(root)
root.mainloop()
