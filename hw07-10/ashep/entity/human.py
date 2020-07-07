# Людина з полями імя, вік, стать. Перевизначити методи init, str, repr, eq
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return f"name: {self.name} age: {self.age} sex: {self.sex}"

    def __repr__(self):
        return f"{self.name}, {self.age}, {self.sex}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.sex == other.sex


# Створити сутність Викладач яка наслідує класс людина, додати поля кафедра, посада. Перевизначити методи init, str, repr, eq
class Lecturer(Human):
    def __init__(self, name, age, sex, department, job_position):
        super().__init__(name=name, age=age, sex=sex)
        self.department = department
        self.job_position = job_position

    def __str__(self):
        return f"name: {self.name}\n" \
               f"age: {self.age}\n" \
               f"sex:{self.sex}\n" \
               f"department: {self.department}\n" \
               f"job_position: {self.job_position}"

    def __repr__(self):
        return f"{self.name}, {self.age}, {self.sex},{self.department},{self.job_position}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.sex == other.sex and self.department == other.department and self.job_position == other.job_position
