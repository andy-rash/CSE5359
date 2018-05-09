from .db_utils import session_manager
from .models import Listing        
from tabulate import tabulate

class AddressBook(object):

#    def __init__(self):
#        self.__validator = Validator()

    def add(self, name: str, phone_number: str):
        with session_manager() as session:
            session.add(
                Listing(
                    name=name,
                    country_code=1,
                    phone_number=int(phone_number)
                )
            )

    def delete_person(self, name: str):
        with session_manager() as session:
            session.query(
                Listing
            ).filter(
                Listing.name == name
            ).delete()

    def delete_number(self, phone_number: str):
        with session_manager() as session:
            session.query(
                Listing
            ).filter(
                Listing.phone_number == phone_number
            ).delete()

    def list(self):
        with session_manager() as session:
            entries = session.query(
                Listing
            ).all()

            headers = ['Name', 'Phone Number']
            data = [[x.name, x.phone_number] for x in entries]
            print(tabulate(data, headers=headers, tablefmt='grid'))

