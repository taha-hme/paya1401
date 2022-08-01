#include <iostream>
using namespace std;
int main()
{
    int n, i;
    long long int f1, f2, c;
    cout << "enter the number of digits: ";
    cin >> n;
    f1 = 4;
    f2 = 14;
    for (i = 0; i <= n - 3; i++)
    {
        c = f2;
        f2 = (3 * f2 + 2 * f1) % 1000000007;
        f1 = c;
    }
    if (n == 1)
        cout << f1;
    else
        cout << f2;
    return 0;
}
