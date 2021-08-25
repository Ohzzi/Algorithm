#include <iostream>
#include <cmath>

int main() {
	int n, m;
	scanf("%d %d", &m, &n);
	int* numbers = new int[n + 1];
	for (int i = 0; i <= n; i++) {
		numbers[i] = 1;
	}
	numbers[0] = 0;
	numbers[1] = 0;
	for (int i = m; i <= n; i++) {
		int root = sqrt(i);
		for (int j = 2; j <= root; j++) {
			if (numbers[i] == 1 && i % j == 0) {
				numbers[i] = 0;
			}
		}
	}
	for (int i = m; i <= n; i++) {
		if (numbers[i] == 1) printf("%d\n", i);
	}
	return 0;
}


/*
����
M�̻� N������ �Ҽ��� ��� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
ù° �ٿ� �ڿ��� M�� N�� �� ĭ�� ���̿� �ΰ� �־�����. (1 �� M �� N �� 1,000,000) M�̻� N������ �Ҽ��� �ϳ� �̻� �ִ� �Է¸� �־�����.
���
�� �ٿ� �ϳ���, �����ϴ� ������� �Ҽ��� ����Ѵ�.
*/