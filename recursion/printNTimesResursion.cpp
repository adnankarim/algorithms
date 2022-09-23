// Online C++ compiler to run C++ program online



// time complexity O(n)
// space complexity O(n) hypothetical as we are using only internal stack at each function call..
#include <iostream>
int N =5;
using namespace std;
void printNTimes(int N){
    cout<<"Adnan"<<'\n';
    if(N==1){
        return;
    }
    
    printNTimes(N-1);
}

int main() {
    // Write C++ code here
   
    printNTimes(5);
    return 0;
}