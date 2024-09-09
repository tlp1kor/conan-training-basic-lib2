from conan import ConanFile
from conan.tools.cmake import CMake
from conan.tools.files import copy  # Import the new copy tool
import os

class MultiplicationLibConan(ConanFile):
    name = "multiplication_lib"
    version = "2.0"
    license = "MIT"
    description = "A simple multiplication library"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"
    exports_sources = "src/*", "CMakeLists.txt"

    def layout(self):
        self.folders.source = "."
        self.folders.build = "__build"
        self.folders.generators = "__build"
    
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
    
    def requirements(self):
        self.requires("fmt/10.2.1")  # Specify the fmt version you want to use

    def package(self):
        # Copy header files to the package's include folder
        copy(self, "*.h", src=os.path.join(self.source_folder, "src"), dst=os.path.join(self.package_folder, "include"))

        # Copy library files (static or dynamic) to the package's lib folder
        copy(self, "*.lib", src=self.build_folder, dst=os.path.join(self.package_folder, "lib"), keep_path=False)
        copy(self, "*.a", src=self.build_folder, dst=os.path.join(self.package_folder, "lib"), keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["multiplication_lib"]
