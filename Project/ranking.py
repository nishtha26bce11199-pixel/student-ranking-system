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