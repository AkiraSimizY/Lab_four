class Animals:
    """Базовый класс для животных"""
    def __init__(self, name: str, age: int):
        self.name = name  # Имя животного
        self.age = age  # Возраст животного

    def make_sound(self) -> None:
        """Метод, который делает звук"""
        pass

class Dogs(Animals):
    """Дочерний класс для собак"""
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed  # Порода собаки

    def make_sound(self) -> None:
        """Перегрузка метода make_sound"""
        return "Гав-гав!"

    def wag_tail(self) -> None:
        """Метод, который показывает, что собака весела"""
        pass

class Cats(Animals):
    """Дочерний класс для кошек"""
    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.color = color  # Цвет шерсти кошки

    def make_sound(self) -> None:
        """Перегрузка метода make_sound"""
        return "Мяу!"

    def scratch_furniture(self) -> None:
        """Метод, который показывает, что кошка царапает мебель"""
        pass