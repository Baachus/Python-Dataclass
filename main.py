import random, string
from dataclasses import dataclass, field

def generate_id()->str:
    return "".join(random.choices(string.ascii_uppercase, k=12))

#match_args and kw_only added with python 3.10
@dataclass(frozen=False)    #if frozen is true class is const.
class Person:
    name: str
    address: str
    active: bool=True   #default value
    email_addresses: list[str] = field(default_factory=list)    #sets default list
    id: str = field(init=False, default_factory=generate_id)    #sets default id with generated id method above
    _search_string: str = field(init=False, repr=False)         #sets default search string and its private with repr

    def __post_init__(self)->None:      #post initialization method to generate data on _search_string
        self._search_string = f"{self.name} {self.address}"

def main()->None:
    person = Person(name="John", address="123 Fake Street")     #initialize class
    print(person)       #prints data

if __name__ == "__main__":
    main()