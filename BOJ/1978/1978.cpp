#include <iostream>
#include <cmath>

int main() {
	int check[1001] = { 1, 1, 0, };
	int number[100];
	int n, cnt = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &number[i]);
	}
	for (int i = 3; i <= 1000; i++) {
		for (int j = 2; j <= sqrt(i); j++) {
			if (i % j == 0 && check[i] == 0) {
				check[i] = 1;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		if (!check[number[i]]) cnt++;
	}
	printf("%d", cnt);
	return 0;
}

/*
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
출력
주어진 수들 중 소수의 개수를 출력한다.
*/