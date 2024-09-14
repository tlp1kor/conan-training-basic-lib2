# Conan Training - Basic
## Microservice Project - Lib2 (Multiplication) uploaded to Artifactory
### It is an Optional Chapter

Contains a feature for microservice calculator application.
It has Multiplication feature which is compiled in form of a static library. The feature here consumed a 3rd party package to implement logging. The library and header is then being shared to another consumer which integrates this feature into an application.
For this `chapter_2.1_upload_package` branch content, the consumer is [Calculator_Application](https://github.com/tlp1kor/conan-training-basic/tree/chapter_3.1_download_package_from_remote). So make sure to build this current application before building the Calculator_Application.

This `chapter_2.1_upload_package` branch creates package: `multiplication_lib/2.0` and uploads it to a conan repository in artifactory.

The application is built with Conan which in background will use CMake in this case.
To build the application please run the following command:
```
./build.sh
```
To Upload the conan package please run the following command:
```
./conan_upload.sh
```
