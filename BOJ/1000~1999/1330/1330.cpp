/*
�� ���� A�� B�� �־����� ��, A�� B�� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
ù° �ٿ� ���� �� ���� �� �ϳ��� ����Ѵ�.

A�� B���� ū ��쿡�� '>'�� ����Ѵ�.
A�� B���� ���� ��쿡�� '<'�� ����Ѵ�.
A�� B�� ���� ��쿡�� '=='�� ����Ѵ�.
*/

#include <iostream>

int main() {
	int a, b;
	scanf("%d %d", &a, &b);
	if (a > b) printf(">");
	else if (a < b) printf("<");
	else if (a == b) printf("==");

	return 0;
}