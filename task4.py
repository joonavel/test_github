## 문제 4: 다중 상속을 이용한 운동선수 학생 클래스
from task3 import GradedStudent


class Athlete:
    def __init__(self, sport):
        self.sport = sport

    def train(self, hours):
        print(f"{self.sport} 종목에서 {hours}시간 동안 훈련했습니다.")


class StudentAthlete(GradedStudent, Athlete):
    def __init__(self, name, age, grade, sport):
        # GradedStudent와 Athlete의 __init__ 메서드를 모두 호출하세요.
        # YOUR CODE HERE
        GradedStudent.__init__(self, name, age, grade)
        Athlete.__init__(self, sport)

    def study(self, s_hours, t_hours):
        # GradedStudent의 study 메서드를 호출하고, 추가로 train 메서드도 호출하세요.
        # YOUR CODE HERE
        GradedStudent.study(self, s_hours)
        Athlete.train(self, t_hours)


# StudentAthlete 클래스의 객체를 생성하고 study 메서드를 호출해보세요.
# YOUR CODE HERE
if __name__ == "__main__":
    sa = StudentAthlete("호준", 19, 3, "태권도")
    sa.study(8, 3)
    sa.study(8, 6)
    sa.study(16, 0)
    sa.study(3, 10)
    sa.study(1, 1)
    sa.study(12, 12)
    print(f"{sa.name}의 평균 점수는 {sa.calculate_average()}입니다.")
