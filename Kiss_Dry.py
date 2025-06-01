# -------------------------------------------------------
# KISS und DRY - Prinzipien in der Softwareentwicklung
# -------------------------------------------------------

# KISS: Keep It Simple, Stupid
# ----------------------------
# Dieses Prinzip sagt: Schreibe deinen Code so einfach wie möglich.
# Vermeide unnötige Komplexität, verschachtelte Logik oder komplizierte Konstrukte,
# wenn es auch einfach geht.
# Einfacher Code ist leichter verständlich, wartbar und weniger fehleranfällig.

# Beispiel 1: KISS - Schlechte Umsetzung (zu kompliziert)
def calculate_discount_bad(price):
    if price > 100:
        if price <= 200:
            discount = 0.1
        else:
            discount = 0.15
    else:
        discount = 0
    return price * (1 - discount)

# Beispiel 1: KISS - Gute Umsetzung (einfach und klar)
def calculate_discount_good(price):
    if price > 200:
        discount = 0.15
    elif price > 100:
        discount = 0.1
    else:
        discount = 0
    return price * (1 - discount)

# Beispiel 2: KISS - Schlechte Umsetzung (unnötige Schleife)
def sum_first_n_bad(numbers, n):
    total = 0
    for i in range(n):
        total += numbers[i]
    return total

# Beispiel 2: KISS - Gute Umsetzung (nutzt eingebaute Funktion)
def sum_first_n_good(numbers, n):
    return sum(numbers[:n])

# Beispiel 3: KISS - Schlechte Umsetzung (zu viele if-Abfragen)
def is_weekend_bad(day):
    if day == 'Saturday' or day == 'Sunday':
        return True
    else:
        return False

# Beispiel 3: KISS - Gute Umsetzung (klarer Ausdruck)
def is_weekend_good(day):
    return day in ['Saturday', 'Sunday']


# -------------------------------------------------------
# DRY: Don’t Repeat Yourself
# --------------------------
# Dieses Prinzip sagt: Vermeide Wiederholungen im Code.
# Wenn du denselben Code mehrfach schreibst, wird die Wartung
# schwierig, Fehler schleichen sich ein und die Übersicht leidet.
# Stattdessen sollten Funktionen oder Schleifen verwendet werden,
# die den Code modular und wiederverwendbar machen.

# Beispiel 1: DRY - Schlechte Umsetzung (Code doppelt)
def greet_user_bad(name):
    print("Hallo " + name + "!")
def greet_admin_bad(name):
    print("Hallo " + name + "! Du bist Admin.")

# Beispiel 1: DRY - Gute Umsetzung (Code wiederverwenden)
def greet_user_good(name, is_admin=False):
    greeting = "Hallo " + name + "!"
    if is_admin:
        greeting += " Du bist Admin."
    print(greeting)

# Beispiel 2: DRY - Schlechte Umsetzung (gleiche Berechnung doppelt)
def circle_area_bad(radius):
    return 3.14159 * radius * radius

def cylinder_volume_bad(radius, height):
    return 3.14159 * radius * radius * height

# Beispiel 2: DRY - Gute Umsetzung (Hilfsfunktion nutzen)
def area_circle(radius):
    return 3.14159 * radius * radius

def volume_cylinder(radius, height):
    return area_circle(radius) * height

# Beispiel 3: DRY - Schlechte Umsetzung (Code kopiert für ähnliche Logik)
def convert_to_usd_bad(euro):
    return euro * 1.1
def convert_to_gbp_bad(euro):
    return euro * 0.85

# Beispiel 3: DRY - Gute Umsetzung (Parameter statt Kopie)
def convert_currency(euro, rate):
    return euro * rate

# -------------------------------------------------------
# Zusammenfassung:
# - KISS fordert einfache, klare Lösungen, keine unnötige Komplexität.
# - DRY fordert Vermeidung von doppeltem Code durch Wiederverwendung.
# Beides zusammen verbessert Lesbarkeit, Wartbarkeit und Qualität deines Codes.
# -------------------------------------------------------
