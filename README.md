# library-management-tool (Completed: 12/12/2020)

# About This Project

This program, is a: library management system. In which there are two different user interfaces for both staff/administrators and any visitors. 

The <b>administrator</b> interface allows workers to: 
- discharge books
- pay/wave fines
- take books out for families
- create a new user
- report lost cards 
- holds to be placed on books
- search up the nearest library which holds a particular book

The <b>visitor</b> interface on the other hand, has been restricted to only: 
- taking books out (checking first if they have their card/details)
- returning books
- viewing their details. 
- check any books being loaned out on their card and gives the due date
- information of previously returned books. 

These two interfaces are separated through login (i.e. username/password) - in which an administrator will have to sign 
a visitor up for access to the visitor interface on their computers. 

There are three different roles for staff:
- Junior
- Senior
- Manager

There are also three different roles for users:
- Visitors
- Event Holders
- Scool Visit

<b>Information is stored and retrieved from the .json files!</b>

# Built With:

- python (Backend)
- Tkinter (Frontend)

# Screenshots:

<b>Staff UI:</b>
<img width="1280" alt="Screenshot 2022-06-07 at 18 12 13" src="https://user-images.githubusercontent.com/60042016/172442557-24fad6ae-5162-46ca-b616-6d660fd8af07.png">
<img width="1280" alt="Screenshot 2022-06-07 at 18 13 14" src="https://user-images.githubusercontent.com/60042016/172442783-e9f3a6bc-ee83-4a1e-be85-fc5310cdae1a.png">
<img width="1280" alt="Screenshot 2022-06-07 at 18 14 01" src="https://user-images.githubusercontent.com/60042016/172442940-82af0476-fec8-4f2b-be34-341e31ada143.png">

<b>User UI:</b>
<img width="1280" alt="Screenshot 2022-06-07 at 18 15 25" src="https://user-images.githubusercontent.com/60042016/172443270-f9bdb8ad-ee5d-477c-913d-01961796f1cb.png">
<img width="1280" alt="Screenshot 2022-06-07 at 18 15 47" src="https://user-images.githubusercontent.com/60042016/172443343-4a5f161f-a010-49a4-adba-ae0556227525.png">

# How To Use:

1. Clone the repo
`git clone https://github.com/mwkhan9/library-management-tool.git`

2. Open Frontend.py

3. Select login type (i.e. user/staff)
#### <b>To see login credentials open user.json/staff.json appropriately. Look for the text next to 'user_name' & 'password' and copy these in</b>
#### (e.g. to sign in as a staff with role manage, user_name == 'staff3' & password == 'billk')
#### (e.g. to sign in as a user with role visitor, user_name == 'Akarim1' & password == '******')


#### To identify items etc. read the appropriate .json files
