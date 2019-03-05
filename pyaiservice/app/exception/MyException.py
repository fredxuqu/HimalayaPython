
class MyException(BaseException):
    def __init__(self, message):
        super().__init__()
        self.message = message

def stuff(message):
    raise MyException(message)


class DatabaseException(Exception):
    def __init__(self, err='数据库错误'):
        Exception.__init__(self, err)


class PreconditionsException(DatabaseException):
    def __init__(self, err='PreconditionsErr'):
        DatabaseException.__init__(self, err)


def testRaise():
    raise PreconditionsException()

