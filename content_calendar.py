import csv

# creating basic data 

# the list of content ideas

content_ideas = [
    "GRWM for wedding makeup",
    "Client transformation before/after",
    "Behind the scenes with setting up",
    "Product review",
    "Soft glam tutorial", 
    "Bridal look breakdown",
    "Makeup tips, Q&A:"
]

# best time to post depending on day (estimating the engagement data)

best_times = {
    "Monday" : "6:00 PM",
    "Tuesday" : "4:00 PM",
    "Wednesday" : "7:00 PM",
    "Thursday" : "5:30 PM",
    "Friday" : "8:00 PM",
    "Saturday" : "3:00 PM",
    "Sunday" : "2:00 PM"
}

# days of the week

days_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# scheduling logic

# loops through days and content ideas
schedule = []
for i, day in enumerate(days_week):
    if i < len(content_ideas):
        idea = content_ideas[i]
    else:
        # this is when more days than ideas, start reusing from the beginning
        idea = content_ideas[i % len(content_ideas)]

    time = best_times.get(day, "6:00PM") #default time if the day is not found

    schedule.append({
        "Day": day,
        "Content Idea": idea, 
        "Suggested Time": time
    })

for item in schedule:
    print(f"{item['Day']}: {item['Content Idea']} at {item['Suggested Time']}")

# for the CSV file (exporting)
    
with open("content_calendar.csv", mode="w", newline= "", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Day", "Content Idea", "Suggested Time"])
    writer.writeheader()
    writer.writerows(schedule)

print("Content calendar saved as content_calendar.csv")