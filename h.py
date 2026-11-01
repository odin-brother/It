class Parent:
    a = 10

class Child1(Parent):
    pass

class Child2(Parent):
    pass

class Child3(Parent):
    a = 99

c1 = Child1()
c2 = Child2()
c3 = Child3()

print(c1.a)
print(c2.a)
print(c3.a)

