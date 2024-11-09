from flask import Flask, request, render_template
import re
1
print("hello rayan")

molecule_formula = input("Formule Molecule: ")
pattern = r'([A-Z][a-z]?)(\d*)'
matches = re.findall(pattern, molecule_formula)
elements_list = {}
elements_dict = {
    "Li": "Lithium", "Na": "Sodium", "K": "Potassium", "Rb": "Rubidium", "Cs": "Cesium", "Fr": "Francium",
    "Be": "Beryllium", "Mg": "Magnesium", "Ca": "Calcium", "Sr": "Strontium", "Ba": "Barium", "Ra": "Radium",
    "Sc": "Scandium", "Ti": "Titanium", "V": "Vanadium", "Cr": "Chromium", "Mn": "Manganese", "Fe": "Iron",
    "Co": "Cobalt", "Ni": "Nickel", "Cu": "Copper", "Zn": "Zinc", "Y": "Yttrium", "Zr": "Zirconium", "Nb": "Niobium",
    "Mo": "Molybdenum", "Tc": "Technetium", "Ru": "Ruthenium", "Rh": "Rhodium", "Pd": "Palladium", "Ag": "Silver",
    "Cd": "Cadmium", "Hf": "Hafnium", "Ta": "Tantalum", "W": "Tungsten", "Re": "Rhenium", "Os": "Osmium",
    "Ir": "Iridium", "Pt": "Platinum", "Au": "Gold", "Hg": "Mercury", "Tl": "Thallium", "Pb": "Lead", "Bi": "Bismuth",
    "Al": "Aluminum", "Ga": "Gallium", "In": "Indium", "Sn": "Tin", "Tl": "Thallium", "Pb": "Lead", "Bi": "Bismuth",
    "La": "Lanthanum", "Ce": "Cerium", "Pr": "Praseodymium", "Nd": "Neodymium", "Pm": "Promethium", "Sm": "Samarium",
    "Eu": "Europium", "Gd": "Gadolinium", "Tb": "Terbium", "Dy": "Dysprosium", "Ho": "Holmium", "Er": "Erbium",
    "Tm": "Thulium", "Yb": "Ytterbium", "Lu": "Lutetium", "Ac": "Actinium", "Th": "Thorium", "Pa": "Protactinium",
    "U": "Uranium", "Np": "Neptunium", "Pu": "Plutonium", "Am": "Americium", "Cm": "Curium", "Bk": "Berkelium",
    "Cf": "Californium", "Es": "Einsteinium", "Fm": "Fermium", "Md": "Mendelevium", "No": "Nobelium", "Lr": "Lawrencium",
    "F": "Fluorine", "Cl": "Chlorine", "Br": "Bromine", "I": "Iodine", "At": "Astatine", "He": "Helium", "Ne": "Neon",
    "Ar": "Argon", "Kr": "Krypton", "Xe": "Xenon", "Rn": "Radon", "C": "Carbon", "N": "Nitrogen", "P": "Phosphorus",
    "S": "Sulfur", "Se": "Selenium", "Te": "Tellurium", "Po": "Polonium"
}
metals = [
    "Li", "Na", "K", "Rb", "Cs", "Fr", "Be", "Mg", "Ca", "Sr", "Ba", "Ra", "Sc", "Ti", "V", "Cr", "Mn", 
    "Fe", "Co", "Ni", "Cu", "Zn", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "Hf", "Ta", 
    "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Al", "Ga", "In", "Sn", "Tl", "Pb", "Bi", 
    "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Ac", "Th", 
    "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"
]
non_metals = [
    "F", "Cl", "Br", "I", "At", "He", "Ne", "Ar", "Kr", "Xe", "Rn", "C", "N", "P", "S", "Se", "Te", "Po"
]

prefixes={
    "1" : "Mon",
    "2" : "Di",
    "3" : "Tri",
    "4" : "Tetr",
    "5" : "Pent",
    "6" : "Hex",
    "7" : "Hept",
    "8" : "Oct",

}



formule_general = ""
for element, n_atoms in matches:
    if n_atoms:
        n_atoms = int(n_atoms)
    else: 
        n_atoms = 1
    elements_list[element] = n_atoms
print(elements_list)
metal = "";
for element in elements_list:
    if element == "H":
        if "H" not in formule_general:
            formule_general += "H"
    if element in metals:
        metal = elements_dict[element]
        if "M" not in formule_general:
            formule_general += "M"
    if element in non_metals:
        if "X" not in formule_general:
            formule_general += "X"
            non_metal = elements_dict[element]
    if element == "O":
        if "O" not in formule_general:
            formule_general += "O"
print(formule_general)
function = ""
nom = ""
vowels = ["a", "e", "i", "o" ]
if formule_general == "HMO":
    function = "Sel"
    Nom = "Hydroxyde de" + metal
    
elif formule_general == "HX" or formule_general == "XH":
    function = "Acide"
    if non_metal[-1] in vowels:
        non_metal = non_metal - non_metal[-1] 
    nom = non_metal +"ure" + " " + "d'hydrogene"
    
elif formule_general == "MO":
    function = "Oxyde"
    nom = "Oxyde de " + metal
elif formule_general == "MX" or formule_general == "XM":
    function = "Sel Binaire"
    if non_metal[-1] in vowels:
        non_metal = non_metal - non_metal[-1] 
    nom = non_metal +"ure" + " de" + metal
elif formule_general == "XO" or formule_general == "OX": 
    function = "Oxy non-metalique"
    prefixe = prefixes[str(n_atoms)]
    nom =   prefixe + "oxyde" + f" de {non_metal}"


    
else:    print("Error")

print(function)
print(nom)
