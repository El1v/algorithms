def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    
    students = 0;

    for start, end in permanence_period:
        if not all(isinstance(p, int) for p in (start,end)): 
            return None

        if(start <= target_time <= end):
            students += 1

    return students

# link de apoio
# https://pt.stackoverflow.com/questions/341085/como-validar-se-um-valor-%C3%A9-uma-tupla-possuindo-uma-string-e-um-inteiro