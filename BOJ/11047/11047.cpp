#include <iostream>
#include <time.h>

using namespace std;

int main() {
	int N, K;
	int count = 0;
	cin >> N >> K;
	int* price = new int[N];
	for (int i = 0; i < N; i++) {
		cin >> price[i];
	}
	for (int i = N-1; i >=0; i--) {
		count += K / price[i];
		K = K % price[i];
	}
	cout << count << endl;
}