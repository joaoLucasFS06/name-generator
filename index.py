import random as rd


def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


def generate_name(names, surnames):
    return f"{rd.choice(names)} {rd.choice(surnames)}"


def generate_names(names, surnames, qty):
    generated_names = []
    for _ in range(qty):
        while True:
            chosen_name = generate_name(names, surnames)
            if chosen_name not in generated_names:
                generated_names.append(chosen_name)
                break
    return generated_names


def main():
    names = read_file("names.txt")
    surnames = read_file("surnames.txt")
    max_names = len(names) * len(surnames)

    while True:
        try:
            qty = int(input("How many names would you like to generate?\n"))

            if qty > max_names:
                print(f"It is only possible to generate a maximum of {max_names}")
                continue

            if qty <= 0:
                print("The quantity must be greater than 0.")
                continue

            generated_names = generate_names(names, surnames, qty)

            for name in generated_names:
                print(name)
            break
            
        except ValueError:
            print("Please, enter a valid integer.")

    while True:
        save = input("Would you like to save the generated names in a separated file? (y/n)\n").lower()

        if save in ("y", "yes"):
            with open("generated_names.txt", "w", encoding="utf-8") as file:
                for name in generated_names:
                    file.write(f"{name}\n")
                print("Saved succesfully.")
            break

        if save in ("n", "no"):
            break

        print("Invalid answer.")


if __name__ == "__main__":
    main()
