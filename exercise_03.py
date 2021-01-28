class Person:
    def __init__(self, first_name, last_name, pesel):
        if len(pesel) != 11 or not pesel.isdigit():
            raise ValueError("Incorrect PESEL number")
        control_number = sum([int(number)*weight % 10 for number, weight in
                              list(zip(pesel, [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]))]) % 10
        if 10 - control_number != int(pesel[-1]):
            raise ValueError("Incorrect PESEL number")
        self.name = first_name
        self.last_name = last_name
        self.pesel = pesel

    @property
    def date_of_birth(self):
        day = int(self.pesel[4:6])
        month = int(self.pesel[2:4])
        year = int(self.pesel[:2])
        year += {0: 1900, 1: 2000, 2: 2100, 3: 2200, 4: 1800}[month // 20]
        month = month % 20
        return day, month, year


if __name__ == "__main__":
    try:
        person = Person("John", "Doe", "95832708202")
        print(person.date_of_birth)
    except ValueError:
        print('Incorrect pesel')
