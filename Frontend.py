from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox
from Backend import *
from tkinter import font as tkfont 

class StartWindow:
    def __init__(self, win):
######################################################################### View Staff Profile ######################################################################
        def ViewStaffProfile():
            #Call the user class to run - in order to run a method within it:
            staff = Staff(first_name, surname, dob, salary, work_hours, work_days, login_ID, password, home_address, phone_no, work_email, role)
            
            Fname = staff.get_first_name(role, login_ID)
            Surname = staff.get_last_name(role, login_ID)
            DoB = staff.get_date_of_birth(role, login_ID)
            Salary = staff.get_salary(role, login_ID)
            Whours = staff.get_work_hours(role, login_ID)
            Wdays = staff.get_work_days(role, login_ID)
            LID = staff.get_login_id(role, login_ID)
            adrs = staff.get_home_address(role, login_ID)
            phn = staff.get_phone_no(role, login_ID)
            eml = staff.get_work_email(role, login_ID)
            rol = staff.get_role(role, login_ID)

            info = Fname, Surname, DoB, Salary, Whours, Wdays, LID, adrs, phn, eml, rol
            
            messagebox.showinfo("Information", info)
        
######################################################################### View User Profile ######################################################################
        def ViewUserProfile():
            #Call the user class to run - in order to run a method within it:
            if role == 'Visitor':
                user = Visitor(name, user_name, password, address, phone_no, email, role, dob, age, books_on_loan, due_dates, users_bills)
                
            elif role == 'School Visit':
                user = SchoolVist(name, user_name, password, address, phone_no, email, role, books_on_loan, due_dates, users_bills)

            elif role == 'Event Holder':
                user = EventHolder(name, user_name, password, address, phone_no, email, role, dob, age, event_name, event_date, time_of_event, event_duration, event_status)  

            Name = user.get_name(role, user_name)
            UN = user.get_user_name(role, user_name)
            adr = user.get_address(role, user_name)
            phn = user.get_phone_no(role, user_name)
            eml = user.get_email(role, user_name)
            rol = user.get_role(role, user_name)

            if role == 'Visitor':
                DoB = user.get_date_of_birth(role, user_name)
                Age = user.get_age(role, user_name)
                Bol = user.get_books_on_loan(role, user_name)
                dates = user.get_due_dates(role, user_name)
                Bills = user.get_bills(role, user_name)

                info = Name, UN, adr, phn, eml, rol, DoB, Age, Bol, dates, Bills
                
            elif role == 'School Visit':
                Bol = user.get_books_on_loan(role, user_name)
                dates = user.get_due_dates(role, user_name)
                Bills = user.get_bills(role, user_name)

                info = Name, UN, adr, phn, eml, rol, Bol, dates, Bills
                
            elif role == 'Event Holder':
                DoB = user.get_date_of_birth(role, user_name)
                Age = user.get_age(role, user_name)
                eName = user.get_event_name(role, user_name)
                eDate = user.get_event_date(role, user_name)
                eTime = user.get_time_of_event(role, user_name)
                eDuration = user.get_event_duration(role, user_name)
                eStatus = user.get_event_status(role, user_name)

                info = Name, UN, adr, phn, eml, rol, DoB, Age, eName, eDate, eTime, eDuration, eStatus

            messagebox.showinfo("Information", info)
        
