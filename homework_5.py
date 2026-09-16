from abc import ABC, abstractmethod

class File(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def get_file_info(self):
        pass

class TextFile(File):
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def open(self):
        print(f"Содержимое файла: {self.content}")

    def get_file_info(self):
        print(f"Текстовый файл: {self.name}")

class ImageFile(File):
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

    def open(self):
        print(r"""
          /\_/\
         ( o.o )
          > ^ <
        """)

    def get_file_info(self):
        print(f"Изображение: {self.name}, размер: {self.width}x{self.height}")

class AudioFile(File):
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def open(self):
        print(f"Воспроизводится аудиофайл: {self.name}")

    def get_file_info(self):
        print(f"Аудиофайл: {self.name}, продолжительность: {self.duration} минут")

files = [
    TextFile("notes.txt", "Сегодня изучаю абстракцию в Python"),
    ImageFile("cat.png", 800, 600),
    AudioFile("music.mp3", 4)
]

for file in files:
    file.open()
    file.get_file_info()

class ArchiveFile(File):
    def open(self):
        print("Открываем архив")

# archive = ArchiveFile()