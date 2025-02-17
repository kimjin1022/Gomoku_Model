# 🏆 Gomoku AI Model

## 📌 프로젝트 개요
🎯 **Gomoku AI Model** 프로젝트는 19x19 바둑판에서 오목을 두는 인공지능을 개발하는 것을 목표로 합니다. 
CNN 기반 모델과 minimax 알고리즘을 활용한 모델을 각각 구현하여 비교하였습니다.

---

## 🧠 CNN 기반 오목 모델
📌 **모델 개요**
- 🎥 [참고 영상](https://www.youtube.com/watch?v=xigPAOl3v7I)을 기반으로 구현하였습니다.
- 원본 영상에서는 **20x20 보드**를 사용하였으나, 이를 **19x19**로 수정하였습니다.

📌 **데이터 처리**
- 📂 `gomocup` 대회의 데이터를 활용하여 모델을 학습하였습니다.
- 원본 기보는 **20x20을 기준**으로 작성되어 있어, **19x19에 맞추기 위해 맨 끝 열에서 둔 기록을 제거**하는 방식으로 전처리하였습니다.

📌 **모델 성능 개선**
- CNN 모델이 **4목 상태에서 경기를 끝내지 않고 수비를 하는 문제**가 발생하여, **경기를 끝낼 수 있는 경우 알고리즘적으로 처리**하여 개선하였습니다.

---

## ♟️ Minimax 기반 오목 모델
📌 **모델 개요**
- CNN 모델이 사용 불가능한 환경에서 새로운 접근법으로 구현되었습니다.
- **가로, 세로, 대각선**을 기준으로 현재 보드의 점수를 계산하여 착수하는 방식으로 구현되었습니다.

📌 **Minimax 알고리즘 적용**
- ♟️ 2수 앞까지 내다보는 방식으로 **`minimax` 알고리즘**을 적용하였습니다.
- 모든 경우의 수를 탐색하면 시간이 오래 걸리므로, **착수 가능 위치를 제한하여 시간을 단축**하였습니다.
  - ⏳ 보통 **1~2초 내에 착수가 가능**하며, **3수 앞까지 보도록 확장하면 10초 이상 소요**됩니다.
- 🏆 비교적 단순한 알고리즘이지만 **실제 플레이에서 예상보다 좋은 성능**을 보였습니다.

---


## 🚀 실행 방법
📌 **추후 GUI 및 추가 기능 업데이트 예정 🚧**

---

## 📚 참고 자료
- 🎥 [YouTube 영상](https://www.youtube.com/watch?v=xigPAOl3v7I)
- 📂 [Gomocup 대회 데이터셋](http://gomocup.org)

---

## 📝 라이선스
📌 **MIT License**
