#Computes GPA for a student, given avg marks:-
def computeGPA(s):
    if s >= 90 and s < 100:
        return 4.5
    elif s >=85  and s < 90:
        return 4.0
    elif s >=80  and s < 85:
        return 3.7
    elif s >=77  and s < 80:
        return 3.3   
    elif s >=73  and s < 77:
        return 3.0
    elif s >=70  and s < 73:
        return 2.7
    elif s >=67  and s < 70:
        return 2.5
    elif s >=63  and s < 67:
        return 2.3
    elif s >=60  and s < 63:
        return 2.0
    elif s >=50  and s < 59:
        return 1.0
    else:
        return 0.0
  