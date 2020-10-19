#include<iostream>
#include<queue>
#include<vector>
#include<string.h>
using namespace std;

int main(int argc, char** argv) {
	int test_case;
	int T;
	cin >> T;
	for (test_case = 1; test_case <= T; ++test_case) {
		int N, M, K, A, B; cin >> N >> M >> K >> A >> B;

		int a_time[10], b_time[10]; //창구 처리 시간
		for (int i = 1; i <= N; i++) cin >> a_time[i];
		for (int i = 1; i <= M; i++) cin >> b_time[i];

		int a_seat[10]; int a_rest_time[10]; int a_number[10];  //접수창구 정보
		int b_seat[10]; int b_rest_time[10]; int b_number[10];  //정비창구 정보
		int list[1001]; for (int i = 1; i <= K; i++) cin >> list[i]; //고객 번호 & 시간

		memset(a_seat, -1, sizeof(a_seat));
		memset(a_rest_time, -1, sizeof(a_rest_time));
		memset(a_number, -1, sizeof(a_number));

		memset(b_seat, -1, sizeof(b_seat));
		memset(b_rest_time, -1, sizeof(b_rest_time));
		memset(b_number, -1, sizeof(b_number));

		queue<int> a_wait, b_wait; //접수 창구 & 정비 창구 대기줄
		vector<int> a_ans, b_ans; //답 도출 vector

		int cnt = 0, time = 0; //정비를 마친 인원 check & 시간 설정
		while (cnt != K) { //시뮬레이션 시작
			for (int i = 1; i <= K; i++) { //도착한 사람들 줄세우기
				if (list[i] == time) //도착했을시
					a_wait.push(i); //번호표로 줄세우기
			}

			for (int i = 1; i <= N; i++) { //접수 마무리
				if (a_rest_time[i] == 0) { //접수 종료시
					a_rest_time[i] = -1; //시간 초기화
					a_seat[i] = -1; //자리 비움 표시
					b_wait.push(a_number[i]); //접수 마무리한사람 정비 줄 세우기
					a_number[i] = -1;
				}
			}

			for (int i = 1; i <= M; i++) { //정비 마무리
				if (b_rest_time[i] == 0) { //정비 종료시
					b_rest_time[i] = -1;
					b_seat[i] = -1;
					b_number[i] = -1;
					cnt++;
				}
			}

			////////////////////////////////////////////////////////////////

			if (!a_wait.empty()) { //접수 창구줄에 서있는 사람이 있는 경우
				for (int i = 1; i <= N; i++) {
					if (a_seat[i] == -1 && !a_wait.empty()) { //자리가 있는경우 // 접수창구로 보내기
						a_seat[i] = 1; //자리 만석 표시
						a_number[i] = a_wait.front(); //번호표 표시
						a_rest_time[i] = a_time[i];
						a_wait.pop();

						if (A == i) a_ans.push_back(a_number[i]); //역학조사
					}
				}
			}

			if (!b_wait.empty()) { //정비 창구줄에 서있는 사람이 있는 경우
				for (int i = 1; i <= M; i++) {
					if (b_seat[i] == -1 && !b_wait.empty()) { //자리가 있는 경우
						b_seat[i] = 1;
						b_number[i] = b_wait.front();
						b_rest_time[i] = b_time[i];
						b_wait.pop();

						if (B == i) b_ans.push_back(b_number[i]); //역학조사
					}
				}
			}
			//////////////////////////////////////////////////////////////
			for (int i = 1; i <= N; i++) a_rest_time[i]--;
			for (int i = 1; i <= M; i++) b_rest_time[i]--;
			time++;
		}

		int ans = 0;
		for (int i = 0; i < a_ans.size(); i++) {
			for (int j = 0; j < b_ans.size(); j++) {
				if (a_ans[i] == b_ans[j]) ans += a_ans[i];
			}
		}
		if (ans == 0) ans = -1;
		cout << "#" << test_case << " " << ans << endl;
	}
	return 0;
}