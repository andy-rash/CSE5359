Robert Rash

Professor Estes

CSE 5359

10 May 2018





## `index.php`

* line 13 -- comment containing site authentication credentials

```php
<!--Attn Developers: Username: test Password: 1234  please remove when development is complete-->
```

## `form.php`

* line 2 -- XSS vulnerability; variable `$blog` gets evaluated as code; not extremely likely since this variable has not been declared anywhere else beforehand

```php
echo "<p>".stripslashes($blog)."</p><br />";
```

## `submit.php`

* line 4 -- sets `user:` cookie without authentication

```php
<?php
$user = $_POST['user'];
$pass = $_POST['pass'];
setcookie("user:", $user);
```

* line 5 -- hardcoded MySQL credentials in public source code

```php
$connect = mysql_connect("localhost", "ghost", "ghost");
```

* line 21 -- potential XSS, though unlikely to happen unless a user gets created that happens to match the format needed for the XSS input

```php
echo "<input type='hidden' value='".$user."' />";
```

* line 28 -- definite, tested XSS vulnerability in `username` input

```php
echo "<div>".stripslashes($user)."</div><br />";
```

## `blog.php`

Contains variable content based on value of `user:` cookie.

Potential new vulnerabilities:

* line 2 -- checks for authentication based on `user:` cookie, but this cookie is not authenticated (anybody can put anything in here)

```php
<?php
$user = $_COOKIE['user:'];
```

* line 16 -- potential XSS, though unlikely to happen unless some of the logic gets changed around (`$user` variable would have to equal `admin` AND a script to be actual XSS vuln.)

```php
else if($user == "admin")
{

...

echo "<input type='hidden' name='user' value='".$user."' />";
```

* line 28 -- potential XSS, though unlikely to happen unless some of the logic gets changed around (`$user` variable would have to equal `test` AND a script to be actual XSS vuln.)

```php
else if($user == "test")
{

...

echo "<input type='hidden' name='user' value='".$user."' />";
```

* line 37 -- potential XSS, though unlikely to happen unless some of the logic gets changed around (`$user` variable would have to equal `anonymous` AND a script to be actual XSS vuln.)

```php
else if($user == "anonymous")
{

...

echo "<input type='hidden' name='user' value='".$user."' />";
```

* line 40 -- potential XSS, though unlikely to happen unless some of the logic gets changed around (`$user` variable would have to equal `anonymous` AND a script to be actual XSS vuln.)

```php
else if($user == "anonymous")
{

...

echo "<input type='hidden' name='user' value='".$user."' />";
```

## `blogSub.php`

* line 3 -- hardcoded MySQL credentials in public source code

```php
$connect = mysql_connect("localhost", "ghost", "ghost");
```

* line 18 -- stored XSS vulnerability

```php
$sql = "SELECT * FROM q";
$valid = mysql_query($sql, $connect);
	while($data = mysql_fetch_array($valid))
		{
				echo "<div><p>".$data['user']." wrote: ".stripslashes($data['blog'])."</p></div>";
				
}
```

## `blogView.php`


* line 5 -- definite, tested XSS vulnerability in blog submission form

```php
<?php
...
$blogPost = $_POST['vuln'];
...
echo $blogPost;
```

* line 6 -- hardcoded MySQL credentials in public source code

```php
$connect = mysql_connect("localhost", "ghost", "ghost");
```

* line 14 -- SQL injection vulnerability

```php
$sql = "UPDATE q SET blog='".$blogPost."' WHERE user='".$user."'";

$valid = mysql_query($sql, $connect);
```