/*
����
N���� ���� �־����� ��, �̸� ������������ �����ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
ù° �ٿ� ���� ���� N(1 �� N �� 1,000,000)�� �־�����. ��° �ٺ��� N���� �ٿ��� ���ڰ� �־�����.
�� ���� ������ 1,000,000���� �۰ų� ���� �����̴�. ���� �ߺ����� �ʴ´�.
*/

#include <iostream>
#include <algorithm>

int main() {
	int n;
	scanf("%d", &n);
	int* arr = new int[n];
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}
	std::sort(arr, arr + n);
	for (int i = 0; i < n; i++) {
		printf("%d\n", arr[i]);
	}
	return 0;
}