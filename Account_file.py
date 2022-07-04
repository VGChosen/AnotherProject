import sqlite3
conn = sqlite3.connect("project_files/Bank_Data.sqlite")
conn.execute("CREATE table IF NOT EXISTS bankist_users(name, phone, password, cash)")


def give_cash_info(name, phone, password):
    myCursor = conn.cursor()
    my_Cash_tuple = myCursor.execute("SELECT cash FROM Bankist_users WHERE (name=?) AND (phone=?) AND (password=?)",
                                     (name, phone, password))
    info_cash = my_Cash_tuple.fetchall()
    for cash_details in info_cash:
        for cash in cash_details:
            return cash


def deposit_money(name, phone, password, money_in_bank, money_to_deposit):

    total_money = money_to_deposit + money_in_bank
    conn.execute(f"UPDATE Bankist_users SET cash={total_money} WHERE (name=?) AND (phone=?) AND (password=?)",
                 (name, phone, password))
    conn.commit()


def withdraw_money(name, phone, password, money_in_bank, money_to_withdraw):

    total_money = money_in_bank - money_to_withdraw
    conn.execute(f"UPDATE Bankist_users SET cash={total_money} WHERE (name=?) AND (phone=?) AND (password=?)",
                 (name, phone, password))
    conn.commit()



def phone_exist(phone):
    search_phone = conn.execute("SELECT phone FROM Bankist_users WHERE phone=?", (phone,))
    search_phone_data = search_phone.fetchall()
    if search_phone_data:
        return True
    else:
        return False


def search_contact_exist(name, phone, password):
    search_query = conn.execute("SELECT name, phone, password FROM Bankist_users WHERE (name=?) AND (phone=?) "
                                "AND (password=?)",(name, phone, password))
    search_query_data = search_query.fetchall()
    if not search_query_data:
        return False
    else:
        return True


class Account:
    def __init__(self, name, phone, password):
        self.name = name
        self.phone = phone
        self.password = password
        self.balance = 0
        conn.execute("INSERT INTO bankist_users VALUES(?, ?, ?, ?)", (self.name, self.phone, self.password,
                                                                      self.balance))
        conn.commit()


    #
    #
    # def deposit(self, money):
    #     self.balance += money
    #     print(f"{money} has been deposited to your account")
    #
    # def withdraw(self, money):
    #     self.balance -= money
    #     print(f"{money} has been withdrawn to your account")

def edit_info(info: int):
    print(info)

