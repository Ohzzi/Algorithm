#include <iostream>
#include <cmath>
#include <algorithm>
#include <map>

int average(int* number, int n) {
	int sum = 0;
	for (int i = 0; i < n; i++) {
		sum += number[i];
	}
	double result = round((double)sum / (double)n);
	return (int)result;
}

int middle(int* number, int n) {
	return (double) number[n / 2];
}

int mode(int* number, int n) {
	std::map<int, int> map;
	for (int i = 0; i < n; i++) {
		map[number[i]]++;
	}
	std::map<int, int>::iterator tmp;
	int get = -1, pos = 0;
	for (auto it = map.begin(); it != map.end(); it++) {
		if (it->second > get) {
			get = it->second;
			pos = it->first;
			tmp = it;
		}
	}
	tmp++;
	for (tmp; tmp != map.end(); tmp++) {
		if (tmp->second == get) {
			pos = tmp->first;
			break;
		}
	}
	return pos;
}

int main() {
	int n;
	scanf("%d", &n);
	int* number = new int[n];
	for (int i = 0; i < n; i++) {
		scanf("%d", &number[i]);
	}
	std::sort(number, number + n);
	printf("%d\n%d\n%d\n%d\n", average(number, n), middle(number, n), mode(number, n), number[n - 1] - number[0]);
	return 0;
}

/*
����
���� ó���ϴ� ���� ����п��� ����� �߿��� ���̴�. ����п��� N���� ���� ��ǥ�ϴ� �⺻ ��谪���� ������ ���� �͵��� �ִ�. ��, N�� Ȧ����� ��������.

������ : N���� ������ ���� N���� ���� ��
�߾Ӱ� : N���� ������ �����ϴ� ������ �������� ��� �� �߾ӿ� ��ġ�ϴ� ��
�ֺ� : N���� ���� �� ���� ���� ��Ÿ���� ��
���� : N���� ���� �� �ִ񰪰� �ּڰ��� ����
N���� ���� �־����� ��, �� ���� �⺻ ��谪�� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.

�Է�
ù° �ٿ� ���� ���� N(1 �� N �� 500,000)�� �־�����. �� ���� N���� �ٿ��� �������� �־�����. �ԷµǴ� ������ ������ 4,000�� ���� �ʴ´�.

���
ù° �ٿ��� �������� ����Ѵ�. �Ҽ��� ���� ù° �ڸ����� �ݿø��� ���� ����Ѵ�.

��° �ٿ��� �߾Ӱ��� ����Ѵ�.

��° �ٿ��� �ֺ��� ����Ѵ�. ���� �� ���� ������ �ֺ� �� �� ��°�� ���� ���� ����Ѵ�.

��° �ٿ��� ������ ����Ѵ�.
*/