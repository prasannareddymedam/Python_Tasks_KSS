""" A web application wants to ensure that users are authenticated before accessing 
sensitive functions. Create a decorator that checks whether the user is logged in before 
allowing access to a function.
"""

def check_login(func):
    def Wrapper():
        print("Login Ok")
        func()
    return Wrapper

@check_login
def show_profile():
    print("Profile Opened")

show_profile()
