student_scores = [12,14,98,54,32,342,2,42,32,32,42,425,35,35,3,2]
# exam_score = sum(student_scores)
# print(exam_score)
sum = 0
for score in student_scores:
    sum+=score
print(sum)
max_score = 0
for score in student_scores:
    if score>max_score:
        max_score = score
print(max_score)