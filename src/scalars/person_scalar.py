import strawberry


@strawberry.type
class Person:
    id: int
    name: str
    age: int


@strawberry.type
class AddPerson:
    message: str = "Person Added"
