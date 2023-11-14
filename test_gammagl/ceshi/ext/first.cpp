#include <iostream>
#include <torch/extension.h>
#include <torch/script.h>
#include <torch/torch.h>
#include <vector>


int64_t add(int64_t a, int64_t b){
    return a + 2 * b;
}

// int main(){
//     int64_t a = 3;
//     int64_t b = 5;

//     std::cout << add(a, b) << std::endl;

//     return 0;
// }

PYBIND11_MODULE(_ext, m){
    m.def("c_add", add);
}


