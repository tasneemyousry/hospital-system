from textwrap import wrap
from tkinter import *
import datetime
import Login
import sql_test
import doctor
import doctor_login_page 
import doctor_homepage

class EditDiagnosis:      
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x800')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Edit Diagnosis')

        self.window['bg']='#ff8776'
    # ====== Frame =========================
        self.frame = Frame(self.window,width=800,height=600,bg='#fec3a6')
        self.frame.place(x=250, y=30)

    
    #===========past diagnosis and prescription==============
        select_query= """select diagnosis,prescription from give_diagnosis where patient_id==? and doctor_id==?"""
        p_id=doctor_homepage.DoctorHomepage.entered_id
        d_id=doctor_login_page.DoctorLoginPage.entered_username
        sql_test.sqlBase.cursor.execute(select_query,(p_id,d_id))

        query_result= sql_test.sqlBase.cursor.fetchone()
       
        if(query_result):
            diagnosis_text= query_result[0]+"\nPrescription:"+ query_result[1]
            self.past_diagnosis_label = Label(self.frame, text="Past Diagnosis And Prescription", bg="#fec3a6", fg="black",
                                    font=("Times New Roman", 22, "bold"))
            self.past_diagnosis_label.place(x=100, y=40)

            self.past_diagnosis= Text(self.frame,relief=RIDGE,borderwidth=4, bg="#ffffff", fg="black",
                                    font=("Times New Roman ", 14, "bold"),width=60,height=4,wrap=WORD)
            self.past_diagnosis.insert(END,diagnosis_text)
            self.past_diagnosis.config(state=DISABLED)
            

            self.past_diagnosis.place(x=70, y=80)


        #========diagnosis entry box==============
            self.diagnosis_label = Label(self.frame, text="New Diagnosis", bg="#fec3a6", fg="black",
                                        font=("Times New Roman", 22, "bold"))
            self.diagnosis_label.place(x=100, y=180)

            self.diagnosis_entry = Text(self.frame,relief=RIDGE,borderwidth=4, bg="#ffffff", fg="black",
                                        font=("Times New Roman ", 14, "bold"),width=60,height=4,wrap=WORD)
            self.diagnosis_entry.place(x=70, y=220)

        #========prescription entry box=================
            self.prescription_label = Label(self.frame, text="New Prescription", bg="#fec3a6", fg="black",
                                        font=("Times New Roman", 22, "bold"))
            self.prescription_label.place(x=100, y=320)

            self.prescription_entry = Text(self.frame,relief=RIDGE,borderwidth=4, bg="#ffffff", fg="black",
                                        font=("Times New Roman ", 14, "bold"),width=60,height=2,wrap=WORD)
            self.prescription_entry.place(x=70, y=360)



        #==========update diagnosis button============
            self.add = Button(self.frame,text='Update', font=("yu gothic ui", 15, "bold"), bg="#ff8776", cursor="hand2",
                                            borderwidth=0,fg='#ffffff', activebackground="#FFFFFF",width=8,height=1,command=self.update)
            self.add.place(x=620, y=470)


        
          

            
        else:
            self.no_entries_box= Label(self.frame,text="No previous Entries, try adding a diagnosis from the add page",
                                        bg="#fec3a6",fg="black",font=("Times New Roman ",18, "bold"))

            self.no_entries_box.place(x=40,y=250)

        # ========back button============
        self.back_button = Button(self.window,text='Back', font=("yu gothic ui", 16, "bold"), bg="#4F77AA", cursor="hand2",
                                            borderwidth=0,fg='#ffffff', activebackground="#FFFFFF",width=6,height=1,command= self.back)
        self.back_button.place(x=195, y=635)
        #=======log out button===============
        self.logout_button = Button(self.window,text='Log out', font=("yu gothic ui", 16, "bold"), bg="#4F77AA", cursor="hand2",
                                      borderwidth=0,fg='#ffffff', activebackground="#FFFFFF",width=6,height=1,command= self.logout)
        self.logout_button.place(x=1010, y=635)

    def update(self):
        entered_diagnosis = self.diagnosis_entry.get("1.0","end-1c")
        entered_prescription = self.prescription_entry.get("1.0","end-1c")
        doctor_id= doctor_login_page.DoctorLoginPage.entered_username
        patient_id=doctor_homepage.DoctorHomepage.entered_id
        diagnosis_date= datetime.datetime.now()

        update_query = """update give_diagnosis 
        set diagnosis= ?,
        prescription = ?,
        diagnosis_date= ?
        where patient_id== ? and doctor_id== ?"""

        sql_test.sqlBase.cursor.execute(update_query,(entered_diagnosis,entered_prescription,diagnosis_date,patient_id,doctor_id))
        add_to_history="""insert into history (patient_id,past_diagnosis) values(?,?)""" 
        sql_test.sqlBase.cursor.execute(add_to_history,(patient_id,entered_diagnosis))
        self.diagnosis_entry.delete('1.0',END)
        self.prescription_entry.delete('1.0',END)



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



def edit_diagnosis():
    window = Tk()
    EditDiagnosis(window)
    window.mainloop()



if __name__ == '__main__':
  edit_diagnosis()