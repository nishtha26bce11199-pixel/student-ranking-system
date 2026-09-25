def calculate_ranks(students):
    # divide students on basis of total marks in descending order
    students.sort(key=lambda x: x['total'], reverse=True)
    
    current_rank = 1
    for i, student in enumerate(students):
# if two students have equal marks, share the rank

        if i > 0 and student['total'] == students[i-1]['total']:
            student['rank'] = students[i-1]['rank']
        else:
            student['rank'] = current_rank
            
        current_rank +=1
    return students

def display_leaderboard(students):
    print("\n" + "=" * 55)
    print(f"{'Rank':<6}{'Roll No':<10}{'Name':<15}{'Total':<8}{'Average':<8}")
    print("=" * 55)
    
    for student in students:
        print(f"{student['rank']:<6}{student['roll_no']:<10}{student['name']:<15}{student['total']:<8}{student['average']:<8.2f}")
    print("=" * 55)
    
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
    
    
    
        
        

