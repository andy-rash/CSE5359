#include <iostream>
#include <string>
#include <unordered_map>

// C headers
#include <cstdio>
#include <cstdlib>

/*
 * non-STD headers
 */
// md5 hashing found here:
// - http://www.zedwood.com/article/cpp-md5-function
// - also see attribution within md5.h and md5.cpp themselves
#include "md5.h"

// cross-platform solution to hiding stdout output:
// - https://stackoverflow.com/questions/1413445/reading-a-password-from-stdcin
#ifdef WIN32
#include <windows.h>
#else
#include <termios.h>
#include <unistd.h>
#endif

struct User {
    char _username[20] = {0};
    char _password[34] = {0};
    int _checking_balance;
    int _savings_balance;

    User(const std::string& username,
         const std::string& password,
         const int& checking_balance,
         const int& savings_balance) {
        strcpy(_username,username.c_str());
        strcpy(_password,password.c_str());
        _checking_balance = checking_balance;
        _savings_balance = savings_balance;
    }
 
};

typedef std::unordered_map<std::string,User> user_store;

std::string salt("0123456789abcdef");

// create some users
User a("Alice",md5("hunter2"+salt),970,300);
User b("Bob",md5("pa$$w0rd"+salt),470,250);
User c("Candice",md5("CorrectHorseBatteryStaple"+salt),680,470);

// initialize in-memory user store
user_store ustore({
    {std::string(a._username), a},
    {std::string(b._username), b},
    {std::string(c._username), c},
}); 


// Authenticate a user
bool authenticate(const std::string& username,
                  const std::string& password) {

    auto res = ustore.find(username);
    if(res != ustore.end()) {
        std::string pwd_hash(md5(password+salt));    
        if(strcmp(res->second._password,pwd_hash.c_str()) == 0) {
            return true;   
        }
    }

    return false; 

}

// Check account balance (checking or savings)
void check_account_balance(const std::string& username,
                           const std::string& account) {

    if(account.compare("checking") == 0) {
        std::cout << "$" << ustore.at(username)._checking_balance  << std::endl;
        return;    
    }

    if(account.compare("savings") == 0) {
        std::cout << "$" << ustore.at(username)._savings_balance  << std::endl;
        return;    
    }

    return;

}

// Withdraw from account (checking or savings)
void withdraw_from_account(const std::string& username,
                           const std::string& account) {
  
    int withdraw_amount = 0;
    int withdraw_limit = 400;
    std::string input;

    std::cout << "Enter withdrawal amount: $";
    std::cin >> input;
    std::cout << std::endl;

    if(atoi(input.c_str()) > withdraw_limit) {
        std::cout << "There is a withdraw limit of $400." << std::endl;
        std::cout << "Transaction cancelled." << std::endl;
        return;
    }

    std::cout << "You withdrew: $";
    printf(input.c_str(), (int *) &withdraw_amount);

    if(account.compare("checking") == 0) {
        ustore.at(username)._checking_balance -= withdraw_amount;
        printf("Your remaining balance is: $%d\n", ustore.at(username)._checking_balance);
        return;        
    }

    if(account.compare("savings") == 0) {
        ustore.at(username)._savings_balance -= withdraw_amount;
        printf("Your remaining balance is: $%d\n", ustore.at(username)._savings_balance);
        return;
    }

    return;

}

// Menu for checking a user's account balance 
void account_balance(const std::string& username) {

    int choice = 0;
    bool persist = true;

    std::system("clear");

    std::cout << std::endl;
    std::cout << "*********************************" << std::endl;
    std::cout << "**       Account Balance      ***" << std::endl;
    std::cout << "*********************************" << std::endl << std::endl;
    
    std::cout << "1. Checking" << std::endl;
    std::cout << "2. Savings" << std::endl;
    std::cout << "3. Back" << std::endl;

    while(persist) {
    
        std::cout << std::endl << ">> ";
        std::cin >> choice;

        while(std::cin.fail()) {

            std::cout << std::endl << "Invalid input. Please try again." << std::endl << std::endl;
            std::cin.clear();
            std::cin.ignore(256,'\n');

            std::cout << std::endl << ">> ";
            std::cin >> choice;

        }
        
        switch(choice) {
        
            case 1:
                check_account_balance(username,"checking");
                break;

            case 2:
                check_account_balance(username,"savings");
                break;

            case 3:
                std::cout << std::endl << "Quitting..." << std::endl << std::endl;
                persist = false;
                break;

            default:
                std::cout << std::endl << "Invalid input. Please try again." << std::endl << std::endl;
                break;

        }

    }

}

