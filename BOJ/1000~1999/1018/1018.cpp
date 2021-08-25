#include <iostream>

std::string WB[8] = {
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW"
};
std::string BW[8] = {
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB"
};

int count(std::string board[], int x, int y) {
	int cntBW = 0, cntWB = 0;
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			if (board[y + i][x + j] != BW[i][j]) cntBW++;
			if (board[y + i][x + j] != WB[i][j]) cntWB++;
		}
	}
	if (cntBW < cntWB) return cntBW;
	else return cntWB;
}

int main() {
	int n, m, min = 9999;
	scanf("%d %d", &n, &m);
	std::string* board = new std::string[n];
	for (int i = 0; i < n; i++) {
		std::cin >> board[i];
	}
	for (int i = 0; i <= n - 8; i++) {
		for (int j = 0; j <= m - 8; j++) {
			int cnt = count(board, j, i);
			if (cnt < min) min = cnt;
		}
	}
	printf("%d", min);
	return 0;
}

/*
����
�����̴� �ڽ��� ���ÿ��� MN���� ���� ���簢������ �������� �ִ� M*N ũ���� ���带 ã�Ҵ�. � ���簢���� ���������� ĥ���� �ְ�, �������� ������� ĥ���� �ִ�.
�����̴� �� ���带 �߶� 8*8 ũ���� ü�������� ������� �Ѵ�.
ü������ �������� ����� �����Ƽ� ĥ���� �־�� �Ѵ�. ��ü������, �� ĭ�� �������� ��� �� �ϳ��� ��ĥ�Ǿ� �ְ�, ���� �����ϴ� �� ���� �簢���� �ٸ� ������ ĥ���� �־�� �Ѵ�.
���� �� ���Ǹ� ������ ü������ ��ĥ�ϴ� ���� �� �������̴�. �ϳ��� �� ���� �� ĭ�� ����� ���, �ϳ��� �������� ����̴�.
���尡 ü����ó�� ĥ���� �ִٴ� ������ ���, �����̴� 8*8 ũ���� ü�������� �߶� �Ŀ� �� ���� ���簢���� �ٽ� ĥ�ؾ߰ڴٰ� �����ߴ�. �翬�� 8*8 ũ��� �ƹ������� ��� �ȴ�.
�����̰� �ٽ� ĥ�ؾ� �ϴ� ���簢���� �ּ� ������ ���ϴ� ���α׷��� �ۼ��Ͻÿ�.

�Է�
ù° �ٿ� N�� M�� �־�����. N�� M�� 8���� ũ�ų� ����, 50���� �۰ų� ���� �ڿ����̴�. ��° �ٺ��� N���� �ٿ��� ������ �� ���� ���°� �־�����. B�� �������̸�, W�� ����̴�.

���
ù° �ٿ� �����̰� �ٽ� ĥ�ؾ� �ϴ� ���簢�� ������ �ּڰ��� ����Ѵ�.
*/