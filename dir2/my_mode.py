def calculate(hours, rate, bonus):
    try:
        return (hours * rate) + bonus
    except TypeError:
        return
