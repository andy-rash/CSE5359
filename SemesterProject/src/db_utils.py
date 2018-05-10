from contextlib import contextmanager
from .models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database configuration
sqlite_file_name = 'address_book.db'
sqlite_file_path = f'./data/{sqlite_file_name}'

engine = create_engine(f'sqlite:///{sqlite_file_path}')
Session = sessionmaker(bind=engine)

# create tables, if they don't already exist
Base.metadata.create_all(bind=engine, checkfirst=True)

@contextmanager
def session_manager():
	'''
	Provides a transactional scope around database operations.

	This has been adapted from the SQLAlchemy Documentation here:
	http://docs.sqlalchemy.org/en/latest/orm/session_basics.html

	'''

	session = Session()
	try:
		yield session
		session.commit()
	except:
		session.rollback()
		raise
	else:
		session.commit()
	finally:
		session.close()

