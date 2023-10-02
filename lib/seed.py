from faker import Faker

import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Customer, Reviews

if __name__ == "__main__":
    engine = create_engine('sqlite:///one_to_many.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Customer).delete()
    session.query(Reviews).delete()

    fake = Faker()

    names = [
        Customer(
            first_name = fake.first_name(),
            last_name = fake.last_name()
        )
        for i in range(50)
    ]

    reviews = [
        Reviews(
            score=random.randint(1,10),
            comment=fake.sentence(),
            customer_id=random.randint(1,50),
        )
        for i in range(50)
    ]

    session.bulk_save_objects(reviews)
    session.bulk_save_objects(names)
    session.commit()
    session.close()