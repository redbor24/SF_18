class Cat:
    name, sex, age = None, None, None
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age


    def print(self):
        print("--------------------")
        print("Имя =", self.name)
        print("Пол =", self.sex)
        print("Возраст =", self.age)

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age
