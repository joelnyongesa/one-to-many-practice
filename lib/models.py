from sqlalchemy.orm import declarative_base, sessionmaker, relationship, backref
from sqlalchemy import ForeignKey, Integer, String, Column, MetaData

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Customer(Base):
    __tablename__ = "games"

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name =  Column(String())

    # relationships
    reviews = relationship("Reviews", backref=backref("game"))

    def __repr__(self):
        return f"Customer(id={self.id}), "+\
            f"name={self.first_name} {self.last_name}"


class Reviews(Base):
    __tablename__ = "reviews"

    id = Column(Integer(), primary_key=True)
    score = Column(Integer())
    comment = Column(String())
    customer_id = Column(Integer(), ForeignKey('games.id'))

    def __repr__(self):
        return f"Review(id={self.id}), "+\
            f"score={self.score}, "+\
            f"customer_id = {self.customer_id}"
