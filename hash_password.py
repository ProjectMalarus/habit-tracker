import bcrypt
#bcrypt.gensalt - generates a 'salt' (pseudorandom string that is added to the password)
#doesn't need any arguments and returns a pseudorandom string

#bcrypt.hashpw is used to create the final hash which is stored in a database
#args - pass in a salt and a password in the form of a bytecode

#bycrypt.checkpw is used to check if the password is correct

#Hash the password that the user entered
def create_hashed_password(plaintextpassword: str):
    bytes = plaintextpassword.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(bytes, salt)
    return hashed_password.decode("utf-8")

#Verify user password
def verify_password(password_entered: str, existing_password: str):
    bytes = password_entered.encode('utf-8')
    salt = bcrypt.gensalt()
    pw_entered = bcrypt.hashpw(bytes, salt)

    existing_password = existing_password.encode('utf-8')

    return bcrypt.checkpw(pw_entered, existing_password)