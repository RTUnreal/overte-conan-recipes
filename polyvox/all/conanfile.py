import os
from conan import ConanFile
from conan.tools.files import get, collect_libs
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout

class PolyvoxConan(ConanFile):
    name = "polyvox"
    license = "MIT"
    url = "https://github.com/overte-org/polyvox/"
    description = "The voxel management and manipulation library"
    settings = "os", "compiler", "build_type", "arch"

    def layout(self):
        cmake_layout(self)

    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["ENABLE_EXAMPLES"] = "OFF"
        tc.variables["ENABLE_TESTS"] = "OFF"
        tc.variables["ENABLE_BINDINGS"] = "OFF"
        tc.variables["BUILD_DOCS"] = "OFF"
        tc.variables["BUILD_MANUAL"] = "OFF"
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        if self.settings.os == "Windows":
            self.cpp_info.includedirs = ['PolyVoxCore/include', 'PolyVoxUtil/include']
            self.cpp_info.libdirs = ['PolyVoxCore/lib', 'PolyVoxUtil/lib']
        else:
            self.cpp_info.includedirs = ['include/PolyVoxCore', 'include/PolyVoxUtil']
        self.cpp_info.libs = collect_libs(self)
