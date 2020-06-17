#include <iostream>
#include "./SortTestHelper/SortTestHelper.h"
using namespace std;
int main()
{
    int *array = SortTestHelper::generate_random_array(100, 1, 20);
    //选择排序
    SortTestHelper::print_array(array, 10);
    Algorithm::test_sort("select_sort", Algorithm::select_sort, array, 100);
    SortTestHelper::print_array(array, 10);

    //插入排序
    // SortTestHelper::print_array(array,10);
    // Algorithm::test_sort("insert_sort", Algorithm::insert_sort,array,10000000);
    // SortTestHelper::print_array(array,10);

    //插入排序plus
    // SortTestHelper::print_array(array,10);
    // Algorithm::test_sort("insert_sort_plus", Algorithm::insert_sort_plus,array,10000);
    // SortTestHelper::print_array(array,10);

    delete[] array;
    return 0;
}