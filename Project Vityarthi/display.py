def display_leaderboard(students):
    print("\n" + "=" * 55)
    print(f"{'Rank':<6}{'Roll No':<10}{'Name':<15}{'Total':<8}{'Average':<8}")
    print("=" * 55)
    
    for student in students:
        print(f"{student['rank']:<6}{student['roll_no']:<10}{student['name']:<15}{student['total']:<8}{student['average']:<8.2f}")
    print("=" * 55)

