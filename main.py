import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

plt.style.use('seaborn-v0_8-darkgrid')  # Modern style

print("🎯 THIS CODE TAKES YOUR SUBJECT MARKS, CALCULATES AVERAGE, PERCENTAGE & PREDICTS NEXT SCORE 🎯")

# STUDENT NAME
Name = input("ENTER YOUR NAME: ").capitalize()
print(f"\nHEY {Name}! LET'S ENTER YOUR SUBJECT MARKS 👇")

# SUBJECTS AND MARKS INPUT
subjects = []
marks = []

for i in range(1, 6):
    subject = input(f"Enter the name of subject {i}: ").capitalize()
    subjects.append(subject)

for subject in subjects:
    mark = float(input(f"Enter your marks for {subject}: "))
    marks.append(mark)

# CALCULATE AVERAGE
average = np.mean(marks)
total_marks = sum(marks)
percentage = (total_marks / (len(marks) * 100)) * 100

print(f"\n📘 Average Marks: {average:.2f}")
print(f"📗 Percentage: {percentage:.2f}%")

# ---------------- PREDICTION FUNCTION ----------------
def predict_next_score(last_marks):
    """
    Predicts the next score using the student's last 5 marks.
    Uses a simple linear regression on their own marks.
    """
    X = np.arange(1, len(last_marks) + 1).reshape(-1, 1)  # 1,2,3,4,5
    y = np.array(last_marks)
    model = LinearRegression()
    model.fit(X, y)
    next_score = model.predict([[len(last_marks) + 1]])
    return next_score[0]

predicted_score = predict_next_score(marks)
print(f"\n🤖 Predicted Next Score: {predicted_score:.2f}")

# ---------------- PLOT GRAPH ----------------
subjects_with_prediction = subjects + ["Predicted"]
marks_with_prediction = marks + [predicted_score]

colors = ['skyblue']*len(subjects) + ['orange']  # Highlight predicted score

plt.figure(figsize=(10,6))
bars = plt.bar(subjects_with_prediction, marks_with_prediction, color=colors, edgecolor='black')

# AVERAGE LINE
plt.axhline(y=average, color='red', linestyle='--', linewidth=2, label=f'Average: {average:.2f}')

# Add text labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 1, f'{height:.2f}', ha='center', fontsize=10, fontweight='bold')

# TITLE & LABELS
plt.title(f"{Name}'s Marks & Predicted Next Score", fontsize=16, fontweight='bold')
plt.ylabel("Marks", fontsize=12)
plt.xlabel("Subjects", fontsize=12)
plt.ylim(0, max(marks_with_prediction)+10)
plt.legend()
plt.tight_layout()
plt.show()
