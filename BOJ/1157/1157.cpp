/*
����
���ĺ� ��ҹ��ڷ� �� �ܾ �־�����, �� �ܾ�� ���� ���� ���� ���ĺ��� �������� �˾Ƴ��� ���α׷��� �ۼ��Ͻÿ�.
��, �빮�ڿ� �ҹ��ڸ� �������� �ʴ´�.
�Է�
ù° �ٿ� ���ĺ� ��ҹ��ڷ� �̷���� �ܾ �־�����. �־����� �ܾ��� ���̴� 1,000,000�� ���� �ʴ´�.
���
ù° �ٿ� �� �ܾ�� ���� ���� ���� ���ĺ��� �빮�ڷ� ����Ѵ�.
��, ���� ���� ���� ���ĺ��� ���� �� �����ϴ� ��쿡�� ?�� ����Ѵ�.
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