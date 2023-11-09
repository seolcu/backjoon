def grade_to_score(grade: str) -> float:
    match grade:
        case "A+":
            return 4.5
        case "A0":
            return 4.0
        case "B+":
            return 3.5
        case "B0":
            return 3.0
        case "C+":
            return 2.5
        case "C0":
            return 2.0
        case "D+":
            return 1.5
        case "D0":
            return 1.0
        case "F":
            return 0.0


# 학점*과목평점의 합
score_sum: float = 0.0
# 학점의 총합
rate_sum: float = 0.0
for i in range(20):
    subject, rate, grade = input().split()
    if grade != "P":
        score_sum += float(rate) * grade_to_score(grade)
        rate_sum += float(rate)

major_score = score_sum / rate_sum
print(major_score)
