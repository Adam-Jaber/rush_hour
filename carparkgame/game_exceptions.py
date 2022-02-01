class RushHourException(BaseException):
    pass


class BoardException(RushHourException):
    def __str__(self):
        return "Board Exception"


class LvlExist(BoardException):
    def __str__(self):
        return "Level does not exist"


class CarException(RushHourException):
    def __str__(self):
        return "Car exception"


class MovementException(CarException):
    def __str__(self):
        return "Car cannot move like that"


class OrientException(MovementException):
    def __str__(self):
        return "Car only moves within its own axis"


class CollisionException(MovementException):
    def __str__(self):
        return "Cant hit cars (shouldn't *)"


class BorderException(MovementException):
    def __str__(self):
        return "Car moves only within the board"


class SignupException(RushHourException):
    def __str__(self):
        return "Invalid info"


class InvalidFName(SignupException):
    def __str__(self):
        return "Invalid first name"


class InvalidLName(SignupException):
    def __str__(self):
        return "Invalid last name"


class UsernameExists(SignupException):
    def __str__(self):
        return "Username already exists"


class InvalidPassword(SignupException):
    def __str__(self):
        return "Invalid password"


class ConfirmError(SignupException):
    def __str__(self):
        return "Password does not match confirmation"
