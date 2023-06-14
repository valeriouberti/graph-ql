from sqlalchemy import select, insert

from db.db import get_session
from models import person_model

from scalars.person_scalar import AddPerson, Person


async def get_people():
    """ Get all person resolver """
    async with get_session() as s:
        sql = select(person_model.Person).order_by(person_model.Person.age)
        db_people = (await s.execute(sql)).scalars().unique().all()
    people_list = []
    for person in db_people:
        person_dict = get_valid_data(person, person_model.Person)
        people_list.append(Person(**person_dict))
    return people_list


async def get_person(id):
    """ Get specific person by id resolver """
    async with get_session() as s:
        sql = select(person_model.Person).filter(person_model.Person.id == id).order_by(person_model.Person.age)
        db_person = (await s.execute(sql)).scalars().unique().one()

    person_dict = get_valid_data(db_person, person_model.Person)
    return Person(**person_dict)


async def add_person(name: str, age: int):
    """ Add Person resolver """
    async with get_session() as s:
        query = insert(person_model.Person).values(name=name, age=age)
        await s.execute(query)
        await s.commit()
    return AddPerson()


def get_valid_data(model_data_object, model_class):
    data_dict = {}
    for column in model_class.__table__.columns:
        try:
            data_dict[column.name] = getattr(model_data_object, column.name)
        except:
            pass
    return data_dict
