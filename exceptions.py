#------------CUSTOM EXCEPTIONS------------

#User Not Found Exception
class UserNotFoundError(Exception):
    pass

#User already exists
class UserAlreadyExistsError(Exception):
    pass

#Incorrect login info
class IncorrectLoginError(Exception):
    pass