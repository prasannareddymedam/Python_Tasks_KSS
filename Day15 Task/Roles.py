#  Decorator-based Access Control 
"""Scenario: 
   Restrict access to certain functions. 
   Task: 
   ● Create a decorator to check user role 
   ● Use condition inside decorator 
   ● Apply decorator to multiple functions 
   ● Store roles in a dictionary
 """

roles = {"Ram":"admin", "Usha":"User"}
current = "Usha"

def check_admin (func):
    def wrapper():
        if roles [current] == "admin":
            return func()
        return "Access Denied!"
    return wrapper
@check_admin
def delete_user():
    return "User Deleted!"
@check_admin
def view_report():
    return "Repeat Viewed!"
print(delete_user())
print(view_report())
