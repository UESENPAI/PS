#include <iostream>
using namespace std;

int main(void){
	int a;
    
	cin >> a;
    
    if(a%4==0 && (a%100!=0 || a%400==0))
    {
        cout << 1;
    }
    else
    {
        cout << 0;
    }
}