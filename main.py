# Name: Zayn Jaber
# Student ID: 43767236
# Email: zynjaber@umich.edu
# Collaborators: me
# GenAI Tools: ChatGPT (used to assist with code structure, debugging, and explaining concepts I didn’t fully understand)
# Functions created by: Zayn Jaber

import csv


def read_penguin_data(filename):

    data = []
    
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:

            if row['species'] and row['island'] and row['body_mass_g'] and row['flipper_length_mm']:
                data.append(row)

    return data



def calculate_avg_body_mass_by_species_and_sex(data):

    totals = {}
    counts = {}

    for row in data:

        species = row["species"]
        sex = row["sex"]
        body_mass = row["body_mass_g"]


        if not sex or not body_mass:
            continue

        try:
            body_mass = float(body_mass)

        except ValueError:
            continue


        if species not in totals:

            totals[species] = {}
            counts[species] = {}
            
        if sex not in totals[species]:
            
            totals[species][sex] = 0
            counts[species][sex] = 0

        totals[species][sex] += body_mass
        counts[species][sex] += 1


    averages = {}
    for species in totals:
        averages[species] = {}
        
        for sex in totals[species]:
            averages[species][sex] = round(totals[species][sex] / counts[species][sex], 2)

    return averages


def calculate_avg_flipper_length_by_island_and_species(data):


    totals = {}
    counts = {}

    for row in data:
        island = row["island"]
        species = row["species"]
        flipper_length = row["flipper_length_mm"]


        if not island or not species or not flipper_length:
            continue

        try:
            flipper_length = float(flipper_length)
        except ValueError:
            continue


        if island not in totals:
            totals[island] = {}
            counts[island] = {}
        if species not in totals[island]:
            totals[island][species] = 0
            counts[island][species] = 0

        totals[island][species] += flipper_length
        counts[island][species] += 1


    averages = {}
    for island in totals:
        averages[island] = {}
        for species in totals[island]:
            averages[island][species] = round(totals[island][species] / counts[island][species], 2)

    return averages

def write_results_to_csv(filename, body_mass_data, flipper_data):


    with open(filename, mode="w", encoding="utf-8") as file:

        file.write("Average Body Mass by Species and Sex\n")
        file.write("Species,Sex,Average Body Mass (g)\n")
        for species, sexes in body_mass_data.items():
            for sex, avg_mass in sexes.items():
                file.write(f"{species},{sex},{avg_mass}\n")

        file.write("\n")


        file.write("Average Flipper Length by Island and Species\n")
        file.write("Island,Species,Average Flipper Length (mm)\n")
        for island, species_data in flipper_data.items():
            for species, avg_flipper in species_data.items():
                file.write(f"{island},{species},{avg_flipper}\n")

    print(f"Results written to {filename}")


def main():

    filename = "penguins.csv"
    data = read_penguin_data(filename)


    body_mass_results = calculate_avg_body_mass_by_species_and_sex(data)
    flipper_results = calculate_avg_flipper_length_by_island_and_species(data)


    output_filename = "output.csv"
    write_results_to_csv(output_filename, body_mass_results, flipper_results)

    print("complete! Check the output.csv file for results.")


if __name__ == "__main__":
    main()