from database import SessionLocal
import schemas
import crud


db = SessionLocal()
users = []
print("Press ESC to quit")

while True:
    username_input = input("Enter a username: ")
    password_input = input("Enter a password: ")

    local_user = schemas.UserCreate(username = username_input, password = password_input)
    created_user = crud.create_user(db, local_user)
    users.append(created_user)
    
    choice = input("Do you want to continue? y/n: ")
    
    if choice.lower() == "n":
        break
    else:
        continue
    
while True:
    delete_db_user = int(input("Enter id of the user you wish to delete: "))
    crud.delete_user(db, delete_db_user)

    choice = input("Do you want to continue? y/n: ")
        
    if choice.lower() == "n":
        break
    else:
        continue

print(users)

db.close()