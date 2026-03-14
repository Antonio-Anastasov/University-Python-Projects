from abc import ABC, abstractmethod


class BaseAstronaut(ABC):
    def __init__(self, id_number: str, salary: float, specialization: str, stamina: int):
        if not id_number.isdigit():
            raise ValueError("ID can contain only digits!")
        if salary < 0:
            raise ValueError("Salary must be a positive number!")
        if not specialization or specialization.isspace():
            raise ValueError("Specialization cannot be empty!")
        if not 0 <= stamina <= 100:
            raise ValueError("Stamina is out of range!")

        self.id_number = id_number
        self.salary = salary
        self.specialization = specialization
        self.stamina = stamina

    @abstractmethod
    def train(self):
        pass