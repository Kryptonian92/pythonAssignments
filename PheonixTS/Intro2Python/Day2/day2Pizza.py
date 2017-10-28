import math

def calculate_slices(people, slices_per_person):
    return slices_per_person + people

def calculate_pizzas(slices, slices_per_pie):
    return math.ceil (slices / slices_per_pie)

def calculate_slices_left(slices_per_pie, pizzas, slices_needed):
    total_slices = slices_per_pie * pizzas
    return math.floor(total_slices % slices_needed)

def main():
    people = int(input("How many people are eating? "))
    slices_per_person = float(input("How many slices per person? "))
    slices = calculate_slices(people, slices_per_person)

    slices_per_pie = int(input("How many slices per pie? "))
    pizzas = calculate_pizzas(slices, slices_per_pie)

    print("You need", pizzas, "pizzas to feed", people, "people")

    slices_left = calculate_slices_left(slices_per_pie, pizzas, slices)
    print("There will be", slices_left, "leftover slices.")

main()
