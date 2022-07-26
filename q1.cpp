#include <iostream>
#include <algorithm>
using namespace std;
int compare(int a, int b)
{
	if (a < b)
		return a;
	else
		return b;
}
int main()
{
	int n, *a, *b, i, s = 0;
	cout << "Enter the length of array: ";
	cin >> n;
	a = new int[n];
	b = new int[n];
	for (i = 0; i < n; i++)
		b[i] = 0;
	cout << "Enter numbers: ";
	for (i = 0; i < n; i++)
		cin >> a[i];
	for (i = 1; i < n; i++)
	{
		b[i] = compare(*max_element(a, a + i), *max_element(a + i + 1, a + n)) - a[i];
	}
	for (i = 1; i < n - 1; i++)
		if (b[i] > 0)
			s += b[i];
	delete[] a;
	delete[] b;
	cout << "Sum = " << s;
	return 0;
}
