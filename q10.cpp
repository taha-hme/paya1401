#include <iostream>
using namespace std;
bool negative = false;
struct Poly
{
	int n;
	int z[20];
};
void ShowPoly(Poly &p)
{
	for (int j = 0; j < p.n; j++)
	{
		switch (p.z[j])
		{
		case 0:
			continue;
		case 1:
			if (j == 0)
				cout << "x^" << p.n - j;
			else
				cout << " + x^" << p.n - j;
			break;
		case -1:
			if (j == 0)
				cout << "-x^" << p.n - j;
			else
				cout << " - x^" << p.n - j;
			break;
		default:
			if (j == 0)
				if (p.z[j] > 1)
					cout << p.z[j] << "x^" << p.n - j;
				else
					cout << "-" << abs(p.z[j]) << "x^" << p.n - j;
			else if (p.z[j] > 1)
				cout << " + " << p.z[j] << "x^" << p.n - j;
			else
				cout << " - " << abs(p.z[j]) << "x^" << p.n - j;
		}
	}
	if (p.z[p.n] > 0)
		cout << " + " << p.z[p.n];
	else if (p.z[p.n] < 0)
		cout << " - " << abs(p.z[p.n]);
	cout << endl;
}
void Input(Poly &p)
{
	cout << "Enter the degree of polynomial: ";
	cin >> p.n;
	cout << "Enter the coefficients: ";
	for (int i = 0; i <= p.n; i++)
		cin >> p.z[i];
	if (p.z[0] < 0)
		negative = true;
	cout << "The polynomial you entered: ";
	ShowPoly(p);
}
Poly FindZero(Poly &M)
{
	int i = 0, j;
	while (M.z[i] == 0)
	{
		if (M.z[i] != 0)
			break;
		i++;
	}
	for (j = i; j <= M.n; j++)
		M.z[j - i] = M.z[j];
	M.n -= i;
	return M;
}
int Divide(Poly M, Poly MA, Poly &kh)
{
	Poly Kh2, T;
	kh.n = M.n - MA.n;
	T.n = M.n;
	for (int i = 0; i <= kh.n; i++)
		kh.z[i] = 0;
	for (int i = 0; i <= T.n; i++)
	{
		if (M.n < MA.n)
			break;
		Kh2.n = M.n;
		for (int i = 0; i <= M.n; i++)
			Kh2.z[i] = 0;
		kh.z[i] = M.z[0] / MA.z[0];
		for (int j = 0; j <= MA.n; j++)
			Kh2.z[j] = kh.z[i] * MA.z[j];
		for (int k = 0; k <= M.n; k++)
			M.z[k] -= Kh2.z[k];
		FindZero(M);
	}
	if (M.z[0] == 0)
		return 1;
	else
		return 0;
}
int main()
{
	int i, k, r, res[11], b = 0;
	Poly M, MA, kh, T;
	MA.n = 1;
	MA.z[0] = 1;
	Input(M);
	cout << "Decomposes into: ";
	if (negative == true)
		cout << "-";
	for (i = 0; i < 11; i++)
		res[i] = 0;
	for (i = 0; i < 11 && M.n > 0; i++)
	{
		MA.z[1] = -1 * i;
		do
		{
			r = Divide(M, MA, kh);
			if (r == 1)
			{
				res[i]++;
				M = kh;
			}
			else
				break;
		} while (M.n > 0);
		if (res[i] == 0)
			b++;
		if (i > b && i > 0)
			cout << " * ";
		if (i == 0)
		{
			if (res[i] > 1)
				cout << "x^" << res[i];
			else if (res[i] == 1)
				cout << "x";
		}
		else
		{
			if (res[i] > 1)
				cout << "(x - " << i << ")^" << res[i];
			else if (res[i] == 1)
				cout << "(x - " << i << ")";
		}
	}
	return 0;
}