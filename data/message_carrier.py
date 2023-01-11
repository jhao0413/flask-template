"""
消息体
"""
# standard library
from datetime import datetime
from typing import Any, List, Optional

from pydantic import BaseModel


class MessageCarrier(BaseModel):
    """
    消息体
    200: 正常
    302: 需要重定向，data里面带redirect_url
    401: 需要登录，要么没登录要么refresh token也失效了
    499: access token失效了，用refresh token去换
    500: 服务器挂了
    """

    def __init__(self):
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.code: int = 200
        self.message: str = None
        self.data: Optional[Any] = None

    def push_succeed_data(
        self, data: Any = None, message: str = None
    ):
        """
        压入成功的数据
        :param data: 
        :param message:
        :return:
        """

        self.data = data
        self.code = 200
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if message:
            self.push_message(message)

    def push_exception(self, err: Exception, code: int = 500):
        """
        压入异常
        :param err:
        :param code:
        :return:
        """
        self.message = str(err)
        self.code = code

    def push_redirect_url(self, redirect_url: str, code: int = 302):
        """
        压入重定向的链接
        :param redirect_url:
        :param code:
        :return:
        """
        self.code = code
        self.data = {"redirect_url": redirect_url}

    def push_message(self, message: str):
        """
        压入消息列表
        :param message:
        :return:
        """
        self.message = message
