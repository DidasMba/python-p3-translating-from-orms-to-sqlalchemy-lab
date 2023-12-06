#from models import Dog


from models import Dog


def create_table():
    Dog.metadata.create_all(session.bind)

def save(obj):
    session.add(obj)
    session.commit()

def get_dogs():
    return session.query(Dog).all()

# Implement other functions in a similar way
