from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def new_from_db(session):
    pass

def get_all(session):
    query=session.query(Dog).all()
    return query

def find_by_name(session, name):
    query=session.query(Dog).filter(Dog.name==name).first()
    return query

def find_by_id(session, id):
    query=session.query(Dog).filter(Dog.id==id).first()
    return query

def find_by_name_and_breed(session, name, breed):
    query=session.query(Dog).filter(Dog.name==name, Dog.breed==breed).first()
    return query

def update_breed(session, dog, breed):
    return session.query(Dog).update({Dog.breed:breed})