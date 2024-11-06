from flask import Flask, render_template, request

import re
app = Flask(__name__)

@app.route('/')
def index():
    molecule_name = None;
    if request.method == 'POST':
        molecule_formula = input("Formula: ")
        pattern = r'([A-Z][a-z]?)(\d*)'
        matches = re.findall(pattern, molecule_formula)
        elements_list = {}
        for elements, n_atoms in matches:
            print(elements)
            print(n_atoms)


    return render_template('home.html', molecule_name=molecule_name)