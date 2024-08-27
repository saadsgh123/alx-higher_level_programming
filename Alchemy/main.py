from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    from sqlalchemy import create_engine, MetaData, text
    from User import User, Base

    metadata = MetaData()
    engine = create_engine("mysql+mysqldb://root:anasaad@localhost/dt_db")
    Base.metadata.reflect(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_user = User(username="saad")
    session.add(new_user)
    session.commit()
