# from dis import dis
# from timeit import timeit

# print(timeit('''
# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# ''')) 3.4465629999758676 23

# print(timeit('''
# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# numbers = [int(number) for number in numbers]
# ''')) 3.571474500000477 23

# print(timeit('''
# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# numbers = [*map(int, numbers)]
# ''')) 2.370272800035309 13

# print(timeit('''
# a = 5
# a = str(a)
# ''')) 0.21789510000962764
# print(timeit('''
# a = 5
# a = f'{a}'
# ''')) 0.38266920001478866

# print(timeit('''
# a = '4'
# b = '2'
# if a.isdigit():
#     a = int(a)
# else:
#     print('invalid value')
#     exit(0)
# if b.isdigit():
#     b = int(b)
# else:
#     print('invalid value')
#     exit(0)
# if b != 0:
#     c = a / b
# else:
#     print('invalid value')
#     exit(0)
# ''')) 1.258230299979914 60

# print(timeit('''
# try:
#     a = int('4')
#     b = int('2')
#     c = a / b
# except ValueError:
#     print('invalid value')
# except ZeroDivisionError:
#     print('invalid value')
# ''')) 0.7632340000127442 44


class Math:

    @classmethod
    async def sum(cls, a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        return a * b

    @classmethod
    def divide(cls, a, b):
        return a / b


import phonenumbers
from pydantic.validators import strict_str_validator
from pydantic import BaseModel, EmailStr

# print(phonenumbers.is_valid_number(phonenumbers.parse('+375111111111')))


class PhoneNumber(str):

    @classmethod
    def __get_validators__(cls):
        yield strict_str_validator
        yield cls.validate

    @classmethod
    def validate(cls, v: str) -> str:
        v = v.strip().replace(' ', '')
        try:
            phone = phonenumbers.parse(v)
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValueError('invalid phone number format')
        else:
            if phonenumbers.is_valid_number(phone):
                return cls(phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.E164))
            raise ValueError('invalid phone number')


class User(BaseModel):
    name: str
    phone_number: PhoneNumber


vasya = User(name='vasya', phone_number='80259145208')
print(vasya.phone_number)
