
# # # # # # numbers = [1, 2, 3, [4, 'hello', 6]]
# # # # #
# # # # #
# # # # # # words = ['hello', 'world', 'python', 'hello']
# # # # # # word = words.pop(2)
# # # # # # print(words)
# # # # # # print(word)
# # # # # # words.remove('hello')
# # # # # # words.append([1, 2, 3])
# # # # # # words.insert(2, 'pycharm')
# # # # # # words.extend('hello')
# # # # # # print(words)
# # # # #
# # # # # numbers1 = [1, 2, 3, 4, 5]
# # # # # numbers2 = [6, 7, 8, 9, 0]
# # # # # numbers3 = numbers1 + numbers2
# # # # # print(numbers3 * 3)
# # # # # print(numbers1)
# # # # # print(numbers2)
# # # #
# # # # # numbers = [3, 5, 2, 4, 2, 6, 7, 8, 3, 4, 2, 5]
# # # # # numbers.sort()
# # # # # print(numbers)
# # # #
# # # # # words = ['Python', 'age', 'hello', 'Apple']
# # # # # words.sort(key=len)
# # # # # sorted_words = sorted(words)
# # # # # print(words)
# # # # # print(sorted_words)
# # # # # words.reverse()
# # # # # reversed_words = words[::-1]
# # # # # reversed_words = list(reversed(words))
# # # # # print(words)
# # # # # print(reversed_words)
# # # #
# # # # from copy import copy, deepcopy
# # # #
# # # # words = ['Python', 'age', 'hello', 'Apple', [1, 2, 3, 4]]
# # # # words2 = deepcopy(words)
# # # # words[4].append('good')
# # # # print(words2)
# # #
# # # # words = ['hello', 'python']
# # # # lst = ['good', 'apple', words]
# # # # lst[2].append('age')
# # # # print(words)
# # #
# # # # numbers = [i**i for i in range(100)]
# # # # print(numbers)
# # # # from pprint import pprint
# # # # n = int(input())  # 3
# # # # matrix = [
# # # #     [0 for j in range(n)]
# # # #     for i in range(n)
# # # # ]
# # # # pprint(matrix)
# # #
# # # # numbers = (5, )
# # # # result = numbers + (6, 7)
# # # # print(result)
# # #
# # # numbers = (1, 2, 3, [4, 5, 6, 7])
# # # numbers[3].clear()
# # # print(numbers)
# #
# # # print({6, 3, 4, 2, 5, 9, 3, 4, 35, 100})
# # #
# #
# # # a = {1, 2, 3, 4}
# # # b = {1, 2, 3, 4, 5, 6, 7}
# # # print(a <= b)
# # # print(a.issubset(b))
# #
# # # words = {'words', 'python', 'hello'}
# # # words.add('pycharm')
# #
# # # s1 = {1, 2, 3, 5}
# # # s2 = {3, 4, 5}
# # # s3 = {5, 6, 7, 3}
# # # s1.update(s2, s3)
# # # s1 |= s2 | s3
# # # print(s1)
# # # print(s2.symmetric_difference(s3))
# # # print(s3.symmetric_difference(s2))
# # # print(s2 ^ s3)
# # # print(s2.intersection(s3, s1))
# # # print(s1 & s3 & s2)
# # # print(s1.difference(s2))
# # # print(s1 - s2)
# # # print(s2.difference(s1))
# # # print(s2 - s1)
# # # s4 = s3.union(s1, s2)
# # # s5 = s3 | s2 | s1
# # # print(s5 == s4)
# #
# # # data = {
# # #     'name': 'Alex',
# # #     'age': 34
# # # }
# # # data['city'] = 'Minsk'
# # # data['name'] = 'Pavel'
# # # print(data)
# #
# # # user = (('name', 'alex'), ('age', 34), ('city', 'minsk'))
# # # data = dict(user)
# # # print(data)
# #
# # values = ('Alex', 34, 'Minsk')
# # keys = ('name', 'age', 'city')
# # # data = {keys[i]: values[i] for i in range(len(values))}
# # # print(data)
# # print({i: i for i in 'hello'})
#
# # data = dict.fromkeys(('name', 'age', 'city'), [])
# # print(data)
#
# data = {
#     'name': 'Alex',
#     'age': 34
# }
# data2 = {
#     'age': 35,
#     'city': 'Minsk'
# }
# new_data = data | data2
# print(new_data)
# print(data)
# print(data2)
#
# # data.update(
# #     {
# #         'age': 35,
# #         'city': 'Minsk'
# #     }
# # )
# # print(data)
# # print(data.setdefault('name', 'Н/У'))
# # print(data)
# # print(data.pop('city', None))
# # print(data)
# # print(list(data))
from collections import *

# numbers = '23627362474274'
# numbers2 = '462538456'
# numbers_counter = Counter(numbers)
# numbers_counter2 = Counter(numbers2)
# # print(numbers_counter.total())
# # print(numbers_counter.most_common(3))
# # print(list(numbers_counter.elements()))
# print(numbers_counter)
# print(numbers_counter2)
# # numbers_counter.subtract(numbers_counter2)
# print(numbers_counter - numbers_counter2)
# q = deque([1, 2, 3, 4, 5])
# q.rotate(2)
# print(q)
# q.rotate(-3)
# print(q)


# user = defaultdict(list)
# user['languages'].append('ru')
# print(user['name'])
# print(user)
# user = OrderedDict({'age': 35, 'city': 'Minsk', 'name': 'Alex'})
# user.move_to_end('city', last=True)
# user.move_to_end('name', last=False)
# print(user)
# User = namedtuple('User', ('name', 'age', 'city'))
# vasya = User(name='vasya', age=34, city='minsk')

# data1 = {'a': 1, 'b': 2}
# data2 = {'c': 3, 'd': 4, 'b': 5}
# chain = ChainMap(data1, data2, data2.copy())
# print(chain['c'])
# chain['e'] = 6
# print(chain)
# chain.parents.parents['f'] = 8
# print(chain)
# numbers = [2, 4, 8, 16, 32]
# text = 'hello world'
# data = {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# users = {
#     0: {'name': 'vasya', 'email': 'vasya@info.com'},
#     1: {'name': 'petya', 'email': 'petya@info.com'},
#     2: {'name': 'masha', 'email': 'masha@info.com'},
# }

# n = int(input('n: '))
# numbers = [2 ** i for i in range(1, n+1)]
# print(numbers)

# text = input('text: ')
# counter = {i: text.count(i) for i in set(text)}
# print(counter)

# n = int(input('n: '))
# users = {
#     i: {
#         key: input(f'{key}: ')
#         for key in ('name', 'email')
#     }
#     for i in range(n)
# }
# print(users)
