cmake_minimum_required(VERSION 3.10)
project(multiplication_lib)

add_library(multiplication_lib src/mul.cpp)
find_package(fmt REQUIRED)  # Find fmt package
target_link_libraries(multiplication_lib fmt::fmt)  # Link fmt to your library
target_include_directories(multiplication_lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src)
