#include <iostream>

int countCroatia(std::string str) {
	int cnt = 0;
	for (int i = 0; i < str.length(); i++) {
		cnt++;
		if (i != str.length() - 1) {
			switch (str[i]) {
			case 'c':
				if (str[i + 1] == '=' || str[i + 1] == '-') {
					i++;
				}
				break;
			case 'd':
				if (i < str.length() - 2 && str[i + 1] == 'z' && str[i + 2] == '=') {
					i += 2;
				}
				else if (str[i + 1] == '-') {
					i++;
				}
				break;
			case 'l':
				if (str[i + 1] == 'j') i++;
				break;
			case 'n':
				if (str[i + 1] == 'j') i++;
				break;
			case 's':
				if (str[i + 1] == '=') i++;
				break;
			case 'z':
				if (str[i + 1] == '=') i++;
				break;
			default:
				break;
			}
		}
	}
	return  cnt;
}

int main() {
	std::string str;
	std::cin >> str;
	printf("%d", countCroatia(str));
	return 0;
}