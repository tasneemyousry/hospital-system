from tkinter import *
from PIL import ImageTk, Image
import doctor_homepage
import add_diagnosis
import edit_diagnosis
import show_history
import Login

class Doctor:      
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x800')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Doctor Homepage')

        self.window['bg']='#ff8776'
    # ====== Frame =========================
        self.frame = Frame(self.window,width=1000,height=700,bg='#fec3a6')
        self.frame.place(x=150, y=30)

    #=========frame pic======================
        self.image = Image.open('images\clinic.jpg')
        self.resized = self.image.resize((1000,500))
        photo = ImageTk.PhotoImage(self.resized)

        self.image_label = Label(self.frame, image=photo, bg='#fec3a6')
        self.image_label.image = photo
        self.image_label.place(x=0,y=0)

    #=======add and edit diagnosis button + show history button ===========
        self.diagnosis_button = Button(self.frame,text='Add Diagnosis', font=("yu gothic ui", 15, "bold"), bg="#ff8776", cursor="hand2",
                                      borderwidth=0,fg='#ffffff', activebackground="#FFFFFF",width=17,height=1,command=self.add_diagnosis)
        self.diagnosis_button.place(x=160, y=525)

        self.diagnosis_button = Button(self.frame,text='Edit Diagnosis', font=("yu gothic ui", 15, "bold"), bg="#ff8776", cursor="hand2",
                                      borderwidth=0,fg='#ffffff', activebackground="#FFFFFF",width=17,height=1,command=self.edit_diagnosis)
        self.diagnosis_button.place(x=430, y=525)

        self.diagnosis_button = Button(self.frame,text='Show History', font=("yu gothic ui", 15, "bold"), bg="#ff8776", cursor="hand2",
                                      borderwidth=0,fg='#ffffff', activebackground="#FFFFFF",width=17,height=1,command=self.show_history)
        self.diagnosis_button.place(x=700, y=525)


    #=====back button==========
        self.back_button = Button(self.frame,text='Back', font=("yu gothic ui", 16, "bold"), bg="#4F77AA", cursor="hand2",
                                      borderwidth=0,fg='#ffffff', activebackground="#FFFFFF",width=6,height=1,command= self.back)
        self.back_button.place(x=50, y=600)

    #======log out button======
        self.logout_button = Button(self.frame,text='Log out', font=("yu gothic ui", 16, "bold"), bg="#4F77AA", cursor="hand2",
                                      borderwidth=0,fg='#ffffff', activebackground="#FFFFFF",width=6,height=1,command= self.logout)
        self.logout_button.place(x=870, y=600)


    #=====back function=========
    def back(self):
      win =Toplevel()
      doctor_homepage.DoctorHomepage(win)
      self.window.withdraw()
      win.deiconify  

    
  #======log out function=========
    def logout(self):
      win =Toplevel()
      Login.LoginPage(win)
      self.window.withdraw()
      win.deiconify  

    def add_diagnosis(self):
      win =Toplevel()
      add_diagnosis.AddDiagnosis(win)
      self.window.withdraw()
      win.deiconify 


    def edit_diagnosis(self):
      win =Toplevel()
      edit_diagnosis.EditDiagnosis(win)
      self.window.withdraw()
      win.deiconify 


    def show_history(self):
      win =Toplevel()
      show_history.ShowHistory(win)
      self.window.withdraw()
      win.deiconify 


    
def doctor():
    window = Tk()
    Doctor(window)
    window.mainloop()


if __name__ == '__main__':
  doctor()