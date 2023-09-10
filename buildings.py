import json
from faker import Faker
from random import randint

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}"
class Building:
    def __init__(self):
        self.residents = []
    def load_residents(self):
        people = Faker()
        app_members = randint(1,5)
        my_list = []
        for i in range(app_members):
            my_list.append(Person(name= people.first_name(), surname= people.last_name(), age= randint(18,72)))
        self.residents.append({f"Apartment {len(self.residents) + 1}": my_list})

    def residents_dict(self):
        for _ in range(30):
            self.load_residents()
        residents_dict = {}
        for index, person in enumerate(self.residents):
            for key, value in person.items():
                residents_dict[f"Apartment {index + 1}"] = [j.__dict__ for j in value]
        return residents_dict
    def add_resident(self, person, app_number):
        if isinstance(person, Person):
            for i in self.residents:
                for key, value in i.items():
                    if key == f"Apartment {app_number}" and len(value) < 5:
                        value.append(person)
                        print("Fine. The new resident arrived.")
                        return
        print("Please check inputs or maybe the apartment limit is reached.")
    def remove_resident(self, name, surname):
        for i in self.residents:
            for key, value in i.items():
                for j in value:
                    if name == j.name and surname == j.surname:
                        value.remove(j)
                        print("Done. That person left us.")
                        return
        print("Cant find that person. He is not our resident or you typed something wrong.")

    def save_to_json(self):
        with open('persons.json', 'w') as data:
            json.dump(self.residents_dict(), data, indent=2)

    def load_from_json(self):
        try:
            with open('persons.json') as data:
                persons = json.load(data)
            return persons
        except FileNotFoundError:
            print("File does not exist.")

    def message_handling(self):
        while True:
            user_input = input(":::: - > ")
            if user_input == "Information":
                print(self)
            elif user_input == "Info":
                try:
                    user_input2 = int(input("Write number of the apartment : "))
                    print("Okay. Here's the info.")
                    for i in self.residents:
                        for key, value in i.items():
                            if key == f"Apartment {user_input2}":
                                for person in value:
                                    print(person.__str__())
                except ValueError:
                    print("You need to input number.")
            elif user_input == "Add":
                name_input = input("Write the name.")
                surname_input = input("Write the surname.")
                try:
                    age_input = int(input("Write the age."))
                    app_number = int(input("Write apartment number where you need to settle."))
                    person = Person(name=name_input, surname=surname_input, age=age_input)
                    self.add_resident(person=person, app_number=app_number)
                    self.save_to_json()
                except ValueError:
                    print("Check all inputs and try again.")
            elif user_input == "Remove":
                name_input = input("Write the name.")
                surname_input = input("Write the surname.")
                try:
                    self.remove_resident(name=name_input, surname=surname_input)
                    self.save_to_json()
                except ValueError:
                    print("Check all inputs and try again.")
            elif user_input == "Stop":
                exit()
            else:
                print("Check all inputs and try again.")
    def greetings(self):
        print("Hello! My name is Sarah, I'm manager of your building.\n"
              "It seems like the building is ready for usage. It's empty now. The building have 30 apartments.\n"
              "During the last month 30 families bought an apartment in your building.\n"
              "Everything is ready. We're waiting for your command to settle residents. Do you want to start?\n"
              "[type 'Yes' to start settling residents]")
        user_input1 = input()
        if user_input1 == 'Yes':
            with open('persons.json', 'w') as data:
                json.dump(self.residents_dict(), data, indent=2)
            print("Okay. I sent you a json file with all residents. \n"
                  "If you want to view all information about your building habitants say 'Information'\n"
                  "If you want to view information about only 1 appartment say 'Info' \n"
                  "If you want to add resident say 'Add' \n"
                  "If you want to remove resident say 'Remove'\n"
                  "And finally if you want to exit say 'Stop'")
            self.message_handling()

    def __str__(self):
        result = ""
        for i in self.residents:
            for key, value in i.items():
                result += f"{key} : "
            for j in value:
                result += f"{j.__str__()} \n"
        return result
def main():
    building = Building()
    building.greetings()

if __name__ == '__main__':
    main()
