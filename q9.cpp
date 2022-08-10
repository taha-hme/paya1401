#include <iostream>
#include <string>
#include <cmath>
using namespace std;
int main()
{
    int n, i;
    string str1, str2;
    cout << "enter the number: ";
    cin >> n;
    str2 = to_string(n);
    for (i = 2; i <= 1001; i++)
    {
        if (log10(i) == floor(log10(i)))
            continue;
        str1 = to_string(n * i);
        if (str1.find(str2) != string::npos)
        {
            cout << n * i;
            break;
        }
    }
    return 0;
}
