from tkinter import *
import datetime
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


    #========diagnosis entry box==============
        self.diagnosis_label = Label(self.frame, text="New Diagnosis", bg="#fec3a6", fg="black",
                                    font=("Times New Roman", 22, "bold"))
        self.diagnosis_label.place(x=100, y=40)

        self.diagnosis_entry = Text(self.frame,relief=RIDGE,borderwidth=4, bg="#ffffff", fg="black",
                                    font=("Times New Roman ", 14, "bold"),width=60,height=8)
        self.diagnosis_entry.place(x=70, y=80)




    #========prescription entry box=================
        self.prescription_label = Label(self.frame, text="New Prescription", bg="#fec3a6", fg="black",
                                    font=("Times New Roman", 22, "bold"))
        self.prescription_label.place(x=100, y=270)

        self.prescription_entry = Text(self.frame,relief=RIDGE,borderwidth=4, bg="#ffffff", fg="black",
                                    font=("Times New Roman ", 14, "bold"),width=60,height=5)
        self.prescription_entry.place(x=70, y=310)

   

    #==========update diagnosis button============
        self.add = Button(self.frame,text='Update', font=("yu gothic ui", 15, "bold"), bg="#ff8776", cursor="hand2",
                                      borderwidth=0,fg='#ffffff', activebackground="#FFFFFF",width=8,height=1,command=self.update)
        self.add.place(x=620, y=470)

    # ========back button============
        self.back_button = Button(self.window,text='Back', font=("yu gothic ui", 16, "bold"), bg="#4F77AA", cursor="hand2",
                                      borderwidth=0,fg='#ffffff', activebackground="#FFFFFF",width=6,height=1,command= self.back)
        self.back_button.place(x=195, y=635)


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

        sql_test.sqlBase.conn.commit()


    def back(self):
        win =Toplevel()
        doctor.Doctor(win)
        self.window.withdraw()
        win.deiconify 



def edit_diagnosis():
    window = Tk()
    EditDiagnosis(window)
    window.mainloop()


if __name__ == '__main__':
  edit_diagnosis()