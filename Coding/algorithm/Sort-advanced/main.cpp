#include <iostream>
#include "./SortTestHelper/SortTestHelper.h"
using namespace std;
int main(){
    int* array = SortTestHelper::generate_random_array(10000,1,200);
    
    // //归并排序
    // SortTestHelper::print_array(array,100);
    // Algorithm::test_sort("merge_sort", Algorithm::merge_sort,array,100);
    // SortTestHelper::print_array(array,100);

    //归并排序
    // SortTestHelper::print_array(array,100);
    // Algorithm::test_sort("merge_sort", Algorithm::merge_sort,array,100);
    // SortTestHelper::print_array(array,100);

    //快速排序
    SortTestHelper::print_array(array,100);
    Algorithm::test_sort("quick_sort", Algorithm::quick_sort,array,100);
    SortTestHelper::print_array(array,100);
    delete[] array;
    return 0;
}