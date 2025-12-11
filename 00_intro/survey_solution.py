participants = [
    {"id": 0, "age": 25, "hours_exercise": 3.2, "gender": "F"},
    {"id": 1, "age": 31, "hours_exercise": 0.0, "gender": "M"},
    {"id": 2, "age": 44, "hours_exercise": 1.5, "gender": "F"},
    {"id": 3, "age": 29, "hours_exercise": 2.0, "gender": "M"},
    {"id": 4, "age": 61, "hours_exercise": 1.5, "gender": "F"},
    {"id": 5, "age": 37, "hours_exercise": -1.0, "gender": "M"}  # Suspicious value
]

# 1. Print Participant Exercise Hours
for p in participants:
    print(f"Participant {p['id']+1}: {p['hours_exercise']} hours")

# 2. Replace Negative Hours With None
for p in participants:
    if p["hours_exercise"] < 0:
        p["hours_exercise"] = None

# 3. Compute Average Weekly Hours
valid_hours = [p["hours_exercise"] for p in participants if p["hours_exercise"] is not None]
overall_avg = sum(valid_hours) / len(valid_hours)
overall_avg = round(overall_avg, 2)
print(f"Overall average hours: {overall_avg}")

# Expected output
# 
# Participant 1: 3.2 hours
# Participant 2: 0.0 hours
# Participant 3: 1.5 hours
# Participant 4: 2.0 hours
# Participant 5: 1.5 hours
# Participant 6: -1.0 hours
# 
# Overall average hours: 1.64

