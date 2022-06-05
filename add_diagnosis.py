from tkinter import *
import datetime
import sql_test
from tkinter import messagebox
import doctor
import doctor_login_page
import doctor_homepage
import Login

class AddDiagnosis:      
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x800')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Add Diagnosis')

        self.window['bg']='#ff8776'
    # ====== Frame =========================
        self.frame = Frame(self.window,width=800,height=600,bg='#fec3a6')
        self.frame.place(x=250, y=30)


    #========diagnosis entry box==============
        self.diagnosis_label = Label(self.frame, text="Diagnosis", bg="#fec3a6", fg="black",
                                    font=("Times New Roman", 22, "bold"))
        self.diagnosis_label.place(x=100, y=40)

        self.diagnosis_entry = Text(self.frame,relief=RIDGE,borderwidth=4, bg="#ffffff", fg="black",
                                    font=("Times New Roman ", 14, "bold"),width=60,height=8,wrap=WORD)
        self.diagnosis_entry.place(x=70, y=80)




    #========prescription entry box=================
        self.prescription_label = Label(self.frame, text="Prescription", bg="#fec3a6", fg="black",
                                    font=("Times New Roman", 22, "bold"))
        self.prescription_label.place(x=100, y=270)

        self.prescription_entry = Text(self.frame,relief=RIDGE,borderwidth=4, bg="#ffffff", fg="black",
                                    font=("Times New Roman ", 14, "bold"),width=60,height=5,wrap=WORD)
        self.prescription_entry.place(x=70, y=310)


    #==========add diagnosis button============
        self.add = Button(self.frame,text='Add', font=("yu gothic ui", 15, "bold"), bg="#ff8776", cursor="hand2",
                                      borderwidth=0,fg='#ffffff', activebackground="#FFFFFF",width=8,height=1,command=self.add)
        self.add.place(x=620, y=470)

    # ========back button============
        self.back_button = Button(self.window,text='Back', font=("yu gothic ui", 16, "bold"), bg="#4F77AA", cursor="hand2",
                                      borderwidth=0,fg='#ffffff', activebackground="#FFFFFF",width=6,height=1,command= self.back)
        self.back_button.place(x=195, y=635)


    #=======log out button===============
        self.logout_button = Button(self.window,text='Log out', font=("yu gothic ui", 16, "bold"), bg="#4F77AA", cursor="hand2",
                                      borderwidth=0,fg='#ffffff', activebackground="#FFFFFF",width=6,height=1,command= self.logout)
        self.logout_button.place(x=1010, y=635)

    def add(self):
        entered_diagnosis = self.diagnosis_entry.get("1.0","end-1c")
        entered_prescription = self.prescription_entry.get("1.0","end-1c")
        doctor_id= doctor_login_page.DoctorLoginPage.entered_username
        patient_id=doctor_homepage.DoctorHomepage.entered_id
        diagnosis_date= datetime.datetime.now()


        #======searching doctor and patient id in diagnosis table========
        select_query_diagnosis='''select * from give_diagnosis 
        where patient_id==? and doctor_id==?'''
        sql_test.sqlBase.cursor.execute(select_query_diagnosis,(patient_id,doctor_id))
        querey_result = sql_test.sqlBase.cursor.fetchone()

        if(querey_result):
            messagebox.showwarning("Warning","Can't add a new diagnosis, try to update it instead from the update page.")
        else:
            add_inputs ="""insert into give_diagnosis(doctor_id,patient_id,diagnosis,prescription,diagnosis_date) values(?,?,?,?,?)"""
            sql_test.sqlBase.cursor.execute(add_inputs,(doctor_id,patient_id,entered_diagnosis,entered_prescription,diagnosis_date))
 
            add_to_history="""insert into history (patient_id,past_diagnosis) values(?,?)""" 
            sql_test.sqlBase.cursor.execute(add_to_history,(patient_id,entered_diagnosis))
            
            self.diagnosis_entry.delete('1.0',END)
            self.prescription_entry.delete('1.0',END)



        sql_test.sqlBase.conn.commit()
        
        
    def back(self):
        win =Toplevel()
        doctor.Doctor(win)
        self.window.withdraw()
        win.deiconify 

    #======log out function=========
    def logout(self):
      win =Toplevel()
      Login.LoginPage(win)
      self.window.withdraw()
      win.deiconify  

def add_diagnosis():
    window = Tk()
    AddDiagnosis(window)
    window.mainloop()


