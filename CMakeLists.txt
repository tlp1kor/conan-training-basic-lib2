cmake_minimum_required(VERSION 3.10)
project(multiplication_lib)

add_library(multiplication_lib src/mul.cpp)
target_include_directories(multiplication_lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src)
