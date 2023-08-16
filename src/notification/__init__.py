import requests
import datetime
import pytz
from dotenv import load_dotenv, find_dotenv
import os
from enum import Enum
from typing import Union


class Notifier:
    def notify(self, message: str = ''):
        raise NotImplementedError('not implemented')

class NotifierColor(Enum):
    INFO = '00ff00'
    SUCCESS = '0000ff'
    ERROR = 'ff0000'

class Message:
    def __init__(self, body: str = '', title: str = '', color: NotifierColor = NotifierColor.INFO):
        self.title = title
        self.body = body
        self.color = color

class SlackNotifier(Notifier):
    DEFAULT_TITLE = '新規お知らせがありました'

    def __init__(self):
        load_dotenv(find_dotenv())
        self.slack_url = os.getenv("SLACK_WEBHOOK_URL")

    def __str_message2class(self, messages: list[str|Message] = []):
        _messages = []
        for m in messages:
            if isinstance(m, str):
                _messages.append(Message(body=m, title=''))
            else:
                _messages.append(m)
        return _messages

    def __build_attachments(self, messages: list[Message] = []):
        return [
            {
                "color": m.color.value,
                "fields": [
                    {
                        "title": m.title,
                        "value": m.body
                    }
                ]
            }
            for m in messages
        ]

    def notify(self, title: str = DEFAULT_TITLE, *messages: Union[str, Message]):

        messages = self.__str_message2class(messages)
        now = datetime.datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%Y/%m/%d/ %H:%M:%S')

        requests.post(self.slack_url, json={
            "icon_emoji": ":t-rex:",
            "text": f"{title}。\n{now}",
            "attachments": self.__build_attachments(messages)
        })
