#include <iostream>
#include <algorithm>

int num[10];

int main() {
	int n, cnt = 0;
	scanf("%d", &n);
	while (n != 0) {
		num[cnt++] = n % 10;
		n /= 10;
	}
	std::sort(num, num + cnt);
	for (int i = cnt-1; i >= 0; i--) {
		printf("%d", num[i]);
	}
	return 0;
}

/*
����
�迭�� �����ϴ� ���� ����. ���� �־�����, �� ���� �� �ڸ����� ������������ �����غ���.

�Է�
ù° �ٿ� �����ϰ����ϴ� �� N�� �־�����. N�� 1,000,000,000���� �۰ų� ���� �ڿ����̴�.

���
ù° �ٿ� �ڸ����� ������������ ������ ���� ����Ѵ�.
*/