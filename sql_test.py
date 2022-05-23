from multiprocessing.dummy import current_process
import sqlite3


class sqlBase():
      cursor = None
      conn =None
      

      try:
         conn= sqlite3.connect("H.db")
      finally:
         if conn:
            conn.execute("PRAGMA foreign_keys=ON")
            cursor = conn.cursor()
            
            cursor.execute(""" create table if not exists DOCTOR (
                DOCTOR_ID            int       not null,
                SPECIALITY           text       null,
                constraint PK_DOCTOR primary key (DOCTOR_ID),
                constraint FK_DOCTOR_IS_STAFF foreign key (DOCTOR_ID)
                references STAFF (STAFF_ID)
                on update cascade on delete cascade
            )
        """)


            cursor.execute("""create table if not exists GIVE_DIAGNOSIS (
            DOCTOR_ID            int                  not null,
            PATIENT_ID           int                  not null,
   DIAGNOSIS            text                 not null,
   PRESCRIPTION         text                 not null,
   DIAGNOSIS_DATE       datetime             not null,
   constraint PK_GIVE_DIAGNOSIS primary key (DOCTOR_ID, PATIENT_ID, DIAGNOSIS_DATE),
   constraint FK_GIVE_DIA_GIVE_DIAG_DOCTOR foreign key (DOCTOR_ID)
      references DOCTOR (DOCTOR_ID)
         on update cascade,
    constraint FK_GIVE_DIA_GIVE_DIAG_PATIENT foreign key (PATIENT_ID)
      references PATIENT (PATIENT_ID)
         on update cascade on delete cascade

)""")

            cursor.execute("""create table if not exists GUARDIANS (
   PATIENT_ID           int                  not null,
   NURSE_ID             int                  not null,
   PHONE_NO             bigint               not null,
   RELATIONSHIP_TO_PATIENT varchar(50)          null,
   constraint PK_GUARDIANS primary key (PATIENT_ID, NURSE_ID),
   constraint FK_GUARDIAN_CAN_CONTA_NURSE foreign key (NURSE_ID)
      references NURSE (NURSE_ID)
         on update cascade,
    
    constraint FK_GUARDIAN_HAS_CONTA_PATIENT foreign key (PATIENT_ID)
      references PATIENT (PATIENT_ID)
         on update cascade
)""")

            cursor.execute("""create table if not exists HISTORY (
   PATIENT_ID           int                  not null,
   NURSE_ID             int                  not null,
   PAST_DIAGNOSIS       text                 not null,
   constraint PK_HISTORY primary key (PATIENT_ID, NURSE_ID),
   constraint FK_HISTORY_HAS_PATIENT foreign key (PATIENT_ID)
      references PATIENT (PATIENT_ID)
         on update cascade on delete cascade,
    constraint FK_HISTORY_OBTAINS_NURSE foreign key (NURSE_ID)
      references NURSE (NURSE_ID)
         on update cascade
    
)""")

            cursor.execute("""create table if not exists HOLDS (
   STAFF_ID             int                  not null,
   constraint PK_HOLDS primary key (STAFF_ID),
    constraint FK_HOLDS_HOLDS_STAFF foreign key (STAFF_ID)
      references STAFF (STAFF_ID)
         on update cascade on delete cascade

)""")


            cursor.execute("""create table if not exists NURSE (
   NURSE_ID             int                  not null,  
   constraint PK_NURSE primary key (NURSE_ID),
   constraint FK_NURSE_IS_A_STAFF foreign key (NURSE_ID)
      references STAFF (STAFF_ID)
         on update cascade on delete cascade
)""")

            cursor.execute("""create table if not exists OBSERVE (
   NURSE_ID             int                  not null,
   ROOM_ID              varchar(10)          not null,
   constraint PK_OBSERVE primary key (NURSE_ID, ROOM_ID),
    constraint FK_OBSERVE_OBSERVE_NURSE foreign key (NURSE_ID)
      references NURSE (NURSE_ID)
         on update cascade on delete cascade,
    constraint FK_OBSERVE_OBSERVE2_ROOM foreign key (ROOM_ID)
      references ROOM (ROOM_ID)
         on update cascade on delete cascade
)""")


            cursor.execute("""create table if not exists PATIENT (
   FIRST_NAME           varchar(50)          not null,
   LAST_NAME            varchar(50)          null,
   GENDER               char(256)            null,
   ADDRESS              varchar(100)         null,
   PHONE_NO             bigint               null,
   PATIENT_ID           int                  not null,
   ROOM_ID              varchar(10)          null,
   BIRTH_DATE           datetime             null,
   constraint PK_PATIENT primary key (PATIENT_ID),
   constraint FK_PATIENT_ASSIGN_TO_ROOM foreign key (ROOM_ID)
      references ROOM (ROOM_ID)
         on update cascade
)""")


            cursor.execute("""create table if not exists ROOM (
   ROOM_ID              varchar(10)          not null,
   PATIENT_ID           int                  null,
   DATE_ADMITTED        datetime             not null,
   DATE_DISCHARGED      datetime             not null,
   constraint PK_ROOM primary key (ROOM_ID),
   constraint FK_ROOM_ASSIGN_TO_PATIENT foreign key (PATIENT_ID)
      references PATIENT (PATIENT_ID)

)""")

            cursor.execute("""create table if not exists SHIFT (
   STAFF_ID             int                  not null,
   START_TIME           datetime             not null,
   END_TIME             datetime             not null,
   constraint PK_SHIFT primary key (STAFF_ID, START_TIME, END_TIME),
   constraint FK_SHIFT_HOLDS2_HOLDS foreign key (STAFF_ID)
      references HOLDS (STAFF_ID)
         on update cascade on delete cascade
   
)""")

            cursor.execute("""create table if not exists STAFF (
   STAFF_ID             int                  not null,
   GENDER               char(256)            null,
   FIRST_NAME           varchar(50)          null,
   LAST_NAME            varchar(50)          null,
   PHONE_NO             bigint               null,
   BIRTH_DATE           datetime             null,
   password             text                 not null,
   constraint PK_STAFF primary key (STAFF_ID)
  )""")




            # cursor.execute("delete from staff")
      

            # cursor.execute("""insert into staff(staff_id,password) values(7,"123")""")
            # cursor.execute("""insert into nurse(nurse_id) values(7)""")


            # cursor.execute("delete from patient")
            # cursor.execute("insert into history(patient_id,nurse_id,past_diagnosis) values(2,7,'i was fine until now')")
   
            # conn.commit()

if __name__ =='__main__':
    sqlBase()
    