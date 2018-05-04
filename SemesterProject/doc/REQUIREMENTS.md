# Acceptable Name and Phone Number Format Standards

When it comes to names and telephone numbers, there are myriad forms that each can take. This fact has been a constant struggle for programmers for ages, both from a functional perspective and a security perspective. For this assignment, it would be impractical to attempt to come up with a "silver bullet" solution to this problem. A better approach would be to devise a narrow range of acceptable forms for each of these categories. So, for this assignment, the acceptable 

## Names

WIP

## Phone Numbers

Acceptable phone number formats will follow 

* (1) the standards set forth by the [North American Numbering Plan (NANP)](https://en.wikipedia.org/wiki/North_American_Numbering_Plan) for numbers inside this jurisdiction and
* (2) the standards set forth in [ITU E.164](https://www.itu.int/rec/T-REC-E.164-201011-I/en) for numbers outside of the NANP jurisdiction. 

This will allow for much versatility in terms of accepting NANP phone numbers while also allowing the possibility of accepting non-NANP phone numbers, albeit with reduced flexibility for those outside phone numbers.

### North American Numbering Plan (NANP)

The North American Numbering Plan includes 25 regions in twenty countries in North America, including the United States and its territories, Canada, and a significant portion of the Caribbean.

A proper NANP phone number consists of these sections:

```
+1			(optional) NANP international calling code

1			(optional) domestic use only, and never in
			combination with the previous section;
			part of a change made to increase the pool of
			numbers in a given area code

XXX			area code -- ranges: [2-9] for first digit,
			[0-8] for the middle digit, and [0-9] for
			the final digit *
			
XXX			central office code -- ranges: [2-9] for
			first digit, [0-9] for next two digits **

XXXX		subscriber code -- ranges: [0-9] for all
			four digits

```
\* when the last two digits are the same (i.e. NXX where X is in [0-8]), this code is known as an easily recognizable code (ERC), which are used to designate special services (e.g. 888 for toll-free service)

\** the last two digits may not be the same if they are both '1'

Acceptable Examples:

```
# valid 7-digit
2355678
235-5678
235 5678
235.5678

# valid 7-digit w/ extension
2355678x4321
235-5678 extension 4321
235 5678 ext4321
235.5678#   4321

# valid 10-digit
2342355678
234-235-5678
234 235-5678
(234) 235-5678
234 235 5678
234.235.5678

# valid 10-digit w/ extension
# valid 10-digit
2342355678x4321
234-235-5678 extension 4321
234 235-5678 ext4321
(234) 235-5678# 4321
234 235 5678      x 9
234.235.5678					extension 5900000

# valid w/ international code, w/o '+'
12342355678
1 234-235-5678
1 234 235-5678
1 (234) 235-5678
1 234 235 5678
1 234.235.5678

# valid w/ international code, w/ '+'
+12342355678
+1 234-235-5678
+1 234 235-5678
+1 (234) 235-5678
+1 234 235 5678
+1 234.235.5678
```

Unacceptable Examples:

```
# invalid -- area code must start with [2-9]
123-234-5678

# invalid -- office code (two trailing numbers == '1')
234-911-5678

# invalid -- office code (starts with '1')
314-159-2653
```

It should be noted that by no means are the above lists of examples exhaustive. There are so many possible test cases that it would be difficult to create an exhaustive list.

### ITU E.164

### Limitations

The guidelines described above provide a great starting place to filter input through regular expressions, and regular expressions will indeed be the initial approach to validating input. However, this approach introduces a limitation in the form of accepting phone numbers that, while they may pass muster relative to the guidelines, may not be actual phone numbers (e.g. a NANP phone number using a valid area code that has yet to be implemented). To be able to handle these edge cases would be an undertaking in its own right, so, for the scope of this project, these cases will not be handled.