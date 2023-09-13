num_students= 16
num_tests = 4

student_scores = []

for student in range(num_students):
    print(f"Enter test scores for Student {student + 1}:")
    scores = []
    for test in range(num_tests):
        score = float(input(f"Test {test + 1}:"))
        scores.append(scores)
print("\nAverage Test Scores:")
for student, scores in enumerate(student_scores):
    average_score = sum(scores) / num_tests
    print(f"Student{student + 1}: {average_score:.2f}")

