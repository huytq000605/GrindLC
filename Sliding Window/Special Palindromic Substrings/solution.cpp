// 6sense interview question
// Given a stream of characters, where the whole stream could not be fitted into memory
// Count how many special palindromic substrings
// Special palindromic string means a string with all same characters or having only 1 different character at the middle

#include<string>
#include<queue>
#include<iostream>

using namespace std;

int solve(string&& s) {
  int result{};
  deque<pair<char, int>> dq;
  for(char c: s) {
    if(!dq.empty() && dq.back().first == c) {
      dq.back().second += 1;
    } else {
      if(!dq.empty()) {
        result += dq.back().second * (dq.back().second + 1) / 2;
      }
      if(dq.size() == 3 && dq[1].second == 1 && dq.front().first == dq.back().first) {
        result += min(dq.front().second, dq.back().second);
      }
      if(dq.size() == 3) {
        dq.pop_front();
      }
      dq.emplace_back(c, 1);
    }
  }

  if(!dq.empty()) {
    result += dq.back().second * (dq.back().second + 1) / 2;
  }
  if(dq.size() == 3 && dq[1].second == 1 && dq[0].first == dq[2].first) {
    result += min(dq.front().second, dq.back().second);
  }

  return result;
}


int main() {
  cout << solve("aaabaaaacaa") << endl; // 26
}

