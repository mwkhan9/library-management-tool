import json
import os.path

from datetime import datetime
from datetime import timedelta

############################################################################## Data Section ################################################################
if os.path.exists('staff.json') == True:
    with open('staff.json') as json_file:
        staff_data = json.load(json_file)
else:
    staff_data = {}
    staff_data['Junior'] = []
    staff_data['Senior'] = []
    staff_data['Manager'] = []

if os.path.exists('user.json') == True:
    with open('user.json') as json_file:
        user_data = json.load(json_file)
else:
    user_data = {}
    user_data['Visitor'] = []
    user_data['Event Holder'] = []
    user_data['School Visit'] = []

if os.path.exists('items.json') == True:
    with open('items.json') as json_file:
        item_data = json.load(json_file)
else:
    item_data = {}
    item_data['DVD'] = []
    item_data['Newspaper_Magazine'] = []
    item_data['Book'] = []

if os.path.exists('reviews.json') == True:
    with open('reviews.json') as json_file:
        review_data = json.load(json_file)
else:
    review_data = {}
    review_data['Reviews'] = []

############################################################################## Staff Class #################################################################

#Staff Class
class Staff(object):
    def __init__(self, fName, sName, dateOfBirth, salary, workHours, workDays, loginID, password, homeAddress, phoneNo, workEmail, role):
        self.first_name = fName
        self.surname = sName
        self.dob = dateOfBirth
        self.salary = salary
        self.work_hours = workHours
        self.work_days = workDays
        self.login_ID = loginID
        self.password = password
        self.home_address = homeAddress
        self.phone_no = phoneNo
        self.work_email = workEmail
        self.role = role

    #Below are the getter methods
    def get_first_name(self, role, user_name):
        for p in staff_data[role]:
            if p['login_ID'] == user_name:
                first_name = p['first_name']
                
        return 'First Name: ' + first_name

    def get_last_name(self, role, user_name):
        for p in staff_data[role]:
            if p['login_ID'] == user_name:
                surname = p['surname']
                
        return 'Last Name: ' + surname

    def get_date_of_birth(self, role, user_name):
        for p in staff_data[role]:
            if p['login_ID'] == user_name:
                dob = p['dob']
                
        return 'Date Of Birth: ' + dob

    def get_salary(self, role, user_name):
        for p in staff_data[role]:
            if p['login_ID'] == user_name:
                salary = p['salary']
                
        return 'Salary: £' + salary

    def get_work_hours(self, role, user_name):
        for p in staff_data[role]:
            if p['login_ID'] == user_name:
                work_hours = p['work_hours']
                
        return 'Work Hours: ' + work_hours

    def get_work_days(self, role, user_name):
        for p in staff_data[role]:
            if p['login_ID'] == user_name:
                work_days = p['work_days']
                
        return 'Work Days: ' + work_days

    def get_login_id(self, role, user_name):
        for p in staff_data[role]:
            if p['login_ID'] == user_name:
                login_ID = p['login_ID']
                
        return 'Login ID: ' + login_ID

    def get_home_address(self, role, user_name):
        for p in staff_data[role]:
            if p['login_ID'] == user_name:
                home_address = p['home_address']
                
        return 'Home Address: ' + home_address

    def get_phone_no(self, role, user_name):
        for p in staff_data[role]:
            if p['login_ID'] == user_name:
                phone_no = p['phone_no']
                
        return 'Phone Number: ' + phone_no

    def get_work_email(self, role, user_name):
        for p in staff_data[role]:
            if p['login_ID'] == user_name:
                work_email = p['work_email']
                
        return 'Work Email: ' + work_email

    def get_role(self, role, user_name):
        for p in staff_data[role]:
            if p['login_ID'] == user_name:
                role = p['role']
                
        return 'Role: ' + role

    #Below are the methods needed to issue item
    def set_books_on_loan(self, item_name, item_type, userName, role): #Takes in the users and items details
        for p in user_data[role]: #Finds the User 
            if p['user_name'] == userName:
                p['books_on_loan'].append(item_name + ' - ' + item_type)  #Stores the items name and type as a single item in the list

        with open('user.json', 'w') as f: #Dumps data back into JSON file
            json.dump(user_data, f)

        self.set_due_dates(userName, role)

    def set_due_dates(self, userName, role):
        today = datetime.now() #Stores todays date
        week = today + timedelta(days = 14) #Stores the date two weeks from now
        global week_formated
        week_formated = week.strftime("%d/%m/%y")  #Formats the date two weeks from now

        for p in user_data[role]: #Finds the User that has logged in
            if p['user_name'] == userName:
                p['due_dates'].append(week_formated)  #Stores the date two weeks from now

        with open('user.json', 'w') as f: #Dumps data back into JSON file
            json.dump(user_data, f)

        print('Your book is due on: ' + str(week_formated))

    def check_bills(self, userName, role):
        for p in user_data[role]: #Finds the User 
            if p['user_name'] == userName:
                users_bills = p['bills']    #Stores the users bills in a variable

        if users_bills == 0 or users_bills == 0.0: #If there is no bill
            statement = 'User has no bills!'
        else:                                       #If there is a bill
            statement = 'Users bill is: £',users_bills

        return statement
            
    def pay_bills(self, userName, role, pay):
        for p in user_data[role]: #Finds the User 
            if p['user_name'] == userName:
                users_bills = p['bills']    #Stores the users bills in a variable

        if users_bills == 0 or users_bills == 0.0: #If there is no bill
            response = 'User has no bills!'
        else:   #If there is a bill
            if pay > users_bills: #Output error if too much is being paid
                response = 'Too much has been entered'
            else:
                users_bills = users_bills - pay #Left over bill will be calculated

                for p in user_data[role]: #Finds the User
                    if p['user_name'] == userName:
                        p['bills'] = users_bills  #Stores the new bill

                with open('user.json', 'w') as f: #Dumps data back into JSON file
                    json.dump(user_data, f)

                response = 'Success. Your bill is now: £',users_bills #Return resulting bill
        return response

    def issue_item(self, ISBNNo, itemType, userName, role): #User inputs the items ISBN number, item type, username and users role
        ISBNNo = ISBNNo
        itemType = itemType
        userName = userName
        role = role
 
        #Find the item with the corresponding ISBN number and store its type and name
        for p in item_data[itemType]:
            if p['ISBN_number'] == ISBNNo:
                item_name = p['name']
                item_type = p['item_type']
                with open('items.json', 'w') as f:
                    json.dump(item_data, f)

        for p in item_data[itemType]:
            if p['name'] == item_name:
                p['status'] = 'Unavailable' #Changes items status to 'Unavailable'
                with open('items.json', 'w') as f:
                    json.dump(item_data, f)
                        
        print('The item you wish to loan has name: "',item_name,'", and is a: "',item_type,'" and has an ISBN number: "',ISBNNo,'" . Success')

        self.set_books_on_loan(item_name, item_type, userName, role) #Call the function to add this to the users list of books on loan
        return week_formated #To return the date to the tkinter file
                                              

    #Below are the methods needed to return an item
    def remove_books_on_loan(self, itemName, itemType, userName, role): #Method to remove items stored in the users account
        for p in user_data[role]: #Finds the User 
            if p['user_name'] == userName:
                books_on_loan = p['books_on_loan']  #Stores the books_on_loan list in a variable

        length = len(books_on_loan) #Find the length of the list

        p = 0 
        while p != length: #Loop will repeat untill all items have been compared
          if books_on_loan[p] == itemName + ' - ' + itemType :
            temp = p #Stores the position of the item in the list
          p = p + 1

        del books_on_loan[temp] #Removes the item at the specific position

        for p in user_data[role]: #Finds the User 
            if p['user_name'] == userName:
                p['books_on_loan'] = books_on_loan #Replaces the old data

        with open('user.json', 'w') as f: #Dumps data back into JSON file
            json.dump(user_data, f)

        self.calculate_bills(temp, userName, role)
        self.remove_due_dates(temp, userName, role)

    def remove_due_dates(self, temp, userName, role):
        for p in user_data[role]: #Finds the User 
            if p['user_name'] == userName:
                due_dates = p['due_dates']  #Stores the due_dates list in a variable

        del due_dates[temp] #Removes the item at the specific position

        for p in user_data[role]: #Finds the User
            if p['user_name'] == userName:
                p['due_dates'] = due_dates  #Stores the new due_dates

        with open('user.json', 'w') as f: #Dumps data back into JSON file
            json.dump(user_data, f)

    def calculate_bills(self, temp, userName, role):

        #Find the due date of the item
        for p in user_data[role]: #Finds the User 
            if p['user_name'] == userName:
                due_dates = p['due_dates']  #Stores the due_dates list in a variable
                users_bills = p['bills']    #Stores the users bills in a variable

        past = due_dates[temp] 
        
        #Set and format todays date
        today = datetime.now() 
        today_formated = today.strftime("%d/%m/%y")

        #Calculate where the '/' character is for todays date
        p=0
        while p < len(today_formated):
            if today_formated[p] == '/':
                temp = p 
                p = len(today_formated)
            p = p+1

        s = 0
        while s < len(today_formated):
            if today_formated[s] == '/':
                last = s + 1
            s = s + 1

        #Seperate each number
        today_year = today_formated[last:]
        today_month = today_formated[temp+1:last-1]
        today_days = today_formated[0:temp]

        #Calculate where the '/' character is for past date
        p=0
        while p < len(past):
            if past[p] == '/':
                temp = p 
                p = len(past)
            p = p+1


        s = 0
        while s < len(past):
            if past[s] == '/':
                last = s + 1
            s = s + 1
            
        #Seperate each number
        past_year = past[last:]
        past_month = past[temp+1:last-1]
        past_days = past[0:temp]

        #Calculate the difference in days
        years = int(today_year) - int(past_year)
        months = int(today_month) - int(past_month)
        days = (int(today_days) - int(past_days)) + (months*28) + (years*365)

        #If the book is returned after 14 days then change the bill
        global bills
        bills = 0
        if days > 14:
            bills = users_bills + (0.15*days) #Calculate new bill
            print('Your bill is now: £',bills)

            for p in user_data[role]: #Finds the User that has logged in
                if p['user_name'] == user_name:
                    p['bills'] = bills  #Stores the new bill

            with open('user.json', 'w') as f: #Dumps data back into JSON file
                json.dump(user_data, f)
        else:
            print('No fine, your bill is still: £',users_bills)
    
    #Method for returning items
    def return_item(self, ISBNNo, itemType, userName, role):
        
        #re-define parameter variables below
        ISBNNo = ISBNNo
        itemType = itemType
        userName = userName
        role = role

        #For loop below - will repeat for every item in the specific item type
        for p in item_data[itemType]:
            
            #if statement below will check any of the items have the same name as that of the item being returned
            if p['ISBN_number'] == ISBNNo:
                
                #Changes the status of the item to available
                p['status'] = 'Available'
                item_name = p['name']
                #Update the changes made to the json file
                with open('items.json', 'w') as f:
                    json.dump(item_data, f)

        self.remove_books_on_loan(item_name, itemType, userName, role)
        return bills
    
    #Method for searhing for items
    def search_item(self, itemType, itemName):
        for p in item_data[itemType]: #For loop runs through item data list
            if itemName == p['name'] : #If statement checks if any items in the list have the same name as the item name being searched for

                #Below returns the information to the frontend file
                date = 'Date Created:', p['date_created']
                status = 'Status:', p['status']
                copies = 'Number Of Copies:', p['number_of_copies']
                return date, status, copies
            else:
                print('Item not found')
        
