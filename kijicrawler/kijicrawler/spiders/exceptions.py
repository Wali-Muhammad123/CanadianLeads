class UserNotAllowedException(Exception):
    def __init__(self, message):
        self.message = message
if __name__ == "__main__":
    try:
        raise UserNotAllowedException(message="User not allowed to login")
    except UserNotAllowedException as e:
        print(e.message)