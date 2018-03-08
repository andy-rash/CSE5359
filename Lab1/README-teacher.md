# CSE 5359 - Lab 1

## Compiling from source

To compile the program, simply run `make` in the current lab's root directory.
The binary file will be placed in the `bin/` folder and can be run using the command `./bin/main.out`.

## Running the Exploit

### Root directory

![](img/1-root-directory.png)

The root directory of the project looks as seen above.

### Compile the program

![](img/2-compile.png)

Compile the program with `make`.

### Run the program

![](img/3-run.png)

Run the program with `./bin/main.out`.

### Login

![](img/4-login-pt1.png)
![](img/5-login-pt2.png)

There are pre-configured accounts available. Check the source code for username/password combinations. The password is blank while typing.

### Main menu

![](img/6-main-menu.png)

Successful login greets the user with the main menu.

### Check account balances

From the main menu, one can check the logged-in user's account balances in the checking and savings accounts.

![](img/7-check-balances.png)
![](img/8-check-checking-account-balance.png)
![](img/9-account-balance-result.png)

### Make withdrawals

Also, from the main menu, one can make withdrawals from the logged-in user's checking and savings accounts.

![](img/10-make-withdrawal.png)
![](img/11-withdraw-from-checking.png)
![](img/12-withdraw-limit.png)

There is an imposed withdrawal limit of $400 per transaction.

### Break through the withdrawal limit

One can break through this limit with a certain input. Here, we use Python to generate 405 'A's in one string.
![](img/13-break-it-pt1.png)

Copy the string for later use.
![](img/14-break-it-pt2.png)

Paste the string into the withdrawal request, making sure to include the `%n` at the end (very important).
![](img/15-break-it-pt3.png)

The withdrawal limit has been bypassed, as can be seen by the balance update after the withdrawal.
![](img/16-what-withdraw-limit.png)