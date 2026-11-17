from json import load
from statistics import mean

with open("students.json", "r", encoding="utf-8") as f:
    students = load(f)

best = max(students, key=lambda baho : baho['grade'])
worst = min(students, key=lambda baho: baho['grade'])

grades = [baho['grade'] for baho in students]

average = round(mean(grades), 2)

print(f"Eng yaxshi talaba: {best['name']} — {best['grade']}")
print(f"Eng past baho: {worst['name']} — {worst['grade']}")
print(f"O'rtacha baho: {average}")