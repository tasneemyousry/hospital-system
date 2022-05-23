/*==============================================================*/
/* DBMS name:      Microsoft SQL Server 2017                    */
/* Created on:     5/20/2022 2:07:51 AM                         */
/*==============================================================*/


if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('DOCTOR') and o.name = 'FK_DOCTOR_IS_STAFF')
alter table DOCTOR
   drop constraint FK_DOCTOR_IS_STAFF
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('GIVE_DIAGNOSIS') and o.name = 'FK_GIVE_DIA_GIVE_DIAG_DOCTOR')
alter table GIVE_DIAGNOSIS
   drop constraint FK_GIVE_DIA_GIVE_DIAG_DOCTOR
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('GIVE_DIAGNOSIS') and o.name = 'FK_GIVE_DIA_GIVE_DIAG_PATIENT')
alter table GIVE_DIAGNOSIS
   drop constraint FK_GIVE_DIA_GIVE_DIAG_PATIENT
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('GUARDIANS') and o.name = 'FK_GUARDIAN_CAN_CONTA_NURSE')
alter table GUARDIANS
   drop constraint FK_GUARDIAN_CAN_CONTA_NURSE
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('GUARDIANS') and o.name = 'FK_GUARDIAN_HAS_CONTA_PATIENT')
alter table GUARDIANS
   drop constraint FK_GUARDIAN_HAS_CONTA_PATIENT
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('HISTORY') and o.name = 'FK_HISTORY_HAS_PATIENT')
alter table HISTORY
   drop constraint FK_HISTORY_HAS_PATIENT
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('HISTORY') and o.name = 'FK_HISTORY_OBTAINS_NURSE')
alter table HISTORY
   drop constraint FK_HISTORY_OBTAINS_NURSE
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('HOLDS') and o.name = 'FK_HOLDS_HOLDS_STAFF')
alter table HOLDS
   drop constraint FK_HOLDS_HOLDS_STAFF
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('NURSE') and o.name = 'FK_NURSE_IS_A_STAFF')
alter table NURSE
   drop constraint FK_NURSE_IS_A_STAFF
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('OBSERVE') and o.name = 'FK_OBSERVE_OBSERVE_NURSE')
alter table OBSERVE
   drop constraint FK_OBSERVE_OBSERVE_NURSE
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('OBSERVE') and o.name = 'FK_OBSERVE_OBSERVE2_ROOM')
alter table OBSERVE
   drop constraint FK_OBSERVE_OBSERVE2_ROOM
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('PATIENT') and o.name = 'FK_PATIENT_ASSIGN_TO_ROOM')
alter table PATIENT
   drop constraint FK_PATIENT_ASSIGN_TO_ROOM
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('ROOM') and o.name = 'FK_ROOM_ASSIGN_TO_PATIENT')
alter table ROOM
   drop constraint FK_ROOM_ASSIGN_TO_PATIENT
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('SHIFT') and o.name = 'FK_SHIFT_HOLDS2_HOLDS')
alter table SHIFT
   drop constraint FK_SHIFT_HOLDS2_HOLDS
go

if exists (select 1
            from  sysobjects
           where  id = object_id('DOCTOR')
            and   type = 'U')
   drop table DOCTOR
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('GIVE_DIAGNOSIS')
            and   name  = 'GIVE_DIAGNOSIS2_FK'
            and   indid > 0
            and   indid < 255)
   drop index GIVE_DIAGNOSIS.GIVE_DIAGNOSIS2_FK
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('GIVE_DIAGNOSIS')
            and   name  = 'GIVE_DIAGNOSIS_FK'
            and   indid > 0
            and   indid < 255)
   drop index GIVE_DIAGNOSIS.GIVE_DIAGNOSIS_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('GIVE_DIAGNOSIS')
            and   type = 'U')
   drop table GIVE_DIAGNOSIS
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('GUARDIANS')
            and   name  = 'CAN_CONTACT_FK'
            and   indid > 0
            and   indid < 255)
   drop index GUARDIANS.CAN_CONTACT_FK
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('GUARDIANS')
            and   name  = 'HAS_CONTACT_TO2_FK'
            and   indid > 0
            and   indid < 255)
   drop index GUARDIANS.HAS_CONTACT_TO2_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('GUARDIANS')
            and   type = 'U')
   drop table GUARDIANS
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('HISTORY')
            and   name  = 'OBTAINS_FK'
            and   indid > 0
            and   indid < 255)
   drop index HISTORY.OBTAINS_FK
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('HISTORY')
            and   name  = 'HAS_FK'
            and   indid > 0
            and   indid < 255)
   drop index HISTORY.HAS_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('HISTORY')
            and   type = 'U')
   drop table HISTORY
go

if exists (select 1
            from  sysobjects
           where  id = object_id('HOLDS')
            and   type = 'U')
   drop table HOLDS
go

