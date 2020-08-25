/*
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.
입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
*/

#include <iostream>

void printMax(int arr[], int size) {
	int	max = 0;
	bool check = false;
	for (int i = 1; i < size; i++) {
		if (arr[i] > arr[max]) {
			max = i;
			check = false;
		}
		else if (arr[i] == arr[max]) {
			check = true;
		}
	}
	if (check) printf("?");
	else printf("%c", max + 65);
}

int main() {
	int alphabet[26];
	std::fill(alphabet, alphabet + 26, 0);
	std::string str;
	std::cin >> str;
	for (int i = 0; i < str.length(); i++) {
		if (str[i] >= 65 && str[i] <= 90)
			alphabet[str[i] - 65]++;
		else if (str[i] >= 97 && str[i] <= 122)
			alphabet[str[i] - 97]++;
	}
	printMax(alphabet, 26);
	return 0;
}