#include <iostream>

int main() {
	int n;
	std::cin >> n;
	int num = 2 * n - 1;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i; j++) {
			std::cout << ' ';
		}
		for (int j = 0; j < num - i * 2; j++) {
			std::cout << '*';
		}
		std::cout << std::endl;
	}
	for (int i = n; i < num; i++) {
		for (int j = 0; j < num - i - 1; j++) {
			std::cout << ' ';
		}
		for (int j = 0; j < i * 2 - num + 2; j++) {
			std::cout << '*';
		}
		std::cout << std::endl;
	}

	return 0;
}