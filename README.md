[![Build Status](https://travis-ci.org/kwallner/conan-bzip2.svg)](https://travis-ci.org/kwallner/conan-bzip2)
[![Build Status](https://ci.appveyor.com/api/projects/status/github/kwallner/conan-bzip2)](https://ci.appveyor.com/project/kwallner/conan-bzip2)

# Info

This repository is forked from https://github.com/lasote/conan-bzip2. 

It is mainly for stable and evaluation purposes. If you need a stable and maintained release please switch to https://github.com/lasote/conan-bzip2. 

# conan-bzip2

[Conan.io](https://conan.io) package for BZip2 library. http://www.bzip.org/

The packages generated with this **conanfile** can be found in [conan.io](https://conan.io/source/bzip2/1.0.6/kwallner/stable).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

## Upload packages to server

    $ conan upload bzip2/1.0.6@kwallner/stable --all

## Reuse the packages

### Basic setup

    $ conan install bzip2/1.0.6@kwallner/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    bzip2/1.0.6@kwallner/stable

    [options]
    bzip2:shared=true # false

    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install .

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.
