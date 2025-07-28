import pandas as pd

# Sample data for Excel creation (you can expand this with all the entries)
data = [
    {
        "HS Code": "9001.10.00",
        "Stat Code": "04",
        "Unit": "..",
        "Goods": "Optical fibres, optical fibre bundles and cables",
        "Rate": "Free",
        "TCO Available": "Yes"
    },
    {
        "HS Code": "9001.30.10",
        "Stat Code": "37",
        "Unit": "No",
        "Goods": "Contact lenses - Ophthalmic powered",
        "Rate": "Free",
        "TCO Available": "Yes"
    },
    {
        "HS Code": "9003.11.00",
        "Stat Code": "29",
        "Unit": "No",
        "Goods": "Frames and mountings - Of plastics",
        "Rate": "5%",
        "TCO Available": "Yes"
    },
    {
        "HS Code": "9004.10.00",
        "Stat Code": "01",
        "Unit": "No",
        "Goods": "Sunglasses",
        "Rate": "5%",
        "TCO Available": "Yes"
    },
    {
        "HS Code": "9006.40.00",
        "Stat Code": "17",
        "Unit": "No",
        "Goods": "Instant print cameras",
        "Rate": "Free",
        "TCO Available": "No"
    }
]

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
file_name = "Chapter_90_Tariff_Details.xlsx"
df.to_excel(file_name, index=False)

print(f"Excel file '{file_name}' created successfully!")
import pandas as pd

