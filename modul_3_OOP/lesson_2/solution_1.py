import datetime


class Person:
    def __init__(
            self,
            name: str,
            age: int
    ):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls,
                        name,
                        birth_year
                        ):
        today = datetime.date.today()
        current_year = today.year
        age = current_year - birth_year
        return cls(name, age)


person = Person.from_birth_year("Vladislav", 1994)

print(f"Имя: {person.name}, Возраст: {person.age} лет")