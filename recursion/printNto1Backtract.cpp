// Online C++ compiler to run C++ program online
// time Complexity: O(n)
// space complexity O(n)
#include <iostream>
int N =5;
using namespace std;
void printNto1Backtract(int N,int count=1){
  
    if(count>N){
        return;
    }
    
    printNto1Backtract(N,count+1);
      cout<<count<<'\n';
}

int main() {
    // Write C++ code here
   
    printNto1Backtract(5);
    return 0;
}