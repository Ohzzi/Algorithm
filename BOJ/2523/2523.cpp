#include <iostream>
#include <cmath>

int main() {
	int n;
	std::cin >> n;
	for (int i = 0; i < 2 * n - 1; i++) {
		for (int j = 0; j < n - abs(i - n + 1); j++) {
			std::cout << '*';
		}
		std::cout << std::endl;
	}
	return 0;
}