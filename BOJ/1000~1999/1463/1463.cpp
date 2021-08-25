/*
����
���� X�� ����� �� �ִ� ������ ������ ���� �� ���� �̴�.

X�� 3���� ������ ��������, 3���� ������.
X�� 2�� ������ ��������, 2�� ������.
1�� ����.
���� N�� �־����� ��, ���� ���� ���� �� ���� ������ ����ؼ� 1�� ������� �Ѵ�. ������ ����ϴ� Ƚ���� �ּڰ��� ����Ͻÿ�.

�Է�
ù° �ٿ� 1���� ũ�ų� ����, 10^6���� �۰ų� ���� ���� N�� �־�����.
*/

#include <iostream>
#include <algorithm>

int main(){
	int n;
	scanf("%d", &n);
	int* count = new int[n + 1];
	for (int i = 0; i < n; i++) {
		count[i] = 0;
	}

	for (int i = 2; i <= n; i++) {
		if (i % 3 == 0 && i % 2 == 0) {
			count[i] = std::min(std::min(count[i / 3], count[i / 2]), count[i - 1]) + 1;
		}
		else if (i % 3 != 0 && i % 2 == 0) {
			count[i] = std::min(count[i / 2], count[i - 1]) + 1;
		}
		else if (i % 3 == 0 && i % 2 != 0) {
			count[i] = std::min(count[i / 3], count[i - 1]) + 1;
		}
		else {
			count[i] = count[i - 1] + 1;
		}
	}
	printf("%d", count[n]);

	return 0;
}