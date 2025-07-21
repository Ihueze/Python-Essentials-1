hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
# convert everything to minutes
total_mins = hour * 60 + mins + dura

# compute the end time in hours and minutes
end_hour = (total_mins // 60) % 24
end_mins = total_mins % 60

# display the result
print(f"{end_hour}:{end_mins}")