if exists (select 1
            from  sysobjects
           where  id = object_id('NURSE')
            and   type = 'U')
   drop table NURSE
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('OBSERVE')
            and   name  = 'OBSERVE2_FK'
            and   indid > 0
            and   indid < 255)
   drop index OBSERVE.OBSERVE2_FK
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('OBSERVE')
            and   name  = 'OBSERVE_FK'
            and   indid > 0
            and   indid < 255)
   drop index OBSERVE.OBSERVE_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('OBSERVE')
            and   type = 'U')
   drop table OBSERVE
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('PATIENT')
            and   name  = 'ASSIGN_TO_FK'
            and   indid > 0
            and   indid < 255)
   drop index PATIENT.ASSIGN_TO_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('PATIENT')
            and   type = 'U')
   drop table PATIENT
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('ROOM')
            and   name  = 'ASSIGN_TO2_FK'
            and   indid > 0
            and   indid < 255)
   drop index ROOM.ASSIGN_TO2_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('ROOM')
            and   type = 'U')
   drop table ROOM
go

if exists (select 1
            from  sysobjects
           where  id = object_id('SHIFT')
            and   type = 'U')
   drop table SHIFT
go

if exists (select 1
            from  sysobjects
           where  id = object_id('STAFF')
            and   type = 'U')
   drop table STAFF
go

/*==============================================================*/
/* Table: DOCTOR                                                */
/*==============================================================*/
create table DOCTOR (
   DOCTOR_ID            int                  not null,
   SPECIALITY           varchar(100)         not null,
   constraint PK_DOCTOR primary key (DOCTOR_ID)
)
go

/*==============================================================*/
/* Table: GIVE_DIAGNOSIS                                        */
/*==============================================================*/
create table GIVE_DIAGNOSIS (
   DOCTOR_ID            int                  not null,
   PATIENT_ID           int                  not null,
   DIAGNOSIS            text                 not null,
   PRESCRIPTION         text                 not null,
   DIAGNOSIS_DATE       datetime             not null,
   constraint PK_GIVE_DIAGNOSIS primary key (DOCTOR_ID, PATIENT_ID, DIAGNOSIS_DATE)
)
go

/*==============================================================*/
/* Index: GIVE_DIAGNOSIS_FK                                     */
/*==============================================================*/




create nonclustered index GIVE_DIAGNOSIS_FK on GIVE_DIAGNOSIS (DOCTOR_ID ASC)
go

/*==============================================================*/
/* Index: GIVE_DIAGNOSIS2_FK                                    */
/*==============================================================*/




create nonclustered index GIVE_DIAGNOSIS2_FK on GIVE_DIAGNOSIS (PATIENT_ID ASC)
go

/*==============================================================*/
/* Table: GUARDIANS                                             */
/*==============================================================*/
create table GUARDIANS (
   PATIENT_ID           int                  not null,
   NURSE_ID             int                  not null,
   PHONE_NO             bigint               not null,
   RELATIONSHIP_TO_PATIENT varchar(50)          null,
   constraint PK_GUARDIANS primary key (PATIENT_ID, NURSE_ID)
)
go

/*==============================================================*/
/* Index: HAS_CONTACT_TO2_FK                                    */
/*==============================================================*/




create nonclustered index HAS_CONTACT_TO2_FK on GUARDIANS (PATIENT_ID ASC)
go

/*==============================================================*/
/* Index: CAN_CONTACT_FK                                        */
/*==============================================================*/




create nonclustered index CAN_CONTACT_FK on GUARDIANS (NURSE_ID ASC)
go

/*==============================================================*/
/* Table: HISTORY                                               */
/*==============================================================*/
create table HISTORY (
   PATIENT_ID           int                  not null,
   NURSE_ID             int                  not null,
   PAST_DIAGNOSIS       text                 not null,
   constraint PK_HISTORY primary key (PATIENT_ID, NURSE_ID)
)
go

/*==============================================================*/
/* Index: HAS_FK                                                */
/*==============================================================*/




create nonclustered index HAS_FK on HISTORY (PATIENT_ID ASC)
go

/*==============================================================*/
/* Index: OBTAINS_FK                                            */
/*==============================================================*/




create nonclustered index OBTAINS_FK on HISTORY (NURSE_ID ASC)
go

/*==============================================================*/
/* Table: HOLDS                                                 */
/*==============================================================*/
create table HOLDS (
   STAFF_ID             int                  not null,
   constraint PK_HOLDS primary key (STAFF_ID)
)
go

/*==============================================================*/
/* Table: NURSE                                                 */
/*==============================================================*/
create table NURSE (
   NURSE_ID             int                  not null,
   constraint PK_NURSE primary key (NURSE_ID)
)
go

/*==============================================================*/
/* Table: OBSERVE                                               */
/*==============================================================*/
create table OBSERVE (
   NURSE_ID             int                  not null,
   ROOM_ID              varchar(10)          not null,
   constraint PK_OBSERVE primary key (NURSE_ID, ROOM_ID)
)
go

/*==============================================================*/
/* Index: OBSERVE_FK                                            */
/*==============================================================*/




create nonclustered index OBSERVE_FK on OBSERVE (NURSE_ID ASC)
go

/*==============================================================*/
/* Index: OBSERVE2_FK                                           */
/*==============================================================*/




