from conans.model.conan_file import ConanFile
from conans import CMake
import os

class DefaultNameConan(ConanFile):
    name = "DefaultName"
    version = "0.1"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    options = {"shared": [True, False]}
    default_options = "shared=False"

    def build(self):
        print(self.build_folder)
        print(self.source_folder)
        print(os.getcwd())
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy(pattern="*.dll", dst="bin", src="bin")
        self.copy(pattern="*.dylib", dst="bin", src="lib")
        
    def test(self):
        self.run(".%sbin%sbzip2 --help" % (os.sep, os.sep))
