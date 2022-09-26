// Online C++ compiler to run C++ program online
#include <iostream>
#include <string>
using namespace std;
bool isPalindromeString(int i, string &arr,int n){
    if (i>=n/2){
        return true;
    }
    if(arr[i]!=arr[n-1-i]){
        return false;
    }
    return isPalindromeString(i+1,arr,n);
}
int main() {
    // Write C++ code here
    
    string arr ="madtam";

    cout<<isPalindromeString(0,arr,arr.length());;
    return 0;
}