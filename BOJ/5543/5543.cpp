#include <iostream>

/*
����
��ٳ��忡�� ���� �� �ȸ��� �޴��� ��Ʈ �޴��̴�.�ֹ��� ��, �ڽ��� ���ϴ� �ܹ��ſ� ���Ḧ �ϳ��� ���,
��Ʈ�� �����ϸ�, ������ �հ迡�� 50���� �� ������ ��Ʈ �޴��� ������ �ȴ�.
�ܹ��Ŵ� �� 3���� �������, �ߴ�����, �ϴ����Ű� �ְ�, ����� �ݶ�� ���̴� �� ������ �ִ�.
�ܹ��ſ� ������ ������ �־����� ��, ���� �� ��Ʈ �޴��� ������ ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
*/

int main() {
	int burgers[3], drinks[2];
	int price = 0, tmp;

	for (int i = 0; i < 3; i++) {
		std::cin >> burgers[i];
	}
	for (int i = 0; i < 2; i++) {
		std::cin >> drinks[i];
	}
	tmp = (burgers[0] < burgers[1]) ? burgers[0] : burgers[1];
	tmp = (tmp < burgers[2]) ? tmp : burgers[2];
	price += tmp;
	price += (drinks[0] < drinks[1]) ? drinks[0] : drinks[1];
	price -= 50;
	std::cout << price << std::endl;

	return 0;
}