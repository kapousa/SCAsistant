from flask import Flask, render_template

app = Flask(__name__)

vendors = ["RANBAXY Fine Chemicals LTD.", "Aurobindo Pharma Limited", "Abbott GmbH & Co. KG",
           "SUN PHARMACEUTICAL INDUSTRIES LTD (RANBAXY LABORATORIES LIMITED)",
           "MERCK SHARP & DOHME IDEA GMBH (FORMALLY MERCK SHARP & DOHME B.V.)",
           "ABBVIE LOGISTICS (FORMERLY ABBOTT LOGISTICS BV)", "Trinity Biotech, Plc", "EY Laboratories",
           "CIPLA LIMITED", "BRISTOL-MYERS SQUIBB", "ACCOUN NIGERIA LIMITED", "Premier Medical Corporation Ltd.",
           "CHEMBIO DIAGNOSTIC SYSTEMS, INC.", "Orgenics, Ltd", "Orasure Technologies Inc.",
           "Standard Diagnostics, Inc.", "JSI R&T INSTITUTE, INC.", "GILEAD SCIENCES IRELAND, INC.",
           "BIO-RAD LABORATORIES (FRANCE)", "TURE PHARMACEUTICALS & MEDICAL SUPPLIES P.L.C.",
           "MYLAN LABORATORIES LTD (FORMERLY MATRIX LABORATORIES)", "S. BUYS WHOLESALER", "IDA FOUNDATION",
           "ZEPHYR BIOMEDICALS", "HETERO LABS LIMITED", "INTERNATIONAL HEALTHCARE DISTRIBUTORS",
           "STRIDES ARCOLAB LIMITED", "ASPEN PHARMACARE", "SHANGHAI KEHUA BIOENGINEERING CO.,LTD.  (KHB)",
           "BIOLYTICAL LABORATORIES INC.", "INVERNESS MEDICAL INNOVATIONS SOUTH AFRICA (PTY) LTD",
           "ABBOTT LABORATORIES (PUERTO RICO)", "SUB-SAHARAN BIOMEDICAL P.L.C.", "SETEMA LIMITED PLC",
           "GLAXOSMITHKLINE EXPORT LIMITED", "OMEGA DIAGNOSTICS LTD", "Hoffmann-La Roche ltd Basel",
           "REINBOLD EXPORT IMPORT", "BUNDI INTERNATIONAL DIAGNOSTICS LTD", "MISSIONPHARMA A/S", "PLURIPHARM S.A.",
           "CENTRAL PHARMACEUTICAL COMPANY NO. 1", "AHN (PTY) LTD (AKA UCB (S.A.)", "KAS MEDICS LIMITED"]


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/pocost', methods=['POST'])
def pocost():  # put application's code here
    return render_template('pocost.html')


if __name__ == '__main__':
    app.run()
