// Online C++ compiler to run C++ program online
// TC = 2^n  as tree is made not exactly 2^2 but exponential clsoe 2^n
//  For a full binary tree, the length for each path is log_2(X) where X is the number of nodes. Now the total numbers for input n is X=2^n. Now that gives that each path is log_2(2^n)= n long.
#include <iostream>

using namespace std;
int fibbonachi(int i){
    if (i<=1){
        return i;
    }
   
    return fibbonachi(i-1) +fibbonachi(i-2);
}
int main() {
    // Write C++ code here

    cout<<fibbonachi(2);
    return 0;
}