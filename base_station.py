from abc import ABC, abstractmethod


class BaseStation(ABC):
    def __init__(self, name: str, capacity: int):
        if not all(c.isalnum() or c == '-' for c in name):
            raise ValueError("Station names can contain only letters, numbers, and hyphens!")
        if capacity < 0:
            raise ValueError("A station cannot have a negative capacity!")

        self.name = name
        self.capacity = capacity
        self.astronauts = []

    def calculate_total_salaries(self):
        return f"{sum(a.salary for a in self.astronauts):.2f}"

    def status(self):
        astronaut_ids = " #".join(sorted(a.id_number for a in self.astronauts)) if self.astronauts else "N/A"
        return f"Station name: {self.name}; Astronauts: {astronaut_ids}; Total salaries: {self.calculate_total_salaries()}"

    @abstractmethod
    def update_salaries(self, min_value: float):
        pass