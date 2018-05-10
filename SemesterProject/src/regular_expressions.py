import re

E164_REGEX = re.compile(
	r'^(?:\+{1})(20|210|211|212|213|214|215|216|217|218|219|220|221|222|223|224|225|226|227|228|229|230|231|232|233|234|235|236|237|238|239|240|241|242|243|244|245|246|247|248|249|250|251|252|253|254|255|256|257|258|259|260|261|262|263|264|265|266|267|268|269|27|28|290|291|292|293|294|295|296|297|298|299|30|31|32|33|34|350|351|352|353|354|355|356|357|358|359|36|370|371|372|373|374|375|376|377|378|379|380|381|382|383|384|385|386|387|388|389|39|40|41|420|421|422|423|424|425|426|427|428|429|43|44|45|46|47|48|49|500|501|502|503|504|505|506|507|508|509|51|52|53|54|55|56|57|58|590|591|592|593|594|595|596|597|598|599|60|61|62|63|64|65|66|670|671|672|673|674|675|676|677|678|679|680|681|682|683|684|685|686|687|688|689|690|691|692|693|694|695|696|697|698|699|7|800|801|802|803|804|805|806|807|808|809|81|82|83|84|850|851|852|853|854|855|856|857|858|859|86|870|871|872|873|874|875|876|877|878|879|880|881|882|883|884|885|886|887|888|889|89|90|91|92|93|94|95|960|961|962|963|964|965|966|967|968|969|970|971|972|973|974|975|976|977|978|979|98|990|991|992|993|994|995|996|997|998|999)(\d{4,14})$'
)

NAME_REGEX = re.compile(
	r'^[^\0\r\n\t!@#$%^&*_+=(){}\[\]<>\\|;:\/?]+$'
)

NANP_REGEX = re.compile(
	r'^(?:\+?1)?([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})([0-9]{4})$'
)

NORMALIZE_REGEX = re.compile(
	r'[^\d+]'
)
