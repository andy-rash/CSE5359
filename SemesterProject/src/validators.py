import re
import sys
from enum import Enum
from .regular_expressions import (
	E164_REGEX,
	NAME_REGEX,
	NANP_REGEX
)

class Validator(object):

	def name(self, name: str) -> str:
		'''
			Validates a name.

			Returns the provided string if validation passes.
			Raises a ValidationError if validation fails.
		'''

		match = NAME_REGEX.match(name)
		if match is not None:
			return match[0]
		else:
			sys.exit(
				'Provided name could not be validated.\nEnsure that the input does not contain any of: \0\r\n\t?!@#$%^&*_+=(){}[]<>|;:\/'
			)

	def normalize_phone_number(self, phone_number: str) -> str:
		'''
			Allows the phone number input to be fairly permissive in what is
			allowed as input without sacrificing proper validation.
		'''
		return re.sub(r'[^\d+]', '', phone_number)

	def phone_number(self, phone_number: str) -> (str):
		'''
			Validates a phone number.

			Returns a dictionary containing

			Raises a ValidationError if validation fails.
		'''

		normalized = self.normalize_phone_number(phone_number)

		nanp = NANP_REGEX.match(normalized)
		if nanp is not None:
			return ('NANP', '1'+nanp[1]+nanp[2]+nanp[3])
		else:
			e164 = E164_REGEX.match(normalized)
			if e164 is not None:
				return ('E164', e164[1]+e164[2])

		sys.exit(
			'Provided phone number could not be validated.\nTry entering the number in the form `XXX-XXX-XXXX` (North America) or `+XXXXXXXXXXXXXXX` (international).'
		)
