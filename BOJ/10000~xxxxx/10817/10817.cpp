/*����
�� ���� A, B, C�� �־�����. �̶�, �� ��°�� ū ������ ����ϴ� ���α׷��� �ۼ��Ͻÿ�. */

#include <iostream>

int main() {
	int num[3];
	for (int i = 0; i < 3; i++) {
		std::cin >> num[i];
	}
	if (num[0] > num[1]) std::swap(num[0], num[1]);
	if (num[1] > num[2]) {
		std::swap(num[1], num[2]);
		if (num[0] > num[1]) std::swap(num[0], num[1]);
	}
	std::cout << num[1];

	return 0;
}