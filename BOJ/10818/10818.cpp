/*
����
N���� ������ �־�����. �̶�, �ּڰ��� �ִ��� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
ù° �ٿ� ������ ���� N (1 �� N �� 1,000,000)�� �־�����. ��° �ٿ��� N���� ������ �������� �����ؼ� �־�����.
��� ������ -1,000,000���� ũ�ų� ����, 1,000,000���� �۰ų� ���� �����̴�.
*/

#include <iostream>

int main() {
	int n;
	std::cin >> n;
	int* arr = new int[n];
	for (int i = 0; i < n; i++) {
		std::cin >> arr[i];
	}
	int max = arr[0], min = arr[0];
	for (int i = 0; i < n; i++) {
		if (arr[i] < min) min = arr[i];
		if (arr[i] > max) max = arr[i];
	}
	printf("%d %d", min, max);

	return 0;
}