# # from threading import Lock
# #
# #
# # class Singleton(type):
# #
# #     _instances: dict = {}
# #     _lock: Lock = Lock()
# #
# #     def __call__(cls, *args, **kwargs):
# #         with cls._lock:
# #             if cls not in cls._instances:
# #                 instance = super().__call__(*args, **kwargs)
# #                 cls._instances[cls] = instance
# #             else:
# #                 cls._instances[cls].__init__(*args, **kwargs)
# #         return cls._instances[cls]
# #
# #
# # class Child(metaclass=Singleton):
# #
# #     def __init__(self, a):
# #         self.a = a
# #
# #
# # child1 = Child(4)
# # child2 = Child(5)
# # print(child1 is child2)
# # print(child1.a)
# # print(child2.a)
#
#
# from abc import ABC, abstractmethod
#
#
# class AbstractProductA(ABC):
#
#     @abstractmethod
#     def name(self):
#         pass
#
#
# class AbstractProductB(ABC):
#
#     @abstractmethod
#     def name(self):
#         pass
#
#
# class ProductA(AbstractProductA):
#
#     def name(self):
#         return self.__class__.__name__
#
#
# class ProductB(AbstractProductB):
#
#     def name(self):
#         return self.__class__.__name__
#
#
# class AbstractFactory(ABC):
#
#     @abstractmethod
#     def create_a(self) -> AbstractProductA:
#         pass
#
#     @abstractmethod
#     def create_b(self) -> AbstractProductB:
#         pass
#
#
# class CarFactory(AbstractFactory):
#
#     def create_a(self) -> AbstractProductA:
#         return ProductA()
#
#     def create_b(self) -> AbstractProductB:
#         return ProductB()
from datetime import datetime
from typing import Literal


class BelpostAPI:

    @classmethod
    def get_status(cls, number: str):
        return {'number': number, 'status': 'SEND', 'time': datetime.now().timestamp()}


class EvropochtaAPI:

    @classmethod
    def track(cls, track_number: str):
        return {'track_number': track_number, 'send_time': datetime.now().isoformat(), 'status': 'SEND'}


class Pochta:

    @classmethod
    def find(cls, number: str, post: Literal['bel', 'evr'] = 'bel'):
        if post not in ('bel', 'evr'):
            raise ValueError('invalid argument post')

        if post == 'bel':
            response = BelpostAPI.get_status(number)
            return {
                'track_number': response['number'],
                'datetime': datetime.fromtimestamp(response['time']),
                'status': response['status']
            }
        else:
            response = EvropochtaAPI.track(number)
            return {
                'track_number': response['number'],
                'datetime': datetime.fromisoformat(response['send_time']),
                'status': response['status']
            }


from abc import ABC, abstractmethod


class Subject(ABC):

    @abstractmethod
    def request(self, url: str, **kwargs):
        pass


class RealSubject(Subject):

    def request(self, url: str, **kwargs):
        return {'status': 200}


from dataclasses import dataclass


@dataclass
class ResponseData:
    status: int


class ProxySubject(Subject):

    def __init__(self, subject: RealSubject):
        self.__subject = subject

    def request(self, url: str, **kwargs):
        if not url.startswith('https://'):
            raise ValueError('url must be start https')
        response = self.__subject.request(url, **kwargs)
        print(f'LOG: {datetime.now()} REQUEST')
        return ResponseData(**response)


class Request:

    def __init__(self, host: str):
        self.host = host

    def _get(self):
        print('get')

    def _post(self):
        print('post')


class Response:

    def __init__(self, directory: str):
        self.directory = directory

    def render(self):
        print('<b>Hello</b>')


class Facade:

    def __init__(self, request: Request = None, response: Response = None, **env):
        self.request = request or Request(host='https://some-site.com')
        self.response = response or Response(directory='templates')

    def get(self):
        self.response.render()
        return self.request._get()

    def post(self):
        self.response.render()
        return self.request._post()
