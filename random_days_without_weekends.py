import datetime
import random

JOURS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def jours_aleatoires_sans_weekend(annee: int, n: int):
    debut = datetime.date(annee, 1, 1)
    fin = datetime.date(annee, 12, 31)

    jours_ouvres = []
    courant = debut
    while courant <= fin:
        if courant.weekday() < 5:
            jours_ouvres.append(courant)
        courant += datetime.timedelta(days=1)

    if n > len(jours_ouvres):
        raise ValueError("N is above the number of working days in the year")

    tirage = random.sample(jours_ouvres, n)

    return [(d, JOURS[d.weekday()]) for d in tirage]

def formatting(l) -> list[str] :
    return [f"{day} {date.day} {MONTHS[date.month - 1]}" for (date, day) in l]

print(formatting(jours_aleatoires_sans_weekend(2026, 15)))