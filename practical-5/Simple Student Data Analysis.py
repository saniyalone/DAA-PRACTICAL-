import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Kiran"],
    "Marks": [75, 85, 60, 90, 65],
    "Attendance": [80, 90, 75, 95, 70]
}
df = pd.DataFrame(data)

print("Student Data:")
print(df
print("\nStudents scoring more than 70:")
print(df[df["Marks"] > 70])
