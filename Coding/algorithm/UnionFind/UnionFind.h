#ifndef _UNIONFIND_H
#define _UNIONFIND_H
#include <cassert>
template <typename T>
class unionfind{
private:
    T* id;
    int count;
public:
    unionfind(int n){
        count = n;
        id = new T[n];
        for ( int i = 0; i < n; i++ ){
            id[i] = i;
        }
    }
    ~unionfind(){
        delete[] id;
    }
    T find(int p){
        return id[p];
    }
    bool is_connected( int p,int q){
        return id[p]==id[q];
    }
    /*连接两个元素*/
    void union_elems(int p,int q ){
        int pid = find(p),qid = find(q);
        if ( pid == qid ){
            return;
        }
        for ( int i = 0; i < count; i++ ){
            if ( qid == id[i] ){
                id[i] = pid;
            }
        }
    }
};
/*基于节点的并查集优化*/
template < typename T >
class unionfind2{
private:
    T* parent;
    int count;
public:
    unionfind2( int n ){
        parent = new T[n];
        count = n ;
        for ( int i = 0; i < count; i++ ){
            parent[i] = i;
        }
    }
    bool is_connected( int p, int q){
        return find(q) == find(p);
    }
    T find( int p ){
        assert( p >=0 && p < count );
        while ( p!= parent[p] ) {
            p = parent[p];
        }
    }
    void union_elems( int p,int q){
        int proot = find(p);
        int qroot = find(q);
        if ( proot == qroot ){
            return;
        }
        parent[p] = qroot;
    }
    ~unionfind2(){
        delete[] parent;
    }
};
/*基于size的优化*/
template < typename T >
class unionfind3{
private:
    T* parent;
    int count;
public:
    unionfind3( int n ){
        parent = new T[n];
        size =  new int[n];
        count = n ;
        for ( int i = 0; i < count; i++ ){
            parent[i] = i;
            size[i] = 1;
        }
    }
    bool is_connected( int p, int q){
        return find(q) == find(p);
    }
    T find( int p ){
        assert( p >=0 && p < count );
        while ( p!= parent[p] ) {
            p = parent[p];
        }
    }
    void union_elems( int p,int q){
        int proot = find(p);
        int qroot = find(q);
        if ( proot == qroot ){
            return;
        }
        parent[p] = qroot;
    }
    ~unionfind3(){
        delete[] parent;
        delete[] size;
    }
};
#endif