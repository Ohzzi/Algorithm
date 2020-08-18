#include <iostream>
#include <algorithm>
#include <ctime>

/*����
/*N���� ���� A[1], A[2], ��, A[N]�� �־��� ���� ��, �� �ȿ� X��� ������ �����ϴ��� �˾Ƴ��� ���α׷��� �ۼ��Ͻÿ�.
/*�Է�
/*ù° �ٿ� �ڿ��� N(1��N��100,000)�� �־�����. ���� �ٿ��� N���� ���� A[1], A[2], ��, A[N]�� �־�����. ���� �ٿ��� M(1��M��100,000)�� �־�����.
/*���� �ٿ��� M���� ������ �־����µ�, �� ������ A�ȿ� �����ϴ��� �˾Ƴ��� �ȴ�. ��� ������ ������ -231 ���� ũ�ų� ���� 231���� �۴�.
/*���
/*M���� �ٿ� ���� ����Ѵ�. �����ϸ� 1��, �������� ������ 0�� ����Ѵ�.*/

void check(int* arr, int n, int size) {
	int	left = 0, mid, right = size - 1;
	while (left <= right) {
		mid = (left + right) / 2;
		if (n == arr[mid]) {
			std::cout << "1\n";
			return;
		}
		else if (n < arr[mid]) {
			right = mid - 1;
		}
		else {
			left = mid + 1;
		}
	}
	std::cout << "0\n";
	return;
}

int main() {
	int n, m;

	std::cin >> n;
	int* A = new int[n];
	for (int i = 0; i < n; i++) {
		std::cin >> A[i];
	}
	std::cin >> m;
	int* B = new int[m];
	for (int i = 0; i < m; i++) {
		std::cin >> B[i];
	}

	std::sort(A, A + n);

	for (int i = 0; i < m; i++) {
		check(A, B[i], n);
	}

	return 0;
}