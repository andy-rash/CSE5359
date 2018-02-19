
CXX = g++
CFLAGS = -g -fno-stack-protector -std=c++11

BIN = bin/
LIB = lib/
SRC = src/

LIB_FILES = md5.cpp

TARGET_TYPE = .out
TARGET = main$(TARGET_TYPE)

all:
	$(CXX) $(CFLAGS) -I $(LIB) $(addprefix $(LIB), $(LIB_FILES)) -o $(BIN)$(TARGET) $(SRC)*.cpp
