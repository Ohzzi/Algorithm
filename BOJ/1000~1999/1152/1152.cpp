/*
����
���� ��ҹ��ڿ� ���⸸���� �̷���� ���ڿ��� �־�����. �� ���ڿ����� �� ���� �ܾ ������? �̸� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
��, �� �ܾ ���� �� �����ϸ� ������ Ƚ����ŭ ��� ����� �Ѵ�.
�Է�
ù �ٿ� ���� ��ҹ��ڿ� ����� �̷���� ���ڿ��� �־�����. �� ���ڿ��� ���̴� 1,000,000�� ���� �ʴ´�.
�ܾ�� ���� �� ���� ���еǸ�, ������ �����ؼ� ������ ���� ����. ���� ���ڿ��� �հ� �ڿ��� ������ ���� ���� �ִ�.
*/

#include <iostream>
#include <string>
#include <sstream>

int main() {
	std::string str, tmp;
	int count = 0;
	std::getline(std::cin, str);
	std::stringstream ss(str);
	while (ss >> tmp) { // ���ڿ��� ������ ��ū���� �и�
		count++;
	}
	std::cout << count;
	return 0;
}