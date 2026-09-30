from passlib.context import CryptContext

ctx = CryptContext(schemes=["bcrypt"])

#Hash the password that the user entered
def create_hashed_password(plaintextpassword: str):
    hashed_password = ctx.hash(plaintextpassword)
    return hashed_password

#Verify user password
def verify_password(password_entered: str, existing_password: str):
    return ctx.verify(password_entered, existing_password)