import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",passwd="Ramki@123",database="HOSTEL")
mycursor = mydb.cursor()

def exit():
    mydb.close() 
    raise SystemExit

def invalid():
    print("Invalid Option")
    footer()

def data_extrect(query,reg_no):
    mycursor.execute(query, (reg_no,))
    myresult = mycursor.fetchall()
    if len(myresult)== 0:
        print("No data found")
    for x in myresult:
        print(x)
    footer()

def header(subheader):
    print()
    print("___Hostel Management System___", subheader)
    print()

def footer():
    print()
    print("1.Back to MainMenu")
    print("2.Exit")

    option_selected = input("Choose the task needed to be performed.")
    if option_selected == "1": main_menu()
    elif option_selected == "2": exit()
    else: invalid()

#new resident

def new_resident():
    header("___Enter Resident Details___")  

    reg_no = input("Reg No:")
    name = input("Name:")
    class_name = input("Class:")
    room_no = input("Room No:")
    parent_name = input("Parent/Guardian Name:")
    address = input("Address with Pincode:")
    contact = input("Contact:")
    pocket_money = input("Pocket Money Details:")
      
    sql = """INSERT INTO ResidentsTable (RegNo, Name, Class, RoomNo, ParentName, Address, Contact, PocketMoney) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
    val = (reg_no, name, class_name, room_no, parent_name, address, contact, pocket_money)
    mycursor.execute(sql, val)
    mydb.commit()
    
    print("___Last Stored Data___")
    print()
    data_extrect("select * from ResidentsTable where RegNo = (%s)", reg_no)

#view residents

def view_residents():
    header("___All Residents Data___")
    mycursor.execute("select * from ResidentsTable")
    myresult = mycursor.fetchall()
    if len(myresult)== 0:
        print("No data found")
    for x in myresult:
        print(x)
    footer()

#particular resident

def particular_resident():
    header("___Particular Residents Data___")
    reg_no = input("Reg No:")
    data_extrect("select * from ResidentsTable where RegNo = (%s)", reg_no)

#particular resident

def particular_parent():
    header("___Particular student's Parent Data___")
    reg_no = input("Enter student's Reg No:")
    data_extrect("""select ParentName, Address, Contact from ResidentsTable where RegNo = (%s)""", reg_no)

#particular student's pocket money balance
 
def particular_pocketmoney():
    header("___Particular student's Pocket money balance Data___")
    reg_no = input("Enter student's Reg No:")
    data_extrect("""select RegNo, Name, Class, RoomNo, PocketMoney from ResidentsTable where RegNo = (%s)""", reg_no)

#update pocket money balance

def update_pocketmoney():
    header("___Update Pocket money balance Data___")
    reg_no = input("Enter student's Reg No:")
    balance = input("Enter new balance amount:")
    mycursor.execute("""UPDATE ResidentsTable SET PocketMoney = (%s) where RegNo = (%s)""", (balance, reg_no))
    mydb.commit()

    print("___Last Updated Data___")
    print()
    data_extrect("""select RegNo, Name, Class, RoomNo, PocketMoney from ResidentsTable where RegNo = (%s)""", reg_no)

#main menu

def main_menu():
    header("___Mainmenu___")
    print("1.Add New Resident")
    print("2.View all existing Residents")
    print("3.View particular Resident")
    print("4.View particular student's parent detail")
    print("5.View particular student's pocketmoney balance")
    print("6.Update particular student's pocket money balance")
    print("7.Exit")

    option_selected = input("Choose the task needed to be performed.")
    if option_selected == "1": new_resident()
    elif option_selected == "2": view_residents()
    elif option_selected == "3": particular_resident()
    elif option_selected == "4": particular_parent()
    elif option_selected == "5": particular_pocketmoney()
    elif option_selected == "6": update_pocketmoney()
    elif option_selected == "7": exit()
    else: invalid()

main_menu()
