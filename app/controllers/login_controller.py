# app/controllers/login_controller.py
from app.models.user_model import UserModel

class LoginController:
    def __init__(self, view):
        self.view = view

    def login(self, username, password):
        if UserModel.authenticate(username, password):
            print("Login successful")
            return True
        else:
            print("Invalid credentials")
            return False

    def change_password(self, username, new_password):
        UserModel.change_password(username, new_password)
        print("Password changed successfully")

