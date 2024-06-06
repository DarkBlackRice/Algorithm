#include <iostream>

using namespace std;

string test1();
string test2();

void main() // entry point
{
	//test1();

	test2();
}

string test1()
{
	string result;

	result = "Hello, World!";

	cout << test1() << endl;

	return result;
}

string test2()
{
	string result;

	cin >> result;

	cout << result << endl;

	return result;
}