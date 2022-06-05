
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, messagebox
import staff_homepage
import staff_login_page
import sql_test



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./doctors_assets") 


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Doctors:
    def __init__(self, window):
        self.window = window
        self.window.title("Staff manager homepage")
        self.window.geometry("1440x810")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)
        self.window.state('zoomed')
        self.window.configure(bg = "#FFFFFF")

        frame = Frame(self.window,
                      bg="#FFFFFF",
                      height=810,
                      width=1440,
                      bd=0,
                      highlightthickness=0,
                      relief="ridge"
                      )
        frame.place(x=0, y=0)

        canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 810,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            29.0,
            28.0,
            anchor="nw",
            text="Add Doctor",
            fill="#000000",
            font=("Inter Light", 20 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("doctor_id1.png"))
        self.entry_bg_1 = canvas.create_image(
            213.5,
            127.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            self.window,
            bd=0,
            bg="#ECE8F2",
            highlightthickness=0
        )
        self.entry_1.place(
            x=56.0,
            y=102.0,
            width=215.0,
            height=48.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("phone_number2.png"))
        self.entry_bg_2 = canvas.create_image(
            213.5,
            272.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            self.window,
            bd=0,
            bg="#ECE8F2",
            highlightthickness=0
        )
        self.entry_2.place(
            x=56.0,
            y=247.0,
            width=315.0,
            height=48.0
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("first_name3.png"))
        self.entry_bg_3 = canvas.create_image(
            762.5,
            127.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            self.window,
            bd=0,
            bg="#ECE8F2",
            highlightthickness=0
        )
        self.entry_3.place(
            x=605.0,
            y=102.0,
            width=315.0,
            height=48.0
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("birthdate4.png"))
        self.entry_bg_4 = canvas.create_image(
            773.5,
            272.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            self.window,
            bd=0,
            bg="#ECE8F2",
            highlightthickness=0
        )
        self.entry_4.place(
            x=616.0,
            y=247.0,
            width=315.0,
            height=48.0
        )

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("last_name5.png"))
        self.entry_bg_5 = canvas.create_image(
            1263.5,
            122.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            self.window,
            bd=0,
            bg="#ECE8F2",
            highlightthickness=0
        )
        self.entry_5.place(
            x=1106.0,
            y=97.0,
            width=315.0,
            height=48.0
        )

        self.entry_image_6 = PhotoImage(
            file=relative_to_assets("speciallity6.png"))
        self.entry_bg_6 = canvas.create_image(
            1263.5,
            264.0,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            self.window,
            bd=0,
            bg="#ECE8F2",
            highlightthickness=0
        )
        self.entry_6.place(
            x=1106.0,
            y=239.0,
            width=315.0,
            height=48.0
        )

        self.entry_image_7 = PhotoImage(
            file=relative_to_assets("password7.png"))
        self.entry_bg_7 = canvas.create_image(
            214.5,
            404.0,
            image=self.entry_image_7
        )
        self.entry_7 = Entry(
            self.window,
            bd=0,
            bg="#ECE8F2",
            highlightthickness=0
        )
        self.entry_7.place(
            x=57.0,
            y=379.0,
            width=315.0,
            height=48.0
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("add_doc1.png"))
        button_1 = Button(
            self.window,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_doctor(),
            relief="flat"
        )
        button_1.image= button_image_1 
        button_1.place(
            x=616.0,
            y=493.0,
            width=315.0,
            height=45.0
        )

        canvas.create_text(
            10.0,
            538.0,
            anchor="nw",
            text="Deleter Doctor",
            fill="#000000",
            font=("Inter Light", 20 * -1)
        )

        self.entry_image_8 = PhotoImage(
            file=relative_to_assets("doctor_2id8.png"))
        self.entry_bg_8 = canvas.create_image(
            214.5,
            656.0,
            image=self.entry_image_8
        )
        self.entry_8 = Entry(
            self.window,
            bd=0,
            bg="#E3DEEC",
            highlightthickness=0
        )
        self.entry_8.place(
            x=57.0,
            y=631.0,
            width=315.0,
            height=48.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("delete_doc2.png"))
        button_2 = Button(
            self.window,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.delete_doctor(),
            relief="flat"
        )
        button_2.image= button_image_2
        button_2.place(
            x=616.0,
            y=733.0,
            width=315.0,
            height=45.0
        )

        canvas.create_text(
            69.0,
            73.0,
            anchor="nw",
            text="Doctor ID",
            fill="#40325C",
            font=("Inter SemiBold", 20 * -1)
        )

        canvas.create_text(
            616.0,
            73.0,
            anchor="nw",
            text="First name",
            fill="#40325C",
            font=("Inter SemiBold", 20 * -1)
        )

        canvas.create_text(
            1111.0,
            68.0,
            anchor="nw",
            text="Last name",
            fill="#594D70",
            font=("Inter SemiBold", 20 * -1)
        )

        canvas.create_text(
            62.0,
            215.0,
            anchor="nw",
            text="Phone Number",
            fill="#40325C",
            font=("Inter SemiBold", 20 * -1)
        )

        canvas.create_text(
            627.0,
            219.0,
            anchor="nw",
            text="Birthdate",
            fill="#40325C",
            font=("Inter SemiBold", 20 * -1)
        )

        canvas.create_text(
            1111.0,
            210.0,
            anchor="nw",
            text="Speciality",
            fill="#40325C",
            font=("Inter SemiBold", 20 * -1)
        )

        canvas.create_text(
            65.0,
            347.0,
            anchor="nw",
            text="Password",
            fill="#40325C",
            font=("Inter SemiBold", 20 * -1)
        )

        canvas.create_text(
            69.0,
            602.0,
            anchor="nw",
            text="Doctor ID",
            fill="#40325C",
            font=("Inter SemiBold", 20 * -1)
        )

        self.entry_image_9 = PhotoImage(
            file=relative_to_assets("gender9.png"))
        self.entry_bg_9 = canvas.create_image(
            773.5,
            401.0,
            image=self.entry_image_9
        )
        self.entry_9 = Entry(
            self.window,
            bd=0,
            bg="#ECE8F2",
            highlightthickness=0
        )
        self.entry_9.place(
            x=616.0,
            y=376.0,
            width=315.0,
            height=48.0
        )

        canvas.create_text(
            631.0,
            352.0,
            anchor="nw",
            text="Gender",
            fill="#40325C",
            font=("Inter SemiBold", 20 * -1)
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("back3.png"))
        button_3 = Button(
            self.window,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.back(),
            relief="flat"
        )
        button_3.image= button_image_3
        button_3.place(
            x=50.0,
            y=756.0,
            width=110.0,
            height=30.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            self.window,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.logout(),
            relief="flat"
        )
        button_4.image= button_image_4
        button_4.place(
            x=1377.0,
            y=26.0,
            width=63.0079345703125,
            height=30.5
        )

        self.entry_image_10 = PhotoImage(
            file=relative_to_assets("password10.png"))
        self.entry_bg_10 = canvas.create_image(
            773.5,
            656.0,
            image=self.entry_image_10
        )
        self.entry_10 = Entry(
            self.window,
            bd=0,
            bg="#E3DEEC",
            highlightthickness=0
        )
        self.entry_10.place(
            x=616.0,
            y=631.0,
            width=315.0,
            height=48.0
        )

        canvas.create_rectangle(
            100.0,
            567.0,
            2500.0,
            568.0,
            fill="#D9D9D9",
            outline="")

        canvas.create_text(
            619.0,
            602.0,
            anchor="nw",
            text="Password",
            fill="#40325C",
            font=("Inter SemiBold", 20 * -1)
        )

    def back(self):
        win=Toplevel()
        staff_homepage.StaffHomePage(win)
        self.window.withdraw()
        win.deiconify

    def logout(self):
        win = Toplevel()
        staff_login_page.StaffLoginPage(win)
        self.window.withdraw()
        win.deiconify

    def add_doctor(self):
        entered_id = self.entry_1.get()
        entered_phonenumber = self.entry_2.get()
        entered_firstname = self.entry_3.get()
        entered_birthdate = self.entry_4.get()
        entered_lastname = self.entry_5.get()
        entered_speciality= self.entry_6.get()
        entered_password = self.entry_7.get()
        entered_gender= self.entry_9.get()

        add_inputs = """insert into staff(staff_id, gender, first_name, last_name, phone_no, birth_date, password) values(?,?,?,?,?,?,?)"""
        sql_test.sqlBase.cursor.execute(add_inputs, (entered_id , entered_gender, entered_firstname, entered_lastname,
        entered_phonenumber, entered_birthdate, entered_password))

        add_inputs1 = """insert into doctor(doctor_id, speciality) values(?,?) """
        sql_test.sqlBase.cursor.execute(add_inputs1, (entered_id, entered_speciality))

        self.entry_1.delete(0,END)
        self.entry_2.delete(0,END)
        self.entry_3.delete(0,END)
        self.entry_4.delete(0,END)
        self.entry_6.delete(0,END)
        self.entry_5.delete(0,END)
        self.entry_7.delete(0,END)
        self.entry_9.delete(0,END)
        

        sql_test.sqlBase.conn.commit()

    def delete_doctor(self):
        entered_doctotr_id = self.entry_8.get()
        entered_password = self.entry_10.get()
        
        select_staff =  ("select * from staff where staff_id==? ")
        sql_test.sqlBase.cursor.execute(select_staff,[entered_doctotr_id])

        querey_result = sql_test.sqlBase.cursor.fetchone()

        if (querey_result):
            update_doctor= (""" delete from staff 
              where staff_id ==? and password ==?""")
            sql_test.sqlBase.cursor.execute(update_doctor,(entered_doctotr_id, entered_password))

            
            self.entry_8.delete(0,END)
            self.entry_10.delete(0, END)
        else:
            messagebox.showwarning( "Doctor id does not exist!", "Please enter the correct id or password")


        sql_test.sqlBase.conn.commit()
    

    

def doctors():
    window = Tk()
    Doctors(window)
    window.mainloop()

if __name__ == '__main__':
    doctors()