############################################################################ Add Items ######################################################################
        
        def AddItem():
            if role == "Manager" or role=="Senior":
                addItem = Toplevel(window) # Toplevel object which will be treated as a new window 
                addItem.title("Add Item") # sets the title of the Toplevel widget 
                addItem.attributes('-fullscreen', True) # sets the geometry of toplevel widget
                addItem.configure(bg='#d8e6db')

                #Title
                self.AddItemFormTitle = Label(addItem, text='Add Item:', bg='#415dfa', font=("Courier", 50)) #Title
                self.AddItemFormTitle.place(x=500, y=0)

                #Form

                #Drop down menu
                itemTypes = [
                "Book",
                "DVD",
                "Newspaper_Magazine"
                ] 

                item_type = StringVar(addItem)
                item_type.set(itemTypes[0]) # default value

                self.lblFormItemType = Label(addItem, text='Item Type:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # StaffRole dropdown Label
                self.lblFormItemType.place(x=200, y=200)
                    
                self.FormItemTypeDropdown = OptionMenu(addItem, item_type, *itemTypes)
                self.FormItemTypeDropdown.place(x=400, y=200)

                ############### Needed for ALL ###############
                self.lblall = Label(addItem, text='NEEDED FOR ALL ITEM TYPES:',bg='#d8e6db', font=("Courier", 17 ,'bold')) # Change Label
                self.lblall.place(x=50, y=250)
                
                self.lblName = Label(addItem, text='Name:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblName.place(x=50, y=300)
                self.entryName = Entry(addItem, bd=1) # Entry Field containing new details 
                self.entryName.place(x=175, y=300)

                self.lblCondition = Label(addItem, text='Condition:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblCondition.place(x=50, y=350)
                self.entryCondition = Entry(addItem, bd=1) # Entry Field containing new details 
                self.entryCondition.place(x=175, y=350)

                self.lblISBNNumber = Label(addItem, text='ISBN Number:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblISBNNumber.place(x=50, y=400)
                self.entryISBNNumber = Entry(addItem, bd=1) # Entry Field containing new details 
                self.entryISBNNumber.place(x=175, y=400)

                self.lblDateCreated = Label(addItem, text='Date Created:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblDateCreated.place(x=50, y=450)
                self.entryDateCreated = Entry(addItem, bd=1) # Entry Field containing new details 
                self.entryDateCreated.place(x=175, y=450)

                self.lblStatus = Label(addItem, text='Status:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblStatus.place(x=50, y=500)
                self.entryStatus = Entry(addItem, bd=1) # Entry Field containing new details 
                self.entryStatus.place(x=175, y=500)

                self.lblNumberOfCopies = Label(addItem, text='Number of Copies:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblNumberOfCopies.place(x=50, y=550)
                self.entryNumberOfCopies = Entry(addItem, bd=1) # Entry Field containing new details 
                self.entryNumberOfCopies.place(x=220, y=550)

                ############### Needed for DVDs ###############
                self.lblall = Label(addItem, text='extra NEEDED FOR ALL DVDs ONLY:',bg='#d8e6db', font=("Courier", 17 ,'bold')) # Change Label
                self.lblall.place(x=400, y=250)

                self.lblDirector = Label(addItem, text='Director:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblDirector.place(x=400, y=300)
                self.entryDirector = Entry(addItem, bd=1) # Entry Field containing new details 
                self.entryDirector.place(x=500, y=300)

                self.lblDuration = Label(addItem, text='Duration:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblDuration.place(x=400, y=350)
                self.entryDuration = Entry(addItem, bd=1) # Entry Field containing new details 
                self.entryDuration.place(x=500, y=350)

                self.lblAgeGroup = Label(addItem, text='Age Group:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblAgeGroup.place(x=400, y=400)
                self.entryAgeGroup = Entry(addItem, bd=1) # Entry Field containing new details 
                self.entryAgeGroup.place(x=500, y=400)

                ############### Needed for Newspaper_Magazine ###############
                self.lblall = Label(addItem, text='extra NEEDED FOR ALL Newspaper/Magazine ONLY:',bg='#d8e6db', font=("Courier", 17 ,'bold')) # Change Label
                self.lblall.place(x=800, y=500)

                self.lblTitle = Label(addItem, text='Title:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblTitle.place(x=800, y=550)
                self.entryTitle = Entry(addItem, bd=1) # Entry Field containing new details 
                self.entryTitle.place(x=900, y=550)

                ############### Needed for Books ###############
                self.lblall = Label(addItem, text='extra NEEDED FOR ALL Books ONLY:',bg='#d8e6db', font=("Courier", 17 ,'bold')) # Change Label
                self.lblall.place(x=800, y=250)

                self.lblAuthor = Label(addItem, text='Author:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblAuthor.place(x=800, y=300)
                self.entryAuthor = Entry(addItem, bd=1) # Entry Field containing new details 
                self.entryAuthor.place(x=900, y=300)

                self.lblGenre = Label(addItem, text='Genre:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblGenre.place(x=800, y=350)
                self.entryGenre = Entry(addItem, bd=1) # Entry Field containing new details 
                self.entryGenre.place(x=900, y=350)

                self.lblPages = Label(addItem, text='Number Of Pages:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblPages.place(x=800, y=400)
                self.entryPages = Entry(addItem, bd=1) # Entry Field containing new details 
                self.entryPages.place(x=950, y=400)

                def AddItems():
                    if item_type.get() == "DVD":
                        item = DVD(item_type.get(), self.entryName.get(), self.entryCondition.get(), self.entryISBNNumber.get(), self.entryDateCreated.get(), self.entryStatus.get(), self.entryNumberOfCopies.get(), self.entryDirector.get(), self.entryDuration.get(), self.entryAgeGroup.get())
                        item.add_dvd_JSON(item_data)

                    elif item_type.get() == "Newspaper_Magazine":                                                
                        item = Newspaper_Magazine(item_type.get(), self.entryName.get(), self.entryCondition.get(), self.entryISBNNumber.get(), self.entryDateCreated.get(), self.entryStatus.get(), self.entryNumberOfCopies.get(), self.entryTitle.get())
                        item.add_newspaper_magazine_JSON(item_data)
                        
                    elif item_type.get() == "Book":
                        item = Book(item_type.get(), self.entryName.get(), self.entryCondition.get(), self.entryISBNNumber.get(), self.entryDateCreated.get(), self.entryStatus.get(), self.entryNumberOfCopies.get(), self.entryAuthor.get(), self.entryGenre.get(), self.entryPages.get())
                        item.add_book_JSON(item_data)

                    messagebox.showinfo("Information", "Success")

                AddStaffBtn = Button(addItem, text='Add Item', command = AddItems, fg = "green")
                AddStaffBtn.place(x=650, y=600)

                ReturnBtn = Button(addItem, text='Return To Menu', command = addItem.destroy, fg = "green")
                ReturnBtn.place(x=500, y=600)

            else:
                messagebox.showinfo("Error", "You are not a Senior Staff Member/Manager")
########################################################################## Add User Members #################################################################
        
        def AddUser():
            addUser = Toplevel(window) # Toplevel object which will be treated as a new window 
            addUser.title("Add Staff Member") # sets the title of the Toplevel widget 
            addUser.attributes('-fullscreen', True) # sets the geometry of toplevel widget
            addUser.configure(bg='#d8e6db')

            #Title
            self.AddUserFormTitle = Label(addUser, text='Add A User Member:', bg='#415dfa', font=("Courier", 50)) #Title
            self.AddUserFormTitle.place(x=500, y=0)

            #Form
                
            #Drop down menu
            userRoles = [
            "Visitor",
            "School Visit",
            "Event Holder"
            ] 

            user_role = StringVar(addUser)
            user_role.set(userRoles[0]) # default value

            self.lblFormUserfRole = Label(addUser, text='User Role:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # StaffRole dropdown Label
            self.lblFormUserfRole.place(x=200, y=200)
                        
            self.FormUserRoleDropdown = OptionMenu(addUser, user_role, *userRoles)
            self.FormUserRoleDropdown.place(x=400, y=200)

            #Entries
            ############### Needed for ALL ###############
            self.lblall = Label(addUser, text='NEEDED FOR ALL USER TYPES:',bg='#d8e6db', font=("Courier", 17 ,'bold')) # Change Label
            self.lblall.place(x=50, y=250)
            
            self.lblName = Label(addUser, text='Name:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
            self.lblName.place(x=50, y=300)
            self.entryName = Entry(addUser, bd=1) # Entry Field containing new details 
            self.entryName.place(x=200, y=300)

            self.lblLoginID = Label(addUser, text='Username:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
            self.lblLoginID.place(x=50, y=350)
            self.entryLoginID = Entry(addUser, bd=1) # Entry Field containing new details 
            self.entryLoginID.place(x=200, y=350)

            self.lblPassword = Label(addUser, text='Password:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
            self.lblPassword.place(x=50, y=400)
            self.entryPassword = Entry(addUser, bd=1) # Entry Field containing new details 
            self.entryPassword.place(x=200, y=400)

            self.lblAddress = Label(addUser, text='Address:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
            self.lblAddress.place(x=50, y=450)
            self.entryAddress = Entry(addUser, bd=1) # Entry Field containing new details 
            self.entryAddress.place(x=200, y=450)

            self.lblPhoneNo = Label(addUser, text='Phone Number:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
            self.lblPhoneNo.place(x=50, y=500)
            self.entryPhoneNo = Entry(addUser, bd=1) # Entry Field containing new details 
            self.entryPhoneNo.place(x=200, y=500)

            self.lblEmail = Label(addUser, text='Email:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
            self.lblEmail.place(x=50, y=550)
            self.entryEmail = Entry(addUser, bd=1) # Entry Field containing new details 
            self.entryEmail.place(x=200, y=550)

            ############### Extra for Visitor ###############
            self.lblvis = Label(addUser, text='Extra NEEDED FOR VISITORS ONLY:',bg='#d8e6db', font=("Courier", 17 ,'bold')) # Change Label
            self.lblvis.place(x=400, y=250)
            
            self.lblDOBvis = Label(addUser, text='Date Of Birth (dd/mm/yyyy):',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
            self.lblDOBvis.place(x=400, y=300)
            self.entryDOBvis = Entry(addUser, bd=1) # Entry Field containing new details 
            self.entryDOBvis.place(x=600, y=300)

            self.lblAgevis = Label(addUser, text='Age:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
            self.lblAgevis.place(x=400, y=350)
            self.entryAgevis = Entry(addUser, bd=1) # Entry Field containing new details 
            self.entryAgevis.place(x=600, y=350)

            ############### Extra for Event Holder ###############
            self.lblholder = Label(addUser, text='Extra NEEDED FOR EVENT HOLDERS ONLY:',bg='#d8e6db', font=("Courier", 17 ,'bold')) # Change Label
            self.lblholder.place(x=800, y=250)
            
            self.lblDOBhold = Label(addUser, text='Date Of Birth (dd/mm/yyyy):',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
            self.lblDOBhold.place(x=800, y=300)
            self.entryDOBhold = Entry(addUser, bd=1) # Entry Field containing new details 
            self.entryDOBhold.place(x=1000, y=300)

            self.lblAgehold = Label(addUser, text='Age:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
            self.lblAgehold.place(x=800, y=350)
            self.entryAgehold = Entry(addUser, bd=1) # Entry Field containing new details 
            self.entryAgehold.place(x=1000, y=350)

            self.lblEventName = Label(addUser, text='Event Name:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
            self.lblEventName.place(x=800, y=400)
            self.entryEventName = Entry(addUser, bd=1) # Entry Field containing new details 
            self.entryEventName.place(x=1000, y=400)

            self.lblEventDate = Label(addUser, text='Event Date:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
            self.lblEventDate.place(x=800, y=450)
            self.entryEventDate = Entry(addUser, bd=1) # Entry Field containing new details 
            self.entryEventDate.place(x=1000, y=450)

            self.lblEventTime = Label(addUser, text='Event Time:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
            self.lblEventTime.place(x=800, y=500)
            self.entryEventTime = Entry(addUser, bd=1) # Entry Field containing new details 
            self.entryEventTime.place(x=1000, y=500)

            self.lblEventDuration = Label(addUser, text='Event Duration (hrs):',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
            self.lblEventDuration.place(x=800, y=550)
            self.entryEventDuration = Entry(addUser, bd=1) # Entry Field containing new details 
            self.entryEventDuration.place(x=1000, y=550)

            
            def AddUserMember():
                if user_role.get() == "Visitor":
                    user = Visitor(self.entryName.get(), self.entryLoginID.get(), self.entryPassword.get(), self.entryAddress.get(), self.entryPhoneNo.get(), self.entryEmail.get(), user_role.get(), self.entryDOBvis.get(), self.entryAgevis.get(), '', '', 0)
                    user.add_visitor_JSON(user_data)

                elif user_role.get() == "School Visit":            
                    user = SchoolVist(self.entryName.get(), self.entryLoginID.get(), self.entryPassword.get(), self.entryAddress.get(), self.entryPhoneNo.get(), self.entryEmail.get(), user_role.get(), '', '', 0)
                    user.add_school_visit_JSON(user_data)
                        
                elif user_role.get() == "Event Holder":
                    user = EventHolder(self.entryName.get(), self.entryLoginID.get(), self.entryPassword.get(), self.entryAddress.get(), self.entryPhoneNo.get(), self.entryEmail.get(), user_role.get(), self.entryDOBhold.get(), self.entryAgehold.get(), self.entryEventName.get(), self.entryEventDate.get(), self.entryEventTime.get(), self.entryEventDuration.get(), 'Not Done')
                    user.add_event_holder_JSON(user_data)

                messagebox.showinfo("Information", "Success")

            AddStaffBtn = Button(addUser, text='Add User', command = AddUserMember, fg = "green")
            AddStaffBtn.place(x=600, y=550)

            ReturnBtn = Button(addUser, text='Return To Menu', command = addUser.destroy, fg = "green")
            ReturnBtn.place(x=450, y=550)
########################################################################## Add Staff Members #################################################################
        
        def AddStaff():
            if role == "Manager":
                addStaff = Toplevel(window) # Toplevel object which will be treated as a new window 
                addStaff.title("Add Staff Member") # sets the title of the Toplevel widget 
                addStaff.attributes('-fullscreen', True) # sets the geometry of toplevel widget
                addStaff.configure(bg='#d8e6db')

                #Title
                self.AddStaffFormTitle = Label(addStaff, text='Add A Staff Member:', bg='#415dfa', font=("Courier", 50)) #Title
                self.AddStaffFormTitle.place(x=500, y=0)

                #Form
                
                #Drop down menu
                staffRoles = [
                "Junior",
                "Senior",
                "Manager"
                ] 

                staff_role = StringVar(addStaff)
                staff_role.set(staffRoles[0]) # default value

                self.lblFormStaffRole = Label(addStaff, text='Staff Role:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # StaffRole dropdown Label
                self.lblFormStaffRole.place(x=200, y=200)
                    
                self.FormStaffRoleDropdown = OptionMenu(addStaff, staff_role, *staffRoles)
                self.FormStaffRoleDropdown.place(x=400, y=200)

                self.lblFname = Label(addStaff, text='First Name:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblFname.place(x=200, y=250)
                self.entryFname = Entry(addStaff, bd=1) # Entry Field containing new details 
                self.entryFname.place(x=400, y=250)

                self.lblSname = Label(addStaff, text='Last Name:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblSname.place(x=200, y=300)
                self.entrySname = Entry(addStaff, bd=1) # Entry Field containing new details 
                self.entrySname.place(x=400, y=300)

                self.lblDOB = Label(addStaff, text='Date Of Birth:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblDOB.place(x=200, y=350)
                self.entryDOB = Entry(addStaff, bd=1) # Entry Field containing new details 
                self.entryDOB.place(x=400, y=350)

                self.lblSalary = Label(addStaff, text='Salary:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblSalary.place(x=200, y=400)
                self.entrySalary = Entry(addStaff, bd=1) # Entry Field containing new details 
                self.entrySalary.place(x=400, y=400)

                self.lblWorkHrs = Label(addStaff, text='Work Hours:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblWorkHrs.place(x=200, y=450)
                self.entryWorkHrs = Entry(addStaff, bd=1) # Entry Field containing new details 
                self.entryWorkHrs.place(x=400, y=450)

                self.lblWorkDys = Label(addStaff, text='Work Days:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblWorkDys.place(x=200, y=500)
                self.entryWorkDys = Entry(addStaff, bd=1) # Entry Field containing new details 
                self.entryWorkDys.place(x=400, y=500)

                self.lblLoginID = Label(addStaff, text='Login ID:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblLoginID.place(x=200, y=550)
                self.entryLoginID = Entry(addStaff, bd=1) # Entry Field containing new details 
                self.entryLoginID.place(x=400, y=550)

                self.lblPassword = Label(addStaff, text='Password:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblPassword.place(x=200, y=600)
                self.entryPassword = Entry(addStaff, bd=1) # Entry Field containing new details 
                self.entryPassword.place(x=400, y=600)

                self.lblHomeAddress = Label(addStaff, text='Address:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblHomeAddress.place(x=200, y=650)
                self.entryHomeAddress = Entry(addStaff, bd=1) # Entry Field containing new details 
                self.entryHomeAddress.place(x=400, y=650)

                self.lblPhoneNo = Label(addStaff, text='Phone Number:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblPhoneNo.place(x=600, y=200)
                self.entryPhoneNo = Entry(addStaff, bd=1) # Entry Field containing new details 
                self.entryPhoneNo.place(x=800, y=200)

                self.lblWorkEmail = Label(addStaff, text='Work Email:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblWorkEmail.place(x=600, y=250)
                self.entryWorkEmail = Entry(addStaff, bd=1) # Entry Field containing new details 
                self.entryWorkEmail.place(x=800, y=250)

                def AddStaffMember():
                    if staff_role.get() == "Junior":
                        staff = Junior(self.entryFname.get(), self.entrySname.get(), self.entryDOB.get(), self.entrySalary.get(), self.entryWorkHrs.get(), self.entryWorkDys.get(), self.entryLoginID.get(), self.entryPassword.get(), self.entryHomeAddress.get(), self.entryPhoneNo.get(), self.entryWorkEmail.get(), staff_role.get())
                        staff.add_junior_JSON(staff_data)

                    elif staff_role.get() == "Senior":
                        staff = Senior(self.entryFname.get(), self.entrySname.get(), self.entryDOB.get(), self.entrySalary.get(), self.entryWorkHrs.get(), self.entryWorkDys.get(), self.entryLoginID.get(), self.entryPassword.get(), self.entryHomeAddress.get(), self.entryPhoneNo.get(), self.entryWorkEmail.get(), staff_role.get())
                        staff.add_senior_JSON(staff_data)
                        
                    elif staff_role.get() == "Manager":
                        staff = Manager(self.entryFname.get(), self.entrySname.get(), self.entryDOB.get(), self.entrySalary.get(), self.entryWorkHrs.get(), self.entryWorkDys.get(), self.entryLoginID.get(), self.entryPassword.get(), self.entryHomeAddress.get(), self.entryPhoneNo.get(), self.entryWorkEmail.get(), staff_role.get())
                        staff.add_manager_JSON(staff_data)

                    messagebox.showinfo("Information", "Success")

                AddStaffBtn = Button(addStaff, text='Add Staff', command = AddStaffMember, fg = "green")
                AddStaffBtn.place(x=800, y=350)

                ReturnBtn = Button(addStaff, text='Return To Menu', command = addStaff.destroy, fg = "green")
                ReturnBtn.place(x=800, y=400)

            else:
                messagebox.showinfo("Error", "You are not a Manager")
        
###################################################################### Item Search Form - USER #################################################################
        
        def UserItemSearchForm():  
            userItemSearchForm = Toplevel(window) # Toplevel object which will be treated as a new window 
            userItemSearchForm.title("Search For An Item") # sets the title of the Toplevel widget 
            userItemSearchForm.attributes('-fullscreen', True) # sets the geometry of toplevel widget
            userItemSearchForm.configure(bg='#d8e6db')

            #Title
            self.UserItemSearchFormTitle = Label(userItemSearchForm, text='Search For An Item:', bg='#415dfa', font=("Courier", 50)) #Title
            self.UserItemSearchFormTitle.place(x=500, y=0)

            #Form
            
            #Drop down menu
            itemType = [
            "DVD",
            "Newspaper_Magazine",
            "Book"
            ] 

            item_type = StringVar(userItemSearchForm)
            item_type.set(itemType[2]) # default value

            self.lblFormItemType = Label(userItemSearchForm, text='Item Type:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # ItemType dropdown Label
            self.lblFormItemType.place(x=200, y=200)
            
            self.FormItemTypeDropdown = OptionMenu(userItemSearchForm, item_type, *itemType)
            self.FormItemTypeDropdown.place(x=400, y=200)

            self.lblItemSearchName = Label(userItemSearchForm, text='Item Name:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Item Name Label
            self.lblItemSearchName.place(x=200, y=400)
            
            self.entryItemSearchName = Entry(userItemSearchForm, bd=1) # Item Name Entry Field 
            self.entryItemSearchName.place(x=400, y=400)

            def ItemSearch():
                if role == 'Visitor':
                    user = Visitor(name, user_name, password, address, phone_no, email, role, dob, age, books_on_loan, due_dates, users_bills)
                    
                elif role == 'School Visit':
                    user = SchoolVist(name, user_name, password, address, phone_no, email, role, books_on_loan, due_dates, users_bills)

                elif role == 'Event Holder':
                    user = EventHolder(name, user_name, password, address, phone_no, email, role, dob, age, event_name, event_date, time_of_event, event_duration, event_status)  

                date, status, copies = user.search_item(item_type.get(), self.entryItemSearchName.get())
                info = date, status, copies 
                messagebox.showinfo("Information", info)
                
            ItemSearchBtn = Button(userItemSearchForm, text='Search', command = ItemSearch, fg = "green")
            ItemSearchBtn.place(x=750, y=600)

            ReturnBtn = Button(userItemSearchForm, text='Return To Menu', command = userItemSearchForm.destroy, fg = "green")
            ReturnBtn.place(x=150, y=600)
        
###################################################################### View Books On Loan #######################################################################
        def ViewBooksOnLoan():
            viewBooksOnLoan = Toplevel(window) # Toplevel object which will be treated as a new window 
            viewBooksOnLoan.title("View Books On Loan") # sets the title of the Toplevel widget 
            viewBooksOnLoan.attributes('-fullscreen', True) # sets the geometry of toplevel widget
            viewBooksOnLoan.configure(bg='#d8e6db')

            #Title
            self.ViewBooksOnLoanTitle = Label(viewBooksOnLoan, text='View Books On Loan:', bg='#415dfa', font=("Courier", 50)) #Title
            self.ViewBooksOnLoanTitle.place(x=500, y=0)

            #Call the user class to run - in order to run a method within it:
            if role == 'Visitor':
                user = Visitor(name, user_name, password, address, phone_no, email, role, dob, age, books_on_loan, due_dates, users_bills)
                
            elif role == 'School Visit':
                user = SchoolVist(name, user_name, password, address, phone_no, email, role, books_on_loan, due_dates, users_bills)

            elif role == 'Event Holder':
                user = EventHolder(name, user_name, password, address, phone_no, email, role, dob, age, event_name, event_date, time_of_event, event_duration, event_status)  

            #Call the method within the class:
            books = user.get_books_on_loan(role, user_name)
            dates = user.get_due_dates(role, user_name)
            tempBills = user.get_bills(role, user_name)
            var = books, dates, tempBills
            messagebox.showinfo('Books On Loan', var)

            ReturnBtn = Button(viewBooksOnLoan, text='Return To Menu', command = viewBooksOnLoan.destroy, fg = "green")
            ReturnBtn.place(x=150, y=600)
########################################################################## View Events Form #######################################################################
        def ViewEventsForm():
            viewEventsForm = Toplevel(window) # Toplevel object which will be treated as a new window 
            viewEventsForm.title("Vuew Events") # sets the title of the Toplevel widget 
            viewEventsForm.attributes('-fullscreen', True) # sets the geometry of toplevel widget
            viewEventsForm.configure(bg='#d8e6db')

            #Title
            self.ViewEventsFormTitle = Label(viewEventsForm, text='View Events:', bg='#415dfa', font=("Courier", 50)) #Title
            self.ViewEventsFormTitle.place(x=500, y=0)

            #Call the user class to run - in order to run a method within it:
            if role == 'Visitor':
                user = Visitor(name, user_name, password, address, phone_no, email, role, dob, age, books_on_loan, due_dates, users_bills)
                
            elif role == 'School Visit':
                user = SchoolVist(name, user_name, password, address, phone_no, email, role, books_on_loan, due_dates, users_bills)

            elif role == 'Event Holder':
                user = EventHolder(name, user_name, password, address, phone_no, email, role, dob, age, event_name, event_date, time_of_event, event_duration, event_status)  

            #Call the method within the class:
            event_names, event_dates, event_holders, event_ages, event_times, event_durations, x = user.search_events()

            for p in range (0,x):
                varName = event_names[p]
                varDate = event_dates[p]
                varHolder = event_holders[p]
                varAge = event_ages[p]
                varTime = event_times[p]
                varDuration = event_durations[p]
                lines = [varName, varDate, varHolder, varAge, varTime, varDuration]
                messagebox.showinfo('Events', lines)

            ReturnBtn = Button(viewEventsForm, text='Return To Menu', command = viewEventsForm.destroy, fg = "green")
            ReturnBtn.place(x=150, y=600)
########################################################################## Edit User #######################################################################
        def EditUserForm():
            editUserForm = Toplevel(window) # Toplevel object which will be treated as a new window 
            editUserForm.title("Edit User Member Form") # sets the title of the Toplevel widget 
            editUserForm.attributes('-fullscreen', True) # sets the geometry of toplevel widget
            editUserForm.configure(bg='#d8e6db')

            #Title
            self.EditUserFormTitle = Label(editUserForm, text='Edit User:', bg='#415dfa', font=("Courier", 50)) #Title
            self.EditUserFormTitle.place(x=500, y=0)


            #Form
            #Drop down menu
            if role == "Visitor":
                
                Change = [
                "Name",
                "Date of Birth",
                "Age",
                "Username",
                "Password",
                "Address",
                "Phone Number",
                "Email"
                ]

            elif role == "School Visit":
                
                Change = [
                "Name",
                "Username",
                "Password",
                "Address",
                "Phone Number",
                "Email"
                ]

            elif role == "Event Holder":
                
                Change = [
                "Name",
                "Date of Birth",
                "Age",
                "Username",
                "Password",
                "Address",
                "Phone Number",
                "Email",
                "Event Name",
                "Event Date",
                "Event Time",
                "Event Duration",
                "Event Status"
                ]

            changeChoice = StringVar(editUserForm)
            changeChoice.set(Change[0]) # default value

            self.lblEditUserFormChangeChoice = Label(editUserForm, text='What would you like to Change:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Choice dropdown Label
            self.lblEditUserFormChangeChoice.place(x=200, y=250)
                
            self.FormUserRoleDropdown = OptionMenu(editUserForm, changeChoice, *Change)
            self.FormUserRoleDropdown.place(x=500, y=250)

            self.lblEditUserFormChange = Label(editUserForm, text='Change to:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
            self.lblEditUserFormChange.place(x=200, y=350)
                
            self.entryEditUserFormChange = Entry(editUserForm, bd=1) # Entry Field containing new details 
            self.entryEditUserFormChange.place(x=400, y=350)

            # User Only Fills In Below Field if they are changing their password
            self.lblEditUserFormOldPass = Label(editUserForm, text='Old password (Only fill in if you are changing your password):',bg='#d8e6db', font=("Courier", 15 ,'bold')) # ItemType dropdown Label
            self.lblEditUserFormOldPass.place(x=200, y=500)
                
            self.entryEditUserFormOldPass = Entry(editUserForm, bd=1) # Entry Field containing old password 
            self.entryEditUserFormOldPass.place(x=800, y=500)
                
                
            def editUser():
                #Call the user class to run - in order to run a method within it:
                if role == 'Visitor':
                    user = Visitor(name, user_name, password, address, phone_no, email, role, dob, age, books_on_loan, due_dates, users_bills)
                
                elif role == 'School Visit':
                    user = SchoolVist(name, user_name, password, address, phone_no, email, role, books_on_loan, due_dates, users_bills)

                elif role == 'Event Holder':
                    user = EventHolder(name, user_name, password, address, phone_no, email, role, dob, age, event_name, event_date, time_of_event, event_duration, event_status)  

                #Call the method within the class:
                if changeChoice.get() == "Name":
                    user.set_name(role, user_name, self.entryEditUserFormChange.get())
                elif changeChoice.get() == "Date of Birth":
                    user.set_date_of_birth(role, user_name, self.entryEditUserFormChange.get())
                elif changeChoice.get() == "Age":
                    user.set_age(role, user_name, self.entryEditUserFormChange.get())
                elif changeChoice.get() == "Username":
                    user.set_username(role, user_name, self.entryEditUserFormChange.get())
                elif changeChoice.get() == "Password":
                    user.set_password(role, user_name, self.entryEditUserFormChange.get(), self.entryEditUserFormOldPass.get())
                elif changeChoice.get() == "Address":
                    user.set_address(role, user_name, self.entryEditUserFormChange.get())
                elif changeChoice.get() == "Phone Number":
                    user.set_phone_no(role, user_name, self.entryEditUserFormChange.get())
                elif changeChoice.get() == "Email":
                    user.set_email(role, user_name, self.entryEditUserFormChange.get())
                elif changeChoice.get() == "Event Name":
                    user.set_event_name(role, user_name, self.entryEditUserFormChange.get())
                elif changeChoice.get() == "Event Date":
                    user.set_event_date(role, user_name, self.entryEditUserFormChange.get())
                elif changeChoice.get() == "Event Time":
                    user.set_time_of_event(role, user_name, self.entryEditUserFormChange.get())
                elif changeChoice.get() == "Event Duration":
                    user.set_event_duration(role, user_name, self.entryEditUserFormChange.get())
                elif changeChoice.get() == "Event Status":
                    user.set_event_status(role, user_name, self.entryEditUserFormChange.get())

                #Display message of success
                messagebox.showinfo("Information", "Success")

            SaveChangesBtn = Button(editUserForm, text='Save Changes', command = editUser, fg = "green")
            SaveChangesBtn.place(x=750, y=600)

            ReturnBtn = Button(editUserForm, text='Return To Menu', command = editUserForm.destroy, fg = "green")
            ReturnBtn.place(x=150, y=600)

###################################################################### Return Item Form - USER #####################################################################
        def UserReturnItemForm():  
            returnItemForm = Toplevel(window) # Toplevel object which will be treated as a new window 
            returnItemForm.title("Return An Item Form") # sets the title of the Toplevel widget 
            returnItemForm.attributes('-fullscreen', True) # sets the geometry of toplevel widget
            returnItemForm.configure(bg='#d8e6db')

            #Title
            self.ReturnItemForm = Label(returnItemForm, text='Return An Item:', bg='#415dfa', font=("Courier", 50)) #Title
            self.ReturnItemForm.place(x=500, y=0)

            #Form
            self.lblIssueItemFormISBNNo = Label(returnItemForm, text='ISBN Number:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # ISBN Label
            self.lblIssueItemFormISBNNo.place(x=200, y=200)
            
            self.entryIssueItemFormISBNNo = Entry(returnItemForm, bd=1) # ISBN Entry Field 
            self.entryIssueItemFormISBNNo.place(x=400, y=200)

            #Drop down menu
            itemType = [
            "DVD",
            "Newspaper_Magazine",
            "Book"
            ] 

            item_type = StringVar(returnItemForm)
            item_type.set(itemType[2]) # default value

            self.lblFormItemType = Label(returnItemForm, text='Item Type:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # ItemType dropdown Label
            self.lblFormItemType.place(x=200, y=400)
            
            self.FormItemTypeDropdown = OptionMenu(returnItemForm, item_type, *itemType)
            self.FormItemTypeDropdown.place(x=400, y=400)

            def returnItem():
                #Call the user class to run - in order to run a method within it:
                if role == 'Visitor':
                    user = Visitor(name, user_name, password, address, phone_no, email, role, dob, age, books_on_loan, due_dates, users_bills)
                
                elif role == 'School Visit':
                    user = SchoolVist(name, user_name, password, address, phone_no, email, role, books_on_loan, due_dates, users_bills)

                elif role == 'Event Holder':
                    user = EventHolder(name, user_name, password, address, phone_no, email, role, dob, age, event_name, event_date, time_of_event, event_duration, event_status)     

                #Call the method within the class:
                bills = user.return_item(self.entryIssueItemFormISBNNo.get(), item_type.get(), user_name, role, books_on_loan, due_dates, users_bills)
                #Display message of success
                return_variable = "Success. Your bill is now: £", bills
                messagebox.showinfo("Information", return_variable)

            IssueItemBtn = Button(returnItemForm, text='Return Item', command = returnItem, fg = "green")
            IssueItemBtn.place(x=750, y=600)

            ReturnBtn = Button(returnItemForm, text='Return To Menu', command = returnItemForm.destroy, fg = "green")
            ReturnBtn.place(x=150, y=600)
###################################################################### Issue Item Form - USER #####################################################################
        def UserIssueItemForm():  
            issueItemForm = Toplevel(window) # Toplevel object which will be treated as a new window 
            issueItemForm.title("Issue Item Form") # sets the title of the Toplevel widget 
            issueItemForm.attributes('-fullscreen', True) # sets the geometry of toplevel widget
            issueItemForm.configure(bg='#d8e6db')

            #Title
            self.IssueItemFormTitle = Label(issueItemForm, text='Issue An Item:', bg='#415dfa', font=("Courier", 50)) #Title
            self.IssueItemFormTitle.place(x=450, y=0)

            #Form
            self.lblIssueItemFormISBNNo = Label(issueItemForm, text='ISBN Number:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # ISBN Label
            self.lblIssueItemFormISBNNo.place(x=200, y=200)
            
            self.entryIssueItemFormISBNNo = Entry(issueItemForm, bd=1) # ISBN Entry Field 
            self.entryIssueItemFormISBNNo.place(x=400, y=200)

            #Drop down menu
            itemType = [
            "DVD",
            "Newspaper_Magazine",
            "Book"
            ] 

            item_type = StringVar(issueItemForm)
            item_type.set(itemType[2]) # default value

            self.lblFormItemType = Label(issueItemForm, text='Item Type:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # ItemType dropdown Label
            self.lblFormItemType.place(x=200, y=400)
            
            self.FormItemTypeDropdown = OptionMenu(issueItemForm, item_type, *itemType)
            self.FormItemTypeDropdown.place(x=400, y=400)


            def issue():
                #Call the user class to run - in order to run a method within it:
                if role == 'Visitor':
                    user = Visitor(name, user_name, password, address, phone_no, email, role, dob, age, books_on_loan, due_dates, users_bills)
                
                elif role == 'School Visit':
                    user = SchoolVist(name, user_name, password, address, phone_no, email, role, books_on_loan, due_dates, users_bills)

                elif role == 'Event Holder':
                    user = EventHolder(name, user_name, password, address, phone_no, email, role, dob, age, event_name, event_date, time_of_event, event_duration, event_status)  

                #Call the method within the class:
                return_date = user.issue_item(self.entryIssueItemFormISBNNo.get(), item_type.get(), user_name, role)
                #Display message of success
                return_variable = "Success. Item needs to be returned for:", return_date
                messagebox.showinfo("Information", return_variable)

            IssueItemBtn = Button(issueItemForm, text='Issue Item', command = issue, fg = "green")
            IssueItemBtn.place(x=750, y=600)

            ReturnBtn = Button(issueItemForm, text='Return To Menu', command = issueItemForm.destroy, fg = "green")
            ReturnBtn.place(x=150, y=600)

####################################################################### Billing A User Form #####################################################################        '''
        def BillUserForm():  
            billUserForm = Toplevel(window) # Toplevel object which will be treated as a new window 
            billUserForm.title("Issue Item Form") # sets the title of the Toplevel widget 
            billUserForm.attributes('-fullscreen', True) # sets the geometry of toplevel widget
            billUserForm.configure(bg='#d8e6db')

            #Title
            self.BillUserFormTitle = Label(billUserForm, text='Billing A User:', bg='#415dfa', font=("Courier", 50)) #Title
            self.BillUserFormTitle.place(x=500, y=0)

            #Form

            #Drop down menu
            userRoles = [
            "Visitor",
            "Event Holder",
            "School Visit"
            ] 

            user_role = StringVar(billUserForm)
            user_role.set(userRoles[0]) # default value

            self.lblFormUserRole = Label(billUserForm, text='User Role:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # UserRole dropdown Label
            self.lblFormUserRole.place(x=200, y=200)
            
            self.FormUserRoleDropdown = OptionMenu(billUserForm, user_role, *userRoles)
            self.FormUserRoleDropdown.place(x=400, y=200)

            self.lblBillUserFormID = Label(billUserForm, text='Username:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Username Label
            self.lblBillUserFormID.place(x=200, y=300)
            
            self.entryBillUserFormID = Entry(billUserForm, bd=1) # Username Entry Field 
            self.entryBillUserFormID.place(x=400, y=300)

            def CheckBills():
                staff = Staff(first_name, surname, dob, salary, work_hours, work_days, login_ID, password, home_address, phone_no, work_email, role)
                statement = staff.check_bills(self.entryBillUserFormID.get(), user_role.get())
                messagebox.showinfo("Information", statement)
   
            CheckBillsBtn = Button(billUserForm, text='Check Bills', command = CheckBills, fg = "blue")
            CheckBillsBtn.place(x=300, y=400)

            self.lblBillUserFormPay = Label(billUserForm, text='Please enter in the form £"0.1" how much you wish to pay:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Payment Label
            self.lblBillUserFormPay.place(x=200, y=500)
            
            self.entryBillUserFormPay = Entry(billUserForm, bd=1) # Payment Entry Field 
            self.entryBillUserFormPay.place(x=750, y=500)

            def PayBills():
                staff = Staff(first_name, surname, dob, salary, work_hours, work_days, login_ID, password, home_address, phone_no, work_email, role)
                response = staff.pay_bills(self.entryBillUserFormID.get(), user_role.get(), self.entryBillUserFormPay.get()) 
                messagebox.showinfo("Information", response)
                
            PayBillsBtn = Button(billUserForm, text='Pay Bills', command = PayBills, fg = "green")
            PayBillsBtn.place(x=750, y=600)

            ReturnBtn = Button(billUserForm, text='Return To Menu', command = billUserForm.destroy, fg = "green")
            ReturnBtn.place(x=150, y=600)
########################################################################## Item Search Form #################################################################
        
        def ItemSearchForm():  
            itemSearchForm = Toplevel(window) # Toplevel object which will be treated as a new window 
            itemSearchForm.title("Search For An Item") # sets the title of the Toplevel widget 
            itemSearchForm.attributes('-fullscreen', True) # sets the geometry of toplevel widget
            itemSearchForm.configure(bg='#d8e6db')

            #Title
            self.ItemSearchFormTitle = Label(itemSearchForm, text='Search For An Item:', bg='#415dfa', font=("Courier", 50)) #Title
            self.ItemSearchFormTitle.place(x=500, y=0)

            #Form
            
            #Drop down menu
            itemType = [
            "DVD",
            "Newspaper_Magazine",
            "Book"
            ] 

            item_type = StringVar(itemSearchForm)
            item_type.set(itemType[2]) # default value

            self.lblFormItemType = Label(itemSearchForm, text='Item Type:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # ItemType dropdown Label
            self.lblFormItemType.place(x=200, y=200)
            
            self.FormItemTypeDropdown = OptionMenu(itemSearchForm, item_type, *itemType)
            self.FormItemTypeDropdown.place(x=400, y=200)

            self.lblItemSearchName = Label(itemSearchForm, text='Item Name:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Item Name Label
            self.lblItemSearchName.place(x=200, y=400)
            
            self.entryItemSearchName = Entry(itemSearchForm, bd=1) # Item Name Entry Field 
            self.entryItemSearchName.place(x=400, y=400)

            def ItemSearch():
                staff = Staff(first_name, surname, dob, salary, work_hours, work_days, login_ID, password, home_address, phone_no, work_email, role)
                date, status, copies = staff.search_item(item_type.get(), self.entryItemSearchName.get())
                info = date, status, copies 
                messagebox.showinfo("Information", info)
                
            ItemSearchBtn = Button(itemSearchForm, text='Search', command = ItemSearch, fg = "green")
            ItemSearchBtn.place(x=750, y=600)

            ReturnBtn = Button(itemSearchForm, text='Return To Menu', command = itemSearchForm.destroy, fg = "green")
            ReturnBtn.place(x=150, y=600)
        
########################################################################## Edit Staff #######################################################################
        
        def EditStaffForm():
            if role == 'Manager':
                editStaffForm = Toplevel(window) # Toplevel object which will be treated as a new window 
                editStaffForm.title("Edit Staff Member Form") # sets the title of the Toplevel widget 
                editStaffForm.attributes('-fullscreen', True) # sets the geometry of toplevel widget
                editStaffForm.configure(bg='#d8e6db')

                #Title
                self.EditStaffFormTitle = Label(editStaffForm, text='Edit Staff:', bg='#415dfa', font=("Courier", 50)) #Title
                self.EditStaffFormTitle.place(x=500, y=0)


                #Form
                self.lblEditStaffFormUsername = Label(editStaffForm, text='Username:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Username Label
                self.lblEditStaffFormUsername.place(x=200, y=200)

                self.entryEditStaffFormUsername = Entry(editStaffForm, bd=1) # Username Entry Field
                self.entryEditStaffFormUsername.place(x=400, y=200)

                #Drop down menu
                staffRoles = [
                "Junior",
                "Senior",
                "Manager"
                ] 

                staff_role = StringVar(editStaffForm)
                staff_role.set(staffRoles[0]) # default value

                self.lblFormStaffRole = Label(editStaffForm, text='Staff Role (Of whose details you are changing):',bg='#d8e6db', font=("Courier", 15 ,'bold')) # StaffRole dropdown Label
                self.lblFormStaffRole.place(x=200, y=300)
                
                self.FormStaffRoleDropdown = OptionMenu(editStaffForm, staff_role, *staffRoles)
                self.FormStaffRoleDropdown.place(x=650, y=300)

                #Drop down menu
                Change = [
                "First Name",
                "Surname",
                "Date of Birth",
                "Salary",
                "Work Hours",
                "Work Days",
                "Username",
                "Password",
                "Home Address",
                "Phone Number",
                "Work Email",
                ] 

                changeChoice = StringVar(editStaffForm)
                changeChoice.set(Change[0]) # default value

                self.lblEditStaffFormChangeChoice = Label(editStaffForm, text='What would you like to Change:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Choice dropdown Label
                self.lblEditStaffFormChangeChoice.place(x=200, y=250)
                
                self.FormStaffRoleDropdown = OptionMenu(editStaffForm, changeChoice, *Change)
                self.FormStaffRoleDropdown.place(x=500, y=250)

                self.lblEditStaffFormChange = Label(editStaffForm, text='Change to:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Change Label
                self.lblEditStaffFormChange.place(x=200, y=350)
                
                self.entryEditStaffFormChange = Entry(editStaffForm, bd=1) # Entry Field containing new details 
                self.entryEditStaffFormChange.place(x=400, y=350)

                # User Only Fills In Below Field if they are changing their password
                self.lblEditStaffFormOldPass = Label(editStaffForm, text='Old password (Only fill in if you are changing your password):',bg='#d8e6db', font=("Courier", 15 ,'bold')) # ItemType dropdown Label
                self.lblEditStaffFormOldPass.place(x=200, y=500)
                
                self.entryEditStaffFormOldPass = Entry(editStaffForm, bd=1) # Entry Field containing old password 
                self.entryEditStaffFormOldPass.place(x=800, y=500)
                
                
                def editStaff():
                    #Call the staff class to run - in order to run a method within it:
                    staff = Manager(first_name, surname, dob, salary, work_hours, work_days, login_ID, password, home_address, phone_no, work_email, role) 

                    #Call the method within the class:
                    if changeChoice.get() == "First Name":
                        staff.set_first_name(staff_role.get(), self.entryEditStaffFormUsername.get(), self.entryEditStaffFormChange.get())
                    elif changeChoice.get() == "Surname":
                        staff.set_last_name(staff_role.get(), self.entryEditStaffFormUsername.get(), self.entryEditStaffFormChange.get())
                    elif changeChoice.get() == "Date of Birth":
                        staff.set_date_of_birth(staff_role.get(), self.entryEditStaffFormUsername.get(), self.entryEditStaffFormChange.get())
                    elif changeChoice.get() == "Salary":
                        staff.set_salary(staff_role.get(), self.entryEditStaffFormUsername.get(), self.entryEditStaffFormChange.get())
                    elif changeChoice.get() == "Work Hours":
                        staff.set_work_hours(staff_role.get(), self.entryEditStaffFormUsername.get(), self.entryEditStaffFormChange.get())
                    elif changeChoice.get() == "Work Days":
                        staff.set_work_days(staff_role.get(), self.entryEditStaffFormUsername.get(), self.entryEditStaffFormChange.get())
                    elif changeChoice.get() == "Username":
                        staff.set_login_id(staff_role.get(), self.entryEditStaffFormUsername.get(), self.entryEditStaffFormChange.get())
                    elif changeChoice.get() == "Password":
                        staff.set_password(staff_role.get(), self.entryEditStaffFormUsername.get(), self.entryEditStaffFormChange.get(), self.entryEditStaffFormOldPass.get())
                    elif changeChoice.get() == "Home Address":
                        staff.set_home_address(staff_role.get(), self.entryEditStaffFormUsername.get(), self.entryEditStaffFormChange.get())
                    elif changeChoice.get() == "Phone Number":
                        staff.set_phone_no(staff_role.get(), self.entryEditStaffFormUsername.get(), self.entryEditStaffFormChange.get())
                    elif changeChoice.get() == "Work Email":
                        staff.set_work_email(staff_role.get(), self.entryEditStaffFormUsername.get(), self.entryEditStaffFormChange.get())

                    #Display message of success
                    messagebox.showinfo("Information", "Success")

                SaveChangesBtn = Button(editStaffForm, text='Save Changes', command = editStaff, fg = "green")
                SaveChangesBtn.place(x=750, y=600)

                ReturnBtn = Button(editStaffForm, text='Return To Menu', command = editStaffForm.destroy, fg = "green")
                ReturnBtn.place(x=150, y=600)
                
            else:
                messagebox.showinfo("Error", "You are not a Manager")
########################################################################## Return Item ######################################################################
        def ReturnItemForm():  
            returnItemForm = Toplevel(window) # Toplevel object which will be treated as a new window 
            returnItemForm.title("Return An Item Form") # sets the title of the Toplevel widget 
            returnItemForm.attributes('-fullscreen', True) # sets the geometry of toplevel widget
            returnItemForm.configure(bg='#d8e6db')

            #Title
            self.ReturnItemForm = Label(returnItemForm, text='Return An Item:', bg='#415dfa', font=("Courier", 50)) #Title
            self.ReturnItemForm.place(x=500, y=0)

            #Form
            self.lblIssueItemFormUsername = Label(returnItemForm, text='Username:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Username Label
            self.lblIssueItemFormUsername.place(x=200, y=200)

            self.entryIssueItemFormUsername = Entry(returnItemForm, bd=1) # Username Entry Field
            self.entryIssueItemFormUsername.place(x=400, y=200)

            #Drop down menu
            userRoles = [
            "Visitor",
            "Event Holder",
            "School Visit"
            ] 

            user_role = StringVar(returnItemForm)
            user_role.set(userRoles[0]) # default value

            self.lblFormUserRole = Label(returnItemForm, text='User Role:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # UserRole dropdown Label
            self.lblFormUserRole.place(x=200, y=300)
            
            self.FormUserRoleDropdown = OptionMenu(returnItemForm, user_role, *userRoles)
            self.FormUserRoleDropdown.place(x=400, y=300)

            self.lblIssueItemFormISBNNo = Label(returnItemForm, text='ISBN Number:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # ISBN Label
            self.lblIssueItemFormISBNNo.place(x=200, y=400)
            
            self.entryIssueItemFormISBNNo = Entry(returnItemForm, bd=1) # ISBN Entry Field 
            self.entryIssueItemFormISBNNo.place(x=400, y=400)

            #Drop down menu
            itemType = [
            "DVD",
            "Newspaper_Magazine",
            "Book"
            ] 

            item_type = StringVar(returnItemForm)
            item_type.set(itemType[2]) # default value

            self.lblFormItemType = Label(returnItemForm, text='Item Type:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # ItemType dropdown Label
            self.lblFormItemType.place(x=200, y=500)
            
            self.FormItemTypeDropdown = OptionMenu(returnItemForm, item_type, *itemType)
            self.FormItemTypeDropdown.place(x=400, y=500)

            def returnItem():
                #Call the staff class to run - in order to run a method within it:
                staff = Staff(first_name, surname, dob, salary, work_hours, work_days, login_ID, password, home_address, phone_no, work_email, role) 
                #Call the method within the class:
                bills = staff.return_item(self.entryIssueItemFormISBNNo.get(), item_type.get(), self.entryIssueItemFormUsername.get(), user_role.get())
                #Display message of success
                return_variable = "Success. Your bill is now: £", bills
                messagebox.showinfo("Information", return_variable)

            IssueItemBtn = Button(returnItemForm, text='Return Item', command = returnItem, fg = "green")
            IssueItemBtn.place(x=750, y=600)

            ReturnBtn = Button(returnItemForm, text='Return To Menu', command = returnItemForm.destroy, fg = "green")
            ReturnBtn.place(x=150, y=600)
######################################################################## Issue Item Form ##############################################################
        def IssueItemForm():  
            issueItemForm = Toplevel(window) # Toplevel object which will be treated as a new window 
            issueItemForm.title("Issue Item Form") # sets the title of the Toplevel widget 
            issueItemForm.attributes('-fullscreen', True) # sets the geometry of toplevel widget
            issueItemForm.configure(bg='#d8e6db')

            #Title
            self.IssueItemFormTitle = Label(issueItemForm, text='Issue An Item:', bg='#415dfa', font=("Courier", 50)) #Title
            self.IssueItemFormTitle.place(x=450, y=0)

            #Form
            self.lblIssueItemFormUsername = Label(issueItemForm, text='Username:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # Username Label
            self.lblIssueItemFormUsername.place(x=200, y=200)

            self.entryIssueItemFormUsername = Entry(issueItemForm, bd=1) # Username Entry Field
            self.entryIssueItemFormUsername.place(x=400, y=200)

            #Drop down menu
            userRoles = [
            "Visitor",
            "Event Holder",
            "School Visit"
            ] 

            user_role = StringVar(issueItemForm)
            user_role.set(userRoles[0]) # default value

            self.lblFormUserRole = Label(issueItemForm, text='User Role:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # UserRole dropdown Label
            self.lblFormUserRole.place(x=200, y=300)
            
            self.FormUserRoleDropdown = OptionMenu(issueItemForm, user_role, *userRoles)
            self.FormUserRoleDropdown.place(x=400, y=300)

            self.lblIssueItemFormISBNNo = Label(issueItemForm, text='ISBN Number:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # ISBN Label
            self.lblIssueItemFormISBNNo.place(x=200, y=400)
            
            self.entryIssueItemFormISBNNo = Entry(issueItemForm, bd=1) # ISBN Entry Field 
            self.entryIssueItemFormISBNNo.place(x=400, y=400)

            #Drop down menu
            itemType = [
            "DVD",
            "Newspaper_Magazine",
            "Book"
            ] 

            item_type = StringVar(issueItemForm)
            item_type.set(itemType[2]) # default value

            self.lblFormItemType = Label(issueItemForm, text='Item Type:',bg='#d8e6db', font=("Courier", 15 ,'bold')) # ItemType dropdown Label
            self.lblFormItemType.place(x=200, y=500)
            
            self.FormItemTypeDropdown = OptionMenu(issueItemForm, item_type, *itemType)
            self.FormItemTypeDropdown.place(x=400, y=500)

            def issue():
                #Call the staff class to run - in order to run a method within it:
                staff = Staff(first_name, surname, dob, salary, work_hours, work_days, login_ID, password, home_address, phone_no, work_email, role) 
                #Call the method within the class:
                return_date = staff.issue_item(self.entryIssueItemFormISBNNo.get(), item_type.get(), self.entryIssueItemFormUsername.get(), user_role.get())
                #Display message of success
                return_variable = "Success. Item needs to be returned for:", return_date
                messagebox.showinfo("Information", return_variable)

            IssueItemBtn = Button(issueItemForm, text='Issue Item', command = issue, fg = "green")
            IssueItemBtn.place(x=750, y=600)

            ReturnBtn = Button(issueItemForm, text='Return To Menu', command = issueItemForm.destroy, fg = "green")
            ReturnBtn.place(x=150, y=600)

######################################################################## Staff Selection Menu #################################################################
        def StaffSelectionMenu():
            staffSelectionMenu = Toplevel(window) # Toplevel object which will be treated as a new window 
            staffSelectionMenu.title("Staff Menu") # sets the title of the Toplevel widget 
            staffSelectionMenu.attributes('-fullscreen', True) # sets the geometry of toplevel widget
            staffSelectionMenu.configure(bg='#415dfa')

            #Title
            self.staffSelectionTitle = Label(staffSelectionMenu, text='Selection Menu:', bg='#415dfa', font=("Courier", 50)) #Title
            self.staffSelectionTitle.place(x=500, y=0)

            #Options
            IssueItemBtn = Button(staffSelectionMenu, text='Issue An Item', command = IssueItemForm)
            IssueItemBtn.place(x=400, y=100)
            ReturnItemBtn = Button(staffSelectionMenu, text='Return Item', command = ReturnItemForm)
            ReturnItemBtn.place(x=400, y=200)
            EditUserBtn = Button(staffSelectionMenu, text='Edit Staff', command = EditStaffForm)
            EditUserBtn.place(x=400, y=300)
            ItemSearchBtn = Button(staffSelectionMenu, text='Item Search', command = ItemSearchForm)
            ItemSearchBtn.place(x=400, y=400)
            BillsBtn = Button(staffSelectionMenu, text='Billing A User', command = BillUserForm)
            BillsBtn.place(x=400, y=500)
            AddStaffBtn = Button(staffSelectionMenu, text='Add A Staff Member', command = AddStaff)
            AddStaffBtn.place(x=400, y=600)
            AddUserBtn = Button(staffSelectionMenu, text='Add A User Member', command = AddUser)
            AddUserBtn.place(x=700, y=100)
            AddItemBtn = Button(staffSelectionMenu, text='Add An Item', command = AddItem)
            AddItemBtn.place(x=700, y=200)
            ProfileBtn = Button(staffSelectionMenu, text='View Profile', command = ViewStaffProfile)
            ProfileBtn.place(x=1000, y=10)

            #Images
            self.issueCanvas = Canvas(staffSelectionMenu, width = 70, height = 70)  
            self.issueCanvas.pack()
            self.image_issue = PhotoImage(file="img/open-book.png")
            self.issueCanvas.create_image(0, 0, anchor=NW, image=self.image_issue)
            self.issueCanvas.place(x=550, y=60)

            self.returnCanvas = Canvas(staffSelectionMenu, width = 70, height = 70)  
            self.returnCanvas.pack()
            self.image_return = PhotoImage(file="img/back.png")
            self.returnCanvas.create_image(0, 0, anchor=NW, image=self.image_return)
            self.returnCanvas.place(x=550, y=160)
            
            self.editCanvas = Canvas(staffSelectionMenu, width = 70, height = 70)  
            self.editCanvas.pack()
            self.image_edit = PhotoImage(file="img/editStaff.png")
            self.editCanvas.create_image(0, 0, anchor=NW, image=self.image_edit)
            self.editCanvas.place(x=550, y=260)

            self.searchCanvas = Canvas(staffSelectionMenu, width = 70, height = 70)  
            self.searchCanvas.pack()
            self.image_search = PhotoImage(file="img/search.png")
            self.searchCanvas.create_image(0, 0, anchor=NW, image=self.image_search)
            self.searchCanvas.place(x=550, y=360)

            self.billCanvas = Canvas(staffSelectionMenu, width = 70, height = 70)  
            self.billCanvas.pack()
            self.image_bill = PhotoImage(file="img/bill.png")
            self.billCanvas.create_image(0, 0, anchor=NW, image=self.image_bill)
            self.billCanvas.place(x=550, y=460)

            self.addStaffCanvas = Canvas(staffSelectionMenu, width = 70, height = 70)  
            self.addStaffCanvas.pack()
            self.imageAddStaff = PhotoImage(file="img/add.png")
            self.addStaffCanvas.create_image(0, 0, anchor=NW, image=self.imageAddStaff)
            self.addStaffCanvas.place(x=550, y=560)

            self.addUserCanvas = Canvas(staffSelectionMenu, width = 70, height = 70)  
            self.addUserCanvas.pack()
            self.imageAddUser = PhotoImage(file="img/add.png")
            self.addUserCanvas.create_image(0, 0, anchor=NW, image=self.imageAddUser)
            self.addUserCanvas.place(x=850, y=60)

            self.addItemCanvas = Canvas(staffSelectionMenu, width = 70, height = 70)  
            self.addItemCanvas.pack()
            self.imageAddItem = PhotoImage(file="img/item.png")
            self.addItemCanvas.create_image(0, 0, anchor=NW, image=self.imageAddItem)
            self.addItemCanvas.place(x=850, y=160)

            self.profileCanvas = Canvas(staffSelectionMenu, width = 70, height = 70)  
            self.profileCanvas.pack()
            self.imageProfile = PhotoImage(file="img/profile.png")
            self.profileCanvas.create_image(0, 0, anchor=NW, image=self.imageProfile)
            self.profileCanvas.place(x=1100, y=5)

######################################################################## User Selection Menu #################################################################
        def UserSelectionMenu():
            userSelectionMenu = Toplevel(window) # Toplevel object which will be treated as a new window 
            userSelectionMenu.title("User Menu") # sets the title of the Toplevel widget 
            userSelectionMenu.attributes('-fullscreen', True) # sets the geometry of toplevel widget
            userSelectionMenu.configure(bg='#93DF31')

            #Title
            self.userSelectionTitle = Label(userSelectionMenu, text='Selection Menu:', bg='#93DF31', font=("Courier", 50)) #Title
            self.userSelectionTitle.place(x=500, y=0)

            #Options
            TakeOutItemBtn = Button(userSelectionMenu, text='Take Out An Item', command = UserIssueItemForm)
            TakeOutItemBtn.place(x=400, y=200)
            ReturnItemBtn = Button(userSelectionMenu, text='Return Item', command = UserReturnItemForm)
            ReturnItemBtn.place(x=400, y=300)
            WriteReviewBtn = Button(userSelectionMenu, text='Edit User', command = EditUserForm) 
            WriteReviewBtn.place(x=400, y=400)
            ViewReviewsBtn = Button(userSelectionMenu, text='View Events', command = ViewEventsForm) 
            ViewReviewsBtn.place(x=400, y=500)
            ViewHistoryBtn = Button(userSelectionMenu, text='View books on loan', command = ViewBooksOnLoan) 
            ViewHistoryBtn.place(x=400, y=600)
            ItemSearchBtn = Button(userSelectionMenu, text='Item Search', command = UserItemSearchForm)
            ItemSearchBtn.place(x=800, y=200)
            ProfileBtn = Button(userSelectionMenu, text='View Profile', command = ViewUserProfile)
            ProfileBtn.place(x=1000, y=10) 

            #Images
            self.issueCanvas = Canvas(userSelectionMenu, width = 70, height = 70)  
            self.issueCanvas.pack()
            self.image_issue = PhotoImage(file="img/issue.png")
            self.issueCanvas.create_image(0, 0, anchor=NW, image=self.image_issue)
            self.issueCanvas.place(x=550, y=160)

            self.returnCanvas = Canvas(userSelectionMenu, width = 70, height = 70)  
            self.returnCanvas.pack()
            self.image_return = PhotoImage(file="img/return.png")
            self.returnCanvas.create_image(0, 0, anchor=NW, image=self.image_return)
            self.returnCanvas.place(x=550, y=260)
            
            self.editCanvas = Canvas(userSelectionMenu, width = 70, height = 70)  
            self.editCanvas.pack()
            self.image_edit = PhotoImage(file="img/editUser.png")
            self.editCanvas.create_image(0, 0, anchor=NW, image=self.image_edit)
            self.editCanvas.place(x=550, y=360)

            self.eventCanvas = Canvas(userSelectionMenu, width = 70, height = 70)  
            self.eventCanvas.pack()
            self.image_events = PhotoImage(file="img/events.png")
            self.eventCanvas.create_image(0, 0, anchor=NW, image=self.image_events)
            self.eventCanvas.place(x=550, y=460)

            self.loanCanvas = Canvas(userSelectionMenu, width = 70, height = 70)  
            self.loanCanvas.pack()
            self.image_loans = PhotoImage(file="img/history.png")
            self.loanCanvas.create_image(0, 0, anchor=NW, image=self.image_loans)
            self.loanCanvas.place(x=550, y=560)

            self.searchCanvas = Canvas(userSelectionMenu, width = 70, height = 70)  
            self.searchCanvas.pack()
            self.image_search = PhotoImage(file="img/itemS.png")
            self.searchCanvas.create_image(0, 0, anchor=NW, image=self.image_search)
            self.searchCanvas.place(x=900, y=160)

            self.profileCanvas = Canvas(userSelectionMenu, width = 70, height = 70)  
            self.profileCanvas.pack()
            self.imageProfile = PhotoImage(file="img/profileUser.png")
            self.profileCanvas.create_image(0, 0, anchor=NW, image=self.imageProfile)
            self.profileCanvas.place(x=1100, y=5)
####################################################################### User Login Page ########################################################################################################

        def UserLogInPage():
            userLoginPage = Toplevel(window) # Toplevel object which will be treated as a new window 
            userLoginPage.title("User Login") # sets the title of the Toplevel widget 
            userLoginPage.attributes('-fullscreen', True) # sets the geometry of toplevel widget
            userLoginPage.configure(bg='#008a70')

            #Title
            self.titleUser=Label(userLoginPage, text='Login Page:', bg='#008a70', font=("Courier", 50)) #Title
            self.titleUser.place(x=500, y=0)

            #Drop down menu
            userRoles = [
            "Visitor",
            "Event Holder",
            "School Visit"
            ] 

            user_role = StringVar(userLoginPage)
            user_role.set(userRoles[0]) # default value

            self.staffDropdown = OptionMenu(userLoginPage, user_role, *userRoles)
            self.staffDropdown.place(x=400, y=200)

            self.lblUserType = Label(userLoginPage, text='User Type:',bg='#008a70', font=("Courier", 15 ,'bold')) # Staff type Label
            self.lblUserType.place(x=200, y=200)
            
            #Entries and Labels
            self.lblUserUser = Label(userLoginPage, text='Username:',bg='#008a70', font=("Courier", 15 ,'bold')) # Username Label
            self.lblUserUser.place(x=200, y=300)
            
            self.lblUserPass = Label(userLoginPage, text='Password:',bg='#008a70', font=("Courier", 15 ,'bold')) # Password Label
            self.lblUserPass.place(x=200, y=400)

            self.entryUserUser = Entry(userLoginPage, bd=1) # Username Entry Field
            self.entryUserUser.place(x=400, y=300)

            self.entryUserPass = Entry(userLoginPage, bd=1) # Password Entry Field
            self.entryUserPass.place(x=400, y=400)

            #button commands - a button widget which will open a new window on button click

            def UserLogIn():
                logInSuccess = 'False' #sets the variable as False initially unless it is changed by the below function
                
                if user_role.get() == 'Visitor':
                    print('You have selected Visitor')
                    for p in user_data['Visitor']: 
                        if p['user_name'] == self.entryUserUser.get() and p['password'] == self.entryUserPass.get(): #For loop checks if the username and password matches and exists within the staff.json file
                            print(p['name'],'You have succesfully logged in!')
                            
                            logInSuccess = 'True' #sets the variable as true so that the function UserLogIn_Menu can run
                            
                            #Below are the variables which will store the users details:
                            name = p['name']
                            user_name = p['user_name']
                            password = p['password']
                            address = p['address']
                            phone_no = p['phone_no']
                            email = p['email']
                            role = p['role']
                            dob = p['dob']
                            age = p['age']
                            books_on_loan  = p['books_on_loan']
                            due_dates = p['due_dates']                
                            users_bills = p['bills']

                            return logInSuccess, name, user_name, password, address, phone_no, email, role, dob, age, books_on_loan, due_dates, users_bills
                            
                        else:
                            print('Incorrect details')

                elif user_role.get() == 'Event Holder':
                    print('You have selected Event Holder')
                    for p in user_data['Event Holder']: 
                        if p['user_name'] == self.entryUserUser.get() and p['password'] == self.entryUserPass.get():  
                            print(p['name'],'You have succesfully logged in!')

                            #Below are the variables which will store the users details:
                            name = p['name']
                            user_name = p['user_name']
                            password = p['password']
                            address = p['address']
                            phone_no = p['phone_no']
                            email = p['email']
                            role = p['role']
                            dob = p['dob']
                            age = p['age']
                            event_name  = p['event_name']
                            event_date  = p['event_date']          
                            time_of_event = p['time_of_event']                
                            event_duration = p['event_duration']
                            event_status  = p['event_status']

                            logInSuccess = 'True'

                            return logInSuccess, name, user_name, password, address, phone_no, email, role, dob, age, event_name, event_date, time_of_event, event_status, event_duration  

                        else:
                            print('Incorrect details')

                elif user_role.get() == 'School Visit':
                    print('You have selected School Visit')
                    for p in user_data['School Visit']: 
                        if p['user_name'] == self.entryUserUser.get() and p['password'] == self.entryUserPass.get(): 
                            print(p['name'],'You have succesfully logged in!')

                            #Below are the variables which will store the users details:
                            name = p['name']
                            user_name = p['user_name']
                            password = p['password']
                            address = p['address']
                            phone_no = p['phone_no']
                            email = p['email']
                            role = p['role']
                            books_on_loan  = p['books_on_loan']
                            due_dates = p['due_dates']                
                            users_bills = p['bills']

                            logInSuccess = 'True'

                            return logInSuccess, name, user_name, password, address, phone_no, email, role, books_on_loan, due_dates, users_bills

                        else:
                            print('Incorrect details')
                else:
                    print('Unknown input')
            
            def UserLogIn_Menu(): #Function for validating users login and then opens a new window
                
                #If login success == 'True' it will store all the correspodning returned values
                if user_role.get()== 'Visitor':
                    logInSuccess, name, user_name, password, address, phone_no, email, role, dob, age, books_on_loan, due_dates, users_bills = UserLogIn()
                    UserStoreVisitor(name, user_name, password, address, phone_no, email, role, dob, age, books_on_loan, due_dates, users_bills)
                elif user_role.get() == 'School Visit':
                    logInSuccess, name, user_name, password, address, phone_no, email, role, books_on_loan, due_dates, users_bills = UserLogIn()
                    UserStoreSchoolVisit(name, user_name, password, address, phone_no, email, role, books_on_loan, due_dates, users_bills)
                elif user_role.get() == 'Event Holder':
                    logInSuccess, name, user_name, password, address, phone_no, email, role, dob, age, event_name, event_date, time_of_event, event_status, event_duration = UserLogIn()
                    UserStoreEventHolder(name, user_name, password, address, phone_no, email, role, dob, age, event_name, event_date, time_of_event, event_status, event_duration)
                    
                # Function below is for validating the users login
                if logInSuccess == 'True':
                    UserSelectionMenu()
                
            UserlogInBtn = Button(userLoginPage, text='Log In', command = UserLogIn_Menu, fg = "green")
            UserlogInBtn.place(x=750, y=400)

######################################################################### Staff Login Page ########################################################################################################

        def StaffLogInPage(): # Function to open a staff login page window 
            staffLoginPage = Toplevel(window) # Toplevel object which will be treated as a new window 
            staffLoginPage.title("Staff Login") # sets the title of the Toplevel widget
            staffLoginPage.attributes('-fullscreen', True) # sets the geometry of toplevel widget
            staffLoginPage.configure(bg='#008a70')

            #Title
            self.titleStaff=Label(staffLoginPage, text='Login Page:', bg='#008a70', font=("Courier", 50)) #Title
            self.titleStaff.place(x=500, y=0)

            #Drop down menu
            staffWorkers = [
            "Junior",
            "Senior",
            "Manager"
            ] 

            staff_role = StringVar(staffLoginPage)
            staff_role.set(staffWorkers[0]) # default value

            self.staffDropdown = OptionMenu(staffLoginPage, staff_role, *staffWorkers)
            self.staffDropdown.place(x=400, y=200)

            self.lblStaffUser = Label(staffLoginPage, text='Staff Type:',bg='#008a70', font=("Courier", 15 ,'bold')) # Staff type Label
            self.lblStaffUser.place(x=200, y=200)
            
            #Entries and Labels
            self.lblStaffUser = Label(staffLoginPage, text='Username:',bg='#008a70', font=("Courier", 15 ,'bold')) # Username Label
            self.lblStaffUser.place(x=200, y=300)
            
            self.lblStaffPass = Label(staffLoginPage, text='Password:',bg='#008a70', font=("Courier", 15 ,'bold')) # Password Label
            self.lblStaffPass.place(x=200, y=400)

            self.entryStaffUser = Entry(staffLoginPage, bd=1) # Username Entry Field
            self.entryStaffUser.place(x=400, y=300)

            self.entryStaffPass = Entry(staffLoginPage, bd=1) # Password Entry Field
            self.entryStaffPass.place(x=400, y=400)

            
            #button commands - a button widget which will open a new window on button click
            def StaffLogIn():
                logInSuccess = 'False' #sets the variable as False initially unless it is changed by the below function
                
                if staff_role.get() == 'Junior':
                    print('You have selected Junior staff member')
                    for p in staff_data['Junior']: 
                        if p['login_ID'] == self.entryStaffUser.get() and p['password'] == self.entryStaffPass.get(): #For loop checks if the username and password matches and exists within the staff.json file
                            print(p['first_name'],'You have succesfully logged in!')

                            logInSuccess = 'True' #sets the variable as true so that the function UserLogIn_Menu can run
                            
                            #Below are the variables which will store the users details:
                            first_name = p['first_name']
                            surname = p['surname']
                            dob = p['dob']
                            salary = p['salary']
                            work_hours = p['work_hours']
                            work_days = p['work_days']
                            login_ID = p['login_ID']
                            password = p['password']
                            home_address = p['home_address']
                            phone_no = p['phone_no']
                            work_email = p['work_email']
                            role = p['role']

                            return logInSuccess, first_name, surname, dob, salary, work_hours, work_days, login_ID, password, home_address, phone_no, work_email, role 
                        else:
                            print('Incorrect details')

                elif staff_role.get() == 'Senior':
                    print('You have selected Senior staff member') 
                    for p in staff_data['Senior']: 
                        if p['login_ID'] == self.entryStaffUser.get() and p['password'] == self.entryStaffPass.get():
                            print(p['first_name'],'You have succesfully logged in!')

                            logInSuccess = 'True'

                            #Below are the variables which will store the users details:
                            first_name = p['first_name']
                            surname = p['surname']
                            dob = p['dob']
                            salary = p['salary']
                            work_hours = p['work_hours']
                            work_days = p['work_days']
                            login_ID = p['login_ID']
                            password = p['password']
                            home_address = p['home_address']
                            phone_no = p['phone_no']
                            work_email = p['work_email']
                            role = p['role']

                            return logInSuccess, first_name, surname, dob, salary, work_hours, work_days, login_ID, password, home_address, phone_no, work_email, role 
                            
                        else:
                            print('Incorrect details')

                elif staff_role.get() == 'Manager':
                    print('You have selected Manager staff member')
                    for p in staff_data['Manager']: 
                        if p['login_ID'] == self.entryStaffUser.get() and p['password'] == self.entryStaffPass.get():
                            print(p['first_name'],'You have succesfully logged in!')

                            logInSuccess = 'True'

                            #Below are the variables which will store the users details:
                            first_name = p['first_name']
                            surname = p['surname']
                            dob = p['dob']
                            salary = p['salary']
                            work_hours = p['work_hours']
                            work_days = p['work_days']
                            login_ID = p['login_ID']
                            password = p['password']
                            home_address = p['home_address']
                            phone_no = p['phone_no']
                            work_email = p['work_email']
                            role = p['role']

                            return logInSuccess, first_name, surname, dob, salary, work_hours, work_days, login_ID, password, home_address, phone_no, work_email, role 
                        else:
                            print('Incorrect details')

                else:
                    print('Unknown Input!')

            def StaffLogIn_Menu(): #Function for validating Staff login and then opens a new window
                
                logInSuccess, first_name, surname, dob, salary, work_hours, work_days, login_ID, password, home_address, phone_no, work_email, role = StaffLogIn()

                if logInSuccess == 'True':
                    StaffStore(first_name, surname, dob, salary, work_hours, work_days, login_ID, password, home_address, phone_no, work_email, role)
                    StaffSelectionMenu()
            
            StafflogInBtn = Button(staffLoginPage, text='Log In', command = StaffLogIn_Menu, fg = "green")
            StafflogInBtn.place(x=750, y=400)

#################################################################### Start Window ########################################################################################################

        #labels
        self.lblWelcome=Label(win, text='Welcome:', bg='#008a70', font=("Courier", 50))
        self.lblChoose=Label(win, text='Please select what type of a user you are:',bg='#008a70', font=("Courier", 15 ,'bold'))

        #label placement
        self.lblWelcome.place(x=500, y=0)
        self.lblChoose.place(x=75, y=200)

        #Function for making - Staff - variables needed, global:
        def StaffStore(firstName, Surname, DoB, Salary, Work_Hours, Work_Days, Login_ID, Password, Home_Address, Phone_No, Work_Email, Role):
            global first_name
            global surname
            global dob
            global salary
            global work_hours
            global work_days
            global login_ID
            global password
            global home_address
            global phone_no
            global work_email
            global role
            first_name = firstName
            surname = Surname
            dob = DoB
            salary = Salary
            work_hours = Work_Hours
            work_days = Work_Days
            login_ID = Login_ID
            password = Password
            home_address = Home_Address
            phone_no = Phone_No
            work_email = Work_Email
            role = Role

        #Function for making - Visitor User - variables needed, global:
        def UserStoreVisitor(Name, User_Name, Password, Address, Phone_No, Email, Role, DoB, Age, Books_On_Loan, Due_Dates, Users_Bills):
            global name
            global user_name
            global password
            global address
            global phone_no
            global email
            global role
            global dob
            global age
            global books_on_loan
            global due_dates
            global users_bills
            name = Name
            user_name = User_Name
            password = Password
            address = Address
            phone_no = Phone_No
            email = Email
            role = Role
            dob = DoB
            age = Age
            books_on_loan = Books_On_Loan
            due_dates = Due_Dates
            users_bills = Users_Bills

        #Function for making - School Visit User - variables needed, global:
        def UserStoreSchoolVisit(Name, User_Name, Password, Address, Phone_No, Email, Role, Books_On_Loan, Due_Dates, Users_Bills):
            global name
            global user_name
            global password
            global address
            global phone_no
            global email
            global role
            global books_on_loan
            global due_dates
            global users_bills
            name = Name
            user_name = User_Name
            password = Password
            address = Address
            phone_no = Phone_No
            email = Email
            role = Role
            books_on_loan = Books_On_Loan
            due_dates = Due_Dates
            users_bills = Users_Bills
            
        #Function for making - Visitor Event Holder - variables needed, global:
        def UserStoreEventHolder(Name, User_Name, Password, Address, Phone_No, Email, Role, DoB, Age, Event_Name, Event_Date, Time_Of_Event, Event_Status, Event_Duration):
            global name
            global user_name
            global password
            global address
            global phone_no
            global email
            global role
            global dob
            global age
            global event_name
            global event_date
            global event_duration
            global time_of_event
            global event_status
            name = Name
            user_name = User_Name
            password = Password
            address = Address
            phone_no = Phone_No
            email = Email
            role = Role
            dob = DoB
            age = Age
            event_name = Event_Name
            event_date = Event_Date
            time_of_event = Time_Of_Event
            event_status = Event_Status
            event_duration = Event_Duration
            
        #button commands - a button widget which will open a new window on button click
        self.bStaff=Button(win, text='Staff', command = StaffLogInPage)
        self.bUser=Button(win, text='User', command = UserLogInPage)

        self.bStaff.place(x=750, y=400)
        self.bUser.place(x=450, y=400)

window=Tk()
mywin=StartWindow(window)
window.configure(bg='#008a70')
window.title('Start Page')
window.attributes('-fullscreen', True)
window.mainloop()



