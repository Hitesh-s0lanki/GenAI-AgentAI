from pydantic import BaseModel
from typing import Optional

class Person(BaseModel):
    name:str
    age:int
    city:str
    salary: Optional[float] = None

person = Person(name="Hitesh", age=21, city="Mumbai")
print(person)


