#include <iostream>
#include <bitset>
#include <cmath>
using namespace std;
int main()
{
    int n, i, s = 0;
    cout << "enter digit number: ";
    cin >> n;
    for (i = round(pow(2, n - 1)); i < round(pow(2, n)); i++)
        if ((bitset<24>(i).to_string().find("00000", 24 - n) != string::npos) || (bitset<24>(i).to_string().find("11111", 24 - n) != string::npos))
            s += 1;
    cout << s;
    return 0;
}
