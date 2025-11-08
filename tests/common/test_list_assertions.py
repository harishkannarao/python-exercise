import dataclasses
from types import MappingProxyType

from assertpy import assert_that


@dataclasses.dataclass(frozen=True)
class Person:
    name: str
    id: int
    skills: frozenset[str] = frozenset()
    alias: tuple[str, ...] = ()
    meta_info: MappingProxyType[str, str] = dataclasses.field(default_factory= lambda: {})


def test_list_assert_on_objects():
    person1: Person = Person(
        name="Foo",
        id=1,
        skills=frozenset(["java", "python"]),
        alias=(*["fierce_programmer"],),
        meta_info=MappingProxyType({"graduation": "university"})
    )
    person2: Person = Person(
        name="Bar",
        id=2
    )
    list_of_persons: tuple[Person, ...] = (person1, person2)

    filtered_persons = tuple(filter(lambda person: person.id == 1, list_of_persons))

    (assert_that(filtered_persons)
     .contains_only(person1))
