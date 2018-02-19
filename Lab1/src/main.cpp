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

typedef std::unordered_map<std::string,std::string> user_store;

int main(int argc, char* argv[]) {

    std::string salt("1234567890abcdef");

    // initialize in-memory user store
    user_store ustore({
        {std::string("Alice"), std::string("AAAA")},
        {std::string("Bob"), std::string("BBBB")},
    }); 

    int x = 0;

    return 0;

}
