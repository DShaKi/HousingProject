import sqlite3
import uuid
import hashlib

conn = sqlite3.connect('HousingDB.db')

"""
1. Find Home
2. House Checker # need changes
3. Request Best Home
4. Show all requests (Admin)
5. Show all Buys (User)
6. UI (User Interface)
7. Request table
"""


class Housing:
    def __init__(self, id, name, username, password, adminname):
        if id == None:
            self.id = str(uuid.uuid1())
        else:
            self.id = id
        self.name = name
        self.admins = [Admin(None, self.id, username, password, adminname)]
        self.users = []
        self.houses = []
        self.requests = []
        conn.execute("INSERT INTO Housing VALUES (?, ?)", (self.id, self.name, ))
        conn.commit()

    def update_values(self):
        self.admins = []
        self.users = []
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User WHERE ID = (?)", (self.id, ))
        users = cursor.fetchall()
        for u in users:
            if u[6] == 0:
                self.admins.append(Admin(u[1], u[2], u[3], u[4], u[5]))
            else:
                self.users.append(User(u[1], u[2], u[3], u[4], u[5]))

    def create_acc(self, username, password, name):
        self.users.append(User(None, self.id, username, password, name))
        print(f"Account with the name {name} successfully added.")

    def get_session(self, username, password):
        all_members = self.admins + self.users
        for u in all_members:
            if u.username == username and u.password == str(hashlib.md5(str(password + self.id).encode('utf-8')).hexdigest()):
                print("Logged in!")
                return Session(self, u)

class User:
    def __init__(self, id, housingid, username, password, name):
        if id == None:
            self.id = str(uuid.uuid1())
        else:
            self.id = id
        self.housingid = housingid
        self.username = username
        self.password = str(hashlib.md5(str(password + housingid).encode('utf-8')).hexdigest())
        self.name = name
        self.isAdmin = False
        conn.execute("INSERT INTO User VALUES (?, ?, ?, ?, ?, ?)", (self.id, self.housingid, self.username, self.password, self.name, self.isAdmin, ))
        conn.commit()

    # need changes
    def add_home(self, housingid, city, address, size, type, available, price, bedroomcount, furnish, other):
        new_house = House(None , housingid, self, city, address, size, type, available, price, bedroomcount, furnish, other)
        return new_house

    def remove_user(self, user):
        print("Access Denied!")


class Admin(User):
    def __init__(self, id, housingid, username, password, name):
        super().__init__(id, housingid, username, password, name)
        self.isAdmin = True
        conn.execute("UPDATE User SET isAdmin = (?) WHERE ID = (?)", (self.isAdmin, self.id, ))
        conn.commit()
    
    def remove_user(self, user):
        conn.execute("DELETE FROM User WHERE ID = (?)", (user.id, ))
        print(f"User {user.name} removed.")
        del user
        conn.commit()

class House:
    def __init__(self, id, housingid, seller: User, city, address, size, type, available, price, bedroomcount, furnish, other):
        if id == None:
            self.id = str(uuid.uuid1())
        else:
            self.id = id
        self.housingid = housingid
        self.sellerid = seller.id
        self.city = city
        self.address = address
        self.size = size
        self.type = type
        self.available = available
        self.price = price
        self.bedroomcount = bedroomcount
        self.furnish = furnish
        self.other = other
        conn.execute("INSERT INTO User VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (self.id, self.housingid, self.sellerid, self.city, self.address, self.size, self.type, self.available, self.price, self.bedroomcount, self.furnish, self.other, ))
        conn.commit()

class Session:
    """hcursor = conn.cursor()
    houses_list = []
    hcursor.execute("SELECT * FROM User")
    database_houses = hcursor.fetchall()"""
    for h in database_houses:
        houses_list.append(h)
    def __init__(self, housing: Housing, user: User):
        self.housing = housing
        self.user = user

    def add_home(self, city, address, size, type, available, price, bedroomcount, furnish, other):
        new_house = self.user.add_home(self.housing.id, city, address, size, type, available, price, bedroomcount, furnish, other)
        self.housing.houses.append(new_house)

    def remove_user(self, name):
        all_members = housing.users + housing.admins
        for u in all_members:
            if u.name == name:
                self.user.remove_user(u)
                self.housing.update_values()

housing = Housing(None, "Hello", "Shayan", "Kermani", "Ker")
s1 = housing.get_session("Shayan", "Kermani")
housing.create_acc("MyAcc", "123", "Shayan2")