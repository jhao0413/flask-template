"""
异常定义类
"""


class BusinessError(Exception):
    """
    业务异常
    """
    def __init__(self, message=None):
        if not message:
            message = "捕捉到业务异常"
        super().__init__(message)
