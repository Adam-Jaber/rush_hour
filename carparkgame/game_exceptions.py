class RushHourException(BaseException):
    pass


class BoardException(RushHourException):
    pass


class LvlExist(BoardException):
    pass


class CarException(RushHourException):
    pass


class MovementException(CarException):
    pass


class OrientException(MovementException):
    pass


class CollisionException(MovementException):
    pass


class BorderException(MovementException):
    pass


class SignupException(RushHourException):
    pass


class InvalidFName(SignupException):
    pass


class InvalidLName(SignupException):
    pass


class UsernameExists(SignupException):
    pass


class InvalidPassword(SignupException):
    pass