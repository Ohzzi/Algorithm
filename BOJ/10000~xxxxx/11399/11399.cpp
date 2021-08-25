#include <iostream>
#include <algorithm>
#include <ctime>

int main() {
	int n, t = 0, result = 0;
	std::cin >> n;
	int* people = new int[n];
	for (int i = 0; i < n; i++) {
		std::cin >> people[i];
	}
	std::sort(people, people + n);
	for (int i = 0; i < n; i++) {
		t += people[i];
		result += t;
	}
	std::cout << result << std::endl;
}