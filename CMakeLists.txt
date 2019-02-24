project(bzip2)
cmake_minimum_required(VERSION 2.8)

add_library(bz2 blocksort.c bzlib.c compress.c  crctable.c  decompress.c  huffman.c randtable.c)
set_target_properties(bz2 PROPERTIES 
    DEBUG_POSTFIX "d"
    POSITION_INDEPENDENT_CODE ON
    )
if (BUILD_SHARED_LIBS)
    set_target_properties(bz2 PROPERTIES 
        COMPILE_DEFINITIONS "bz2_SHARED_LIB"
        INTERFACE_COMPILE_DEFINITIONS "bz2_SHARED_LIB"
        )
    if (CMAKE_CXX_COMPILER_ID MATCHES "Clang" OR CMAKE_CXX_COMPILER_ID MATCHES "GNU") 
        set_target_properties(bz2 PROPERTIES 
            COMPILE_FLAGS "-fvisibility=hidden"
            )
    endif()
endif()

install(FILES bzlib.h
    DESTINATION include
    )

install(TARGETS bz2 
    EXPORT BZip2
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
    )

install(EXPORT BZip2
    FILE BZip2Config.cmake
    DESTINATION .
    )
    
add_executable(bzip2 bzip2.c)
target_link_libraries(bzip2 bz2)
install(TARGETS bzip2
    RUNTIME DESTINATION bin
    )