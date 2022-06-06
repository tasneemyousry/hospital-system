from tkinter import *
from PIL import ImageTk, Image
import nurse_homepage
import nurse_login_page
import sql_test


class PatientInfo:
    def __init__(self, window):
        self.window=window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Patient info')
        self.window['bg']='#FFFFFF'

        # ========================================================================
        # ============ rooms Image ================================================
        # ========================================================================
        self.nurse_homepage_image=Image.open('images\homepage.jpg')
        self.resized=self.nurse_homepage_image.resize((600,400))
        photo = ImageTk.PhotoImage(self.resized)
        self.nurse_homepage_image_label = Label(self.window, image=photo, bg='#FFFFFF')
        self.nurse_homepage_image_label.image = photo
        self.nurse_homepage_image_label.place(x=700, y=50)

        #============= patient id Label===============
        self.label = Label(self.window, text="Patient ID", bg='#FFFFFF',fg="black",
                                    font=("Times New Roman", 18, "bold"))
        self.label.place(x=300, y=550)

        #=====patient id entry box==========
        self.patient_id_entry = Entry(self.window, highlightthickness=3,relief=FLAT, bg="#ffffff", fg="black",
                                font=("Times New Roman ", 14, "bold"),width=20)
        self.patient_id_entry.place(x=430, y=550)


        #=====show info button==========
        self.add_button = Button(self.window,text='Show info', font=("yu gothic ui", 15, "bold"), bg="#90FFBD", cursor="hand2",
                                    borderwidth=0,fg='#000000', activebackground="#FFFFFF",width=17,height=1,command=self.show)
        self.add_button.place(x=800, y=540)

        #=====back button==========
        self.back_button = Button(self.window,text='Back', font=("yu gothic ui", 16, "bold"), bg="#4F77AA", cursor="hand2",
                                      borderwidth=0,fg='#000000', activebackground="#FFFFFF",width=6,height=1,command= self.back)
        self.back_button.place(x=50, y=600)

        #=======log out button ===========
        self.logout_button = Button(self.window,text='logout', font=("yu gothic ui", 15, "bold","underline"), bg="#FFFFFF", cursor="hand2",
                                    borderwidth=0,fg='#000000', activebackground="#FFFFFF",width=17,height=1,command=self.logout)
        self.logout_button.place(x=1200, y=40)

    def show(self):
       #========select querey==============
        PatientInfo.patient_id =self.patient_id_entry.get()
        select_query=("""select * from patient where patient_id==?""")
        sql_test.sqlBase.cursor.execute(select_query,(PatientInfo.patient_id))
        result= sql_test.sqlBase.cursor.fetchone()

        if(result):
            
            print_records=''
            for record in result :
                    print_records += str(record) + " "
            self.entry= Label(self.window,text=print_records,width=20,height=1,fg='black',bg='#ffffff',
                       font=("Times New Roman", 18, "bold"))
            self.entry.place(x=200,y=200)
        
        else:
            self.no_entries_box= Label(self.window,text="patient does not exist",
                                        bg="#ffffff",fg="black",font=("Times New Roman ",18, "bold"))

            self.no_entries_box.place(x=200,y=200)

        self.patient_id_entry.delete(0,END)

    

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

def patient_info():
    window = Tk()
    PatientInfo(window)
    window.mainloop()


if __name__ == '__main__':
  patient_info()