#sub-classes below will inherit all the attributes from the parent class above
class Junior(Staff):
    def __init__(self, fName, sName, dateOfBirth, salary, workHours, workDays, loginID, password, homeAddress, phoneNo, workEmail, role):
        #Below line allows for all the attributes to be assigned to each inputed variable exactly the same to the parent class - Staff
        super().__init__(fName, sName, dateOfBirth, salary, workHours, workDays, loginID, password, homeAddress, phoneNo, workEmail, role)

    #Method for adding data to JSON file
    def add_junior_JSON(self, data):
        staff_data['Junior'].append(self.__dict__) #Appends staff_data
        with open('staff.json', 'w') as outfile:
            json.dump(data, outfile) #Adds staff_data into the staff json file

class Senior(Staff):
    def __init__(self, fName, sName, dateOfBirth, salary, workHours, workDays, loginID, password, homeAddress, phoneNo, workEmail, role):
        super().__init__(fName, sName, dateOfBirth, salary, workHours, workDays, loginID, password, homeAddress, phoneNo, workEmail, role)

    #Method for adding data to JSON file
    def add_senior_JSON(self, data):
        staff_data['Senior'].append(self.__dict__)
        with open('staff.json', 'w') as outfile:
            json.dump(data, outfile)

class Manager(Senior):
    def __init__(self, fName, sName, dateOfBirth, salary, workHours, workDays, loginID, password, homeAddress, phoneNo, workEmail, role):
        super().__init__(fName, sName, dateOfBirth, salary, workHours, workDays, loginID, password, homeAddress, phoneNo, workEmail, role)

    #Below are the setter methods
    def set_first_name(self, role, userID, fName):
        for p in staff_data[role]:
            if p['login_ID'] == userID:
                p['first_name'] = fName

        with open('staff.json', 'w') as f: #Dumps the new data into the JSON file
            json.dump(staff_data, f)
            

    def set_last_name(self, role, userID, sName):
        for p in staff_data[role]:
            if p['login_ID'] == userID:
                p['surname'] = sName

        with open('staff.json', 'w') as f:
            json.dump(staff_data, f)

    def set_date_of_birth(self, role, userID, dateOfBirth):
        for p in staff_data[role]:
            if p['login_ID'] == userID:
                p['dob'] = dateOfBirth

        with open('staff.json', 'w') as f:
            json.dump(staff_data, f)

    def set_salary(self, role, userID, salary):
        for p in staff_data[role]:
            if p['login_ID'] == userID:
                p['salary'] = salary

        with open('staff.json', 'w') as f:
            json.dump(staff_data, f)

    def set_work_hours(self, role, userID, workHours):
        for p in staff_data[role]:
            if p['login_ID'] == userID:
                p['work_hours'] = workHours

        with open('staff.json', 'w') as f:
            json.dump(staff_data, f)

    def set_work_days(self, role, userID, workDays):
        for p in staff_data[role]:
            if p['login_ID'] == userID:
                p['work_days'] = workDays

        with open('staff.json', 'w') as f:
            json.dump(staff_data, f)

    def set_login_id(self, role, userID, loginID):
        for p in staff_data[role]:
            if p['login_ID'] == userID:
                p['login_ID'] = loginID

        with open('staff.json', 'w') as f:
            json.dump(staff_data, f)
    
    def set_password(self, role, userID, newPassword, oldPassword): #3 variables passed through parameteres here - needed for validation
        for p in staff_data[role]:
            if p['login_ID'] == userID:
                confirmp = p['password']
        
        if old_password != confirmp: #To validate that the a genuine user is attempting to change their password
            print('Password does not match')
        else:
            for p in staff_data[role]:
                if p['login_ID'] == userID:
                    p['password'] = newPassword

            with open('staff.json', 'w') as f:
                json.dump(staff_data, f)

    def set_home_address(self, role, userID, homeAddress):
        for p in staff_data[role]:
            if p['login_ID'] == userID:
                p['home_address'] = homeAddress

        with open('staff.json', 'w') as f:
            json.dump(staff_data, f)

    def set_phone_no(self, role, userID, phoneNo):
        for p in staff_data[role]:
            if p['login_ID'] == userID:
                p['phone_no'] = phoneNo

        with open('staff.json', 'w') as f:
            json.dump(staff_data, f)

    def set_work_email(self, role, userID, workEmail):
        for p in staff_data[role]:
            if p['login_ID'] == userID:
                p['work_email'] = workEmail

        with open('staff.json', 'w') as f:
            json.dump(staff_data, f)

    #Method for adding data to JSON file
    def add_manager_JSON(self, data):
        staff_data['Manager'].append(self.__dict__)
        with open('staff.json', 'w') as outfile:
            json.dump(data, outfile)


