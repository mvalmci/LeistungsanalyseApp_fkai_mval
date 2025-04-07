from my_classes import Subject, Supervisor, Experiment
from datetime import datetime

if __name__ == "__main__":

    # Erstellen eines Leistungstests
    supervisor = Supervisor("FirstName", "LastName")
    subject = Subject("FirstName", "LastName", "female", 30)
    subject.estimate_max_hr()

    experiment = Experiment("Leistungstest", datetime.now())
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)

    print(experiment.name)
    print(experiment.date)
    print('Subject:')
    print(experiment.subject.first_name)
    print(experiment.subject.last_name)
    print('Supervisor:')
    print(experiment.supervisor.first_name)
    print(experiment.supervisor.last_name)
    print('Maximal Herzfrequenz:')
    print(subject.estimate_max_hr())

    