from my_classes import Supervisor, Subject, Experiment
from datetime import datetime

if __name__ == "__main__":
    # Erstellen eines Leistungstests
    supervisor = Supervisor("Marius", "Valenta", "2005-05-22")
    subject = Subject("Max", "Mustermann", "2000-03-22", "male", "max.mustermann@mci4me.at")
    

    experiment = Experiment("Leistungstest", datetime.now().date())
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)

    print(experiment)
    print(f"Versuchsleiter: {supervisor.first_name} {supervisor.last_name}")
    print(f"Estimatet max HR der Versuchsperson: {subject.estimate_max_hr()}")