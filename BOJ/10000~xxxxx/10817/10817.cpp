/*문제
세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. */

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