from typing import List

import strawberry

from resolvers.person_resolver import get_person, get_people
from scalars.person_scalar import Person


@strawberry.type
class Query:

    @strawberry.field
    async def people(self) -> List[Person]:
        """ Get all people """
        people_data_list = await get_people()
        return people_data_list

    @strawberry.field
    async def person(self, id: int) -> Person:
        """ Get user by id """
        person_dict = await get_person(id)
        return person_dict
