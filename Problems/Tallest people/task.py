def tallest_people(**people):
    altura_maxima = max(people.values())
    highest_people = []
    for key, value in people.items():
        if value == altura_maxima:
            highest_people.append(key)
    highest_people.sort()
    for people in highest_people:
        print(people, ":", altura_maxima)
