from my_classes import Person
from my_classes import Subject

if __name__ == "__main__":
    
   def test_workflow():
    
       person = Person(first_name="Max")
       person.put()

    
       subject = Subject(first_name="Max", email="max.mustermann@mci4me.at")
       subject.update_email(new_email="maxmustermann.new@mci4me.at")

