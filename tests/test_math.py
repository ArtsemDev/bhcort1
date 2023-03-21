# from unittest import TestCase
#
from lesson15 import Math
#
#
# class TestMath(TestCase):
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.math = Math(4, 2)
#
#     def test_sum(self):
#         values = [(2, 3, 5), (5, 6, 12)]
#         for line in values:
#             with self.subTest():
#                 self.math.a = line[0]
#                 self.math.b = line[1]
#                 self.assertEqual(self.math.sum(),  line[2])
#
#     # def test_multiply(self):
#     #     self.assertEqual(self.math.multiply(),  30)
#
#     # def test_divide(self):
#     #     self.assertEqual(self.math.divide(), 2)


import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'a, b, c',
    (
            (2, 4, 6),
            (4, 5, 9),
            (7, 3, 10)
    )
)
async def test_sum(a, b, c):
    assert await Math.sum(a, b) == c
