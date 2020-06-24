class Human:

    _sex = frozenset(("male", "female"))

    def __init__(self, name, age, sex):
        if not name.isalpha():
            raise Exception("Name should contain alpha")
        if not isinstance(age, int):
            raise Exception("Age is not number")
        if age > 100 or age < 1:
            raise Exception("Incorrect age")
        if not sex.lower() in self._sex:
            raise Exception("Sex should be 'male' or 'female")
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return f"\nname:{self.name}, age:{self.age}, sex:{self.sex}"

    def __repr__(self):
        return f"\nname:{self.name}, age:{self.age}, sex:{self.sex}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age \
               and self.sex == other.sex


class Teacher(Human):
    def __init__(self, name, age, sex, cathedra, position):
        super().__init__(name=name, age=age, sex=sex)
        self.cathedra = cathedra
        self.position = position

    def __str__(self):
        return f"name:{self.name}, age:{self.age}, sex:{self.sex}, " \
               f"cathedra:{self.cathedra}, position:{self.position}"

    def __repr__(self):
        return {"name": self.name,
                "age": self.age,
                "sex": self.sex,
                "cathedra": self.cathedra,
                "position": self.position}

    def __eq__(self, other):
        return self.name == other.name\
               and self.age == other.age\
               and self.sex == other.sex\
               and self.cathedra == other.cathedra\
               and self.position == other.position

