from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import datetime
import nurse_homepage
import nurse_login_page
import sql_test



class Patients:
    def __init__(self, window):
        self.window=window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Patients')
        self.window['bg']='#FFFFFF'

        # ========================================================================
        # ============ patient Image ================================================
        # ========================================================================
        self.nurse_homepage_image=Image.open('images\homepage.jpg')
        self.resized=self.nurse_homepage_image.resize((600,400))
        photo = ImageTk.PhotoImage(self.resized)
        self.nurse_homepage_image_label = Label(self.window, image=photo, bg='#FFFFFF')
        self.nurse_homepage_image_label.image = photo
        self.nurse_homepage_image_label.place(x=700, y=50)

        #=============Labels===============
        self.label = Label(self.window, text="Patient ID", bg='#FFFFFF',fg="black",
                                    font=("Times New Roman", 18, "bold"))
        self.label.place(x=200,y=50)
        self.label = Label(self.window, text="First name", bg='#FFFFFF',fg="black",
                                    font=("Times New Roman", 18, "bold"))
        self.label.place(x=200,y=100)
        self.label = Label(self.window, text="Last name", bg='#FFFFFF',fg="black",
                                    font=("Times New Roman", 18, "bold"))
        self.label.place(x=200,y=150)
        self.label = Label(self.window, text="gender", bg='#FFFFFF',fg="black",
                                    font=("Times New Roman", 18, "bold"))
        self.label.place(x=200,y=200)
        self.label = Label(self.window, text="Address", bg='#FFFFFF',fg="black",
                                    font=("Times New Roman", 18, "bold"))
        self.label.place(x=200,y=250)
        self.label = Label(self.window, text="phone number", bg='#FFFFFF',fg="black",
                                    font=("Times New Roman", 18, "bold"))
        self.label.place(x=200,y=300)
        self.label = Label(self.window, text="room id", bg='#FFFFFF',fg="black",
                                    font=("Times New Roman", 18, "bold"))
        self.label.place(x=200,y=350)
        self.label = Label(self.window, text="birth date", bg='#FFFFFF',fg="black",
                                    font=("Times New Roman", 18, "bold"))
        self.label.place(x=200,y=400)
        #=====entry boxes==========
        self.patient_id_entry = Entry(self.window, highlightthickness=3,relief=FLAT, bg="#ffffff", fg="black",
                                font=("Times New Roman ", 14, "bold"),width=20)
        self.patient_id_entry.place(x=385,y=50)
        self.first_name_entry = Entry(self.window, highlightthickness=3,relief=FLAT, bg="#ffffff", fg="black",
                                font=("Times New Roman ", 14, "bold"),width=20)
        self.first_name_entry.place(x=385,y=100)
        self.last_name_entry = Entry(self.window, highlightthickness=3,relief=FLAT, bg="#ffffff", fg="black",
                                font=("Times New Roman ", 14, "bold"),width=20)
        self.last_name_entry.place(x=385,y=150)
        self.gender_entry = Entry(self.window, highlightthickness=3,relief=FLAT, bg="#ffffff", fg="black",
                                font=("Times New Roman ", 14, "bold"),width=20)
        self.gender_entry.place(x=385,y=200)
        self.address_entry = Entry(self.window, highlightthickness=3,relief=FLAT, bg="#ffffff", fg="black",
                                font=("Times New Roman ", 14, "bold"),width=20)
        self.address_entry.place(x=385,y=250)
        self.phone_number_entry = Entry(self.window, highlightthickness=3,relief=FLAT, bg="#ffffff", fg="black",
                                font=("Times New Roman ", 14, "bold"),width=20)
        self.phone_number_entry.place(x=385,y=300)
        self.room_id_entry = Entry(self.window, highlightthickness=3,relief=FLAT, bg="#ffffff", fg="black",
                                font=("Times New Roman ", 14, "bold"),width=20)
        self.room_id_entry.place(x=385,y=350)
        self.birth_date_entry = Entry(self.window, highlightthickness=3,relief=FLAT, bg="#ffffff", fg="black",
                                font=("Times New Roman ", 14, "bold"),width=20)
        self.birth_date_entry.place(x=385,y=400)

        #=====buttons==========
        self.add_button = Button(self.window,text='Add patient', font=("yu gothic ui", 15, "bold"), bg="#90FFBD", cursor="hand2",
                                    borderwidth=0,fg='#000000', activebackground="#FFFFFF",width=17,height=1,command=self.add)
        self.add_button.place(x=430, y=550)
        self.delete_button = Button(self.window,text='Delete patient', font=("yu gothic ui", 15, "bold"), bg="#90FFBD", cursor="hand2",
                                    borderwidth=0,fg='#000000', activebackground="#FFFFFF",width=17,height=1,command=self.delete)
        self.delete_button.place(x=700, y=550)
        self.edit_button = Button(self.window,text='Edit patient', font=("yu gothic ui", 15, "bold"), bg="#90FFBD", cursor="hand2",
                                    borderwidth=0,fg='#000000', activebackground="#FFFFFF",width=17,height=1,command=self.edit)
        self.edit_button.place(x=970, y=550)

        #=====back button==========
        self.back_button = Button(self.window,text='Back', font=("yu gothic ui", 16, "bold"), bg="#4F77AA", cursor="hand2",
                                      borderwidth=0,fg='#000000', activebackground="#FFFFFF",width=6,height=1,command= self.back)
        self.back_button.place(x=50, y=600)

        #=======log out button ===========
        self.logout_button = Button(self.window,text='logout', font=("yu gothic ui", 15, "bold","underline"), bg="#FFFFFF", cursor="hand2",
                                    borderwidth=0,fg='#000000', activebackground="#FFFFFF",width=17,height=1,command=self.logout)
        self.logout_button.place(x=1200, y=40)
    
    #=======add function===========
    def add(self):
       patient_id = self.patient_id_entry.get()
       first_name = self.first_name_entry.get()
       last_name = self.last_name_entry.get()
       gender = self.gender_entry.get()
       address = self.address_entry.get()
       phone_number = self.phone_number_entry.get()
       room_id = self.room_id_entry.get()
       birth_date = self.birth_date_entry.get()

       #======make sure patient exists ========
       select_query="select * from patient where patient_id==? "
       sql_test.sqlBase.cursor.execute(select_query,(patient_id))
       querey_result = sql_test.sqlBase.cursor.fetchone()

       if(querey_result):
            messagebox.showwarning("Patient id exists!","use Edit button to update info")
       else:
            add_patient =("""insert into patient(patient_id,first_name,last_name,gender,address,phone_no,room_id,birth_date)
                          values(?,?,?,?,?,?,?,?)""")
            sql_test.sqlBase.cursor.execute(add_patient,(patient_id,first_name,last_name,gender,address,phone_number,room_id,birth_date))
            
            #======clear inputs========
            self.patient_id_entry.delete(0,END)
            self.first_name_entry.delete(0,END)
            self.last_name_entry.delete(0,END)
            self.gender_entry.delete(0,END)
            self.address_entry.delete(0,END)
            self.phone_number_entry.delete(0,END)
            self.room_id_entry.delete(0,END)
            self.birth_date_entry.delete(0,END)
            

           
       sql_test.sqlBase.conn.commit()


    #=======delete function===========   
    def delete(self):
       patient_id = self.patient_id_entry.get()

       #======make sure patient does not exist alredy========
       select_query="select * from patient where patient_id==? "
       sql_test.sqlBase.cursor.execute(select_query,(patient_id))
       querey_result = sql_test.sqlBase.cursor.fetchone()

       if(querey_result):
            update_patient =("""delete from patient 
             where patient_id==?""")
            sql_test.sqlBase.cursor.execute(update_patient,(patient_id))
            
            #======clear inputs========
            self.patient_id_entry.delete(0,END)
            self.first_name_entry.delete(0,END)
            self.last_name_entry.delete(0,END)
            self.gender_entry.delete(0,END)
            self.address_entry.delete(0,END)
            self.phone_number_entry.delete(0,END)
            self.room_id_entry.delete(0,END)
            self.birth_date_entry.delete(0,END)

       else:
            messagebox.showwarning("Patient id does not exist!","use add button to add patient")

       sql_test.sqlBase.conn.commit()

    #=======update function===========
    def edit(self):
       patient_id = self.patient_id_entry.get()
       first_name = self.first_name_entry.get()
       last_name = self.last_name_entry.get()
       gender = self.gender_entry.get()
       address = self.address_entry.get()
       phone_number = self.phone_number_entry.get()
       room_id = self.room_id_entry.get()
       birth_date = self.birth_date_entry.get()

       #======make sure patient does not exist alredy========
       select_query="select * from patient where patient_id==? "
       sql_test.sqlBase.cursor.execute(select_query,(patient_id))
       querey_result = sql_test.sqlBase.cursor.fetchone()

       if(querey_result):
            update_patient =("""update patient set
             first_name=?,
             last_name=?,
             gender=?,
             address=?,
             phone_no=?,
             room_id=?,
             birth_date=?
             where patient_id==?""")
            sql_test.sqlBase.cursor.execute(update_patient,(first_name,last_name,gender,address,phone_number,room_id,birth_date,patient_id))
            
            #======clear inputs========
            self.patient_id_entry.delete(0,END)
            self.first_name_entry.delete(0,END)
            self.last_name_entry.delete(0,END)
            self.gender_entry.delete(0,END)
            self.address_entry.delete(0,END)
            self.phone_number_entry.delete(0,END)
            self.room_id_entry.delete(0,END)
            self.birth_date_entry.delete(0,END)

       else:
            messagebox.showwarning("Patient id does not exist!","use add button to add patient")

       sql_test.sqlBase.conn.commit()

    #=====back function=========
    def back(self):
        win =Toplevel()
        nurse_homepage.NurseHomepage(win)
        self.window.withdraw()
        win.deiconify  

    #=====logout function=========
    def logout(self):
        win=Toplevel()
        nurse_login_page.NurseLoginPage(win)
        self.window.withdraw()
        win.deiconify

def patients():
    window = Tk()
    Patients(window)
    window.mainloop()


if __name__ == '__main__':
  patients()