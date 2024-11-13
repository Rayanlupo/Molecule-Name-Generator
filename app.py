from flask import Flask, request, render_template
import re

app = Flask(__name__)
def get_molecule_name(molecule_formula):
    error = False
    error_message = ""
    pattern = r'([A-Z][a-z]?)(\d*)'
    matches = re.findall(pattern, molecule_formula)
    elements_list = {}
    elements_dict = {
    "Li": "Lithium", "Na": "Sodium", "K": "Potassium", "Rb": "Rubidium", "Cs": "Césium", "Fr": "Francium",
    "Be": "Béryllium", "Mg": "Magnésium", "Ca": "Calcium", "Sr": "Strontium", "Ba": "Baryum", "Ra": "Radium",
    "Sc": "Scandium", "Ti": "Titane", "V": "Vanadium", "Cr": "Chrome", "Mn": "Manganèse", "Fe": "Fer",
    "Co": "Cobalt", "Ni": "Nickel", "Cu": "Cuivre", "Zn": "Zinc", "Y": "Yttrium", "Zr": "Zirconium", "Nb": "Niobium",
    "Mo": "Molybdène", "Tc": "Technétium", "Ru": "Ruthénium", "Rh": "Rhodium", "Pd": "Palladium", "Ag": "Argent",
    "Cd": "Cadmium", "Hf": "Hafnium", "Ta": "Tantale", "W": "Tungstène", "Re": "Rhénium", "Os": "Osmium",
    "Ir": "Iridium", "Pt": "Platine", "Au": "Or", "Hg": "Mercure", "Tl": "Thallium", "Pb": "Plomb", "Bi": "Bismuth",
    "Al": "Aluminium", "Ga": "Gallium", "In": "Indium", "Sn": "Étain", "La": "Lanthane", "Ce": "Cérium", 
    "Pr": "Praséodyme", "Nd": "Néodyme", "Pm": "Prométhium", "Sm": "Samarium", "Eu": "Europium", "Gd": "Gadolinium", 
    "Tb": "Terbium", "Dy": "Disprosium", "Ho": "Holmium", "Er": "Erbium", "Tm": "Thulium", "Yb": "Ytterbium", 
    "Lu": "Lutétium", "Ac": "Actinium", "Th": "Thorium", "Pa": "Protactinium", "U": "Uranium", "Np": "Neptunium", 
    "Pu": "Plutonium", "Am": "Américium", "Cm": "Curium", "Bk": "Berkélium", "Cf": "Californium", "Es": "Einsteinium", 
    "Fm": "Fermium", "Md": "Mendélévium", "No": "Nobélium", "Lr": "Lawrencium", "F": "Fluor", "Cl": "Chlore", 
    "Br": "Brome", "I": "Iode", "At": "Astate", "He": "Hélium", "Ne": "Néon", "Ar": "Argon", "Kr": "Krypton", 
    "Xe": "Xénon", "Rn": "Radon", "C": "Carbone", "N": "Azote", "P": "Phosphore", "S": "Soufre", "Se": "Sélénium", 
    "Te": "Tellure", "Po": "Polonium"
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
    liste_d_anions_polyatomiques={
        "H2PO4" : "DiHydrogenoPhosphate",
        "H2PO3" : "DiHydrogenoPhosphite",
        "HCO3" : "Hidrogenocarbonate",
        "HSO3" : "Hydrogenosulfite",
        "HSO4" : "Hydrogenosulfate",
        "CN" : "Cyanure",
        "OH" : "Hydroxyde",
        "NO3" : "Nitrate",
        "NO2" : "Nitrite",
        "CN" : "Cyanure",
        "MnO4" : "Permanganate",
        "SCN" : "Thiocyanate",
        "ClO" : "Hypochlorite",
        "ClO2" : "Hypochlorate",
        "ClO3" : "Chlorate",
        "ClO4" : "Perchlorate",
        "HPO4" : "Hydrogenophosphate",
        "HPO3" : "Hydrogenophosphite",
        "CO3" : "Carbonate",
        "SO4" : "Sulfate",
        "SO3" : "Sulfite",
        "CrO4" : "Chromate",
        "Cr2O7" : "Dichromate",
        "S2O3" : "Thiosulfate",
        "SiO3" : "Silicate",
        "BO3" : "Borate",
        "PO3" : "Phosphite",
        "PO4" : "Phosphate",

        }
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
                formule_H = element + str(elements_list[element])
        if element in metals:
            metal_formula = element
            metal = elements_dict[element]
            formule_metal = element + str(elements_list[element])
            if "M" not in formule_general:
                formule_general += "M"

        if element in non_metals:
            if "X" not in formule_general:
                formule_general += "X"
                formule_non_metal = element + str(elements_list[element])
                non_metal = elements_dict[element]
        if element == "O":

            if "O" not in formule_general:
                formule_general += "O"
                formule_oxygen = element + str(elements_list[element])


    print(formule_general)
    function = ""
    nom = ""
    vowels = ["a", "e", "i", "o" ]
    if formule_general == "HXO":
        function = "Acide"
        i = molecule_formula.replace("H", "")
        if i in liste_d_anions_polyatomiques:
            nom = liste_d_anions_polyatomiques[i] + " d'hydrogene"

    if formule_general == "HMO":
        function = "Sel Binaire "
        nom = "Hydroxyde de" + metal

    elif formule_general == "HX" or formule_general == "XH":
        function = "Acide"
        if non_metal[-1] in vowels:
            non_metal = non_metal.replace(non_metal[-1], "") 
        print(non_metal)
        nom = non_metal +"ure" + " " + "d'hydrogene"

    elif formule_general == "MO":
        function = "Oxyde"
        nom = "Oxyde de " + metal
    elif formule_general == "MX" or formule_general == "XM":
        function = "Sel Binaire"
        if non_metal[-1] in vowels:
            non_metal = non_metal - non_metal[-1] 
        nom = non_metal +"ure" + " de" + metal
    elif formule_general == "MXO":
        function = "Sel Ternaire"
        print(metal_formula)
        removed_metal = molecule_formula.replace(metal_formula, "")
        print(removed_metal)
        nom = liste_d_anions_polyatomiques[removed_metal] + f" de {metal}"
    elif formule_general == "XO" or formule_general == "OX":

        function = "Oxyde non-metalique"
        prefixe_o = prefixes[str(n_atoms)]
        for elem in elements_list:
            if elements_list[elem] == non_metal:
                x_form = elem
        prefix_x = prefixes[str(elements_list[elem])]
        nom =   prefixe_o + "oxyde" + f" de {prefix_x.lower()}{non_metal.lower()}"
    elif formule_general == "MOH":
        function = "Hydroxide"
        nom = "Hydroxyde de " + metal
    if nom and function:
        error = False
    else:
        error =True
        nom = None
        
        error_message = "No compound Found"
        return error, error_message, nom, function
    

    return nom, function, error, error_message
@app.route('/', methods=['GET', 'POST'])
def index():
    error = False
    error_message = ""
    name = None
    function = None
    formula = None
    
    
    if request.method == 'POST':
        formula = request.form.get('formula')
        name, function, error, error_message = get_molecule_name(formula)
        if name and function:
            error = False
        else:
            error = True
            name = None
            function = None
            
        
    return render_template('home.html', name=name, function=function, error=error, error_message=error_message, formula=formula)

if __name__ == "__main__":
    app.run(debug=True)
