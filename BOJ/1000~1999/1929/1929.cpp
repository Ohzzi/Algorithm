#include <iostream>
#include <cmath>

int main() {
	int m, n;
	scanf("%d %d", &m, &n);
	for (int i = m; i <= n; i++) {
		bool check = true;
		int root = sqrt(i);
		if (i == 1) check = false;
		if (i % 2 == 0 && i != 2) {
			check = false;
		}
		else {
			for (int j = 2; j <= root; j++) {
				if (i % j == 0) {
					check = false;
					break;
				}
			}
		}
		if (check) {
			printf("%d\n", i);
		}
	}
	return 0;
}
/*
문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
*/