// Withdraw money from a user's account
void withdrawal(const std::string& username) {

    int choice = 0;
    bool persist = true;

    std::system("clear");

    std::cout << std::endl;
    std::cout << "*********************************" << std::endl;
    std::cout << "**         Withdrawal         ***" << std::endl;
    std::cout << "*********************************" << std::endl << std::endl;
    
    std::cout << "1. Checking account" << std::endl;
    std::cout << "2. Savings account" << std::endl;
    std::cout << "3. Back" << std::endl;

    while(persist) {
    
        std::cout << std::endl << ">> ";
        std::cin >> choice;

        while(std::cin.fail()) {

            std::cout << std::endl << "Invalid input. Please try again." << std::endl << std::endl;
            std::cin.clear();
            std::cin.ignore(256,'\n');

            std::cout << std::endl << ">> ";
            std::cin >> choice;

        }
        
        switch(choice) {
        
            case 1:
                withdraw_from_account(username,"checking");
                break;

            case 2:
                withdraw_from_account(username,"savings");
                break;

            case 3:
                std::cout << std::endl << "Quitting..." << std::endl << std::endl;
                persist = false;
                break;

            default:
                std::cout << std::endl << "Invalid input. Please try again." << std::endl << std::endl;
                break;

        }

    }

}

void set_stdin_echo(bool enable = true) {
#ifdef WIN32
    HANDLE h_stdin = GetStdHandle(STD_INPUT_HANDLE);
    DWORD mode;
    GetConsoleMode(h_stdin, &mode);

    if(!enable) {
        mode &= ~ENABLE_ECHO_INPUT;    
    } else {
        mode |= ENABLE_ECHO_INPUT;    
    }

    SetConsoleMode(h_stdin, &mode);
#else
    struct termios tty;
    tcgetattr(STDIN_FILENO, &tty);

    if(!enable) {
        tty.c_lflag &= ~ECHO;     
    } else {
        tty.c_lflag |= ECHO;    
    }

    (void) tcsetattr(STDIN_FILENO, TCSANOW, &tty);
#endif
}

int main(int argc, char* argv[]) { 

    /*
     * Authentication
     */
    std::string username;
    std::string password;
    
    std::cout << "Login as: ";
    std::cin >> username;
    std::cout << username + "'s password: ";

    set_stdin_echo(false);
    std::cin >> password;
    set_stdin_echo(true);
    std::cout << std::endl;

    if(!authenticate(username,password)) {
        std::cerr << "Incorrect username or password." << std::endl;    
        return -1;
    }

    /*
     * Menu items
     */
    int choice = 0;
    bool persist = true;

restart:

    std::system("clear");

    std::cout << std::endl;
    std::cout << "*********************************" << std::endl;
    std::cout << "**  Ultrasecure Savings Bank  ***" << std::endl;
    std::cout << "*********************************" << std::endl << std::endl;
    
    std::cout << "1. Check account balance" << std::endl;
    std::cout << "2. Make a withdrawal" << std::endl;
    std::cout << "3. Quit" << std::endl;

    while(persist) {
    
        std::cout << std::endl << ">> ";
        std::cin >> choice;

        while(std::cin.fail()) {

            std::cout << std::endl << "Invalid input. Please try again." << std::endl << std::endl;
            std::cin.clear();
            std::cin.ignore(256,'\n');

            std::cout << std::endl << ">> ";
            std::cin >> choice;

        }
        
        switch(choice) {
        
            case 1:
                account_balance(username);
                goto restart;
                break;

            case 2:
                withdrawal(username);
                goto restart;
                break;

            case 3:
                std::cout << std::endl << "Quitting..." << std::endl << std::endl;
                persist = false;
                break;

            default:
                std::cout << std::endl << "Invalid input. Please try again." << std::endl << std::endl;
                break;

        }

    }

//    int i = 500;
//
//    std::string input;
//    std::cout << "Enter word with proper length: ";
//    std::cin >> input;
//    std::cout << std::endl;
//
//    printf("You typed: ");
//    printf(input.c_str(), (int *) &i);
//    printf("i = %d\n", i);

    return 0;

}
