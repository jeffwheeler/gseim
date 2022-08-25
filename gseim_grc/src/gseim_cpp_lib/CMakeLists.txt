add_custom_command(
    COMMAND python3 -m gseim_cpp_lib.gen_ebe
                    ${CMAKE_CURRENT_BINARY_DIR}/get_ebe.cpp
                    ${CMAKE_SOURCE_DIR}/gseim/data/ebe/*.ebe
    OUTPUT get_ebe.cpp
    DEPENDS gen_ebe.py ${CMAKE_SOURCE_DIR}/gseim/data/ebe/
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
)

add_custom_command(
    COMMAND python3 -m gseim_cpp_lib.gen_xbe
                       ${CMAKE_CURRENT_BINARY_DIR}/get_xbe.cpp
                       ${CMAKE_SOURCE_DIR}/gseim/data/xbe/*.xbe
    OUTPUT get_xbe.cpp
    DEPENDS gen_xbe.py ${CMAKE_SOURCE_DIR}/gseim/data/xbe/
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
)

set(gseim_solder_headers
    cctfile.h
    global.h
    utils.h
    routines1.h
    routines2.h
    xbelib.h
    xbeusr.h
    xbejac.h
    ebelib.h
    ebeusr.h
    ebejac.h
    circuit.h
    solveblocks.h
    solveparm.h
    sysmat.h
    ijmat.h
    knuthmat.h
    matop.h
    matgnrl1.h
    matrix_2.h
    user_f.h
    get_yyy.h
)

add_library(gseim_solver_lib
    ${gseim_solder_headers}
    cctfile.cpp
    global.cpp
    utils.cpp
    routines1.cpp
    routines2.cpp
    xbelib.cpp
    xbeusr.cpp
    xbejac.cpp
    ebelib.cpp
    ebeusr.cpp
    ebejac.cpp
    circuit.cpp
    solveblocks.cpp
    solveparm.cpp
    sysmat.cpp
    ijmat.cpp
    knuthmat.cpp
    matop.cpp
    matgnrl1.cpp
    matrix_2.cpp
    user_f.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/get_ebe.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/get_xbe.cpp
)

target_include_directories(gseim_solver_lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

add_executable(
    gseim_solver
    gsmain.cpp
)

target_link_libraries(gseim_solver PUBLIC gseim_solver_lib)

install(
    TARGETS gseim_solver
    DESTINATION bin
)

add_library(
    filter
    MODULE
    utils.cpp
    matrix_2.cpp
    ijmat.cpp
    pic_dummy.cpp
    global.h
    knuthmat.h
    utils.h
    matrix_2.h
    ijmat.h
)

install(
    TARGETS filter
    LIBRARY DESTINATION lib
)
