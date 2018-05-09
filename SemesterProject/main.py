import argparse
import sys
from src.address_book import AddressBook

parser = argparse.ArgumentParser(
    description='Address book listing program.',
    prog='address_book'
)

# ensure that only one of each command is run at a given time
# with a mutually exclusive group
group = parser.add_mutually_exclusive_group(required=True)

# ADD command
group.add_argument(
    '-a', '--add',
    help=
    '''
    Add an entry to the address book.
    ''',
    nargs=2,
    metavar=('"<person>"','"<phone number>"')
)

# DELETE <person> command
group.add_argument(
    '-dp', '--delete-person',
    help=
    '''
    Delete an entry from the address book by a person's name.
    ''',
    metavar='"<person>"'
)

# DELETE <phone number> command
group.add_argument(
    '-dn', '--delete-number',
    help=
    '''
    Delete an entry from the address book by a person's phone number.
    ''',
    metavar='"<phone number>"'
)

# LIST command
group.add_argument(
    '-l', '--list',
    help=
    '''
    List the entries in the address book.
    ''',
    action='store_true'
)

args = vars(parser.parse_args())

if __name__ == '__main__':

    address_book = AddressBook()
    
    if args['add'] is not None:
        address_book.add(*args['add'])
        sys.exit(0)

    elif args['delete_person'] is not None:
        address_book.delete_person(args['delete_person'])
        sys.exit(0)

    elif args['delete_number'] is not None:
        address_book.delete_number(args['delete_number'])
        sys.exit(0)

    elif args['list'] is not False:
        address_book.list()
        sys.exit(0)

    else:

        # execution will likely never reach this, but it's nice to
        # have a default
        raise ValueError









