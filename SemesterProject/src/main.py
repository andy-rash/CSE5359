from db_utils import session_manager
from models import Listing        

with session_manager() as session:
    listing = Listing(name='Bill Wurtz', phone_number='420 696 9696')

    session.add(listing)

