import os
import shutil

from conans import CMake, tools
from conans import ConanFile


class Bzip2Conan(ConanFile):
    name = "bzip2"
    version = "1.0.6"
    branch = "master"
    generators = "cmake"
    settings = "os", "compiler", "arch", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"
    url = "https://github.com/kwallner/conan-bzip2"
    license = "BSD-style license"
    description = "bzip2 is a freely available, patent free (see below), high-quality data " \
                  "compressor. It typically compresses files to within 10% to 15% of the best" \
                  " available techniques (the PPM family of statistical compressors), whilst " \
                  "being around twice as fast at compression and six times faster at decompression."
    exports = ["CMakeLists.txt"]
    exports_sources = ["patches/bzip2-1.0.6_modern_cmake_build.patch"]
    no_copy_source = True
    
    @property
    def zip_folder_name(self):
        return "bzip2-%s" % self.version

    def config(self):
        del self.settings.compiler.libcxx

    def source(self):
        zip_name = "bzip2-%s.tar.gz" % self.version
        #tools.download("http://www.bzip.org/%s/%s" % (self.version, zip_name), zip_name, verify=False)
        tools.download("https://netcologne.dl.sourceforge.net/project/bzip2/%s" % zip_name, zip_name)
        tools.check_md5(zip_name, "00b516f4704d4a7cb50a1d97e6e8e15b")
        tools.unzip(zip_name)
        os.unlink(zip_name)
        
        # Prepare for CMake
        shutil.move("CMakeLists.txt", "%s/CMakeLists.txt" % self.zip_folder_name)
        tools.patch(patch_file="patches/bzip2-1.0.6_modern_cmake_build.patch")
    
    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"]= self.options.shared
        cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.shared or self.options.fPIC
        cmake.configure(source_dir="%s/%s" % (self.source_folder, self.zip_folder_name))
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = [ "bz2%s" % ("d" if self.settings.build_type == "Debug" else "") ]
