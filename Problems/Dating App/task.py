def select_dates(potential_dates):
    names = []
    for person in potential_dates:
        if person["age"] > 30 and "art" in person["hobbies"]:
            names.append(person["name"])
    return ", ".join(names)


