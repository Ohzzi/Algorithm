#include <iostream>
#include <ctime>
#include <algorithm>

class conference {
public:
	int t_start, t_end;

	bool operator <(conference& conf) {
		if (this->t_end == conf.t_end) {
			return this->t_start < conf.t_start; // 둘의 끝나는 시간이 같으면 시작 시간이 빠른 회의를 앞으로 정렬
		}
		else return this->t_end < conf.t_end;
	}
};

int main() {
	int N, t = 0, count = 0;
	clock_t start, end;
	std::cin >> N;
	start = clock();
	conference* conf = new conference[N];
	for (int i = 0; i < N; i++) {
		std::cin >> conf[i].t_start >> conf[i].t_end;
	}
	std::sort(conf, conf + N); // 끝나는 시간 기준으로 오름차순 정렬
	
	for (int i = 0; i < N; i++) {
		if (conf[i].t_start >= t) {
			t = conf[i].t_end;
			count++;
		}
	}
	end = clock();
	std::cout << count << std::endl;
	std::cout << end - start << std::endl;
}