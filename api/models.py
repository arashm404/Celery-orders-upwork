from sqlalchemy import Column, Integer, String, create_engine , BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for SQLAlchemy models
Base = declarative_base()

# Define the MyPizza model
class MyPizza(Base):
    __tablename__ = "myPizzas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    total_used = Column(Integer)
    not_usable_till = Column(Integer)
    last_used = Column(BigInteger)
    
class OrdersList(Base):
    __tablename__ = "myOrdersList"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, index=True)
    quantity = Column(Integer)

# Database configuration

#DATABASE_URL = "postgresql://postgres:password@postgres:5432/postgres"
DATABASE_URL = "postgresql://username:password@db:5432/testdb"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the tables in the database
Base.metadata.create_all(bind=engine)
