#include <iostream>
#include <string>
#include <tuple>
#include <unordered_map>

// C headers
#include <cstdio>

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
    int _balance;
    User(const std::string& username,
         const std::string& password,
         const int& balance) {
        strcpy(_username,username.c_str());
        strcpy(_password,password.c_str());
        _balance = balance;
    }
};

typedef std::unordered_map<std::string,User> user_store;

std::string salt("0123456789abcdef");

// create some users
User a("Alice",md5("hunter2"+salt),97);
User b("Bob",md5("pa$$w0rd"+salt),47);
User c("Candice",md5("CorrectHorseBatteryStaple"+salt),68);

// initialize in-memory user store
user_store ustore({
    {a._username, a},
    {b._username, b},
    {c._username, c},
}); 


// Authenticate a user
bool authenticate(const std::string& username,
                  const std::string& password) {

    auto res = ustore.find(username.c_str());
    if(res != ustore.end()) {
        std::string pwd_hash(md5(password+salt));    
        if(strcmp(res->second._password,pwd_hash.c_str()) == 0) {
            return true;   
        }
    }

    return false;

}

// Check a user's account balance
void check_acc_balance(const std::string& username,
                       const std::string& password) {

    if(authenticate(username,password)) {
       


    }

    return;

}

// Withdraw money from a user's account
void withdraw(const std::string& username,
              const std::string& password) {

    if(authenticate(username,password)) {
    
        

    }

    return;

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
    
    std::cout << "1. Check account balance." << std::endl;
    std::cout << "2. Make a withdrawal." << std::endl;
    std::cout << "3. Quit." << std::endl;
    

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
