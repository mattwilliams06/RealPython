# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f'{self.name}: {self.age}'

# alex = Person('Alex', 15)
# mabel = Person('Mabel', 14)
# eddie = Person('Eddie', 12)

# p = [alex, mabel, eddie]
# print(p)
# p.sort(key=lambda x: x.name)
# print(p)

# nums = list(range(1,21))
# print(nums)
# evens = list(filter(lambda x: x%2 == 0, nums))
# odds = list(filter(lambda x: x%2 != 0, nums))
# print(evens)
# print(odds)

# import numpy as np
# avg = np.mean(nums)
# above_avg = list(filter(lambda x: x > avg, nums))
# print(nums)
# print(avg)
# print(above_avg)

# nicknames = ['Rockies', 'Braves', 'Reds', 'Orioles', 'Nationals',
# 'Giants', 'A\'s', 'Padres']
# print(nicknames)
# short = list(filter(lambda x: len(x) < 6, nicknames))
# print(short)

# nums = list(range(1,11))
# print(nums)
# # sq_nums = list(map(lambda x: x**2, nums))
# # print(sq_nums)
# evens = list(map(lambda x: x%2==0, nums))
# print(evens)

# wc_teams = [('Brazil', 21), ('Argentina', 16), ('Germany', 19),
# ('Italy', 17), ('England', 15)]
# print(wc_teams)
# new = list(map(lambda team: (team[0], team[1]+1), wc_teams))
# print(new)
# new.sort(key=lambda team: team[1], reverse=True)
# print(new)

# from functools import reduce
# # nums = list(range(1,11))
# # total = reduce(lambda x, y: x*y, nums)
# # print(total)
# names = ['dan', 'steve', 'kate', 'jackie', 'your mom', 'up your butt']
# conc = reduce(lambda x, y: x+y, names, '')
# print(conc.replace(' ', ''))

import unittest

squared = lambda x: x**2

class LambdaTest(unittest.TestCase):
    def test_squared(self):
        self.assertEqual(squared(2), 4)

    def test_zero(self):
        self.assertEqual(squared(0), 0)

    def test_negative(self):
        self.assertEqual(squared(-2), 4)

if __name__ == '__main__':
    unittest.main(verbosity=2)