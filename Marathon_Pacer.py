kilometers = 10
miles = kilometers/1.61
hours = 0
minutes = 42
seconds = 42
total_seconds = (hours*60*60) + (minutes * 60) + seconds

average_pace_persecond = total_seconds / miles
pace_minutes, pace_seconds = divmod(round(average_pace_persecond), 60)

total_hours = total_seconds / 3600
print(total_hours)
mph = miles/total_hours 

print(f"Average pace: {pace_minutes} minutes, {pace_seconds} seconds per mile")
print(f"Average speed: {mph} miles per hour")