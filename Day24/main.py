from dataclasses import dataclass
from typing import Optional
#Basic data class with default values

'''@dataclass()
class person:
    name: str
    age: int = 30

p = person ("Surya")
print(p)'''

@dataclass()
class Car:
    name: str
    year: Optional[int] = None

p = Car ("Honda", 1999)
print(f"The car brand {p.name} was launched on the year {p.year}")