import re

'''
Names
-------------

Names vary significantly. They can take all kinds of forms and shapes
depending on the origin. It would be a near insurmountable task to truly
validate a name, so a more considerate approach would be to simply blacklist
certain characters that are likely to never appear in a name. Of course, there
are certainly exceptions to this, but those are exceedingly rare edge cases.

Some punctuation exclusions from the blacklist include, but are not limited to
characters in the range [.,"-'], which are all used fairly commonly in names,
notably the " character, which is often used to denote nicknames.

'''
NAME_REGEX = re.compile(
	r'^[^\0\r\n\t!@#$%^&*_+=(){}\[\]<>\\|;:\/?]+$'
)


'''
Phone numbers
--------------

The NANP regular expression was largely derived from a Stack Overflow response
here:
    https://stackoverflow.com/a/123666

It accepts only 10 digit phone numbers but allows variable formatting styles.
Accepted delimiters include [().-] as well as whitespace.

Extensions are not handled by this regular expression, as it is technically a
separate instruction once the actual phone number has connected.

'''
NANP_REGEX = re.compile(
	r'^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})$'
	r'^'
	r''
	r'$'
	)

E164_REGEX = re.compile(r'^\+?\s*(1|20|210|211|212|213|214|215|216|217|218|219|220|221|222|223|224|225|226|227|228|229|230|231|232|233|234|235|236|237|238|239|240|241|242|243|244|245|246|247|248|249|250|251|252|253|254|255|256|257|258|259|260|261|262|263|264|265|266|267|268|269|27|28|290|291|292|293|294|295|296|297|298|299|30|31|32|33|34|350|351|352|353|354|355|356|357|358|359|36|370|371|372|373|374|375|376|377|378|379|380|381|382|383|384|385|386|387|388|389|39|40|41|420|421|422|423|424|425|426|427|428|429|43|44|45|46|47|48|49|500|501|502|503|504|505|506|507|508|509|51|52|53|54|55|56|57|58|590|591|592|593|594|595|596|597|598|599|60|61|62|63|64|65|66|670|671|672|673|674|675|676|677|678|679|680|681|682|683|684|685|686|687|688|689|690|691|692|693|694|695|696|697|698|699|7|800|801|802|803|804|805|806|807|808|809|81|82|83|84|850|851|852|853|854|855|856|857|858|859|86|870|871|872|873|874|875|876|877|878|879|880|881|882|883|884|885|886|887|888|889|89|90|91|92|93|94|95|960|961|962|963|964|965|966|967|968|969|970|971|972|973|974|975|976|977|978|979|98|990|991|992|993|994|995|996|997|998|999)\s*(\d{1,14})$')
