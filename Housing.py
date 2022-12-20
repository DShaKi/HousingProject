import sqlite3
import uuid
import hashlib

conn = sqlite3.connect('HousingDB.db')

"""
1. Find Home 
2. Request Best Home 
"""

class Housing:
    def __init__(self, id, name, username, password, adminname, add_database):
        if add_database == True:
            if id == None:
                self.id = str(uuid.uuid1())
            else:
                self.id = id
            self.name = name
            self.admins = [Admin(None, self.id, username, password, adminname, True)]
            self.users = []
            self.houses = []
            self.house_requests = []
            self.requests = []
            conn.execute("INSERT INTO Housing VALUES (?, ?, ?, ?, ?)", (self.id, self.name, username, password, adminname, ))
            conn.commit()
        else:
            self.id = id
            self.name = name
            self.admins = [Admin(None, self.id, username, password, adminname, False)]
            self.users = []
            self.houses = []
            self.house_requests = []
            self.requests = []
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM User WHERE HousingID = (?)" , (self.id ,))
            dusers = cursor.fetchall()
            for u in dusers:
                if u[5] == 1:
                    self.admins.append(Admin(u[0], u[1], u[2], u[3], u[4], False))
                else:
                    self.users.append(User(u[0], u[1], u[2], u[3], u[4], False))
            cursor.execute("SELECT * FROM House WHERE HousingID = (?)" , (self.id ,))
            dhouses = cursor.fetchall()
            for h in dhouses:
                self.houses.append(House(h[0], h[1], h[2], h[3], h[4], h[5], h[6], h[7], h[8], h[9], h[10], h[11], h[12], False))
            cursor.execute("SELECT * FROM HouseRequest")
            dhouse_requests = cursor.fetchall()
            for r in dhouse_requests:
                self.house_requests.append(r[0])

    def update_values(self):
        self.admins = []
        self.users = []
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User WHERE ID = (?)", (self.id, ))
        users = cursor.fetchall()
        for u in users:
            if u[6] == 0:
                self.admins.append(Admin(u[0], u[1], u[2], u[3], u[4], False))
            else:
                self.users.append(User(u[0], u[1], u[2], u[3], u[4], False))

    def create_acc(self, username, password, name):
        self.users.append(User(None, self.id, username, password, name, True))
        print(f"Account with the name {name} successfully added.")

    def get_session(self, username, password):
        all_members = self.admins + self.users
        for u in all_members:
            if u.username == username and u.password == str(hashlib.md5(str(password + self.id).encode('utf-8')).hexdigest()):
                print("Logged in!")
                return Session(self, u)

class User:
    def __init__(self, id, housingid, username, password, name, add_database):
        if id == None:
            self.id = str(uuid.uuid1())
        else:
            self.id = id
        self.housingid = housingid
        self.username = username
        self.password = str(hashlib.md5(str(password + housingid).encode('utf-8')).hexdigest())
        self.name = name
        self.isAdmin = False
        if add_database == True:
            conn.execute("INSERT INTO User VALUES (?, ?, ?, ?, ?, ?)", (self.id, self.housingid, self.username, self.password, self.name, self.isAdmin, ))
            conn.commit()

    def add_house(self, housingid, city, address, size, type, available, price, bedroomcount, furnish, other, approval):
        new_house = House(None , housingid, self.id, city, address, size, type, available, price, bedroomcount, furnish, other, approval, True)
        return new_house

    def remove_user(self, user):
        print("Access Denied!")


class Admin(User):
    def __init__(self, id, housingid, username, password, name, add_database):
        super().__init__(id, housingid, username, password, name, add_database)
        self.isAdmin = True
        conn.execute("UPDATE User SET isAdmin = (?) WHERE ID = (?)", (self.isAdmin, self.id, ))
        conn.commit()
    
    def remove_user(self, user):
        conn.execute("DELETE FROM User WHERE ID = (?)", (user.id, ))
        print(f"User {user.name} removed.")
        del user
        conn.commit()

class House:
    def __init__(self, id, housingid, sellerid, city, address, size, type, available, price, bedroomcount, furnish, other, approval, add_database):
        # apprval -> 0 = Accepted, 1 = Declined, 2 = Under Review
        if id == None:
            self.id = str(uuid.uuid1())
        else:
            self.id = id
        self.housingid = housingid
        self.sellerid = sellerid
        self.city = city
        self.address = address
        self.size = size
        self.type = type
        self.available = available
        self.price = price
        self.bedroomcount = bedroomcount
        self.furnish = furnish
        self.other = other
        self.approval = approval
        if add_database == True:
            conn.execute("INSERT INTO House VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (self.id, self.housingid, self.sellerid, self.city, self.address, self.size, self.type, self.available, self.price, self.bedroomcount, self.furnish, self.other, self.approval, ))
            conn.commit()

class Session:
    def __init__(self, housing: Housing, user: User):
        self.housing = housing
        self.user = user

    def add_house(self, city, address, size, type, available, price, bedroomcount, furnish, other):
        new_house = self.user.add_house(self.housing.id, city, address, size, type, available, price, bedroomcount, furnish, other, 3)
        self.housing.houses.append(new_house)
        self.housing.house_requests.append(new_house)
        conn.execute("INSERT INTO HouseRequest VALUES (?)", (new_house.id, ))
        conn.commit()
        print("Your request has sent to your housing.")

    def remove_user(self, name, all_members):
        all_members = self.housing.users + self.housing.admins
        for u in all_members:
            if u.name == name:
                self.user.remove_user(u)
                self.housing.update_values()

    def check_approval(self, houseid):
        if self.user.isAdmin == True or self.user.isAdmin == 1:
            for h in self.housing.houses:
                if h.id == houseid:
                    index = self.housing.houses.index(h)
                    self.housing.houses[index].approval == 0
                    conn.execute("UPDATE House SET Approval = (?) WHERE HouseID = (?)", (0, h.id, ))
                    conn.commit()
                    index2 = self.housing.house_requests.index(h.id)
                    self.housing.house_requests.remove(h.id)
                    print("The house approved.")
                else:
                    print("There is no house with this id.")
        else:
            print("Access Denied!")

main_cursor = conn.cursor()
main_cursor.execute("SELECT * FROM Housing")
dmain_housings = main_cursor.fetchall()
main_housings = []
for h in dmain_housings:
    main_housings.append(Housing(h[0], h[1], h[2], h[3], h[4], False))
# housing = Housing(None, "Hello", "Shayan", "Kermani", "ShK", True)
# s3 = housing.get_session("Shayan", "Kermani")
# housing.create_acc("MyAcc", "123", "ShK2")
# s4 = housing.get_session("MyAcc", "123")
# s4.add_house("Tehran", "123", 120, "Sell", 1, 1200, 2, 1, "Nothing")
s1 = main_housings[0].get_session("Shayan", "Kermani")
s2 = main_housings[0].get_session("MyAcc", "123")
s1.check_approval(main_housings[0].house_requests[0])