#include <iostream>
using namespace std;

int main() {
	int input, temp;       // 입력받을 케이스 input 그리고 임시변수 temp
	int sum = 0;           // 숫자의 총 합을 입력받을 변수입니다.
	char num;              // 숫자를 문자로 입력받습니다. ( 한 문자씩 끊어서 더할 것입니다 . )
	cin >> input;          // test case의 수를 입력받습니다.
	cin.get();             //마지막에 "\n" 개행문자가 입력이 되는데, 이를 없애주기 위해 입력받습니다.
	
	for (int i = 0; i < input; i++) {
		cin.get(num);          // 문자로 입력받은 숫자를 하나씩 변수에 저장합니다.
		temp = num - '0';      // 문자이기 때문에 '0'을 지워주는 작업을 합니다.
		sum += temp;           // 숫자 한 자리씩 더합니다.
	}                     
	
	cout << sum << endl;       // 총 합계를 출력합니다.
}