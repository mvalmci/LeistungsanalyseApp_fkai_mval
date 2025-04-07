class Subject():
    def __init__(self, first_name, last, sex, age):
      self.first_name = first_name
      self.last_name = last
      self.sex = sex
      self.age = age

    def estimate_max_hr(self):
      """A function that estimates the maximum heart rate of a subject"""
      pass

class Supervisor():
    def __init__(self, first_name, last_name):
      self.first_name = first_name
      self.last_name = last_name

class Experiment():
    def __init__(self, name, date):
      self.name = name
      self.date = date

    def add_subject(self, subject):
      self.subject = subject

    def add_supervisor(self, supervisor):
      self.supervisor = supervisor

