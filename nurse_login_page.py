from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sql_test
import Login
import nurse_homepage


class NurseLoginPage:
    entered_username=NONE
    entered_pass=None
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Nurse Login Page')

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
        self.sign_in_image_nurse = Image.open('images\ic_nurse.png')
        self.resized=self.sign_in_image_nurse.resize((150,150))
        photo = ImageTk.PhotoImage(self.resized)
        self.sign_in_image_nurse_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.sign_in_image_nurse_label.image = photo
        self.sign_in_image_nurse_label.place(x=800, y=50)


        
            # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="ID", bg="#ffffff", fg="black",
                                    font=("Times New Roman", 18, "bold"))
        self.username_label.place(x=750, y=200)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#ffffff", fg="black",
                                    font=("Times New Roman ", 13, "bold"))
        self.username_entry.place(x=750, y=230, width=200)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#d3d3d3", highlightthickness=0)
        self.username_line.place(x=750, y=250)
  

         # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#ffffff", fg="black",
                                    font=("Times New Roman", 18, "bold"))
        self.password_label.place(x=750, y=270)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#ffffff", fg="black",
                                    show='*',font=("Times New Roman", 13, "bold"))
        self.password_entry.place(x=750, y=300, width=200)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#d3d3d3", highlightthickness=0)
        self.password_line.place(x=750, y=320)
      

        # =========== Sign in ==================================================
        self.signin_button_label = Button(self.window,text='SIGN IN', font=("yu gothic ui", 10, "bold"), bg="#de1738", cursor="hand2",
                                          borderwidth=0,fg='#ffffff', activebackground="#FFFFFF",width=8,height=2,command=self.signIn)
        self.signin_button_label.place(x=950, y=450)


        # ==============back to login button=====================
        self.back_to_login_label = Button(self.window,text='Back To Login', font=("yu gothic ui", 12, "bold"), bg="#1e2f97", cursor="hand2",
                                          borderwidth=0,fg='#ffffff', activebackground="#FFFFFF",width=20,height=2,command=self.go_back_to_login)
        self.back_to_login_label.place(x=900, y=550)


    def go_back_to_login(self):
        win =Toplevel()
        Login.LoginPage(win)
        self.window.withdraw()
        win.deiconify  

    def signIn(self):
        NurseLoginPage.entered_username =self.username_entry.get()
        NurseLoginPage.entered_pass = self.password_entry.get()

        find_user= ("""select staff_id,password 
        from (select staff.'staff_id', staff.'password'
        from staff,nurse
        where staff.'staff_id'=nurse.'nurse_id' )
        where staff_id ==? and password==?
        """)

        sql_test.sqlBase.cursor.execute(find_user,[NurseLoginPage.entered_username,NurseLoginPage.entered_pass])

        result= sql_test.sqlBase.cursor.fetchone()
        
        if result:
            pass
            win =Toplevel()
            nurse_homepage.NurseHomepage(win)
            self.window.withdraw()
            win.deiconify  
            
        else:
            messagebox.showerror("Can't login", "Invalid Credentials")
    

def nurse_login_page():
    window = Tk()
    NurseLoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    nurse_login_page()