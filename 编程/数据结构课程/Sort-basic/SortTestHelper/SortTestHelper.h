#ifndef _SORTTESTHELPER_H
#define _SORTTESTHELPER_H

#include <iostream>
#include <time.h>
#include <cassert>
#include <stdlib.h>
#include <string>
using namespace std;

namespace SortTestHelper{
    int* generate_random_array(int n,int range_l,int range_h){
        assert(range_l <= range_h);
        int* array = new int[n];
        srand(time(NULL));
        for ( int i = 0; i<n; i++ ){
            array[i] = rand()%(range_h-range_l+1) + range_l;
        }
        return array;
    }
    template <typename T>
    void print_array(T array,int n){
        for( int i = 0; i < n; i++ ){
            cout << array[i] << "  ";
        }
        cout << endl;
    }
    template <typename T>
    void swap(T* a,T* b){
        a = a - b;
        b = b + a;
        a = b - a;
    }
}
namespace Algorithm{

    /*
    *@algoruthm:选择排序
    *@brief:复杂度 O(n^2)
    *依次找出前面的最小元素或最大元素然后再与当前元素做比较，进而进行排序，即为选择排序。
    *@author:Mr Qi Xiao
    *@date:2017-07-20
    */
    template <typename T>
    void select_sort(T array[],int n){
        int MinIndex;
        for (int i = 0; i < n; i++ ){
            MinIndex = i;
            for (int j = i+1; j < n; j++){
                if ( array[j] < array[MinIndex] ){
                    MinIndex = j;
                }
            }
            swap(array[i],array[MinIndex]);
        }
    }

    template <typename T>
    /*
    *@algorithm:插入排序 复杂度 O(n^2)
    *@brief:依次将当前元素与后面的元素作比较，在合适的时候交换位置插入，即为插入排序。
    *@date:2017-07-20
    *@author:Mr Qi Xiao
    */
    void insert_sort(T array[],int n){
        for ( int i = 1; i < n; i++ ){
            for ( int j = i; j > 0;j-- ){
                if ( array[j] < array[j-1] ){
                    swap(array[j],array[j-1]);
                    break;
                }
            }
        }
    }

    template <typename T>
    void insert_sort_plus(T array[],int n){
        for ( int i = 1; i < n; i++ ){
            int j;
            T e = array[i];
            for (j = i; j > 0 && array[j-1] > e; j--){
                array[j] = array[j-1];
            }
            array[j] = e;
        }
    } 
    template <typename T>
    void shell_sort(T array[],int n){
        ;
    }
    
    template <typename T>
    void test_sort(string sortname,void(*sort)(T[],int),T array[],int n){
        clock_t StartTime = clock();
        sort(array,n);
        clock_t EndTime = clock();
        cout << sortname << ":" << (double(EndTime - StartTime))/CLOCKS_PER_SEC << "S" << endl;
    }
}

#endif