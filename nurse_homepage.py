from tkinter import *
from PIL import ImageTk, Image
import nurse_login_page
import patients
import patient_info
import guardians
import nurse_history



class NurseHomepage:
    def __init__(self, window):
        self.window=window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Nurse homepage')
        self.window['bg']='#FFFFFF'

        # ========================================================================
        # ============ nurse homepage Image ================================================
        # ========================================================================
        self.nurse_homepage_image=Image.open('images\homepage.jpg')
        self.resized=self.nurse_homepage_image.resize((700,500))
        photo = ImageTk.PhotoImage(self.resized)
        self.nurse_homepage_image_label = Label(self.window, image=photo, bg='#FFFFFF')
        self.nurse_homepage_image_label.image = photo
        self.nurse_homepage_image_label.place(x=300, y=5)


        #=======add delete and update patinent button ,add delete and update rooms button ===========
        self.patient_button = Button(self.window,text='Patients', font=("yu gothic ui", 15, "bold"), bg="#90FFBD", cursor="hand2",
                                    borderwidth=0,fg='#000000', activebackground="#FFFFFF",width=17,height=1,command=self.patients)
        self.patient_button.place(x=160, y=550)

        self.room_button = Button(self.window,text='show patient info', font=("yu gothic ui", 15, "bold"), bg="#90FFBD", cursor="hand2",
                                    borderwidth=0,fg='#000000', activebackground="#FFFFFF",width=17,height=1,command=self.patient_info)
        self.room_button.place(x=430, y=550)

        #=======retrieve patient history button, guardians button ===============
        self.history_button = Button(self.window,text='Patient History', font=("yu gothic ui", 15, "bold"), bg="#90FFBD", cursor="hand2",
                                    borderwidth=0,fg='#000000', activebackground="#FFFFFF",width=17,height=1,command=self.history)
        self.history_button.place(x=700, y=550)

        self.guardians_button = Button(self.window,text='Guardians', font=("yu gothic ui", 15, "bold"), bg="#90FFBD", cursor="hand2",
                                    borderwidth=0,fg='#000000', activebackground="#FFFFFF",width=17,height=1,command=self.guardians)
        self.guardians_button.place(x=970, y=550)

        #=======log out button ===========
        self.logout_button = Button(self.window,text='logout', font=("yu gothic ui", 15, "bold","underline"), bg="#FFFFFF", cursor="hand2",
                                    borderwidth=0,fg='#000000', activebackground="#FFFFFF",width=17,height=1,command=self.logout)
        self.logout_button.place(x=1200, y=40)


    
    def patients(self):
        win=Toplevel()
        patients.Patients(win)
        self.window.withdraw()
        win.deiconify 
    
    def patient_info(self):
        win=Toplevel()
        patient_info.PatientInfo(win)
        self.window.withdraw()
        win.deiconify
    
    def history(self):
        win=Toplevel()
        nurse_history.NurseHistory(win)
        self.window.withdraw()
        win.deiconify
    
    def guardians(self):
        win=Toplevel()
        guardians.Guardians(win)
        self.window.withdraw()
        win.deiconify

    #=====logout function=========
    def logout(self):
        win=Toplevel()
        nurse_login_page.NurseLoginPage(win)
        self.window.withdraw()
        win.deiconify





def nurse_homepage():
    window = Tk()
    NurseHomepage(window)
    window.mainloop()


if __name__ == '__main__':
  nurse_homepage()