#!/usr/bin/python
#第一行定义解释器的位置
import datetime

print("hello world")


class human:
    '定义人类'

    def __init__(self, name, birthday):
        self.birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d")
        self.age = datetime.datetime.now().year - self.birthday.year
        self.name = name
        self.gender = "male"

    def eat(self, food):
        print(self.name + " eatingt " + food)

    def sleep(self):
        print(self.name + " sleeping")


tom = human("Tom", "2012-12-15")
tom.gender = "fmale"
print(tom.name, " is ", tom.age, " yeas old")
tom.eat("rice")
tom.sleep()

rose = human("Rose", "1982-03-11")
print(rose.name, " is ", rose.age, " yeas old")
