from tkinter import *
import sql_test
import doctor
import doctor_homepage
import Login


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

    
    
   

    #========select querey + gui==============
        select_query="""select distinct past_diagnosis from history where patient_id==?"""
        patient_id=doctor_homepage.DoctorHomepage.entered_id
        sql_test.sqlBase.cursor.execute(select_query,(patient_id))
        result= sql_test.sqlBase.cursor.fetchall()

        if(result):
        #=========history label ============
            self.history_label = Label(self.frame, text="Patient History", bg="#fec3a6", fg="black",
                                    font=("Times New Roman", 22, "bold"))
            self.history_label.place(x=100, y=40)
    
            
            

        #=======displaying column headers===============
            self.e= Label(self.frame,width=10,text="Patient ID",fg='white',bg='#ff8776', font=("Times New Roman", 16, "bold"))
            self.e.place(x=70,y=90)
            # self.e= Label(self.frame,width=15,text="Nurse ID",fg='white',bg='#ff8776', font=("Times New Roman", 16, "bold"))
            # self.e.place(x=290,y=90)
            self.e= Label(self.frame,width=55,text="Past Diagnosis",fg='white',bg='#ff8776', font=("Times New Roman", 16, "bold"))
            self.e.place(x=70,y=130)

            self.entry1= Label(self.frame,width=44,text=patient_id,height=1,fg='black',bg='#ffffff',
                            font=("Times New Roman", 15, "bold"),borderwidth=2,relief=RIDGE)
            self.entry1.place(x=203,y=90)
            c=170
            
            for record in result :   
                    self.entry2= Text(self.frame,width=66,height=3,fg='black',bg='#ffffff',
                            font=("Times New Roman", 15, "bold"),borderwidth=2,relief=RIDGE)
                    self.entry2.insert(END,record[0])
                    self.entry2.place(x=70,y=c)
                    self.entry2.config(state=DISABLED)
                    c+=85
        
        else:
            self.no_entries_box= Label(self.frame,text="The patient has no history.",
                                        bg="#fec3a6",fg="black",font=("Times New Roman ",18, "bold"))

            self.no_entries_box.place(x=230,y=250)


    # ========back button============
        self.back_button = Button(self.window,text='Back', font=("yu gothic ui", 16, "bold"), bg="#4F77AA", cursor="hand2",
                                      borderwidth=0,fg='#ffffff', activebackground="#FFFFFF",width=6,height=1,command= self.back)
        self.back_button.place(x=195, y=635)

     #=======log out button===============
        self.logout_button = Button(self.window,text='Log out', font=("yu gothic ui", 16, "bold"), bg="#4F77AA", cursor="hand2",
                                      borderwidth=0,fg='#ffffff', activebackground="#FFFFFF",width=6,height=1,command= self.logout)
        self.logout_button.place(x=1010, y=635)

    #======log out function=========
    def logout(self):
      win =Toplevel()
      Login.LoginPage(win)
      self.window.withdraw()
      win.deiconify  



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
