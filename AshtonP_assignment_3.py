# Personal Information Storage
full_name = "Ashton Partridge"
student_email = "awpartridge@ncat.edu"
hometown = "Greensboro, NC"
graduation_semester = "Spring 2028"
major = "Computer Science"

# Academic Data Organization
current_courses = ["COMP 163", "COMP 180", "SPCH 250", "HIST 106"]
completed_courses = ["English", "Physics I", "Calculus I", "Micro-Economics", "Calculus II"]
credit_hours = [3, 3, 3, 3]
GPA_history = [4.0, 3.8, 3.2, 3.7]

# Contact Information Storage
emergency_contact = ("Mom", "Melanie Partridge", "704-555-0199")
home_address = ("456 Oak Street","Charlotte","NC", "28202")
instagram_info = ("Instagram", "@pasht0n7", 7)
twitter_info = ("Twitter", "N/A", 0)
birthday = ("Birthday", 5, 22, 2006)

# Intrest Tracking
current_skills = {"Python basics", "LUA", "Problem solving", "Time management"}
skills_to_learn = {"JavaScript", "Data structures", "Git", "SQL", "Public speaking", "HTML"}
career_intrests = {"Software development", "Data science", "Game development"}
hobbies = {"Gaming", "Movies", "Reading", "Fishing", "Music"}
entertainment_backlog = {"LOTR: Extended Cut", "Blue Velvet", "No Country For Old Men", "Game of Thrones"}

# Organizational Mapping
course_credits = {"COMP 163": 3, "COMP 180":3, "SPCH 250": 3, "HIST 106": 3}
course_professors = {"COMP 163": "Prof. Rhodes", "COMP 180": "Dr. Pioro", "SPCH 250": "Dr. Crossen", "HIST 106": "Dr. Devoe"}
course_rooms = {"COMP 163": "M-Eric 300", "COMP 180": "M-Eric 201", "ENG 101": "Crosby 121", "HIS 105": "Crosby 210"}
monthy_budget = {"Food": 220, "Entertainment": 170, "Books": 115, "Transportation": 80}
study_hours_per_subject = {"Programming": 10, "Speech": 4, "History": 6}
contact_directory = {"Mom": "704-555-0199", "Roomate": "336-555-7821", "Academic Advisor": "336-334-5000"}

# Required Calculations
total_credit_hours = sum(credit_hours) # Adds all the elements of the list credit_hours together
cumulative_GPA = round(sum(GPA_history)/ len(GPA_history),2) # Adds all of the elements of the GPA_history list and divides it by its length to calculate cumulative GPA
count_of_complete_courses = len(completed_courses)
total_study_hours = study_hours_per_subject["English"] + study_hours_per_subject["History"] + study_hours_per_subject["Math"] + study_hours_per_subject["Programming"]
academic_load = total_credit_hours + total_study_hours
monthy_budget_total = monthy_budget["Books"] + monthy_budget["Entertainment"] + monthy_budget["Food"] + monthy_budget["Transportation"]
daily_food_budget = round(monthy_budget["Food"]/30, 2)
annual_budget_projection = monthy_budget_total * 12
study_cost_per_hours = round(monthy_budget["Books"]/total_study_hours, 2)

# Analytics Calculations
total_followers = instagram_info[2] + twitter_info[2] # Adds the 2 follower counts
skills_count_comparison = len(current_skills) - len(skills_to_learn) # curent goals - learning goals
contact_directory_size = len(contact_directory)
entertainment_backlog_count = len(entertainment_backlog)

# Output
print("=" * 64) # Repeats the "=" string 64 times to reduce line length
print(" " * 13, "PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("=" * 64)
print(f"Student: {full_name} | Email: {student_email}")
print(f"From: {hometown} | Graduating: {graduation_semester}")
print(f"Major: {major}\n")

print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {total_credit_hours} credits across {len(current_courses)} courses")
print(f"Cumulative GPA: {cumulative_GPA}")
print(f"Weekly Study Time: {total_study_hours} hours")
print(f"Academic Investment: ${study_cost_per_hours} per study hour\n")

print("Current Courses:")
print(f"{current_courses[0]} - {credit_hours[0]} credits - {course_professors["COMP 163"]} - {course_rooms["COMP 163"]}")
print(f"{current_courses[1]} - {credit_hours[1]} credits - {course_professors["COMP 180"]} - {course_rooms["COMP 180"]}")
print(f"{current_courses[2]} - {credit_hours[2]} credits - {course_professors["SPCH 250"]} - {course_rooms["SPCH 250"]}")
print(f"{current_courses[3]} - {credit_hours[3]} credits - {course_professors["HIST 106"]} - {course_rooms["HIST 106"]}\n")

print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills:", current_skills)
print(f"Learning Goals:", skills_to_learn)
print("Career Interests:", career_intrests)
print(f"Skills Currently Have: {len(current_skills)}")
print(f"Skills Want to Learn: {len(skills_to_learn)}\n")

print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${monthy_budget_total}")
print(f"Food: ${monthy_budget["Food"]} (${daily_food_budget}/day)")
print(f"Entertainment: ${monthy_budget["Entertainment"]}")
print(f"Books: ${monthy_budget["Books"]}")
print(f"Transportation: ${monthy_budget["Transportation"]}")
print(f"Annual Projection: ${annual_budget_projection}\n")

print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]}, {home_address[2]} {home_address[3]}")
print(f"Social Media Presence: {total_followers} followers across 2 platforms")
print(f"Key Contacts: {len(contact_directory)} people in directory\n")

print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {len(completed_courses)}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog: {entertainment_backlog_count} items")
print(f"Current Hobbies: {len(hobbies)} activities")
print("=" * 64)