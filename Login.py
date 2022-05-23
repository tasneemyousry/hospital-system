from tkinter import *
from PIL import ImageTk, Image
import doctor_login_page
import nurse_login_page
import staff_login_page


class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Login Page')

        self.window['bg']='#ebfafa'

     
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window,width=1100,height=600,bg='white')
        self.lgn_frame.place(x=100, y=80)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "WELCOME"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#FFFFFF",
                             fg='#de1738',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=215, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('images\hospital.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image_doctor = Image.open('images\doctor.jpg')
        self.resized=self.sign_in_image_doctor.resize((150,150))
        photo = ImageTk.PhotoImage(self.resized)
        self.sign_in_image_doctor_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.sign_in_image_doctor_label.image = photo
        self.sign_in_image_doctor_label.place(x=700, y=50)


        
        self.sign_in_image_nurse = Image.open('images\ic_nurse.png')
        self.resized=self.sign_in_image_nurse.resize((130,130))
        photo = ImageTk.PhotoImage(self.resized)
        self.sign_in_image_nurse_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.sign_in_image_nurse_label.image = photo
        self.sign_in_image_nurse_label.place(x=710, y=230)




        self.sign_in_image_manager = Image.open('images\manager.jpg')
        self.resized=self.sign_in_image_manager.resize((145,155))
        photo = ImageTk.PhotoImage(self.resized)
        self.sign_in_image_manager_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.sign_in_image_manager_label.image = photo
        self.sign_in_image_manager_label.place(x=705, y=400)

        
        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.doctor_button_label = Label(self.lgn_frame, bg='#ADD8E6',height=2,width=25)
        self.doctor_button_label.place(x=870, y=120)
        self.login_doctor = Button(self.doctor_button_label, text='LOGIN AS A DOCTOR', font=("yu gothic ui", 10, "bold"),bd=0,
                            bg='#ADD8E6', cursor='hand2', activebackground='#3047ff', fg='white',command=self.go_to_doctor_login)

        self.login_doctor.place(x=20, y=5)


        self.nurse_button_label = Label(self.lgn_frame, bg='#F03801',width=25,height=2)
        self.nurse_button_label.image = photo
        self.nurse_button_label.place(x=870, y=280)
        self.login_nurse = Button(self.nurse_button_label, text='LOGIN AS A NURSE', font=("yu gothic ui", 10, "bold"),bd=0,
                            bg='#F03801', cursor='hand2', activebackground='#3047ff', fg='white',command=self.go_to_nurse_login)
        self.login_nurse.place(x=20, y=5)


      
        self.manager_button_label = Label(self.lgn_frame, width=25,height=2,bg='#46a2da')
        self.manager_button_label.place(x=870, y=450)
        self.login_manager = Button(self.manager_button_label, text='LOGIN AS A STAFF', font=("yu gothic ui", 10, "bold"), bd=0,
                            bg='#46a2da', cursor='hand2', activebackground='#3047ff', fg='white',command=self.go_to_staff_login)
        self.login_manager.place(x=20, y=5)




        # =========== Sign Up ==================================================
        self.sign_label = Label(self.window, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, fg='black',bg='#ffffff')
        self.sign_label.place(x=850, y=640)

        self.signup_button_label = Button(self.window,text='REGISTER', font=("yu gothic ui", 10, "bold"), bg="#de1738", cursor="hand2",
                                          borderwidth=0,fg='#ffffff', activebackground="#FFFFFF",width=8,height=2)
        self.signup_button_label.place(x=980, y=630)

      
    def go_to_doctor_login(self):
        win =Toplevel()
        doctor_login_page.DoctorLoginPage(win)
        self.window.withdraw()
        win.deiconify

    def go_to_nurse_login(self):
        win =Toplevel()
        nurse_login_page.NurseLoginPage(win)
        self.window.withdraw()
        win.deiconify

    def go_to_staff_login(self):
        win =Toplevel()
        staff_login_page.StaffLoginPage(win)
        self.window.withdraw()
        win.deiconify




def login_page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    login_page()