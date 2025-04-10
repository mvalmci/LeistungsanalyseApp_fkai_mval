from datetime import date

class Person:
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.__birth_date = birth_date  # private attribute

    def calculate_age(self):
        today = date.today()
        birth_date = date.fromisoformat(self.__birth_date)
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age


class Subject(Person):
    def __init__(self, first_name, last_name, birth_date, sex):
        super().__init__(first_name, last_name, birth_date)
        self.sex = sex

    def estimate_max_hr(self):
        age = self.calculate_age()
        if self.sex.lower() == "female":
            max_hr = 226 - age
        else:
            max_hr = 220 - age
        return max_hr


class Supervisor(Person):
    def __init__(self, first_name, last_name, birth_date):
        super().__init__(first_name, last_name, birth_date)


class Experiment:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.subjects = []
        self.supervisors = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def add_supervisor(self, supervisor):
        self.supervisors.append(supervisor)

    def __str__(self):
        return f"Experiment: {self.name}, Date: {self.date}, Subjects: {len(self.subjects)}, Supervisors: {len(self.supervisors)}"