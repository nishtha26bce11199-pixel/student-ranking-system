from ranking import calculate_ranks
from display import display_leaderboard


def run_ranking_system():
    students = []
    print("--- Student Ranking System ---")
    
    try:
        num_students = int(input("Enter total number of students: "))
        num_subjects = int(input("Enter number of subjects: "))
        
    except ValueError:
        print("Enter valid integers for student and subject counts.")
        return
    
    for i in range(num_students):
        print(f"\n--- Student {i+1} Details ---")
        roll_no = input("Roll Number: ")
        name = input("Name: ")
        
        marks = []
        for j in range(num_subjects):
            while True:
                try:
                    mark = float(input(f" Marks for subject {j+1} (0-100): "))
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    
                    print(" Error: Marks must be between 0 and 100.")
                except ValueError:
                    print(" Error: Enter a valid decimal number. ")
                    
        total = sum(marks)
        average = total / num_subjects
# Store it as a plain dictionary
        students.append({
            "roll_no": roll_no,
            "name": name,
            "total": total,
            "average": average,
        })
        
    ranked_list = calculate_ranks(students)
    display_leaderboard(ranked_list)
    
# Execute the program
run_ranking_system()
    
    
    
        
        

