import sys
from .db_utils import session_manager
from .models import Listing
from sqlalchemy import or_
from tabulate import tabulate
from .validators import Validator

class AddressBook(object):

	def __init__(self):
		self.__validator = Validator()

	def add(self, name: str, phone_number: str):

		name = self.__validator.name(name)
		phone_number = self.__validator.phone_number(phone_number)

		with session_manager() as session:

			# check if data already exists in database;
			# fail gracefully if it does
			result = session.query(
				Listing
			).filter(
				or_(
					Listing.name == name,
					Listing.phone_number == phone_number[1]
				)
			).one_or_none()

			if result is not None:
				sys.exit('Entry already exists in database.')

			# insert into database
			new_listing = Listing(
				name=name,
				number_plan=phone_number[0],
				phone_number=phone_number[1]
			)

			session.add(new_listing)
			print(f'Successfully added {new_listing}')

	def delete_person(self, name: str):

		name = self.__validator.name(name)

		with session_manager() as session:
			session.query(
				Listing
			).filter(
				Listing.name == name
			).delete()

			print(f'Successfully deleted entry with name: {name}')

	def delete_number(self, phone_number: str):

		phone_number = self.__validator.phone_number(phone_number)

		with session_manager() as session:
			session.query(
				Listing
			).filter(
				Listing.phone_number == phone_number[1]
			).delete()

			print(f'Successfully deleted entry with phone number: +{phone_number[1]}')

	def list(self):
		with session_manager() as session:
			entries = session.query(
				Listing
			).all()

			headers = ['Name', 'Phone Number']
			data = [[x.name, f'+{x.phone_number}'] for x in entries]
			print(tabulate(data, headers=headers, tablefmt='grid'))
