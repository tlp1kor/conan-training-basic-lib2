#include "mul.h"
#include <fmt/core.h>  // Include fmt header

int multiply(int a, int b) {
    fmt::print("LOGGING [mul.cpp]: Multiplying {} and {}\n", a, b);
    return a * b;
}
