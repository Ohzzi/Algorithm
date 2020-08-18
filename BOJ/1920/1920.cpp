#include <iostream>
#include <algorithm>
#include <ctime>

/*문제
/*N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
/*입력
/*첫째 줄에 자연수 N(1≤N≤100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1≤M≤100,000)이 주어진다.
/*다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.
/*출력
/*M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.*/

bool check(int* arr, int n, int size) {
	int	left = 0, mid, right = size - 1;
	while (left <= right) {
		mid = (left + right) / 2;
		if (n == arr[mid]) {
			return true;
		}
		else if (n < arr[mid]) {
			right = mid - 1;
		}
		else {
			left = mid + 1;
		}
	}
	return false;
}

int main() {
	int n, m;
	clock_t start, end;

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
	std::cout << std::endl;

	start = clock();

	std::sort(A, A + n);

	for (int i = 0; i < m; i++) {
		if (check(A, B[i], n)) {
			std::cout << 1 << std::endl;
		}
		else {
			std::cout << 0 << std::endl;
		}
	}

	end = clock();
	std::cout << std::endl << end - start << std::endl;

	return 0;
}