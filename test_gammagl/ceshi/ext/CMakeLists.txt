cmake_minimum_required(VERSION 3.21)
project(test)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})

find_package(Torch REQUIRED)

# find_package(OpenMP REQUIRED)
# if(OPENMP_FOUND)
#     message("Found OpenMP")
#     add_definitions(-DCOMPILE_WITH_OMP)
#     set(CMAKE_C_FLAGS ${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS})
#     set(CMAKE_CXX_FLAGS ${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS})
# endif()

# find_package(CUDA)
# if(${CUDA_FOUND})
#     message("Found CUDA")
#     add_definitions(-DCOMPILE_WITH_CUDA)
# endif()

# add_library(test first.cpp)
add_executable(test first.cpp)
target_link_libraries(test ${TORCH_LIBRARIES} ${PYTHON_LIBRARIES})