# Data for sections 9011 to 9019 – Add more as needed
data = [
    {"HS Code": "9011.10.00", "Stat Code": "03", "Unit": "No", "Goods": "Stereoscopic microscopes", "Rate": "Free", "TCO": "No"},
    {"HS Code": "9011.20.00", "Stat Code": "04", "Unit": "No", "Goods": "Other microscopes for photomicrography, etc.", "Rate": "Free", "TCO": "No"},
    {"HS Code": "9011.80.00", "Stat Code": "04", "Unit": "No", "Goods": "Other microscopes", "Rate": "Free", "TCO": "No"},
    {"HS Code": "9011.90.00", "Stat Code": "06", "Unit": "..", "Goods": "Parts and accessories for microscopes", "Rate": "Free", "TCO": "No"},
    
    {"HS Code": "9012.10.00", "Stat Code": "20", "Unit": "No", "Goods": "Microscopes other than optical; diffraction apparatus", "Rate": "Free", "TCO": "No"},
    {"HS Code": "9012.90.00", "Stat Code": "20", "Unit": "..", "Goods": "Parts and accessories", "Rate": "Free", "TCO": "No"},
    
    {"HS Code": "9013.20.00", "Stat Code": "10", "Unit": "No", "Goods": "Lasers, other than laser diodes", "Rate": "Free", "TCO": "No"},
    {"HS Code": "9013.80.00", "Stat Code": "54", "Unit": "No", "Goods": "Other optical devices, appliances and instruments", "Rate": "Free", "TCO": "No"},
    
    {"HS Code": "9014.10.00", "Stat Code": "16", "Unit": "No", "Goods": "Direction finding compasses", "Rate": "Free", "TCO": "No"},
    {"HS Code": "9015.10.00", "Stat Code": "78", "Unit": "No", "Goods": "Rangefinders", "Rate": "Free", "TCO": "No"},
    
    {"HS Code": "9016.00.00", "Stat Code": "80", "Unit": "..", "Goods": "Balances of a sensitivity of 5 cg or better", "Rate": "Free", "TCO": "No"},
    
    {"HS Code": "9017.10.00", "Stat Code": "08", "Unit": "No", "Goods": "Drafting tables and machines", "Rate": "Free", "TCO": "No"},
    {"HS Code": "9017.20.10", "Stat Code": "40", "Unit": "No", "Goods": "Disc calculators, protractors, etc.", "Rate": "5%", "TCO": "Yes"},
    {"HS Code": "9017.30.00", "Stat Code": "50", "Unit": "No", "Goods": "Micrometers, callipers and gauges", "Rate": "Free", "TCO": "No"},
    
    {"HS Code": "9018.11.00", "Stat Code": "16", "Unit": "..", "Goods": "Electro-cardiographs", "Rate": "Free", "TCO": "No"},
    {"HS Code": "9018.12.00", "Stat Code": "43", "Unit": "No", "Goods": "Ultrasonic scanning apparatus", "Rate": "Free", "TCO": "No"},
    {"HS Code": "9018.13.00", "Stat Code": "44", "Unit": "No", "Goods": "MRI apparatus", "Rate": "Free", "TCO": "No"},
    {"HS Code": "9018.20.00", "Stat Code": "20", "Unit": "..", "Goods": "UV or IR ray apparatus", "Rate": "Free", "TCO": "No"},
    
    {"HS Code": "9019.10.00", "Stat Code": "12", "Unit": "..", "Goods": "Mechano-therapy, massage apparatus", "Rate": "Free", "TCO": "No"},
    {"HS Code": "9019.20.00", "Stat Code": "84", "Unit": "..", "Goods": "Ozone/oxygen/aerosol therapy apparatus", "Rate": "Free", "TCO": "No"},
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Export to Excel
output_file = "Chapter90_HS_Codes_9011_to_9019.xlsx"
df.to_excel(output_file, index=False)

print(f"Excel sheet '{output_file}' created successfully!")
import pandas as pd

# Data sample for codes 9020 to 9033 (extend or automate as needed)
data = [
    {"HS Code": "9020.00.00", "Stat Code": "51", "Unit": "..", "Goods": "Breathing appliances for underwater", "Rate": "Free", "TCO": ""},
    {"HS Code": "9020.00.00", "Stat Code": "52", "Unit": "..", "Goods": "Other breathing appliances and gas masks", "Rate": "Free", "TCO": ""},
    
    {"HS Code": "9021.10.10", "Stat Code": "64", "Unit": "..", "Goods": "Footwear and insoles made to measure for orthopedic disorder", "Rate": "Free", "TCO": ""},
    {"HS Code": "9021.10.20", "Stat Code": "69", "Unit": "..", "Goods": "Footwear (NSA) for orthopedic conditions", "Rate": "5%", "TCO": ""},
    {"HS Code": "9021.10.30", "Stat Code": "56", "Unit": "..", "Goods": "Special insoles (NSA) for orthopedic conditions", "Rate": "5%", "TCO": ""},
    {"HS Code": "9021.10.42", "Stat Code": "73", "Unit": "..", "Goods": "Parts of titanium for orthopedic appliances", "Rate": "Free", "TCO": ""},
    {"HS Code": "9021.21.00", "Stat Code": "17", "Unit": "..", "Goods": "Artificial teeth", "Rate": "Free", "TCO": ""},
    {"HS Code": "9021.29.90", "Stat Code": "90", "Unit": "..", "Goods": "Other dental fittings", "Rate": "Free", "TCO": ""},

    {"HS Code": "9022.12.00", "Stat Code": "45", "Unit": "..", "Goods": "Computed tomography apparatus", "Rate": "Free", "TCO": ""},
    {"HS Code": "9022.30.00", "Stat Code": "28", "Unit": "No", "Goods": "X-ray tubes", "Rate": "Free", "TCO": ""},

    {"HS Code": "9025.11.00", "Stat Code": "07", "Unit": "No", "Goods": "Liquid-filled thermometers for direct reading", "Rate": "Free", "TCO": ""},
    {"HS Code": "9026.10.20", "Stat Code": "59", "Unit": "No", "Goods": "Gauges used in passenger motor vehicles", "Rate": "5%", "TCO": ""},

    {"HS Code": "9027.10.00", "Stat Code": "01", "Unit": "No", "Goods": "Gas or smoke analysis apparatus", "Rate": "Free", "TCO": ""},
    {"HS Code": "9027.81.00", "Stat Code": "80", "Unit": "No", "Goods": "Mass spectrometers", "Rate": "Free", "TCO": ""},

    {"HS Code": "9028.10.10", "Stat Code": "24", "Unit": "No", "Goods": "Household gas meters", "Rate": "Free", "TCO": ""},
    {"HS Code": "9028.30.00", "Stat Code": "17", "Unit": "No", "Goods": "Single-phase electricity meters", "Rate": "Free", "TCO": ""},

    {"HS Code": "9030.10.00", "Stat Code": "74", "Unit": "No", "Goods": "Radiation measuring instruments", "Rate": "Free", "TCO": ""},
    {"HS Code": "9030.20.00", "Stat Code": "75", "Unit": "No", "Goods": "Oscilloscopes and oscillographs", "Rate": "Free", "TCO": ""},
    {"HS Code": "9030.31.00", "Stat Code": "40", "Unit": "No", "Goods": "Multimeters without recording device", "Rate": "Free", "TCO": ""},
    
    {"HS Code": "9031.10.80", "Stat Code": "69", "Unit": "No", "Goods": "Other machines for balancing mechanical parts", "Rate": "Free", "TCO": ""},
    {"HS Code": "9031.80.00", "Stat Code": "83", "Unit": "No", "Goods": "Other measuring instruments and machines", "Rate": "Free", "TCO": ""},

    {"HS Code": "9032.10.00", "Stat Code": "50", "Unit": "No", "Goods": "Thermostats", "Rate": "Free", "TCO": ""},
    {"HS Code": "9032.89.80", "Stat Code": "89", "Unit": "No", "Goods": "Other automatic regulating instruments", "Rate": "Free", "TCO": ""},

    {"HS Code": "9033.00.00", "Stat Code": "11", "Unit": "..", "Goods": "Parts & accessories not specified in Chapter 90", "Rate": "Free", "TCO": ""}
]

# Create DataFrame
df = pd.DataFrame(data)

# Export to Excel
output_file = "chapter_90_hs_codes.xlsx"
df.to_excel(output_file, index=False)

print(f"✅ Excel file '{output_file}' has been created successfully.")
import pandas as pd

# Sample structured data from Chapter 91
data = [
    {"HS Code": "9101.11.00", "Stat Code": "36", "Unit": "No", "Goods": "Wrist-watches, electrically operated, mechanical display only", "Rate": "Free"},
    {"HS Code": "9101.19.00", "Stat Code": "37", "Unit": "No", "Goods": "Wrist-watches, electrically operated, other", "Rate": "Free"},
    {"HS Code": "9101.21.00", "Stat Code": "04", "Unit": "No", "Goods": "Wrist-watches, other, with automatic winding", "Rate": "Free"},
    {"HS Code": "9101.29.00", "Stat Code": "39", "Unit": "No", "Goods": "Wrist-watches, other", "Rate": "Free"},
    {"HS Code": "9102.11.00", "Stat Code": "42", "Unit": "No", "Goods": "Wrist-watches (not of 9101), mechanical display only", "Rate": "Free"},
    {"HS Code": "9102.12.00", "Stat Code": "43", "Unit": "No", "Goods": "Wrist-watches (not of 9101), opto-electronic display only", "Rate": "Free"},
    {"HS Code": "9105.11.00", "Stat Code": "50", "Unit": "No", "Goods": "Alarm clocks, electrically operated", "Rate": "Free"},
    {"HS Code": "9105.29.00", "Stat Code": "60", "Unit": "No", "Goods": "Wall clocks, other", "Rate": "Free"},
    {"HS Code": "9106.10.00", "Stat Code": "27", "Unit": "No", "Goods": "Time-registers and recorders", "Rate": "5% DCS:Free"},
    {"HS Code": "9107.00.00", "Stat Code": "24", "Unit": "No", "Goods": "Time switches with clock/watch movement or synchronous motor", "Rate": "5%"},
    {"HS Code": "9108.12.00", "Stat Code": "33", "Unit": "No", "Goods": "Watch movements, opto-electronic display", "Rate": "Free"},
    {"HS Code": "9109.10.00", "Stat Code": "20", "Unit": "No", "Goods": "Clock movements, electrically operated", "Rate": "Free"},
    {"HS Code": "9110.11.00", "Stat Code": "11", "Unit": "SR", "Goods": "Watch movements, unassembled, complete", "Rate": "Free"},
    {"HS Code": "9111.20.00", "Stat Code": "17", "Unit": "No", "Goods": "Watch cases of base metal", "Rate": "Free"},
    {"HS Code": "9113.10.00", "Stat Code": "23", "Unit": "..", "Goods": "Watch straps of precious metal", "Rate": "5% CA:Free"},
    {"HS Code": "9114.90.00", "Stat Code": "90", "Unit": "..", "Goods": "Other clock or watch parts", "Rate": "Free"}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to Excel
output_filename = "chapter_91_clocks_and_watches.xlsx"
df.to_excel(output_filename, index=False)

print(f"✅ Excel file '{output_filename}' has been created successfully.")
import pandas as pd

# Chapter 92 data
data = [
    {"HS Code": "9201.10.00", "Stat Code": "51", "Unit": "No", "Goods": "Upright pianos", "Rate": "Free"},
    {"HS Code": "9201.20.00", "Stat Code": "52", "Unit": "No", "Goods": "Grand pianos", "Rate": "Free"},
    {"HS Code": "9201.90.00", "Stat Code": "53", "Unit": "No", "Goods": "Other pianos and keyboard stringed instruments", "Rate": "Free"},
    {"HS Code": "9202.10.00", "Stat Code": "07", "Unit": "No", "Goods": "String instruments played with a bow", "Rate": "Free"},
    {"HS Code": "9202.90.00", "Stat Code": "38", "Unit": "No", "Goods": "Acoustic guitars including acoustic-electric", "Rate": "5% DCS:4% DCT:5%"},
    {"HS Code": "9202.90.00", "Stat Code": "39", "Unit": "No", "Goods": "Other string musical instruments", "Rate": "5% DCS:4% DCT:5%"},
    {"HS Code": "9205.10.00", "Stat Code": "13", "Unit": "No", "Goods": "Brass-wind instruments", "Rate": "Free"},
    {"HS Code": "9205.90.00", "Stat Code": "15", "Unit": "No", "Goods": "Flutes and piccolos", "Rate": "Free"},
    {"HS Code": "9205.90.00", "Stat Code": "16", "Unit": "No", "Goods": "Clarinets", "Rate": "Free"},
    {"HS Code": "9205.90.00", "Stat Code": "36", "Unit": "No", "Goods": "Saxophones", "Rate": "Free"},
    {"HS Code": "9206.00.00", "Stat Code": "42", "Unit": "SR", "Goods": "Drum sets", "Rate": "Free"},
    {"HS Code": "9206.00.00", "Stat Code": "43", "Unit": "No", "Goods": "Other drums", "Rate": "Free"},
    {"HS Code": "9206.00.00", "Stat Code": "44", "Unit": "No", "Goods": "Cymbals", "Rate": "Free"},
    {"HS Code": "9207.10.00", "Stat Code": "40", "Unit": "No", "Goods": "Organs (electric, keyboard)", "Rate": "Free"},
    {"HS Code": "9207.90.00", "Stat Code": "48", "Unit": "No", "Goods": "Electric bass guitars", "Rate": "5% DCS:4% DCT:5%"},
    {"HS Code": "9208.10.00", "Stat Code": "26", "Unit": "No", "Goods": "Musical boxes", "Rate": "Free"},
    {"HS Code": "9208.90.00", "Stat Code": "27", "Unit": "No", "Goods": "Other musical instruments & signaling items", "Rate": "Free"},
    {"HS Code": "9209.30.00", "Stat Code": "51", "Unit": "..", "Goods": "Guitar and bass guitar strings", "Rate": "Free"},
    {"HS Code": "9209.91.00", "Stat Code": "31", "Unit": "..", "Goods": "Parts/accessories for pianos", "Rate": "Free"},
    {"HS Code": "9209.92.00", "Stat Code": "32", "Unit": "..", "Goods": "Parts/accessories for 9202 instruments", "Rate": "5% DCS:4% DCT:5%"},
    {"HS Code": "9209.94.00", "Stat Code": "34", "Unit": "..", "Goods": "Parts/accessories for 9207 instruments", "Rate": "Free"},
    {"HS Code": "9209.99.00", "Stat Code": "54", "Unit": "..", "Goods": "Other musical parts/accessories", "Rate": "Free"}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to Excel
output_file = "chapter_92_musical_instruments.xlsx"
df.to_excel(output_file, index=False)

print(f"✅ Excel file '{output_file}' has been created successfully.")
