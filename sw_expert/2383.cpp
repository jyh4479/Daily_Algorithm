#include<iostream>
#include<queue>
#include<vector>
#include<string.h>
#include<bitset>
#include<cmath>
using namespace std;

int map[15][15] = { 0 }; //방 선언
int p[10] = { 0 }; //들어갈 계단 설정

class man { //사람 정보를 가질 객체 생성
public:
	int i, j;
	int time1, time2;

	man(int i, int j, int time1, int time2) {
		this->i = i;
		this->j = j;
		this->time1 = time1;
		this->time2 = time2;
	}
};

class stair {
public:
	int i, j, used;
	stair(int i, int j, int used) {
		this->i = i;
		this->j = j;
		this->used = used;
	}
	stair() {
		this->i = 0;
		this->j = 0;
		this->used = 0;
	}
};

int main(int argc, char** argv) {
	int test_case; int T; cin >> T;
	for (test_case = 1; test_case <= T; ++test_case) {
		int N; cin >> N; //방크기 입력
		vector<man> list; //계단에 도착하는 사람 list
		vector<stair> s_list; //계단 위치 정보를 위한 선언

		for (int i = 1; i <= N; i++) {//계단과 사람정보 입력
			for (int j = 1; j <= N; j++) {
				cin >> map[i][j];

				if (map[i][j] != 0 && map[i][j] != 1) { //계단인 경우
					stair newNode(i, j, map[i][j]);
					s_list.push_back(newNode); //계단 정보 입력
				}
			}
		}

		for (int i = 1; i <= N; i++) { //정보 입력
			for (int j = 1; j <= N; j++) {
				if (map[i][j] == 1) { //사람인 경우
					int min, min1, min2, number; //최소 거리를 계산

					min1 = abs((i - s_list[0].i)) + abs((j - s_list[0].j)); //각 계단 까지의 거리 계산
					min2 = abs((i - s_list[1].i)) + abs((j - s_list[1].j));

					man newNode(i, j, min1, min2);
					list.push_back(newNode);
				}
			}
		}

		int time = 0, cnt = 0, ans = 9999;
		for (int i = 0; i < pow(2,list.size()); i++, time = 0, cnt = 0) {
			for (int j = 0; j < list.size(); j++) { //모든 경우 탐색을 위한 조건
				p[j] = bitset<10>(i)[j];
			}

			//Time 시뮬레이션 시작
			queue<man> s1, s2; int s_use1[3], s_use2[3];
			memset(s_use1, -1, sizeof(s_use1));
			memset(s_use2, -1, sizeof(s_use2));

			while (cnt != list.size()) {
				for (int i = 0; i < list.size(); i++) { //계단에 도착한 사람 check
					if (p[i] == 0) {
						if (list[i].time1 == time) { //도착한 경우 계단 줄에 넣기
							s1.push(list[i]);
						}
					}
					else if (p[i] == 1) {
						if (list[i].time2 == time) {
							s2.push(list[i]);
						}
					}
				}

				for (int i = 0; i < 3; i++) { //게단1을 다 내려온사람 check
					if (s_use1[i] == 0) { //다 내려온 경우
						s_use1[i] = -1;   //빈자리로 초기화
						cnt++; //완료되었음을 표시
					}
				}

				for (int i = 0; i < 3; i++) { //게단2을 다 내려온사람 check
					if (s_use2[i] == 0) { //다 내려온 경우
						s_use2[i] = -1;   //빈자리로 초기화
						cnt++; //완료되었음을 표시
					}
				}


				if (!s1.empty()) { //계단1 줄에 사람이 있는경우
					for (int i = 0; i < 3; i++) { //계단에 들어갈 수 있는지 확인
						if (s_use1[i] < 0 && !s1.empty()) { //빈자리가 있는경우
							s_use1[i] = s_list[0].used; //시간 설정
							s1.pop();
						}
					}
				}


				if (!s2.empty()) { //계단2 줄에 사람이 있는경우
					for (int i = 0; i < 3; i++) { //계단에 들어갈 수 있는지 확인
						if (s_use2[i] < 0 && !s2.empty()) { //빈자리가 있는경우
							s_use2[i] = s_list[1].used; //시간 설정
							s2.pop();
						}
					}
				}

				for (int i = 0; i < 3; i++) { s_use1[i]--; s_use2[i]--; }
				time++;
			}
			if (ans > time)
				ans = time;
		}
		cout << "#" << test_case << " " << ans << endl;
	}
	return 0;
}