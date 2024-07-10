# 2. 중급 문제
from task1 import Student


## 문제 3: 성적 계산 기능 추가
class GradedStudent(Student):
    def __init__(self, name, age, grade):
        super().__init__(name, age, grade)
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def calculate_average(self):
        # scores 리스트의 평균을 계산하여 반환하는 메서드를 작성하세요.
        # YOUR CODE HERE
        if not self.scores:
            return 0
        avg = sum(self.scores) / len(self.scores)
        return avg

    def get_score(self, hours):
        if hours < 4:
            return 20
        elif hours < 8:
            return 50
        elif hours < 16:
            return 100
        else:
            return 40

    def study(self, hours):
        super().study(hours)
        # 공부한 시간에 비례하여 임의의 점수를 생성하고 add_score 메서드를 호출하세요.
        # YOUR CODE HERE
        score = self.get_score(hours)
        self.add_score(score)
        print(
            f"""{hours} 시간 공부한 {self.name}은/는 이번 시험에서 {score} 점을 받았습니다."""
        )


# GradedStudent 클래스의 객체를 생성하고, 여러 번 study 메서드를 호출한 후 평균 점수를 계산해보세요.
# YOUR CODE HERE
if __name__ == "__main__":
    student = GradedStudent("철수", "18", "3")
    student.study(14)
    student.study(1)
    student.study(6)
    student.study(19)
    print(f"{student.name}의 평균 점수는 {student.calculate_average()}입니다.")
