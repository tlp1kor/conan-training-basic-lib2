# Conan Training - Basic
## Microservice Project - Lib2 (Multiplication)

Contains a feature for microservice calculator application.
It has Addition feature which is compiled in form of a static library. The feature here consumed a 3rd party package to implement logging. The library and header is then being shared to another consumer which integrates this feature into an application.
For this `chapter_2_dependency_handling` branch content, the consumer is [Calculator_Application](https://github.com/tlp1kor/conan-training-basic/tree/chapter_3_transitive_dependencies). So make sure to build this current application before building the Calculator_Application.

This `chapter_2_dependency_handling` branch creates package: `multiplication_lib/2.0`

The application is built with Conan which in background will use CMake in this case.
To build the application please run the following command:
```
./build.sh
```
