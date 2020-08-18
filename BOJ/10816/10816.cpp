#include <iostream>
#include <algorithm>
#include <iterator>
#include <ctime>

/*
����
���� ī��� ���� �ϳ��� ������ �ִ� ī���̴�. ����̴� ���� ī�� N���� ������ �ִ�. ���� M���� �־����� ��,
�� ���� �����ִ� ���� ī�带 ����̰� �� �� ������ �ִ��� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.

�Է�
ù° �ٿ� ����̰� ������ �ִ� ���� ī���� ���� N(1 �� N �� 500,000)�� �־�����. ��° �ٿ��� ���� ī�忡 �����ִ� ������ �־�����.
���� ī�忡 �����ִ� ���� -10,000,000���� ũ�ų� ����, 10,000,000���� �۰ų� ����.
��° �ٿ��� M(1 �� M �� 500,000)�� �־�����. ��° �ٿ��� ����̰� �� �� ������ �ִ� ���� ī������ ���ؾ� �� M���� ������ �־�����,
�� ���� �������� ���еǾ��� �ִ�. �� ���� -10,000,000���� ũ�ų� ����, 10,000,000���� �۰ų� ����.

���
ù° �ٿ� �Է����� �־��� M���� ���� ���ؼ�, �� ���� ���� ���� ī�带 ����̰� �� �� ������ �ִ����� �������� ������ ����Ѵ�.
*/

int main() {
	int n, m;
	clock_t start, end;
	
	std::cin >> n;
	int* card = new int[n];
	for (int i = 0; i < n; i++) {
		std::cin >> card[i];
	}
	std::cin >> m;
	int* integer = new int[m];
	for (int i = 0; i < m; i++) {
		std::cin >> integer[i];
	}
	std::cout << std::endl;

	start = clock();

	std::sort(card, card + n);

	for (int i = 0; i < m; i++) {
		int result = std::upper_bound(card, card + n, integer[i]) - std::lower_bound(card, card + n, integer[i]);
		std::cout << result << " ";
	}
	std::cout << std::endl << std::endl;

	end = clock();
	std::cout << end - start << std::endl;

	return 0;
	
}