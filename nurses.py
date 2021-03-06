
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
ASSETS_PATH = OUTPUT_PATH / Path("./Nurses_assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Nurses:
    def __init__(self,window):

        self.window = window
        self.window.title("Nurses")
        self.window.resizable(False, False)
        self.window.geometry("1440x900")
        self.window.state('zoomed')
        self.window.configure(bg = "#FFFFFF")


        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 810,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            65.0,
            20.0,
            anchor="nw",
            text="Add Nurse",
            fill="#000000",
            font=("Inter Light", 20 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("nurse_id1.png"))
        self.entry_bg_1 = canvas.create_image(
            213.0,
            125.0,
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
            y=100.0,
            width=314.0,
            height=48.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("phone_number2.png"))
        self.entry_bg_2 = canvas.create_image(
            213.0,
            270.0,
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
            y=245.0,
            width=314.0,
            height=48.0
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("first_name3.png"))
        self.entry_bg_3 = canvas.create_image(
            763.0,
            125.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            self.window,
            bd=0,
            bg="#ECE8F2",
            highlightthickness=0
        )
        self.entry_3.place(
            x=606.0,
            y=100.0,
            width=314.0,
            height=48.0
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("birthdate4.png"))
        self.entry_bg_4 = canvas.create_image(
            763.0,
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
            x=606.0,
            y=247.0,
            width=314.0,
            height=48.0
        )

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("last_name5.png"))
        self.entry_bg_5 = canvas.create_image(
            1263.0,
            125.0,
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
            y=100.0,
            width=314.0,
            height=48.0
        )

        self.entry_image_6 = PhotoImage(
            file=relative_to_assets("gender6.png"))
        self.entry_bg_6 = canvas.create_image(
            1263.0,
            266.0,
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
            y=241.0,
            width=314.0,
            height=48.0
        )

        self.entry_image_7 = PhotoImage(
            file=relative_to_assets("password7.png"))
        self.entry_bg_7 = canvas.create_image(
            214.0,
            402.0,
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
            y=377.0,
            width=314.0,
            height=48.0
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("add_nurse.png"))
        button_1 = Button(
            self.window,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_nurse(),
            relief="flat"
        )
        button_1.image= button_image_1
        button_1.place(
            x=606.0,
            y=465.0,
            width=314.0,
            height=45.0
        )

        canvas.create_text(
            22.0,
            538.0,
            anchor="nw",
            text="Deleter Nurse",
            fill="#000000",
            font=("Inter Light", 20 * -1)
        )

        self.entry_image_8 = PhotoImage(
            file=relative_to_assets("nurse_2id8.png"))
        self.entry_bg_8 = canvas.create_image(
            213.0,
            647.0,
            image=self.entry_image_8
        )
        self.entry_8 = Entry(
            self.window,
            bd=0,
            bg="#E3DEEC",
            highlightthickness=0
        )
        self.entry_8.place(
            x=56.0,
            y=622.0,
            width=314.0,
            height=48.0
        )

        canvas.create_text(
            606.0,
            586.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1)
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self.window,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:self.delete_nurse(),
            relief="flat"
        )

        button_2.place(
            x=606.0,
            y=738.0,
            width=314.0,
            height=45.0
        )
        button_2.image = button_image_2
        canvas.create_text(
            69.0,
            71.0,
            anchor="nw",
            text="Nurse ID",
            fill="#40325C",
            font=("Inter SemiBold", 20 * -1)
        )

        canvas.create_text(
            616.0,
            71.0,
            anchor="nw",
            text="First name",
            fill="#40325C",
            font=("Inter SemiBold", 20 * -1)
        )

        canvas.create_text(
            1111.0,
            71.0,
            anchor="nw",
            text="Last name",
            fill="#594D70",
            font=("Inter SemiBold", 20 * -1)
        )

        canvas.create_text(
            65.0,
            217.0,
            anchor="nw",
            text="Phone Number",
            fill="#40325C",
            font=("Inter SemiBold", 20 * -1)
        )

        canvas.create_text(
            616.0,
            221.0,
            anchor="nw",
            text="Birthdate",
            fill="#40325C",
            font=("Inter SemiBold", 20 * -1)
        )

        canvas.create_text(
            65.0,
            345.0,
            anchor="nw",
            text="Password",
            fill="#40325C",
            font=("Inter SemiBold", 20 * -1)
        )

        canvas.create_text(
            65.0,
            593.0,
            anchor="nw",
            text="Nurse ID",
            fill="#40325C",
            font=("Inter SemiBold", 20 * -1)
        )

        canvas.create_text(
            1111.0,
            210.0,
            anchor="nw",
            text="Gender",
            fill="#40325C",
            font=("Inter SemiBold", 20 * -1)
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
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
            x=28.0,
            y=748.0,
            width=120.0,
            height=35.0
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
        button_4.image = button_image_4
        button_4.place(
            x=1376.0,
            y=25.0,
            width=64.07025146484375,
            height=29.0
        )

        self.entry_image_9 = PhotoImage(
            file=relative_to_assets("password9.png"))
        self.entry_bg_9 = canvas.create_image(
            763.5,
            647.0,
            image=self.entry_image_9
        )
        self.entry_9 = Entry(
            self.window,
            bd=0,
            bg="#E3DEEC",
            highlightthickness=0
        )
        self.entry_9.place(
            x=606.0,
            y=622.0,
            width=315.0,
            height=48.0
        )

        canvas.create_rectangle(
            0.0,
            567.0,
            1974.0,
            568.0,
            fill="#D9D9D9",
            outline="")

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

    def add_nurse(self):
        id_entry = self.entry_1.get()
        phonenumber_entry = self.entry_2.get()
        fisrtname_entry = self.entry_3.get()
        birthdate_entry = self.entry_4.get()
        lastname_entry = self.entry_5.get()
        gender_entry= self.entry_6.get()
        password_entry = self.entry_7.get()


        add_inputs = """insert or replace into staff(staff_id, gender, first_name, last_name, phone_no, birth_date, password) values(?,?,?,?,?,?,?)"""
        sql_test.sqlBase.cursor.execute(add_inputs, (id_entry , gender_entry, fisrtname_entry, lastname_entry, phonenumber_entry, birthdate_entry, password_entry,))

        add_inputs1 = """insert into nurse(nurse_id) values(?) """
        sql_test.sqlBase.cursor.execute(add_inputs1, [id_entry])

        self.entry_1.delete(0,END)
        self.entry_2.delete(0,END)
        self.entry_3.delete(0,END)
        self.entry_4.delete(0,END)
        self.entry_6.delete(0,END)
        self.entry_5.delete(0,END)
        self.entry_7.delete(0,END)

        sql_test.sqlBase.conn.commit()

    def delete_nurse(self):
        entered_nurse_id = self.entry_8.get()
        entered_password = self.entry_9.get()
        
        select_staff =  ("select * from staff where staff_id==? ")
        sql_test.sqlBase.cursor.execute(select_staff,[entered_nurse_id])

        querey_result = sql_test.sqlBase.cursor.fetchone()

        if (querey_result):
            update_nurse= (""" delete from staff 
              where staff_id ==? and password ==?""")
            
            sql_test.sqlBase.cursor.execute(update_nurse,(entered_nurse_id, entered_password))


            self.entry_8.delete(0,END)
            self.entry_9.delete(0,END)
            
        else:
            messagebox.showwarning("use add button to add nurse", "Nurse id does not exist!")

        sql_test.sqlBase.conn.commit()

def nurses():
    window = Tk()
    Nurses(window)
    window.mainloop()

if __name__ == '__main__':
    nurses()