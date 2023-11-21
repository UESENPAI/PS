#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int main() {
    vector<int> cases;
    int max = 0;
    int count = 0;
    while (1) {
        int i;
        cin >> i;
        if (i == 0)
            break;
        if (i > max)
            max = i;
        cases.push_back(i);
    }
    bool *prime = new bool[2 * max + 1];
    fill_n(prime, 2 * max + 1, 1);
    prime[0] = false;
    prime[1] = false;
    for (int i = 2; i <= sqrt(2*max); i++)
        if(prime[i] == true)
            for(int j = i*2; j <= (2*max); j += i)
                prime[j] = false;

    for(int j = 0; j < cases.size(); j++)
    {
        for(int k = cases[j]+1; k <= 2*cases[j]; k++)
            if(prime[k] == true)
                count++;
        cout << count << '\n';
        count = 0;
    }
    return 0;
}