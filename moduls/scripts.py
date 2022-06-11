from moduls.globals import *

# find user index in Users list by id
def find_user_index(id):
    for i in range(len(Users)):
        if Users[i].id == id:
            return i