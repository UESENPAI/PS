#include <iostream>
#include <ios>
using namespace std;

int main()
{
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int testNum = 0;

	cin >> testNum;

	int *p = new int[testNum];
	int a, b;

	for (int i = 0; i < testNum; i++)
	{
		cin >> a >> b;
		p[i] = a + b;
	}

	for (int i = 0; i < testNum; i++)
	{
		cout << p[i] << "\n";
	}

    return 0;
}