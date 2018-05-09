import re
from enum import Enum
from .regular_expressions import (
	E164_REGEX,
	NAME_REGEX,
	NANP_REGEX
)

class ValidatorType(Enum):
	name = 1
	phone_number = 2

	@classmethod
	def has_value(cls, value):
		return value in cls.__members__

class Validator(object):

	def name(self, name: str) -> bool:
		pass

	def normalize_phone_number(self, phone_number: str) -> str:
		return re.sub(r'[^\d+]', '', phone_number)

	def phone_number(self, phone_number: str) -> bool:
		pass
