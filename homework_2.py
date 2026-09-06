class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education
    def introduce(self):
        if self.higher_education:
            print("Привет, я " + self.name + ", родился " + self.birth_date + ", по профессии я " + self.occupation + ", высшее образование есть.")
        else:
            print("Привет, я " + self.name + ", родился " + self.birth_date + ", по профессии я " + self.occupation + ", высшего образования нет.")

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        super().introduce()
        print("Учусь в группе " + self.group_name + ".")

class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        super().introduce()
        print("Мое хобби " + self.hobby + ".")

classmate1 = Classmate("Алексей", "12.02.2002", "менеджер по продажам", True, "701")
classmate2 = Classmate("Дархан", "17.09.2006", "повар", False, "530")
friend1 = Friend("Вячеслав", "15.01.1999", "окулист", True, "игра на гитаре")
friend2 = Friend("Василий", "17.10.1998", "геодезист", True, "вольная борьба")

classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()