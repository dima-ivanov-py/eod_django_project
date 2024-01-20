import pytest

from entities.utilities.injector import Injector, inject


class Person:
    def __init__(
        self,
        age: int,
        name: str,
    ) -> None:
        self.name = name
        self.age = age


class PersonService:
    @inject
    def __init__(
        self,
        person: Person,
    ) -> None:
        self._person = person


class HrService:
    @inject
    def __init__(
        self,
        person_service: PersonService,
        person: Person,
    ) -> None:
        self._person = person
        self._person_service = person_service


class CompanyService:
    @inject
    def __init__(
        self,
        person_service: PersonService,
        person: Person,
        hr_service: HrService,
    ) -> None:
        self._person_service = person_service
        self._person = person
        self._hr_service = hr_service


class TestInjectorService:
    @pytest.fixture(autouse=True)
    def clean_injector_class_kwargs(self):
        Injector.type_kwargs = {}

    def test_1(self):
        Injector.register(Person, name="Eric", age=13)

        person = Injector.get_instance(Person)

        assert person.name == "Eric"
        assert person.age == 13

    def test_2(self):
        Injector.register(Person, name="Bill", age=21)

        person_service = PersonService()

        person = person_service._person
        assert person.name == "Bill"
        assert person.age == 21

    def test_3(self):
        Injector.register(Person, name="Bill", age=21)
        Injector.register(PersonService, person="SomePerson")

        person_service = PersonService()

        person = person_service._person
        assert person == "SomePerson"

    def test_4(self):
        Injector.register(Person, name="Richard", age=41)

        hr_service = HrService()

        person_service = hr_service._person_service
        hr_service_person = hr_service._person
        person_service_person = person_service._person
        assert hr_service_person.name == "Richard"
        assert hr_service_person.age == 41
        assert person_service_person.name == "Richard"
        assert person_service_person.age == 41

    def test_5(self):
        Injector.register(Person, name="Richard", age=41)

        hr_service = HrService(person=Person(name="Ron", age=33))

        person_service = hr_service._person_service
        hr_service_person = hr_service._person
        person_service_person = person_service._person
        assert person_service_person.name == "Richard"
        assert person_service_person.age == 41
        assert hr_service_person.name == "Ron"
        assert hr_service_person.age == 33

    def test_6(self):
        Injector.register(Person, name="Nancy", age=51)
        Injector.register(PersonService, person="SomePerson")
        Injector.register(
            HrService,
            person_service=PersonService(),
            person=Person(name="Morris", age=63),
        )
        Injector.register(
            CompanyService,
            person=Person(name="Edvard", age=5),
            person_service=PersonService(person=Person(name="Igor", age=9)),
            hr_service=HrService(),
        )

        person = Injector.get_instance(Person)
        person_service = PersonService()
        hr_service = HrService()
        company_service = CompanyService()

        assert person.name == "Nancy"
        assert person.age == 51
        assert person_service._person == "SomePerson"
        assert hr_service._person_service._person == "SomePerson"
        assert hr_service._person.name == "Morris"
        assert hr_service._person.age == 63
        assert company_service._person_service._person.name == "Igor"
        assert company_service._person_service._person.age == 9

    def test_7(self):
        Injector.register(PersonService, person="SomePerson")

        person_service = PersonService(person=Person(name="Igor", age=9))

        assert person_service._person.name == "Igor"
        assert person_service._person.age == 9

    def test_8(self):
        Injector.register(PersonService, person="SomePerson")

        person_service = PersonService()

        assert person_service._person == "SomePerson"

    def test_9(self):
        Injector.register(Person, name="Mary", age=35)

        person_service = PersonService()
        hr_service = HrService(person=Person(name="John", age=25))

        assert person_service._person.name == "Mary"
        assert person_service._person.age == 35
        assert hr_service._person_service._person.name == "Mary"
        assert hr_service._person_service._person.age == 35
        assert hr_service._person.name == "John"
        assert hr_service._person.age == 25

    def test_10(self):
        Injector.register(PersonService, person=Person(name="Ursula", age=45))

        person_service = PersonService()
        hr_service = HrService(
            person_service=PersonService(person=Person(name="Amanda", age=55)),
            person=Person(name="Cindy", age=65),
        )

        assert person_service._person.name == "Ursula"
        assert person_service._person.age == 45
        assert hr_service._person_service._person.name == "Amanda"
        assert hr_service._person_service._person.age == 55
        assert hr_service._person.name == "Cindy"
        assert hr_service._person.age == 65

    def test_11(self):
        Injector.register(Person, name="Mary", age=35)
        Injector.register(PersonService, person=Person(name="Ursula", age=45))

        person_service = PersonService()
        hr_service = HrService(
            person_service=PersonService(person=Person(name="Amanda", age=55)),
        )

        assert person_service._person.name == "Ursula"
        assert person_service._person.age == 45
        assert hr_service._person_service._person.name == "Amanda"
        assert hr_service._person_service._person.age == 55
        assert hr_service._person.name == "Mary"
        assert hr_service._person.age == 35

    def test_12(self):
        class Hubspot3:
            def __init__(self, api_key: str, secret_number: int) -> None:
                self._api_key = api_key
                self._secret_number = secret_number

        class HubspotClient(Hubspot3):
            @inject
            def __init__(self, *args, **kwargs) -> None:
                super().__init__(*args, **kwargs)

        Injector.register(HubspotClient, api_key="U3KS", secret_number=35)

        hubspot_client = HubspotClient()

        assert hubspot_client._api_key == "U3KS"
        assert hubspot_client._secret_number == 35