create nonclustered index OBSERVE2_FK on OBSERVE (ROOM_ID ASC)
go

/*==============================================================*/
/* Table: PATIENT                                               */
/*==============================================================*/
create table PATIENT (
   FIRST_NAME           varchar(50)          not null,
   LAST_NAME            varchar(50)          not null,
   GENDER               char(256)            null,
   ADDRESS              varchar(100)         null,
   PHONE_NO             bigint               null,
   PATIENT_ID           int                  not null,
   ROOM_ID              varchar(10)          null,
   BIRTH_DATE           datetime             null,
   constraint PK_PATIENT primary key (PATIENT_ID)
)
go

/*==============================================================*/
/* Index: ASSIGN_TO_FK                                          */
/*==============================================================*/




create nonclustered index ASSIGN_TO_FK on PATIENT (ROOM_ID ASC)
go

/*==============================================================*/
/* Table: ROOM                                                  */
/*==============================================================*/
create table ROOM (
   ROOM_ID              varchar(10)          not null,
   PATIENT_ID           int                  null,
   DATE_ADMITTED        datetime             not null,
   DATE_DISCHARGED      datetime             not null,
   constraint PK_ROOM primary key (ROOM_ID)
)
go

/*==============================================================*/
/* Index: ASSIGN_TO2_FK                                         */
/*==============================================================*/




create nonclustered index ASSIGN_TO2_FK on ROOM (PATIENT_ID ASC)
go

/*==============================================================*/
/* Table: SHIFT                                                 */
/*==============================================================*/
create table SHIFT (
   STAFF_ID             int                  not null,
   START_TIME           datetime             not null,
   END_TIME             datetime             not null,
   constraint PK_SHIFT primary key (STAFF_ID, START_TIME, END_TIME)
)
go

/*==============================================================*/
/* Table: STAFF                                                 */
/*==============================================================*/
create table STAFF (
   STAFF_ID             int                  not null,
   GENDER               char(256)            null,
   FIRST_NAME           varchar(50)          not null,
   LAST_NAME            varchar(50)          not null,
   PHONE_NO             bigint               not null,
   BIRTH_DATE           datetime             not null,
   constraint PK_STAFF primary key (STAFF_ID)
)
go

alter table DOCTOR
   add constraint FK_DOCTOR_IS_STAFF foreign key (DOCTOR_ID)
      references STAFF (STAFF_ID)
         on update cascade on delete cascade
go

alter table GIVE_DIAGNOSIS
   add constraint FK_GIVE_DIA_GIVE_DIAG_DOCTOR foreign key (DOCTOR_ID)
      references DOCTOR (DOCTOR_ID)
         on update cascade
go

alter table GIVE_DIAGNOSIS
   add constraint FK_GIVE_DIA_GIVE_DIAG_PATIENT foreign key (PATIENT_ID)
      references PATIENT (PATIENT_ID)
         on update cascade on delete cascade
go

alter table GUARDIANS
   add constraint FK_GUARDIAN_CAN_CONTA_NURSE foreign key (NURSE_ID)
      references NURSE (NURSE_ID)
         on update cascade
go

alter table GUARDIANS
   add constraint FK_GUARDIAN_HAS_CONTA_PATIENT foreign key (PATIENT_ID)
      references PATIENT (PATIENT_ID)
         on update cascade
go

alter table HISTORY
   add constraint FK_HISTORY_HAS_PATIENT foreign key (PATIENT_ID)
      references PATIENT (PATIENT_ID)
         on update cascade on delete cascade
go

alter table HISTORY
   add constraint FK_HISTORY_OBTAINS_NURSE foreign key (NURSE_ID)
      references NURSE (NURSE_ID)
         on update cascade
go

alter table HOLDS
   add constraint FK_HOLDS_HOLDS_STAFF foreign key (STAFF_ID)
      references STAFF (STAFF_ID)
         on update cascade on delete cascade
go

alter table NURSE
   add constraint FK_NURSE_IS_A_STAFF foreign key (NURSE_ID)
      references STAFF (STAFF_ID)
         on update cascade on delete cascade
go

alter table OBSERVE
   add constraint FK_OBSERVE_OBSERVE_NURSE foreign key (NURSE_ID)
      references NURSE (NURSE_ID)
         on update cascade on delete cascade
go

alter table OBSERVE
   add constraint FK_OBSERVE_OBSERVE2_ROOM foreign key (ROOM_ID)
      references ROOM (ROOM_ID)
         on update cascade on delete cascade
go

alter table PATIENT
   add constraint FK_PATIENT_ASSIGN_TO_ROOM foreign key (ROOM_ID)
      references ROOM (ROOM_ID)
         on update cascade
go

alter table ROOM
   add constraint FK_ROOM_ASSIGN_TO_PATIENT foreign key (PATIENT_ID)
      references PATIENT (PATIENT_ID)
go

alter table SHIFT
   add constraint FK_SHIFT_HOLDS2_HOLDS foreign key (STAFF_ID)
      references HOLDS (STAFF_ID)
         on update cascade on delete cascade
go

