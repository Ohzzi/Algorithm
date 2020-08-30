#include <iostream>
#include <cmath>

int main() {
	int m, n;
	scanf("%d %d", &m, &n);
	for (int i = m; i <= n; i++) {
		bool check = true;
		int root = sqrt(i);
		if (i == 1) check = false;
		if (i % 2 == 0 && i != 2) {
			check = false;
		}
		else {
			for (int j = 2; j <= root; j++) {
				if (i % j == 0) {
					check = false;
					break;
				}
			}
		}
		if (check) {
			printf("%d\n", i);
		}
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