#Staff Objects
'''            
staff1 = Junior('Waseh', 'Khan', '09/04/2003', '£2000', '24', '4', 'staff1', 'wasehk', '20 Isla Nublr', '0242094029', 'hello_world@email.com', 'Junior')
staff1.add_junior_JSON(staff_data)


staff2 = Senior('Mr', 'Burrows', '09/04/2003', '£2100', '25', '5', 'staff2', 'burrowsm', '21 Isla Nublr', '0242094030', 'hello_world2@email.com', 'Senior')
staff2.add_senior_JSON(staff_data)

staff3 = Manager('Bill', 'Khan', '10/04/2003', '£2200', '26', '6', 'staff3', 'billk', '22 Isla Nublr', '0242094031', 'hello_world3@email.com', 'Manager')
staff3.add_manager_JSON(staff_data)
'''
############################################################################## User Class #################################################################

#User Class
class User(object):
    def __init__(self, name, username, password, address, PhoneNo, email, role):
        self.name = name
        self.user_name = username
        self.password = password
        self.address = address
        self.phone_no = PhoneNo
        self.email = email
        self.role= role

    #Below are the getter methods
    def get_name(self, role, user_name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                name = p['name']
        
        return 'Name: ' + name

    def get_user_name(self, role, user_name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                user_name = p['user_name']
                
        return 'Login ID: ' + user_name

    def get_address(self, role, user_name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                address = p['address']
        
        return 'Address: ' + address

    def get_phone_no(self, role, user_name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                phone_no = p['phone_no']
                
        return 'Phone Number: ' + phone_no

    def get_email(self, role, user_name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                email = p['email']
                
        return 'Email: ' + email

    def get_role(self, role, user_name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                role = p['role']
        
        return 'Role: ' + role

    #Below are the setter methods
    def set_name(self, role, user_name, name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                p['name'] = name

        with open('user.json', 'w') as f:
            json.dump(user_data, f)

    def set_date_of_birth(self, role, user_name, dateOfBirth):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                p['dob'] = dateOfBirth

        with open('user.json', 'w') as f:
            json.dump(user_data, f)

    def set_username(self, role, user_name, username):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                p['user_name'] = username

        with open('user.json', 'w') as f:
            json.dump(user_data, f)
            
    def set_password(self, role, user_name, newPassword, oldPassword): # Function requires validation
        for p in user_data[role]:
            if p['user_name'] == user_name:
                confirmp = p['password']
                
        if old_password != confirmp: #To validate that the a genuine user is attempting to change their password
            print('Password does not match')
        else:
            for p in user_data[role]:
                if p['user_name'] == user_name:
                    p['password'] = newPassword

            with open('staff.json', 'w') as f:
                json.dump(staff_data, f)


    def set_address(self, role, user_name, address):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                p['address'] = address

        with open('user.json', 'w') as f:
            json.dump(user_data, f)

    def set_phone_no(self, role, user_name, phoneNo):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                p['phone_no'] = phoneNo

        with open('user.json', 'w') as f:
            json.dump(user_data, f)

    def set_email(self, role, user_name, email):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                p['email'] = email

        with open('user.json', 'w') as f:
            json.dump(user_data, f)

    def update_events(self):
        for p in user_data['Event Holder']: #For loop repeats for every event 
            if p['event_status'] == 'Not Done': #It will only check event which are not done yet

                date = p['event_date'] #Stores the date of the event
                today = datetime.today() #Stores todays date
                today = today.strftime("%d/%m/%y") # Formats todays date

                if date < today: #Checks if the date has passed
                    p['event_status'] = 'Done' #If the date of the event has gone, it marks the event as done
                    
                    with open('user.json', 'w') as f: #Dumps data back into JSON file
                        json.dump(user_data, f)

    def search_events(self):
        self.update_events()
        x = 0
        for p in user_data['Event Holder']: #For loop repeats for every event holder
            if p['event_status'] == 'Not Done': #It will only check event which are not done yet
                eventName = 'Event Name:', p['event_name']
                eventDate = 'Event Date:', p['event_date']
                eventHolder = 'Event Holder:', p['name']
                eventAge = 'Event Holder Age:', p['age']
                eventTime = 'Time of Event:', p['time_of_event']
                eventDuration = 'Event Duration:', p['event_duration'],'hrs'

                event_names = []
                event_dates = []
                event_holders = []
                event_ages = []
                event_times = []
                event_durations = []
                
                event_names.append(eventName)
                event_dates.append(eventDate)
                event_holders.append(eventHolder)
                event_ages.append(eventAge)
                event_times.append(eventTime)
                event_durations.append(eventDuration)
                x = x+1
            else:
                event_names = []
                event_dates = []
                event_holders = []
                event_ages = []
                event_times = []
                event_durations = []
                
                
            return event_names, event_dates, event_holders, event_ages, event_times, event_durations, x

    #Method for searhing for items
    def search_item(self, itemType, itemName):
        for p in item_data[itemType]: #For loop runs through item data list
            if itemName == p['name'] : #If statement checks if any items in the list have the same name as the item name being searched for
                '''
                print('Date Created:', p['date_created'])
                print('Status:', p['status'])
                print('Number Of Copies:', p['number_of_copies'])
                '''
                #Below returns the information to the frontend file
                date = 'Date Created:', p['date_created']
                status = 'Status:', p['status']
                copies = 'Number Of Copies:', p['number_of_copies']
                return date, status, copies
            else:
                print('Item not found')

#sub-classes below will inherit all the attributes from the parent class above
class Visitor(User):
    def __init__(self, name, username, password, address, PhoneNo, email, role, dateOfBirth, age, booksOnLoan, dueDates, Bills):
        #Below line allows for all the attributes to be assigned to each inputed variable exactly the same to the parent class - User
        super().__init__(name, username, password, address, PhoneNo, email, role)
        self.dob = dateOfBirth
        self.age = age
        self.books_on_loan = [booksOnLoan]
        self.due_dates = [dueDates]
        self.bills = Bills

    #Below are the getter methods
    def get_date_of_birth(self, role, user_name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                dob = p['dob']
        
        return 'Date Of Birth: ' + dob
    
    def get_age(self, role, user_name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                age = p['age']
        
        return 'Age: ' + self.age

    def get_books_on_loan(self, role, user_name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                books_on_loan = p['books_on_loan']

        return 'Books On Loan: ' , books_on_loan

    def get_due_dates(self, role, user_name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                due_dates = p['due_dates']

        return 'Due Dates: ' , due_dates

    def get_bills(self, role, user_name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                users_bills = p['bills']

        return 'Bills: ' , users_bills

    #Below are the setter methods
    def set_date_of_birth(self, role, user_name, dob):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                p['dob'] = dob

        with open('user.json', 'w') as f:
            json.dump(user_data, f)

    def set_age(self, role, user_name, age):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                p['age'] = age

        with open('user.json', 'w') as f:
            json.dump(user_data, f)

    def set_books_on_loan(self, item_name, item_type, user_name, role):
        for p in user_data[role]: #Finds the User that has logged in
            if p['user_name'] == user_name:
                p['books_on_loan'].append(item_name + ' - ' + item_type)  #Stores the items name and type as a single item in the list

        with open('user.json', 'w') as f: #Dumps data back into JSON file
            json.dump(user_data, f)

        self.set_due_dates(user_name, role)

    def set_due_dates(self, user_name, role):
        today = datetime.now() #Stores todays date
        week = today + timedelta(days = 14) #Stores the date two weeks from now
        global week_formated
        week_formated = week.strftime("%d/%m/%y")  #Formats the date two weeks from now

        for p in user_data[role]: #Finds the User that has logged in
            if p['user_name'] == user_name:
                p['due_dates'].append(week_formated)  #Stores the date two weeks from now

        with open('user.json', 'w') as f: #Dumps data back into JSON file
            json.dump(user_data, f)

        print('Your book is due on: ' + str(week_formated))
       
    def issue_item(self, ISBNNo, itemType, user_name, role): #User inputs the items ISBN number and items type
        ISBNNo = ISBNNo
        itemType = itemType
 
        #Find the item with the corresponding ISBN number and store its type and name
        for p in item_data[itemType]:
            if p['ISBN_number'] == ISBNNo:
                item_name = p['name']
                item_type = p['item_type']
                with open('items.json', 'w') as f:
                    json.dump(item_data, f)

        for p in item_data[itemType]:
            if p['name'] == item_name:
                p['status'] = 'Unavailable' #Changes items status to 'Unavailable'
                with open('items.json', 'w') as f:
                    json.dump(item_data, f)
                        
        print('The item you wish to loan has name: "',item_name,'", and is a: "',item_type,'" and has an ISBN number: "',ISBNNo,'" . Success')

        self.set_books_on_loan(item_name, item_type, user_name, role) #Call the function to add this to the users list of books on loan
        return week_formated #To return the date to the tkinter file
                                              

    #Method for adding data to JSON file
    def add_visitor_JSON(self, data):
        user_data['Visitor'].append(self.__dict__)
        with open('user.json', 'w') as outfile:
            json.dump(data, outfile)

    def remove_books_on_loan(self, itemName, itemType, user_name, role, books_on_loan, due_dates, users_bills): #Method to remove items stored in the users account
        length = len(books_on_loan) #Find the length of the list

        p = 0 
        while p != length: #Loop will repeat untill all items have been compared
          if books_on_loan[p] == itemName + ' - ' + itemType :
            temp = p #Stores the position of the item in the list
          p = p + 1

        del books_on_loan[temp] #Removes the item at the specific position

        for p in user_data[role]: #Finds the User that has logged in
            if p['user_name'] == user_name:
                p['books_on_loan'] = books_on_loan #Replaces the old data

        with open('user.json', 'w') as f: #Dumps data back into JSON file
            json.dump(user_data, f)       

        self.calculate_bills(temp, user_name, role, due_dates, users_bills)
        self.remove_due_dates(temp, user_name, role, due_dates, users_bills)
        
    def remove_due_dates(self, temp, user_name, role, due_dates, users_bills):
        
        del due_dates[temp] #Removes the item at the specific position

        for p in user_data[role]: #Finds the User that has logged in
            if p['user_name'] == user_name:
                p['due_dates'] = due_dates  #Stores the new date

        with open('user.json', 'w') as f: #Dumps data back into JSON file
            json.dump(user_data, f)

    def calculate_bills(self, temp, user_name, role, due_dates, users_bills):

        #Find the due date of the item
        past = due_dates[temp]
        
        #Set and format todays date
        today = datetime.now() 
        today_formated = today.strftime("%d/%m/%y")

        #Calculate where the '/' character is for todays date
        p=0
        while p < len(today_formated):
            if today_formated[p] == '/':
                temp = p 
                p = len(today_formated)
            p = p+1


        s = 0
        while s < len(today_formated):
            if today_formated[s] == '/':
                last = s + 1
            s = s + 1

        #Seperate each number
        today_year = today_formated[last:]
        today_month = today_formated[temp+1:last-1]
        today_days = today_formated[0:temp]

        #Calculate where the '/' character is for yesterdays date
        p=0
        while p < len(past):
            if past[p] == '/':
                temp = p 
                p = len(past)
            p = p+1


        s = 0
        while s < len(past):
            if past[s] == '/':
                last = s + 1
            s = s + 1
            
        #Seperate each number
        past_year = past[last:]
        past_month = past[temp+1:last-1]
        past_days = past[0:temp]

        #Calculate the difference in days
        years = int(today_year) - int(past_year)
        months = int(today_month) - int(past_month)
        days = (int(today_days) - int(past_days)) + (months*28) + (years*365)

        #If the book is returned after 14 days then change the bill
        global bills
        bills = 0
        if days > 14:
            bills = users_bills + (0.15*days) #Calculate new bill
            print('Your bill is now: £',bills)

            for p in user_data[role]: #Finds the User that has logged in
                if p['user_name'] == user_name:
                    p['bills'] = bills  #Stores the new bill

            with open('user.json', 'w') as f: #Dumps data back into JSON file
                json.dump(user_data, f)
        else:
            print('No fine, your bill is still: £',users_bills)
        
    #Method for returning items
    def return_item(self, ISBNNo, itemType, userName, role, books_on_loan, due_dates, users_bills):
        
        #re-define parameter variables below
        ISBNNo = ISBNNo
        itemType = itemType

        #For loop below - will repeat for every item in the specific item type
        for p in item_data[itemType]:
            
            #if statement below will check any of the items have the same name as that of the item being returned
            if p['ISBN_number'] == ISBNNo:
                
                #Changes the status of the item to available
                p['status'] = 'Available'
                item_name = p['name']
                #Update the changes made to the json file
                with open('items.json', 'w') as f:
                    json.dump(item_data, f)

        self.remove_books_on_loan(item_name, itemType, userName, role, books_on_loan, due_dates, users_bills)
        return bills
            
class EventHolder(User):
    def __init__(self, name, username, password, address, PhoneNo, email, role, dateOfBirth, age, eventName, eventDate, timeOfEvent, eventDuration, eventStatus):
        super().__init__(name, username, password, address, PhoneNo, email, role)
        self.dob = dateOfBirth
        self.age = age
        self.event_name = eventName
        self.event_date = eventDate
        self.time_of_event = timeOfEvent
        self.event_duration = eventDuration
        self.event_status = 'Not Done'

    #Below are the getter methods
    def get_date_of_birth(self, role, user_name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                dob = p['dob']
                
        return 'Date Of Birth: ' + dob

    def get_age(self, role, user_name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                age = p['age']
                
        return 'Age: ' , age

    def get_event_name(self, role, user_name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                event_name = p['event_name']
                
        return 'Event Name: ' + event_name

    def get_event_date(self, role, user_name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                event_date = p['event_date']
                
        return 'Event Date: ' , event_date

    def get_time_of_event(self, role, user_name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                time_of_event = p['time_of_event']
                
        return 'Time Of Event: ' , time_of_event

    def get_event_duration(self, role, user_name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                event_duration = p['event_duration']
                
        return 'Event Duration: ' , event_duration

    def get_event_status(self, role, user_name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                event_status = p['event_status']
                
        return 'Event Status: ' + event_status

    #Below are the setter methods
    def set_date_of_birth(self, role, user_name, dob):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                p['dob'] = dob

        with open('user.json', 'w') as f:
            json.dump(user_data, f)

    def set_age(self, role, user_name, age):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                p['age'] = age

        with open('user.json', 'w') as f:
            json.dump(user_data, f)

    def set_event_name(self, role, user_name, eventName):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                p['event_name'] = eventName

        with open('user.json', 'w') as f:
            json.dump(user_data, f)

    def set_event_date(self, role, user_name, eventDate):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                p['event_date'] = eventDate

        with open('user.json', 'w') as f:
            json.dump(user_data, f)
        
    def set_time_of_event(self, role, user_name, timeOfEvent):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                p['time_of_event'] = timeOfEvent

        with open('user.json', 'w') as f:
            json.dump(user_data, f)

    def set_event_duration(self, role, user_name, eventDuration):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                p['event_duration'] = eventDuration

        with open('user.json', 'w') as f:
            json.dump(user_data, f)

    def set_event_status(self, role, user_name, eventStatus):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                p['event_status'] = eventStatus

        with open('user.json', 'w') as f:
            json.dump(user_data, f)

    #Method for adding data to JSON file
    def add_event_holder_JSON(self, data):
        user_data['Event Holder'].append(self.__dict__)
        with open('user.json', 'w') as outfile:
            json.dump(data, outfile)

class SchoolVist(User):
    def __init__(self, name, username, password, address, PhoneNo, email, role, booksOnLoan, dueDates, Bills):
        super().__init__(name, username, password, address, PhoneNo, email, role)
        self.books_on_loan = [booksOnLoan]
        self.due_dates = [dueDates]
        self.bills = Bills

    #Method for adding data to JSON file
    def add_school_visit_JSON(self, data):
        user_data['School Visit'].append(self.__dict__)
        with open('user.json', 'w') as outfile:
            json.dump(data, outfile)

    #Below are the getter methods
    def get_books_on_loan(self, role, user_name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
               books_on_loan =  p['books_on_loan'] 
                
        return 'Books On Loan: ' , self.books_on_loan

    def get_due_dates(self, role, user_name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                due_dates =  p['due_dates'] 
                
        return 'Due Dates: ' , self.due_dates

    def get_bills(self, role, user_name):
        for p in user_data[role]:
            if p['user_name'] == user_name:
                bills =  p['bills'] 
                
        return 'Bills: ' , self.bills

    #Below are the setter methods
    def set_books_on_loan(self, item_name, item_type, user_name, role):
        for p in user_data[role]: #Finds the User that has logged in
            if p['user_name'] == user_name:
                p['books_on_loan'].append(item_name + ' - ' + item_type)  #Stores the items name and type as a single item in the list

        with open('user.json', 'w') as f: #Dumps data back into JSON file
            json.dump(user_data, f)

        self.set_due_dates(user_name, role)

    def set_due_dates(self, user_name, role):
        today = datetime.now() #Stores todays date
        week = today + timedelta(days = 14) #Stores the date two weeks from now
        global week_formated
        week_formated = week.strftime("%d/%m/%y")  #Formats the date two weeks from now

        for p in user_data[role]: #Finds the User that has logged in
            if p['user_name'] == user_name:
                p['due_dates'].append(week_formated)  #Stores the date two weeks from now

        with open('user.json', 'w') as f: #Dumps data back into JSON file
            json.dump(user_data, f)

        print('Your book is due on: ' + str(week_formated))
       
    def issue_item(self, ISBNNo, itemType, user_name, role): #User inputs the items ISBN number and items type
        ISBNNo = ISBNNo
        itemType = itemType
 
        #Find the item with the corresponding ISBN number and store its type and name
        for p in item_data[itemType]:
            if p['ISBN_number'] == ISBNNo:
                item_name = p['name']
                item_type = p['item_type']
                with open('items.json', 'w') as f:
                    json.dump(item_data, f)

        for p in item_data[itemType]:
            if p['name'] == item_name:
                p['status'] = 'Unavailable' #Changes items status to 'Unavailable'
                with open('items.json', 'w') as f:
                    json.dump(item_data, f)
                        
        print('The item you wish to loan has name: "',item_name,'", and is a: "',item_type,'" and has an ISBN number: "',ISBNNo,'" . Success')

        self.set_books_on_loan(item_name, item_type, user_name, role) #Call the function to add this to the users list of books on loan
        return week_formated #To return the date to the tkinter file
                                              

    def remove_books_on_loan(self, itemName, itemType, user_name, role, books_on_loan, due_dates, users_bills): #Method to remove items stored in the users account
        length = len(books_on_loan) #Find the length of the list

        p = 0 
        while p != length: #Loop will repeat untill all items have been compared
          if books_on_loan[p] == itemName + ' - ' + itemType :
            temp = p #Stores the position of the item in the list
          p = p + 1

        del books_on_loan[temp] #Removes the item at the specific position

        for p in user_data[role]: #Finds the User that has logged in
            if p['user_name'] == user_name:
                p['books_on_loan'] = books_on_loan #Replaces the old data

        with open('user.json', 'w') as f: #Dumps data back into JSON file
            json.dump(user_data, f)       

        self.calculate_bills(temp, user_name, role, due_dates, users_bills)
        self.remove_due_dates(temp, user_name, role, due_dates, users_bills)
        
    def remove_due_dates(self, temp, user_name, role, due_dates, users_bills):
        
        del due_dates[temp] #Removes the item at the specific position

        for p in user_data[role]: #Finds the User that has logged in
            if p['user_name'] == user_name:
                p['due_dates'] = due_dates  #Stores the new date

        with open('user.json', 'w') as f: #Dumps data back into JSON file
            json.dump(user_data, f)

    def calculate_bills(self, temp, user_name, role, due_dates, users_bills):

        #Find the due date of the item
        past = due_dates[temp]
        
        #Set and format todays date
        today = datetime.now() 
        today_formated = today.strftime("%d/%m/%y")

        #Calculate where the '/' character is for todays date
        p=0
        while p < len(today_formated):
            if today_formated[p] == '/':
                temp = p 
                p = len(today_formated)
            p = p+1


        s = 0
        while s < len(today_formated):
            if today_formated[s] == '/':
                last = s + 1
            s = s + 1

        #Seperate each number
        today_year = today_formated[last:]
        today_month = today_formated[temp+1:last-1]
        today_days = today_formated[0:temp]

        #Calculate where the '/' character is for yesterdays date
        p=0
        while p < len(past):
            if past[p] == '/':
                temp = p 
                p = len(past)
            p = p+1


        s = 0
        while s < len(past):
            if past[s] == '/':
                last = s + 1
            s = s + 1
            
        #Seperate each number
        past_year = past[last:]
        past_month = past[temp+1:last-1]
        past_days = past[0:temp]

        #Calculate the difference in days
        years = int(today_year) - int(past_year)
        months = int(today_month) - int(past_month)
        days = (int(today_days) - int(past_days)) + (months*28) + (years*365)

        #If the book is returned after 14 days then change the bill
        global bills
        bills = 0
        if days > 14:
            bills = users_bills + (0.15*days) #Calculate new bill
            print('Your bill is now: £',bills)

            for p in user_data[role]: #Finds the User that has logged in
                if p['user_name'] == user_name:
                    p['bills'] = bills  #Stores the new bill

            with open('user.json', 'w') as f: #Dumps data back into JSON file
                json.dump(user_data, f)
        else:
            print('No fine, your bill is still: £',users_bills)
        
    #Method for returning items
    def return_item(self, ISBNNo, itemType, userName, role, books_on_loan, due_dates, users_bills):
        
        #re-define parameter variables below
        ISBNNo = ISBNNo
        itemType = itemType

        #For loop below - will repeat for every item in the specific item type
        for p in item_data[itemType]:
            
            #if statement below will check any of the items have the same name as that of the item being returned
            if p['ISBN_number'] == ISBNNo:
                
                #Changes the status of the item to available
                p['status'] = 'Available'
                item_name = p['name']
                #Update the changes made to the json file
                with open('items.json', 'w') as f:
                    json.dump(item_data, f)

        self.remove_books_on_loan(item_name, itemType, userName, role, books_on_loan, due_dates, users_bills)
        return bills
    
#User Objects
'''
user1 = Visitor('Adam Karim', 'Akarim1', '******', '20 Isla Sorna','012345678910', 'hi_world2@email.com', 'Visitor', '09/04/2003', '17', '', '', 0)
user1.add_visitor_JSON(user_data)
                    
user2 = EventHolder('Mr Iqbal', 'Miqbal1', '******', '21 Isla Sorna','012345678911', 'hi_world2@email.com', 'Event Holder', '09/04/2003', '17', 'Coding Club', '03/10/20', '12:00', '1', 'Not Done')
user2.add_event_holder_JSON(user_data)

user3 = SchoolVist('Ahmed Vatch', 'Avatch1', '******', '22 Isla Sorna','012345678912', 'hi_world2@email.com', 'School Visit','', '', 0)
user3.add_school_visit_JSON(user_data)
'''
############################################################################## Items Class #################################################################

#Items Class
class Items(object):
    def __init__(self, itemType, name, condition, ISBNNumber, dateCreated, status, numberOfCopies):
        self.item_type = itemType
        self.name = name
        self.condition = condition
        self.ISBN_number = ISBNNumber
        self.date_created = dateCreated
        self.status = status
        self.number_of_copies = numberOfCopies

    #Below are the getter methods
    def get_item_type(self):
        return 'Type: ' + self.item_type

    def get_name(self):
        return 'Name: ' + self.name

    def get_condition(self):
        return 'Condition: ' + self.condition

    def get_ISBN_number(self):
        return 'ISBN Number: ' + self.ISBN_number

    def get_date_created(self):
        return 'Date Created: ' + self.date_created

    def get_status(self):
        return 'Status: ' + self.status

    def get_number_of_copies(self):
        return 'Number Of Copies: ' + self.number_of_copies

    #Below are the setter methods
    def set_item_type(self, itemType):
        self.item_type = itemType

    def set_name(self, name):
        self.name = name

    def set_condition(self, condition):
        self.condition = condition

    def set_ISBN_number(self, ISBNNumber):
        self.ISBN_number = ISBNNumber

    def set_date_created(self, dateCreated):
        self.date_created = dateCreated

    def set_status(self, status):
        self.status = status

    def set_number_of_copies(self, numberOfCopies):
        self.number_of_copies = numberOfCopies


#sub-classes below will inherit all the attributes from the parent class above
class DVD(Items):
    def __init__(self, itemType, name, condition, ISBNNumber, dateCreated, status, numberOfCopies, director, duration, ageGroup):
        #Below line allows for all the attributes to be assigned to each inputed variable exactly the same to the parent class - Items
        super().__init__(itemType, name, condition, ISBNNumber, dateCreated, status, numberOfCopies)
        self.director = director
        self.duration = duration
        self.age_group = ageGroup

    #Below are the getter methods
    def get_director(self):
        return 'Director: ' + self.director

    def get_duration(self):
        return 'Duration: ' + self.duration

    def get_age_group(self):
        return 'Age Group: ' + self.age_group

    #Below are the setter methods
    def set_director(self, director):
        self.director = director

    def set_duration(self, duration):
        self.duration = duration

    def set_age_group(self, ageGroup):
        self.age_group = ageGroup

    #Method for adding data to JSON file
    def add_dvd_JSON(self, data):
        item_data['DVD'].append(self.__dict__)
        with open('items.json', 'w') as outfile:
            json.dump(data, outfile)

class Newspaper_Magazine(Items):
    def __init__(self, itemType, name, condition, ISBNNumber, dateCreated, status, numberOfCopies, title):
        super().__init__(itemType, name, condition, ISBNNumber, dateCreated, status, numberOfCopies)
        self.title = title

    #Below are the getter methods
    def get_title(self):
        return 'Title: ' + self.title

    #Below are the setter methods
    def set_title(self, title):
        self.title = title

    #Method for adding data to JSON file
    def add_newspaper_magazine_JSON(self, data):
        item_data['Newspaper_Magazine'].append(self.__dict__)
        with open('items.json', 'w') as outfile:
            json.dump(data, outfile)
 

class Book(Items):
    def __init__(self, itemType, name, condition, ISBNNumber, dateCreated, status, numberOfCopies, author, genre, numberOfPages):
        super().__init__(itemType, name, condition, ISBNNumber, dateCreated, status, numberOfCopies)
        self.author = author
        self.genre = genre
        self.number_of_pages = numberOfPages

    #Below are the getter methods
    def get_author(self):
        return 'Author: ' + self.author

    def get_genre(self):
        return 'Genre: ' + self.genre

    def get_number_of_pages(self):
        return 'Number Of Pages: ' + self.number_of_pages

    #Below are the setter methods
    def set_author(self, author):
        self.author = author

    def set_genre(self, genre):
        self.genre = genre

    def set_number_of_pages(self, numberOfPages):
        self.number_of_pages = numberOfPages

    #Method for adding data to JSON file
    def add_book_JSON(self, data):
        item_data['Book'].append(self.__dict__) 
        with open('items.json', 'w') as outfile:
            json.dump(data, outfile) 

#Item Objects
'''            
item1 = DVD('DVD', 'Jurassic World', 'New', '0123456897', '01/01/1993', 'Unavailable', '3', 'Steven Spielberg', '2.2 hrs', 'PG')
item1.add_dvd_JSON(item_data)

item2 = Newspaper_Magazine('Newspaper_Magazine', 'The Guardian', 'New', '0123456898', '02/02/1993', 'Unavailable', '2', 'New Vaccine')
item2.add_newspaper_magazine_JSON(item_data)

item3 = Book('Book', 'Jurassic Park', 'Old', '0123456899', '03/03/1993', 'Unavailable', '1', 'Michael Crichton', '2.12 hrs', '12+')
item3.add_book_JSON(item_data)
'''
############################################################################## Extra Info #################################################################

#Below is the code needed to add an item
'''
user1 = Visitor('Adam Karim', 'Akarim1', '******', '20 Isla Sorna','012345678910', 'hi_world2@email.com', 'Visitor', '09/04/2003', '17')
user1.issue_item('0123456897','DVD')
'''
#Below is the code needed to remove an item
'''
user1 = Visitor('Adam Karim', 'Akarim1', '******', '20 Isla Sorna','012345678910', 'hi_world2@email.com', 'Visitor', '09/04/2003', '17')
user1.return_item('0123456897', 'DVD')
'''
#Below is the code needed to add an item as a Staff
'''
staff1 = Junior('Waseh', 'Khan', '09/04/2003', '£2000', '24', '4', 'staff1', 'wasehk', '20 Isla Nublr', '0242094029', 'hello_world@email.com', 'Junior')
staff1.issue_item('0123456897','DVD', 'Akarim1', 'Visitor')
'''
#Below is the code needed to remove an item as a Staff
'''
staff1 = Junior('Waseh', 'Khan', '09/04/2003', '£2000', '24', '4', 'staff1', 'wasehk', '20 Isla Nublr', '0242094029', 'hello_world@email.com', 'Junior')
staff1.return_item('0123456897','DVD', 'Akarim1', 'Visitor')
'''
#Below is the code needed to pay for bills
'''
staff1 = Junior('Waseh', 'Khan', '09/04/2003', '£2000', '24', '4', 'staff1', 'wasehk', '20 Isla Nublr', '0242094029', 'hello_world@email.com', 'Junior')
staff1.pay_bills('Akarim1', 'Visitor')
'''
#Below is the code needed to search for an item
'''
staff1 = Junior('Waseh', 'Khan', '09/04/2003', '£2000', '24', '4', 'staff1', 'wasehk', '20 Isla Nublr', '0242094029', 'hello_world@email.com', 'Junior')
staff1.search_item('Newspaper_Magazine', 'The Guardian')
'''
#Below is the code needed to update and search for an event
'''
user1 = Visitor('Adam Karim', 'Akarim1', '******', '20 Isla Sorna','012345678910', 'hi_world2@email.com', 'Visitor', '09/04/2003', '17')
user1.search_events()
'''
