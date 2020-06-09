class Animal:
    name = "dog"

    def __test__(self):
        print("测试")

    def langu(self, b = "Bob"):
        print(b)

newAnimal = Animal()
# print(newAnimal.name)
newAnimal.langu()

# Animal.__test__(newAnimal)
# Animal.__test(newAnimal)
newAnimal.__test__()


import random
print(int(random.random()*10))
print(random.randrange(10))
print(random.sample(range(1,11), 10))


