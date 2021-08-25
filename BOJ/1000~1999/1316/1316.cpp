#include <iostream>

bool isGroupWord(std::string str) {
	bool check[26] = { false, };
	int i = 0;
	while (i < str.length() - 1) {
		if (str[i] != str[i + 1]) {
			check[str[i] - 'a'] = true;
			if (check[str[i + 1] - 'a']) return false;
		}
		i++;
	}
	return true;
}

int main() {
	int n, cnt = 0;
	scanf("%d", &n);
	std::string str[100];
	for (int i = 0; i < n; i++) {
		std::cin >> str[i];
		if (isGroupWord(str[i])) cnt++;
	}
	printf("%d", cnt);
	return 0;
}

/*
����
�׷� �ܾ�� �ܾ �����ϴ� ��� ���ڿ� ���ؼ�, �� ���ڰ� �����ؼ� ��Ÿ���� ��츸�� ���Ѵ�.
���� ���, ccazzzzbb�� c, a, z, b�� ��� �����ؼ� ��Ÿ����, kin�� k, i, n�� �����ؼ� ��Ÿ���� ������ �׷� �ܾ�������,
aabbbccb�� b�� �������� ��Ÿ���� ������ �׷� �ܾ �ƴϴ�.
�ܾ� N���� �Է����� �޾� �׷� �ܾ��� ������ ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
ù° �ٿ� �ܾ��� ���� N�� ���´�. N�� 100���� �۰ų� ���� �ڿ����̴�.
��° �ٺ��� N���� �ٿ� �ܾ ���´�. �ܾ�� ���ĺ� �ҹ��ڷθ� �Ǿ��ְ� �ߺ����� ������, ���̴� �ִ� 100�̴�.
���
ù° �ٿ� �׷� �ܾ��� ������ ����Ѵ�.
*/