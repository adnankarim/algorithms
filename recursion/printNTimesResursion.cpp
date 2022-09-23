// Online C++ compiler to run C++ program online
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