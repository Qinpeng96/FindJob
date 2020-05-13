#include <iostream>
#include "tree.h"
using namespace std;
int main( void ){
    int arr[10] = {1,2,3,4,5,6,7,8,9,10};
    cout <<  binary_search(arr,10,7) << endl;
    cout <<  binary_search_recursion(arr,10,15) << endl;
    return 0;
}
