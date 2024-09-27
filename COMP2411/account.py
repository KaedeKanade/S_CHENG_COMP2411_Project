import json
import os
import random

admin_key = 'AdminKey'
staff_key = 'StaffKey'

class Account:
    def __init__(self, user_id, email, password, username, account_type):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.username = username
        self.account_type = account_type

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'email': self.email,
            'password': self.password,
            'username': self.username,
            'account_type': self.account_type
        }

class AccountManagementSystem:
    def __init__(self, storage_file='accounts.json'):
        self.storage_file = storage_file
        self.accounts = self.load_accounts()

    def generate_user_id(self):
        while True:
            user_id = ''.join(random.choices('0123456789', k=12))
            if user_id not in self.accounts:
                return user_id

    def load_accounts(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                return {acc['user_id']: Account(**acc) for acc in json.load(file)}
        return {}

    def save_accounts(self):
        with open(self.storage_file, 'w') as file:
            json.dump([acc.to_dict() for acc in self.accounts.values()], file)

    def create_account(self):
        email = input("Your email(would serving as your account): ")
        password = input("Password: ")
        lastname = input("Your last name: ")
        firstname = input("Your first name: ")
        username = f"{firstname} {lastname}"
        phone = input('Your contact phone number: ')
        code = input("(Optional) enter identity code: ")
        if code == admin_key:
            account_type = 'admin'
        elif code == staff_key:
            account_type = 'staff'
        else:
            account_type = 'customer'
        user_id = self.generate_user_id()
        new_account = Account(user_id, email, phone, password, username, account_type)
        self.accounts[user_id] = new_account
        self.save_accounts()
        return new_account

    def read_account(self, user_id):
        return self.accounts.get(user_id)

    def delete_account(self, user_id):
        if user_id in self.accounts:
            del self.accounts[user_id]
            self.save_accounts()
            return True
        return False

    def list_accounts(self):
        return [acc.to_dict() for acc in self.accounts.values()]