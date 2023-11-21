#include <iostream>
using namespace std;

int main(void){
	int a, b, c = -1, sum = 0;
	int ten = 10;
    
	cin >> a >> b;
    
	for(int i = 0; i < 3; i++) {
		c = b % ten;
        
		cout << a * c * 10 /ten << endl;
        
        sum += a * c;
		b -= c;
		ten *= 10;
	}
	cout << sum;
}