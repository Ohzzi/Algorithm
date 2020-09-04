#include <iostream>
#include <cmath>

int main() {
	int check[1001] = { 1, 1, 0, };
	int number[100];
	int n, cnt = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &number[i]);
	}
	for (int i = 3; i <= 1000; i++) {
		for (int j = 2; j <= sqrt(i); j++) {
			if (i % j == 0 && check[i] == 0) {
				check[i] = 1;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		if (!check[number[i]]) cnt++;
	}
	printf("%d", cnt);
	return 0;
}

/*
����
�־��� �� N�� �߿��� �Ҽ��� �� ������ ã�Ƽ� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
ù �ٿ� ���� ���� N�� �־�����. N�� 100�����̴�. �������� N���� ���� �־����µ� ���� 1,000 ������ �ڿ����̴�.
���
�־��� ���� �� �Ҽ��� ������ ����Ѵ�.
*/