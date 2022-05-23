from tkinter import *
import sql_test
import doctor
import doctor_homepage


class ShowHistory:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x800')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('History')

        self.window['bg']='#ff8776'
    # ====== Frame =========================
        self.frame = Frame(self.window,width=800,height=600,bg='#fec3a6')
        self.frame.place(x=250, y=30)

    
    #=========history label ============
        self.history_label = Label(self.frame, text="Patient History", bg="#fec3a6", fg="black",
                                    font=("Times New Roman", 22, "bold"))
        self.history_label.place(x=100, y=40)

    #========select querey + gui==============
        select_query="""select * from history where patient_id==?"""
        patient_id=doctor_homepage.DoctorHomepage.entered_id
        sql_test.sqlBase.cursor.execute(select_query,(patient_id))

    
        r=90
        c=130

    #=======displaying column headers===============
        self.e= Label(self.frame,width=15,text="Patient ID",fg='white',bg='#ff8776', font=("Times New Roman", 16, "bold"))
        self.e.place(x=90,y=90)
        self.e= Label(self.frame,width=15,text="Nurse ID",fg='white',bg='#ff8776', font=("Times New Roman", 16, "bold"))
        self.e.place(x=290,y=90)
        self.e= Label(self.frame,width=15,text="Past Diagnosis",fg='white',bg='#ff8776', font=("Times New Roman", 16, "bold"))
        self.e.place(x=490,y=90)


        
        for record in sql_test.sqlBase.cursor:
            for j in range(len(record)):
                self.entry= Label(self.frame,text=record[j],width=15,height=3,fg='black',bg='#ffffff',
                        font=("Times New Roman", 15, "bold"),borderwidth=2,relief=RIDGE)
                self.entry.place(x=r,y=c)
                r+=200
            #     line = Canvas(self.frame, width=300, height=2.0, bg="#d3d3d3", highlightthickness=0)
            # line.grid(row=r+5)
            c+=40
    


    # ========back button============
        self.back_button = Button(self.window,text='Back', font=("yu gothic ui", 16, "bold"), bg="#4F77AA", cursor="hand2",
                                      borderwidth=0,fg='#ffffff', activebackground="#FFFFFF",width=6,height=1,command= self.back)
        self.back_button.place(x=195, y=635)







    def back(self):
        win =Toplevel()
        doctor.Doctor(win)
        self.window.withdraw()
        win.deiconify 




def show_history():
    window = Tk()
    ShowHistory(window)
    window.mainloop()


if __name__ == '__main__':
  show_history()