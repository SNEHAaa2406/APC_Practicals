def total_marks(marks):
    return sum(marks)


def percentage(marks):
    total = sum(marks)
    return total / len(marks)


def grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"