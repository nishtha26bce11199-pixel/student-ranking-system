def calculate_ranks(students):

    students.sort(key=lambda x: x['total'], reverse=True)
    
    current_rank = 1
    for i, student in enumerate(students):

        if i > 0 and student['total'] == students[i-1]['total']:
            student['rank'] = students[i-1]['rank']
        else:
            student['rank'] = current_rank
            
        current_rank +=1
    return students