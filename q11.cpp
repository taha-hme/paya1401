#include <iostream>
using namespace std;
int main()
{
	int n, i, j, k = 0;
	cout << "Enter the length of array: ";
	cin >> n;
	int a[n + 1];
	cout << "Enter numbers: ";
	for (i = 1; i <= n; i++)
		cin >> a[i];
	for (i = 1; i < n; i++)
		for (j = i + 1; j <= n; j++)
		{
			if (a[i] > a[j])
				k++;
		}
	cout << "Number of i,j is: " << k;
	return 0;
}
