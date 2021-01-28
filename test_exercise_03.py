import pytest
from exercise_03 import Person


def test_date_of_birth_is_correct_dynamically_counted():
    person = Person("John", "Doe", "19230916249")
    assert person.date_of_birth == (9, 3, 2019)


def test_incorrect_pesel_is_raised_exception():
    with pytest.raises(ValueError):
        Person("John", "Doe", "12345678912")


        
