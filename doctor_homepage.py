from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sql_test
import doctor_login_page
import doctor
import Login


class DoctorHomepage:
  entered_id=None
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

#=============Patient id entry box===============
    self.label = Label(self.frame, text="Patient ID", bg='#fec3a6',fg="black",
                                    font=("Times New Roman", 20, "bold"))
    self.label.place(x=250,y=530)

#======= entry box=============
    self.patient_id_entry = Entry(self.frame, highlightthickness=2,relief=FLAT, bg="#ffffff", fg="black",
                                font=("Times New Roman ", 14, "bold"),width=20)
    self.patient_id_entry.place(x=385,y=535)

#=====sumbit button===========
    self.submit_button = Button(self.frame,text='OK', font=("yu gothic ui", 12, "bold"), bg="#ff8776", cursor="hand2",
                                      borderwidth=0,fg='#ffffff', activebackground="#FFFFFF",width=5,height=1,command=self.ok)
    self.submit_button.place(x=620, y=535)


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
      doctor_login_page.DoctorLoginPage(win)
      self.window.withdraw()
      win.deiconify  


#======log out function=========
  def logout(self):
      win =Toplevel()
      Login.LoginPage(win)
      self.window.withdraw()
      win.deiconify  
#===log in function ==========
  def ok(self):
    DoctorHomepage.entered_id =self.patient_id_entry.get()
    
    find_user= ("""select patient_id
    from patient
    where patient_id ==? """)

    sql_test.sqlBase.cursor.execute(find_user,[DoctorHomepage.entered_id])

    result= sql_test.sqlBase.cursor.fetchone()
    
    if result:
      win =Toplevel()
      doctor.Doctor(win)
      self.window.withdraw()
      win.deiconify  
      
    else:
      messagebox.showerror("Error!","Can't find the specified patient.")


    
def doctor_home_page():
    window = Tk()
    DoctorHomepage(window)
    window.mainloop()


if __name__ == '__main__':
  doctor_home_page()