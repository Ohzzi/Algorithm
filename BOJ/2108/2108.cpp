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
문제
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

출력
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

둘째 줄에는 중앙값을 출력한다.

셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

넷째 줄에는 범위를 출력한다.
*/