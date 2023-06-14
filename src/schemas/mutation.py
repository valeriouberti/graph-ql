import strawberry

from resolvers.person_resolver import add_person

from scalars.person_scalar import AddPerson


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def add_person(self, name: str, age: int) -> AddPerson:
        """ Add sticky note """
        person = await add_person(name, age)
        return person
