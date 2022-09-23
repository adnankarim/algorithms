// Online C++ compiler to run C++ program online
// time Complexity: O(n)
// space complexity O(n)
#include <iostream>

using namespace std;
int sumuptoNfunctional(int N){
  
    if(N==0){
    
        return 0;
    }
    
    return N + sumuptoNfunctional(N-1);
     
}

int main() {
    // Write C++ code here
   
    cout<<sumuptoNfunctional(3);
    return 0;
}