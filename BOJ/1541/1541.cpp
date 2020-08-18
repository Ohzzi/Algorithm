#include <iostream>
#include <ctime>
#include <string>

int main() {
	int result = 0, temp = 0, i = 0;
	bool check = true;
	clock_t start, end;

	std::string str;
	std::cin >> str;

	start = clock();
	while (i < str.length()) {
		if (isalnum(str[i])) {
			temp *= 10;
			temp += (str[i] - '0');
		}
		else {
			result += temp;
			temp = 0;
			if (str[i] == '-') {
				i++;
				check = false;
				break;
			}
		}
		i++;
	}
	while (!check && i < str.length()) {
		if (isalnum(str[i])) {
			temp *= 10;
			temp += (str[i] - '0');
		}
		else {
			result -= temp;
			temp = 0;
		}
		i++;
	}

	if (check) result += temp;
	else result -= temp;

	std::cout << result << std::endl;
	end = clock();
	std::cout << end - start << std::endl;
}