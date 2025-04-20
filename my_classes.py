from datetime import date
import requests
from requests import request
import json

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
    
    def put(self,id,first_name, last_name,birth_year):
        self.id = id
        self.first_name = first_name
        self.__birth_year = birth_year

        url = f"http://127.0.0.1:5000/person/123"

        data = {
            "id": id,
            "first_name": first_name,
            "birth_year": birth_year
        }

        #daten in JSON umwandeln
        data_json = json.dumps(data)

        #POST request an die URL senden
        response = request.put(url, data=data_json)

        #Antwort ausgeben
        print(response.text)

class Subject(Person):
    def __init__(self, first_name, last_name, birth_date, sex, email):
        self.email = email
        super().__init__(first_name, last_name, birth_date)
        self.sex = sex

    def estimate_max_hr(self):
        age = self.calculate_age()
        if self.sex.lower() == "female":
            max_hr = 226 - age
        else:
            max_hr = 220 - age
        return max_hr
    
    
    def update_email(self, new_email):
        self.email = new_email
        url = f"http://127.0.0.1:5000/person/123"
        data = {
            "email": new_email
        }
        #daten in JSON umwandeln
        data_json = json.dumps(data)

        #POST request an die URL senden
        response = request.put(url, json=data)



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