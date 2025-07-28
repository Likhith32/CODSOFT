import pandas as pd

# Sample structured data - ideally loaded from Excel
data = {
    'Heading': ['8401.10.00', '8401.20.00', '8401.30.00', '8401.40.00',
                '8402.11.00', '8402.12.00', '8402.19.00', '8402.20.00', '8402.90.00',
                '8403.10.00', '8403.90.00', '8404.10.00', '8404.20.00', '8404.90.00',
                '8405.10.00', '8405.90.00', '8406.10.00', '8406.81.00', '8406.82.00', '8406.90.00'],
    'Code': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '70', '66', '67', '68'],
    'Unit': ['No', '..', 'kg', '..', 'No', 'No', 'No', 'No', '..',
             'No', '..', 'No', 'No', '..', '..', '..', 'No', 'No', 'No', '..'],
    'Goods': [
        'Nuclear reactors',
        'Machinery and apparatus for isotopic separation, and parts thereof',
        'Fuel elements (cartridges), non-irradiated',
        'Parts of nuclear reactors',
        'Watertube boilers with a steam production exceeding 45 t per hour',
        'Watertube boilers with a steam production not exceeding 45 t per hour',
        'Other vapour generating boilers, including hybrid boilers',
        'Super-heated water boilers',
        'Parts',
        'Boilers',
        'Parts',
        'Auxiliary plant for use with boilers of 8402 or 8403',
        'Condensers for steam or other vapour power units',
        'Parts',
        'Producer gas or water gas generators, etc.',
        'Parts',
        'Turbines for marine propulsion',
        'Of an output exceeding 40 MW',
        'Of an output not exceeding 40 MW',
        'Parts'
    ],
    'Rate': ['5%', 'Free', '5%', '5%', '5%', '5%', '5%', '5%', '5%',
             '5%', '5%', '5%', 'Free', '5%', '5%', '5%', 'Free', 'Free', 'Free', 'Free']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display entire DataFrame
print("Complete Chapter 84 Entries:")
print(df)

# Filter example: Search for "boilers"
keyword = "boiler"
filtered = df[df['Goods'].str.contains(keyword, case=False, na=False)]

print("\nFiltered rows containing keyword '{}':".format(keyword))
print(filtered)

# Export filtered results to Excel
filtered.to_excel("filtered_boiler_entries.xlsx", index=False)

# Save full data as Excel (optional)
df.to_excel("chapter84_full.xlsx", index=False)
import pandas as pd

# Define the structured data as a list of dictionaries
data = [
    {"Reference Number": "8407.10.00", "Statistical Code": "23", "Unit": "No", "Goods": "Aircraft engines", "Rate#": "Free", "Tariff concession orders": ""},
    
    {"Reference Number": "8407.21.00", "Statistical Code": "", "Unit": "No", "Goods": "Outboard motors", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "", "Statistical Code": "61", "Unit": "No", "Goods": "..Not exceeding 9.9 kW", "Rate#": "", "Tariff concession orders": ""},
    {"Reference Number": "", "Statistical Code": "62", "Unit": "No", "Goods": "..Exceeding 9.9 kW but not exceeding 15.9 kW", "Rate#": "", "Tariff concession orders": ""},
    {"Reference Number": "", "Statistical Code": "63", "Unit": "No", "Goods": "..Exceeding 15.9 kW but not exceeding 28.9 kW", "Rate#": "", "Tariff concession orders": ""},
    {"Reference Number": "", "Statistical Code": "64", "Unit": "No", "Goods": "..Exceeding 28.9 kW", "Rate#": "", "Tariff concession orders": ""},
    {"Reference Number": "", "Statistical Code": "65", "Unit": "No", "Goods": "..Not exceeding 19.9 kW", "Rate#": "", "Tariff concession orders": ""},
    {"Reference Number": "", "Statistical Code": "49", "Unit": "No", "Goods": "..Exceeding 19.9 kW but not exceeding 28.9 kW", "Rate#": "", "Tariff concession orders": ""},
    {"Reference Number": "", "Statistical Code": "50", "Unit": "No", "Goods": "..Exceeding 28.9 kW but not exceeding 33.9 kW", "Rate#": "", "Tariff concession orders": ""},
    {"Reference Number": "", "Statistical Code": "51", "Unit": "No", "Goods": "..Exceeding 33.9 kW but not exceeding 41.9 kW", "Rate#": "", "Tariff concession orders": ""},
    {"Reference Number": "", "Statistical Code": "52", "Unit": "No", "Goods": "..Exceeding 41.9 kW but not exceeding 49.9 kW", "Rate#": "", "Tariff concession orders": ""},
    {"Reference Number": "", "Statistical Code": "53", "Unit": "No", "Goods": "..Exceeding 49.9 kW but not exceeding 57.9 kW", "Rate#": "", "Tariff concession orders": ""},
    {"Reference Number": "", "Statistical Code": "54", "Unit": "No", "Goods": "..Exceeding 57.9 kW but not exceeding 68.9 kW", "Rate#": "", "Tariff concession orders": ""},
    {"Reference Number": "", "Statistical Code": "55", "Unit": "No", "Goods": "..Exceeding 68.9 kW but not exceeding 90.9 kW", "Rate#": "", "Tariff concession orders": ""},
    {"Reference Number": "", "Statistical Code": "56", "Unit": "No", "Goods": "..Exceeding 90.9 kW but not exceeding 112.9 kW", "Rate#": "", "Tariff concession orders": ""},
    {"Reference Number": "", "Statistical Code": "57", "Unit": "No", "Goods": "..Exceeding 112.9 kW but not exceeding 179.9 kW", "Rate#": "", "Tariff concession orders": ""},
    {"Reference Number": "", "Statistical Code": "58", "Unit": "No", "Goods": "..Exceeding 179.9 kW", "Rate#": "", "Tariff concession orders": ""},
    {"Reference Number": "", "Statistical Code": "59", "Unit": "No", "Goods": "Other", "Rate#": "", "Tariff concession orders": ""},

    {"Reference Number": "8407.29.00", "Statistical Code": "25", "Unit": "No", "Goods": "Other", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8407.31.00", "Statistical Code": "26", "Unit": "No", "Goods": "Of a cylinder capacity not exceeding 50 cm3", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8407.32.00", "Statistical Code": "11", "Unit": "No", "Goods": "Exceeding 50 c​m3 but not exceeding 250 cm3", "Rate#": "Free", "Tariff concession orders": ""},

    # Add more entries similarly as needed...
]

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("engine_tariffs.xlsx", index=False)

print("Excel file 'engine_tariffs.xlsx' created successfully.")
import pandas as pd

# List of tariff entries
tariff_data = [
    {"Reference Number": "8409.10.00", "Statistical Code": "56", "Unit": "..", "Goods": "For aircraft engines", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8409.91.10", "Statistical Code": "16", "Unit": "..", "Goods": "Valves - Original equipment", "Rate#": "5%", "Tariff concession orders": "View TCOs"},
    {"Reference Number": "8409.91.10", "Statistical Code": "63", "Unit": "..", "Goods": "Other including carburettors and parts thereof, piston rings and piston pins - Original equipment", "Rate#": "5%", "Tariff concession orders": ""},
    {"Reference Number": "8409.91.10", "Statistical Code": "58", "Unit": "..", "Goods": "Carburettors and parts thereof - Replacement equipment", "Rate#": "5%", "Tariff concession orders": ""},
    {"Reference Number": "8409.91.10", "Statistical Code": "36", "Unit": "No", "Goods": "Piston with pin (excluding pistons with rings)", "Rate#": "5%", "Tariff concession orders": ""},
    {"Reference Number": "8409.91.10", "Statistical Code": "37", "Unit": "No", "Goods": "Piston assemblies", "Rate#": "5%", "Tariff concession orders": ""},
    {"Reference Number": "8409.91.10", "Statistical Code": "64", "Unit": "..", "Goods": "Other including piston pins, piston rings and valves", "Rate#": "5%", "Tariff concession orders": ""},
    {"Reference Number": "8409.91.10", "Statistical Code": "47", "Unit": "..", "Goods": "Other", "Rate#": "5%", "Tariff concession orders": ""},
    {"Reference Number": "8409.91.90", "Statistical Code": "65", "Unit": "..", "Goods": "Other", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8409.99.10", "Statistical Code": "27", "Unit": "..", "Goods": "Original equipment", "Rate#": "5%", "Tariff concession orders": ""},
    {"Reference Number": "8409.99.10", "Statistical Code": "44", "Unit": "..", "Goods": "Replacement equipment for highway motor vehicles", "Rate#": "5%", "Tariff concession orders": ""},
    {"Reference Number": "8409.99.10", "Statistical Code": "32", "Unit": "..", "Goods": "Other", "Rate#": "5%", "Tariff concession orders": ""},
    {"Reference Number": "8409.99.90", "Statistical Code": "62", "Unit": "..", "Goods": "Other", "Rate#": "Free", "Tariff concession orders": "View TCOs"},
    
    {"Reference Number": "8410.11.00", "Statistical Code": "01", "Unit": "No", "Goods": "Hydraulic turbines <= 1000 kW", "Rate#": "5%", "Tariff concession orders": "View TCOs"},
    {"Reference Number": "8410.12.00", "Statistical Code": "02", "Unit": "No", "Goods": "Hydraulic turbines > 1000 kW <= 10000 kW", "Rate#": "5%", "Tariff concession orders": "View TCOs"},
    {"Reference Number": "8410.13.00", "Statistical Code": "03", "Unit": "No", "Goods": "Hydraulic turbines > 10000 kW", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8410.90.00", "Statistical Code": "04", "Unit": "..", "Goods": "Parts, including regulators", "Rate#": "5%", "Tariff concession orders": "View TCOs"},
    
    {"Reference Number": "8411.11.00", "Statistical Code": "05", "Unit": "No", "Goods": "Turbo-jets <= 25 kN", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8411.12.00", "Statistical Code": "06", "Unit": "No", "Goods": "Turbo-jets > 25 kN", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8411.21.00", "Statistical Code": "07", "Unit": "No", "Goods": "Turbo-propellers <= 1100 kW", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8411.22.00", "Statistical Code": "08", "Unit": "No", "Goods": "Turbo-propellers > 1100 kW", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8411.81.00", "Statistical Code": "09", "Unit": "No", "Goods": "Other gas turbines <= 5000 kW", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8411.82.00", "Statistical Code": "10", "Unit": "No", "Goods": "Other gas turbines > 5000 kW", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8411.91.00", "Statistical Code": "11", "Unit": "..", "Goods": "Parts of turbo-jets/turbo-propellers", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8411.99.00", "Statistical Code": "12", "Unit": "..", "Goods": "Other parts", "Rate#": "Free", "Tariff concession orders": ""},
    
    {"Reference Number": "8412.10.00", "Statistical Code": "13", "Unit": "No", "Goods": "Reaction engines other than turbo-jets", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8412.21.00", "Statistical Code": "14", "Unit": "..", "Goods": "Hydraulic power engines - Linear acting (cylinders)", "Rate#": "5%", "Tariff concession orders": "View TCOs"},
    {"Reference Number": "8412.29.00", "Statistical Code": "15", "Unit": "No", "Goods": "Hydraulic power engines - Other", "Rate#": "5%", "Tariff concession orders": "View TCOs"},
    {"Reference Number": "8412.31.00", "Statistical Code": "16", "Unit": "..", "Goods": "Pneumatic power engines - Linear acting", "Rate#": "5%", "Tariff concession orders": "View TCOs"},
    {"Reference Number": "8412.39.10", "Statistical Code": "27", "Unit": "No", "Goods": "Actuators for valves; compressed gas engines", "Rate#": "5%", "Tariff concession orders": "View TCOs"},
    {"Reference Number": "8412.39.90", "Statistical Code": "19", "Unit": "No", "Goods": "Other pneumatic engines", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8412.80.00", "Statistical Code": "30", "Unit": "No", "Goods": "Wind turbines", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8412.80.00", "Statistical Code": "35", "Unit": "..", "Goods": "Other", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8412.90.10", "Statistical Code": "21", "Unit": "..", "Goods": "Parts for 8412.10.00, 8412.39.90, 8412.80.00", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8412.90.90", "Statistical Code": "22", "Unit": "..", "Goods": "Other parts", "Rate#": "5%", "Tariff concession orders": "View TCOs"},
]

# Convert to DataFrame
df = pd.DataFrame(tariff_data)

# Export to Excel
df.to_excel("tariff_engines_parts.xlsx", index=False)

print("Excel file 'tariff_engines_parts.xlsx' created successfully.")
import pandas as pd

# Structured tariff data from Reference Numbers 8413 to 8416
data = [
    # 8413 - PUMPS FOR LIQUIDS
    {"Reference Number": "8413.11.00", "Statistical Code": "23", "Unit": "No", "Goods": "Pumps for dispensing fuel or lubricants", "Rate#": "Free", "Tariff concession orders": "View TCOs for 8413.11.00"},
    {"Reference Number": "8413.19.00", "Statistical Code": "24", "Unit": "No", "Goods": "Other", "Rate#": "5%", "Tariff concession orders": "View TCOs for 8413.19.00"},
    {"Reference Number": "8413.20.00", "Statistical Code": "25", "Unit": "No", "Goods": "Hand pumps", "Rate#": "5%", "Tariff concession orders": "View TCOs for 8413.20.00"},
    {"Reference Number": "8413.30.10", "Statistical Code": "03", "Unit": "No", "Goods": "Fuel/oil/petrol pumps for combustion engines", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8413.30.90", "Statistical Code": "35", "Unit": "No", "Goods": "Other fuel/lubricating/cooling medium pumps", "Rate#": "5%", "Tariff concession orders": "View TCOs for 8413.30.90"},
    {"Reference Number": "8413.40.00", "Statistical Code": "05", "Unit": "No", "Goods": "Concrete pumps", "Rate#": "5%", "Tariff concession orders": "View TCOs for 8413.40.00"},
    {"Reference Number": "8413.50.10", "Statistical Code": "06", "Unit": "No", "Goods": "Mining/metallurgical industry pumps", "Rate#": "5% DCS:4% DCT:5%", "Tariff concession orders": "View TCOs for 8413.50.10"},
    {"Reference Number": "8413.50.90", "Statistical Code": "60", "Unit": "No", "Goods": "Other reciprocating pumps", "Rate#": "5%", "Tariff concession orders": "View TCOs for 8413.50.90"},
    {"Reference Number": "8413.60.10", "Statistical Code": "10", "Unit": "No", "Goods": "Rotary pumps for mining/metallurgical use", "Rate#": "5% DCS:4% DCT:5%", "Tariff concession orders": "View TCOs for 8413.60.10"},
    {"Reference Number": "8413.60.90", "Statistical Code": "61", "Unit": "No", "Goods": "Other rotary pumps", "Rate#": "5%", "Tariff concession orders": "View TCOs for 8413.60.90"},
    {"Reference Number": "8413.70.10", "Statistical Code": "14", "Unit": "No", "Goods": "Centrifugal pumps for mining/metallurgy", "Rate#": "5% DCS:4% DCT:5%", "Tariff concession orders": "View TCOs for 8413.70.10"},
    {"Reference Number": "8413.70.90", "Statistical Code": "62", "Unit": "No", "Goods": "Other centrifugal pumps", "Rate#": "5%", "Tariff concession orders": "View TCOs for 8413.70.90"},
    {"Reference Number": "8413.81.10", "Statistical Code": "17", "Unit": "No", "Goods": "Pumps for mining/metallurgy", "Rate#": "5% DCS:4% DCT:5%", "Tariff concession orders": ""},
    {"Reference Number": "8413.81.90", "Statistical Code": "63", "Unit": "No", "Goods": "Other pumps", "Rate#": "5%", "Tariff concession orders": "View TCOs for 8413.81.90"},
    {"Reference Number": "8413.82.00", "Statistical Code": "20", "Unit": "No", "Goods": "Liquid elevators", "Rate#": "5%", "Tariff concession orders": ""},
    {"Reference Number": "8413.91.10", "Statistical Code": "21", "Unit": "..", "Goods": "Parts for mining/metallurgical pumps", "Rate#": "5% DCS:4% DCT:5%", "Tariff concession orders": "View TCOs for 8413.91.10"},
    {"Reference Number": "8413.91.20", "Statistical Code": "64", "Unit": "..", "Goods": "Parts of pumps of 8413.30.10", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8413.91.90", "Statistical Code": "65", "Unit": "..", "Goods": "Other pump parts", "Rate#": "5%", "Tariff concession orders": "View TCOs for 8413.91.90"},
    {"Reference Number": "8413.92.00", "Statistical Code": "23", "Unit": "..", "Goods": "Parts of liquid elevators", "Rate#": "5%", "Tariff concession orders": ""},

    # 8414 - AIR OR VACUUM PUMPS, FANS
    {"Reference Number": "8414.10.10", "Statistical Code": "24", "Unit": "No", "Goods": "Vacuum pumps for semiconductors/displays", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8414.10.90", "Statistical Code": "26", "Unit": "No", "Goods": "Other vacuum pumps", "Rate#": "5%", "Tariff concession orders": "View TCOs for 8414.10.90"},
    {"Reference Number": "8414.20.00", "Statistical Code": "25", "Unit": "No", "Goods": "Hand/foot air pumps", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8414.30.00", "Statistical Code": "66", "Unit": "No", "Goods": "Compressors for refrigeration", "Rate#": "5%", "Tariff concession orders": "View TCOs for 8414.30.00"},
    {"Reference Number": "8414.40.10", "Statistical Code": "35", "Unit": "No", "Goods": "Air compressors ≤ 3 m3/min", "Rate#": "Free", "Tariff concession orders": "View TCOs for 8414.40.10"},
    {"Reference Number": "8414.40.20", "Statistical Code": "36", "Unit": "No", "Goods": "Air compressors > 3 m3/min and ≤ 25", "Rate#": "Free", "Tariff concession orders": "View TCOs for 8414.40.20"},
    {"Reference Number": "8414.40.90", "Statistical Code": "54", "Unit": "No", "Goods": "Other air compressors", "Rate#": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8414.51.00", "Statistical Code": "01", "Unit": "No", "Goods": "Fans ≤ 125 W", "Rate#": "5%", "Tariff concession orders": "View TCOs for 8414.51.00"},

    # 8415 - AIR CONDITIONING MACHINES
    {"Reference Number": "8415.10.00", "Statistical Code": "37", "Unit": "No", "Goods": "ACs < 3 kW", "Rate#": "5%", "Tariff concession orders": "View TCOs for 8415.10.00"},
    {"Reference Number": "8415.20.00", "Statistical Code": "60", "Unit": "No", "Goods": "Vehicle air conditioners", "Rate#": "5%", "Tariff concession orders": "View TCOs for 8415.20.00"},
    {"Reference Number": "8415.81.00", "Statistical Code": "20", "Unit": "No", "Goods": "Reversible heat pump ACs", "Rate#": "5%", "Tariff concession orders": "View TCOs for 8415.81.00"},
    {"Reference Number": "8415.82.00", "Statistical Code": "63", "Unit": "No", "Goods": "ACs with refrigerating unit", "Rate#": "5%", "Tariff concession orders": "View TCOs for 8415.82.00"},
    {"Reference Number": "8415.90.00", "Statistical Code": "66", "Unit": "..", "Goods": "Parts for ACs", "Rate#": "5%", "Tariff concession orders": "View TCOs for 8415.90.00"},

    # 8416 - FURNACE BURNERS
    {"Reference Number": "8416.10.00", "Statistical Code": "25", "Unit": "No", "Goods": "Furnace burners for liquid fuel", "Rate#": "5% CA:Free", "Tariff concession orders": ""},
    {"Reference Number": "8416.20.00", "Statistical Code": "26", "Unit": "No", "Goods": "Other furnace burners", "Rate#": "5% CA:Free", "Tariff concession orders": "View TCOs for 8416.20.00"},
    {"Reference Number": "8416.30.00", "Statistical Code": "27", "Unit": "..", "Goods": "Mechanical stokers", "Rate#": "5% DCS:4% DCT:5%", "Tariff concession orders": "View TCOs for 8416.30.00"},
    {"Reference Number": "8416.90.00", "Statistical Code": "28", "Unit": "..", "Goods": "Parts for burners/stokers", "Rate#": "5% CA:Free", "Tariff concession orders": "View TCOs for 8416.90.00"},
]

# Create DataFrame and save to Excel
df = pd.DataFrame(data)
file_path = "/mnt/data/tariff_8413_to_8416.xlsx"
df.to_excel(file_path, index=False)

file_path
import pandas as pd

# Data for HS codes 8417 to 8419
data = [
    # 8417
    [8417.10, 29, 'No', 'Furnaces and ovens for the roasting, melting or other heat-treatment of ores, pyrites or of metals', '5% DCS:4% DCT:5%'],
    [8417.20, 30, 'No', 'Bakery ovens, including biscuit ovens', '5% DCS:4% DCT:5%'],
    [8417.80, 31, 'No', 'Other', '5% DCS:4% DCT:5%'],
    [8417.90, 32, '..', 'Parts', '5% DCS:4% DCT:5%'],

    # 8418
    [8418.10, '', '', 'Combined refrigerator‑freezers, fitted with separate external doors or drawers, or combinations thereof', 'Free'],
    [8418.21, '', '', 'Compression-type (household)', '5%'],
    [8418.29, 21, 'No', 'Other (household)', '5%'],
    [8418.30, '', '', 'Freezers, chest type ≤ 800L', 'Free'],
    [8418.40, '', '', 'Freezers, upright type ≤ 900L', 'Free'],
    [8418.50, 30, 'No', 'Furniture with refrigerating or freezing equipment', '5%'],
    [8418.61, 32, 'No', 'Heat pumps other than air conditioning machines of 8415', '5%'],
    [8418.69, '', '', 'Other refrigerating or freezing equipment', '5%'],
    [8418.91, 48, '..', 'Furniture designed to receive refrigerating or freezing equipment', '5%'],
    [8418.99, '', '', 'Other parts', '5%'],

    # 8419
    [8419.11, 9, 'No', 'Instantaneous gas water heaters', '5%'],
    [8419.12, 1, 'No', 'Solar water heaters', 'Free'],
    [8419.19, 90, 'No', 'Other non-electric water heaters', '5%'],
    [8419.20, 11, 'No', 'Medical, surgical or laboratory sterilisers', '5% DCS:4% DCT:5%'],
    [8419.33, 3, 'No', 'Lyophilisation apparatus, freeze drying units and spray dryers', 'Free'],
    [8419.34, 4, 'No', 'Dryers for agricultural products', '5% DCS:4% DCT:5%'],
    [8419.35, 5, 'No', 'Dryers for wood, paper pulp, paper or paperboard', 'Free'],
    [8419.39, '', '', 'Other dryers', '5%'],
    [8419.40, 15, 'No', 'Distilling or rectifying plant', '5% DCS:4% DCT:5%'],
    [8419.50, 36, '..', 'Heat exchange units', '5% DCS:4% DCT:5%'],
    [8419.60, 17, '..', 'Machinery for liquefying air or other gases', 'Free'],
    [8419.81, '', '', 'Hot drink/cooking or heating food machines', '5% DCS:4% DCT:5%'],
    [8419.89, '', '', 'Other equipment', '5% DCS:4% DCT:5%'],
    [8419.90, 7, '..', 'Parts', '5%']
]

# Define column headers
columns = ['Reference Number', 'Statistical Code', 'Unit', 'Goods', 'Rate#']

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save to Excel
output_file = 'tariff_8417_to_8419.xlsx'
df.to_excel(output_file, index=False)

print(f"✅ Excel file '{output_file}' created successfully.")
import pandas as pd

# Data from 8420 to 8423
data = [
    # 8420
    [8420.10, '01', '..', 'Calendering or other rolling machines', 'Free'],
    [8420.91, '02', '..', 'Cylinders', '5% DCS:4% DCT:5%'],
    [8420.99, '03', '..', 'Other', 'Free'],

    # 8421
    [8421.11, '04', 'No', 'Cream separators', 'Free'],
    [8421.12, '05', 'No', 'Clothes-dryers', 'Free'],
    [8421.19, '20', 'No', 'Other centrifuges', '5%'],
    [8421.21, '36', '..', 'Filtering machinery for swimming pools', '5%'],
    [8421.21, '90', '..', 'Other water filtering machinery', '5% DCS:4% DCT:5%'],
    [8421.22, '08', '..', 'Filtering beverages other than water', '5% DCS:4% DCT:5%'],
    [8421.23, '', '', 'Oil or petrol-filters for internal combustion engines', '5%'],
    [8421.29, '10', 'No', 'Liquid filters (fluoropolymers, membrane ≤140 microns)', '5% → 2.5% → Free'],
    [8421.29, '90', 'No', 'Other liquid filters', '5% DCS:4% DCT:5%'],
    [8421.31, '', '', 'Intake air filters for IC engines', '5%'],
    [8421.32, '60', 'No', 'Catalytic converters/particulate filters', '5% DCS:4% DCT:5%'],
    [8421.39, '10', 'No', 'Gas filters (SS housing, ≤1.3 cm)', '5% → 3.75% → Free'],
    [8421.39, '90', 'No', 'Other gas filters', '5% DCS:4% DCT:5%'],
    [8421.91, '50', '..', 'Parts of centrifuges', '5%'],
    [8421.99, '10', '..', 'Parts of goods 8421.29.10 / 8421.39.10', '5% → 3.75% → Free'],
    [8421.99, '90', '17', 'Other parts', '5%'],

    # 8422
    [8422.11, '22', 'No', 'Dish washing machines (household)', 'Free'],
    [8422.19, '23', 'No', 'Other dish washing machines', '5% DCS:4% DCT:5%'],
    [8422.20, '24', 'No', 'Machinery for cleaning or drying bottles or containers', '5% DCS:4% DCT:5%'],
    [8422.30, '21', 'No', 'Hand electro-mechanical bottle filling/sealing machinery', '5%'],
    [8422.30, '90', '25', 'Other container processing machinery', '5% DCS:4% DCT:5%'],
    [8422.40, '10', '26', 'Hand electro-mechanical wrapping machinery', 'Free'],
    [8422.40, '90', '', 'Other wrapping machines (single & multi-function)', 'Free'],
    [8422.90, '49', '..', 'Parts of 8422 machines', '5%'],

    # 8423
    [8423.10, '', '', 'Personal/household weighing machines', 'Free'],
    [8423.20, '10', '01', 'Conveyor scales using electronics', '5% → 2.5% → Free'],
    [8423.20, '90', '02', 'Other conveyor scales', '5%'],
    [8423.30, '10', '03', 'Bagging/hopper scales using electronics', '5% → 2.5% → Free'],
    [8423.30, '90', '04', 'Other bagging scales', '5%'],
    [8423.81, '10', '05', 'Scales ≤30kg using electronics', '5% → 2.5% → Free'],
    [8423.81, '90', '06', 'Other scales ≤30kg', '5%'],
    [8423.82, '10', '07', 'Scales >30kg to 5000kg using electronics', '5% → 2.5% → Free'],
    [8423.82, '90', '08', 'Other scales >30kg to 5000kg', '5%'],
    [8423.89, '10', '09', 'Other scales using electronics', '5% → 2.5% → Free'],
    [8423.89, '90', '10', 'Other weighing machinery', '5%'],
    [8423.90, '10', '11', 'Parts of electronic weighing machinery', '5% → 2.5% → Free'],
    [8423.90, '90', '12', 'Other parts of weighing machinery', '5%']
]

# Define column headers
columns = ['Reference Number', 'Statistical Code', 'Unit', 'Goods', 'Rate#']

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save to Excel
output_path = 'tariff_8420_to_8423.xlsx'
df.to_excel(output_path, index=False)

print(f"✅ Excel file '{output_path}' has been created successfully.")
import pandas as pd

# Data for HS Codes 8424 to 8428
data = [
    # 8424
    [8424.10, '08', 'No', 'Fire extinguishers, whether or not charged', '5%'],
    [8424.20, '09', 'No', 'Spray guns, imported separately', '5% DCS:4% DCT:5%'],
    [8424.20, '45', 'No', 'Spraying assemblies', '5%'],
    [8424.20, '44', 'No', 'Other spray appliances', '5%'],
    [8424.30, '50', 'No', 'Hand-held electro-mechanical sand blasters', '5%'],
    [8424.30, '51', 'No', 'Other sand blasters', '5% DCS:4% DCT:5%'],
    [8424.41, '01', 'No', 'Portable agricultural sprayers', '5%'],
    [8424.49, '10', 'No', 'Other agricultural sprayers', '5%'],
    [8424.82, '11', 'No', 'Other agricultural appliances', '5%'],
    [8424.89, '10', '16', 'Motor vehicle washer devices', '5%'],
    [8424.89, '20', '17', 'Sprayers for printed circuit boards', '5% → 3.75% → Free'],
    [8424.89, '40', '53', 'Electro-mechanical spraying tools', '5%'],
    [8424.89, '90', '91', 'Other', '5% DCS:4% DCT:5%'],
    [8424.90, '10', '58', 'Parts of 8424.89.20', '5% → 3.75% → Free'],
    [8424.90, '20', '59', 'Parts of 8424.30.10', '5%'],
    [8424.90, '90', '92', 'Other parts', '5%'],

    # 8425
    [8425.11, '23', 'No', 'Electric chain hoists and pulley tackle', '5%'],
    [8425.11, '24', 'No', 'Wire rope hoists', '5%'],
    [8425.11, '25', 'No', 'Other electric hoists', '5%'],
    [8425.19, '31', 'No', 'Manual chain hoists', '5%'],
    [8425.19, '28', 'No', 'Other manual hoists', '5%'],
    [8425.19, '37', 'No', 'Pneumatic hoists', '5%'],
    [8425.31, '29', 'No', 'Electric winches or capstans', '5%'],
    [8425.39, '30', 'No', 'Other winches/capstans', '5%'],
    [8425.41, '04', 'No', 'Garage jacks', '5%'],
    [8425.42, '27', 'No', 'Hydraulic jacks', '5%'],
    [8425.49, '28', 'No', 'Other jacks', '5%'],

    # 8426
    [8426.11, '09', 'No', 'Overhead travelling cranes', '5%'],
    [8426.12, '10', 'No', 'Mobile lifting frames, straddle carriers', '5%'],
    [8426.19, '11', 'No', 'Other overhead cranes', '5%'],
    [8426.20, '12', 'No', 'Tower cranes', '5%'],
    [8426.30, '13', 'No', 'Portal or pedestal jib cranes', '5%'],
    [8426.41, '14', 'No', 'Self-propelled crane on tyres ≤50t', '5%'],
    [8426.41, '15', 'No', 'Self-propelled crane on tyres >50t', '5%'],
    [8426.49, '16', 'No', 'Other self-propelled crane ≤50t', '5%'],
    [8426.49, '17', 'No', 'Other self-propelled crane >50t', '5%'],
    [8426.91, '18', 'No', 'Vehicle-mounted cranes', '5%'],
    [8426.99, '19', 'No', 'Other cranes', '5%'],

    # 8427
    [8427.10, '20', 'No', 'Electric non-rider forklift <1500kg', '5%'],
    [8427.10, '21', 'No', 'Electric non-rider forklift ≥1500kg', '5%'],
    [8427.10, '22', 'No', 'Electric rider forklift <1500kg', '5%'],
    [8427.10, '23', 'No', 'Electric rider forklift 1500–2000kg', '5%'],
    [8427.10, '24', 'No', 'Electric rider forklift 2000–3000kg', '5%'],
    [8427.10, '25', 'No', 'Electric rider forklift ≥3000kg', '5%'],
    [8427.10, '26', 'No', 'Other electric forklifts', '5%'],
    [8427.20, '01', 'No', 'Other self-propelled truck <1500kg', '5%'],
    [8427.20, '02', 'No', '1500–2000kg', '5%'],
    [8427.20, '03', 'No', '2000–3000kg', '5%'],
    [8427.20, '04', 'No', '3000–4000kg', '5%'],
    [8427.20, '05', 'No', '4000–5000kg', '5%'],
    [8427.20, '06', 'No', '5000–6000kg', '5%'],
    [8427.20, '07', 'No', '≥6000kg', '5%'],
    [8427.20, '08', 'No', 'Other', '5%'],
    [8427.90, '32', 'No', 'Other trucks', '5%'],

    # 8428
    [8428.10, '11', 'No', 'Lifts and skip hoists', '5%'],
    [8428.20, '12', 'No', 'Pneumatic elevators and conveyors', '5%'],
    [8428.31, '13', 'No', 'Elevators for underground use', '5%'],
    [8428.32, '14', 'No', 'Bucket elevators', '5%'],
    [8428.33, '15', 'No', 'Belt elevators', '5%'],
    [8428.39, '40', 'No', 'Other elevators', '5%'],
    [8428.40, '17', 'No', 'Escalators and walkways', 'Free'],
    [8428.60, '19', 'No', 'Teleferics, ski lifts, traction units', '5%'],
    [8428.70, '20', 'No', 'Industrial robots', '5%'],
    [8428.90, '90', 'No', 'Other lifting/handling machines', '5%']
]

# Create DataFrame
df = pd.DataFrame(data, columns=['Reference Number', 'Statistical Code', 'Unit', 'Goods', 'Rate#'])

# Save to Excel
file_path = 'tariff_8424_to_8428.xlsx'
df.to_excel(file_path, index=False)

print(f"✅ Excel file '{file_path}' has been created.")
import pandas as pd

# HS Codes 8429 to 8433
data = [
    # 8429
    [8429.11, '38', 'No', 'Bulldozers (track laying)', 'Free'],
    [8429.19, '39', 'No', 'Bulldozers (other)', 'Free'],
    [8429.20, '40', 'No', 'Graders and levellers', '5%'],
    [8429.30, '28', 'No', 'Scrapers', 'Free'],
    [8429.40, '29', 'No', 'Tamping machines and road rollers', '5%'],
    [8429.51, '41', 'No', 'Track-laying or underground shovel loaders >16t', 'Free'],
    [8429.51, '36', 'No', 'Other front-end shovel loaders', '5%'],
    [8429.52, '38', 'No', 'Excavators or draglines >12t or >5m³', 'Free'],
    [8429.52, '39', 'No', 'Other revolving superstructure machines', '5%'],
    [8429.59, '36', '..', 'Mechanical shovels >5m³', 'Free'],
    [8429.59, '04', '..', 'Four-wheel drive wheel loaders', '5%'],
    [8429.59, '40', '..', 'Other machinery', '5%'],

    # 8430
    [8430.10, '06', 'No', 'Pile-drivers and pile-extractors', 'Free'],
    [8430.20, '07', 'No', 'Snow-ploughs and snow-blowers', 'Free'],
    [8430.31, '08', 'No', 'Self-propelled coal/rock cutters and tunnellers', 'Free'],
    [8430.39, '09', 'No', 'Other coal/rock cutters and tunnellers', 'Free'],
    [8430.41, '41', 'No', 'Self-propelled rotary/percussive rock drills', '5%'],
    [8430.49, '43', 'No', 'Other rotary/percussive rock drills', '5%'],
    [8430.50, '45', 'No', 'Other machinery, self-propelled', '5%'],
    [8430.61, '23', 'No', 'Tamping or compacting machinery', 'Free'],
    [8430.69, '30', 'No', 'Scrapers (not self-propelled)', 'Free'],
    [8430.69, '32', 'No', 'Other (not self-propelled)', 'Free'],

    # 8431
    [8431.10, '27', '..', 'Parts of 8425 (hoists etc.)', '5%'],
    [8431.10, '46', '..', 'Other parts of 8425', '5%'],
    [8431.20, '29', '..', 'Fork arms of 8427', '5%'],
    [8431.20, '30', '..', 'Other parts of 8427', '5%'],
    [8431.20, '31', '..', 'Other', '5%'],
    [8431.31, '01', '..', 'Parts of lifts, skip hoists, escalators', '5%'],
    [8431.39, '10', '..', 'Other parts of 8428', '5%'],
    [8431.41, '03', '..', 'Buckets, shovels, grabs, grips (8426/29/30)', '5%'],
    [8431.42, '04', '..', 'Blades for bulldozers or angledozers', '5%'],
    [8431.43, '31', '..', 'Parts of 8430.41/49 boring machinery', '5%'],
    [8431.49, '32', '..', 'Parts of coal/rock cutters (8430.3)', 'Free'],
    [8431.49, '33', '..', 'Other', '5%'],

    # 8432
    [8432.10, '08', 'No', 'Ploughs', 'Free'],
    [8432.21, '09', 'No', 'Disc harrows', 'Free'],
    [8432.29, '47', 'No', 'Other harrows etc.', 'Free'],
    [8432.31, '02', 'No', 'No-till seeders/planters', 'Free'],
    [8432.39, '10', 'No', 'Other seeders/planters', 'Free'],
    [8432.41, '11', 'No', 'Manure spreaders', 'Free'],
    [8432.42, '17', 'No', 'Fertiliser distributors', 'Free'],
    [8432.80, '14', 'No', 'Other machinery for soil preparation', 'Free'],
    [8432.90, '15', 'No', 'Discs (parts)', 'Free'],
    [8432.90, '35', '..', 'Parts for agricultural machinery', 'Free'],
    [8432.90, '59', '..', 'Other parts', 'Free'],

    # 8433
    [8433.11, '55', 'No', 'Ride-on tractor mowers (horizontal blade)', '5%'],
    [8433.11, '56', 'No', 'Walk-behind mowers (horizontal blade)', '5%'],
    [8433.11, '48', 'No', 'Other horizontal blade mowers', '5%'],
    [8433.19, '62', 'No', 'Ride-on mowers (other)', 'Free'],
    [8433.19, '63', 'No', 'Walk-behind mowers (other)', 'Free'],
    [8433.19, '66', 'No', 'Other mowers', 'Free'],
    [8433.20, '26', 'No', 'Other mowers, incl. cutter bar', '5%'],
    [8433.30, '49', 'No', 'Other haymaking machinery', 'Free'],
    [8433.40, '36', 'No', 'Round bale hay balers', 'Free'],
    [8433.40, '37', 'No', 'Other balers', 'Free'],
    [8433.51, '29', 'No', 'Combine harvester-threshers', 'Free'],
    [8433.52, '30', 'No', 'Other threshing machinery', 'Free'],
    [8433.53, '01', 'No', 'Root or tuber harvesting machines', 'Free'],
    [8433.59, '39', 'No', 'Cotton pickers, maize harvesters, tree shakers', 'Free'],
    [8433.59, '43', 'No', 'Other harvesting machinery', '5%'],
    [8433.60, '06', 'No', 'Machines for sorting/agri produce', '5%'],
    [8433.90, '07', '..', 'Parts of combine harvesters', 'Free'],
    [8433.90, '44', '..', 'Other parts', '5%']
]

# Create DataFrame
df = pd.DataFrame(data, columns=['Reference Number', 'Statistical Code', 'Unit', 'Goods', 'Rate#'])

# Save to Excel
file_path = 'tariff_8429_to_8433.xlsx'
df.to_excel(file_path, index=False)

print(f"✅ Excel file '{file_path}' has been created.")
import pandas as pd

# Data for HS Codes 8434 to 8443
data = [
    # 8434
    [8434.10, '12', 'No', 'Milking machines', '5%'],
    [8434.20, '13', 'No', 'Dairy machinery', '5%'],
    [8434.90, '14', '..', 'Parts of milking/dairy machinery', '5%'],

    # 8435
    [8435.10, '15', '..', 'Wine/cider/fruit juice presses/crushers', 'Free'],
    [8435.90, '16', '..', 'Parts', 'Free'],

    # 8436
    [8436.10, '17', '..', 'Machinery for preparing animal feed', '5%'],
    [8436.21, '18', 'No', 'Poultry incubators and brooders', '5%'],
    [8436.29, '19', '..', 'Other poultry-keeping machinery', '5%'],
    [8436.80, '41', '..', 'Tree fellers and harvesters', 'Free'],
    [8436.80, '42', '..', 'Other machinery', '5%'],
    [8436.91, '21', '..', 'Parts of poultry-keeping machines', '5%'],
    [8436.99, '22', '..', 'Other parts', '5%'],

    # 8437
    [8437.10, '23', 'No', 'Seed/grain sorting/cleaning machines', '5%'],
    [8437.80, '24', 'No', 'Other cereal/legume machinery', 'Free'],
    [8437.90, '45', '..', 'Parts', 'Free'],

    # 8438
    [8438.10, '27', '..', 'Macaroni/spaghetti machines', 'Free'],
    [8438.10, '28', '..', 'Other bakery machinery', '5%'],
    [8438.20, '29', '..', 'Confectionery/chocolate machinery', '5%'],
    [8438.30, '30', '..', 'Sugar manufacture machinery', '5%'],
    [8438.40, '31', '..', 'Brewery machinery', '5%'],
    [8438.50, '32', '..', 'Meat/poultry preparation machinery', '5%'],
    [8438.60, '33', '..', 'Fruit/nut/vegetable preparation machinery', '5%'],
    [8438.80, '35', '..', 'Other food machinery', '5%'],
    [8438.90, '38', '..', 'Parts for 8438.10–8438.40 machinery', '5%'],
    [8438.90, '37', '..', 'Other parts', '5%'],

    # 8439
    [8439.10, '01', '..', 'Pulp making machinery', 'Free'],
    [8439.20, '02', '..', 'Paper or board making machinery', 'Free'],
    [8439.30, '03', '..', 'Paper finishing machinery', 'Free'],
    [8439.91, '04', '..', 'Parts of pulp machinery', 'Free'],
    [8439.99, '05', '..', 'Other parts', '5%'],

    # 8440
    [8440.10, '06', 'No', 'Book-binding machinery', 'Free'],
    [8440.90, '07', '..', 'Parts', 'Free'],

    # 8441
    [8441.10, '08', 'No', 'Sheeters/slitters/slitter-rewinders', 'Free'],
    [8441.10, '39', 'No', 'Other cutting machines', 'Free'],
    [8441.20, '12', 'No', 'Bag/sack/envelope making machines', 'Free'],
    [8441.30, '36', 'No', 'Box/carton/tube making machines', 'Free'],
    [8441.40, '15', 'No', 'Moulding machines (paper pulp)', 'Free'],
    [8441.80, '16', 'No', 'Rewinders', '5%'],
    [8441.80, '90', 'No', 'Other paper machinery', 'Free'],
    [8441.90, '18', '..', 'Parts of 8441.10.10/8441.80.10', '5%'],
    [8441.90, '19', '..', 'Parts of 8441.10.90', 'Free'],
    [8441.90, '20', '..', 'Parts of 8441.30.00', 'Free'],
    [8441.90, '21', '..', 'Other parts', 'Free'],

    # 8442
    [8442.30, '25', 'No', 'Plate/cylinder printing machinery', 'Free'],
    [8442.40, '40', '..', 'Parts of above machinery', 'Free'],
    [8442.50, '27', 'kg', 'Prepared plates/cylinders for printing', 'Free'],

    # 8443
    [8443.11, '28', 'No', 'Offset printers (reel-fed)', 'Free'],
    [8443.12, '29', 'No', 'Offset printers (sheet-fed, office)', 'Free'],
    [8443.13, '50', 'No', 'Other offset printers', 'Free'],
    [8443.14, '51', 'No', 'Letterpress printers (reel-fed)', 'Free'],
    [8443.15, '52', 'No', 'Letterpress printers (other)', 'Free'],
    [8443.16, '53', 'No', 'Flexographic printers', 'Free'],
    [8443.17, '54', 'No', 'Gravure printers', 'Free'],
    [8443.19, '55', 'No', 'Hot stamping machines', '5%'],
    [8443.19, '56', 'No', 'Other printing machinery', 'Free'],
    [8443.32, '30', 'No', 'Other printers (network capable)', 'Free'],
    [8443.39, '42', 'No', 'Photocopiers (direct process)', 'Free'],
    [8443.39, '43', 'No', 'Photocopiers (indirect process)', 'Free'],
    [8443.39, '44', 'No', 'Other photocopiers', 'Free'],
    [8443.39, '92', 'No', 'Thermo-copying apparatus', 'Free'],
    [8443.39, '93', 'No', 'Ink-jet', 'Free'],
    [8443.39, '94', 'No', 'Other', 'Free'],
    [8443.91, '60', '..', 'Parts of 8443.19.10', 'Free'],
    [8443.91, '66', '..', 'Accessories', 'Free'],
    [8443.91, '69', '..', 'Parts', 'Free'],
    [8443.99, '71', '..', 'Paper feeders', 'Free'],
    [8443.99, '72', '..', 'Sorters', 'Free'],
    [8443.99, '75', '..', 'Other', 'Free']
]

# Create DataFrame
df = pd.DataFrame(data, columns=['Reference Number', 'Statistical Code', 'Unit', 'Goods', 'Rate#'])

# Save to Excel
file_path = 'tariff_8434_to_8443.xlsx'
df.to_excel(file_path, index=False)

print(f"✅ Excel file '{file_path}' has been created.")
import pandas as pd

# Data list for HS codes 8444 to 8454
data = [
    # 8444
    [8444.00, '06', 'No', 'Machines for extruding, drawing, texturing or cutting man-made textile materials', 'Free'],

    # 8445
    [8445.11, '07', 'No', 'Carding machines', 'Free'],
    [8445.12, '08', 'No', 'Combing machines', 'Free'],
    [8445.13, '09', 'No', 'Drawing or roving machines', 'Free'],
    [8445.19, '05', 'No', 'Other fibre prep machines', 'Free'],
    [8445.20, '12', 'No', 'Textile spinning machines', 'Free'],
    [8445.30, '13', 'No', 'Textile doubling or twisting machines', 'Free'],
    [8445.40, '14', 'No', 'Textile winding/reeling machines', 'Free'],
    [8445.90, '15', 'No', 'Other textile machinery', 'Free'],

    # 8446
    [8446.10, '16', 'No', 'Looms ≤30 cm width', 'Free'],
    [8446.21, '17', 'No', 'Power looms >30 cm shuttle type', 'Free'],
    [8446.29, '18', 'No', 'Other shuttle type looms', 'Free'],
    [8446.30, '19', 'No', 'Shuttleless looms >30 cm', 'Free'],

    # 8447
    [8447.11, '20', 'No', 'Circular knitting machines ≤165 mm', 'Free'],
    [8447.12, '21', 'No', 'Circular knitting machines >165 mm', 'Free'],
    [8447.20, '22', 'No', 'Flat knitting & stitch-bonding machines', 'Free'],
    [8447.90, '23', 'No', 'Other knitting/stitch machines', 'Free'],

    # 8448
    [8448.11, '24', '..', 'Dobbies/Jacquards and related', 'Free'],
    [8448.19, '25', '..', 'Other auxiliary machinery', 'Free'],
    [8448.20, '26', '..', 'Parts of 8444 or auxiliaries', 'Free'],
    [8448.31, '27', '..', 'Card clothing', 'Free'],
    [8448.32, '28', '..', 'Parts of fibre prep machines', 'Free'],
    [8448.33, '29', 'No', 'Spindles, flyers, rings etc.', 'Free'],
    [8448.39, '30', '..', 'Other parts of 8445', 'Free'],
    [8448.42, '32', 'No', 'Reeds, healds & heald-frames', 'Free'],
    [8448.49, '31', 'No', 'Other loom parts', 'Free'],
    [8448.51, '34', '..', 'Needles/sinkers for stitch forming', 'Free'],
    [8448.59, '35', '..', 'Other parts of 8447', 'Free'],

    # 8449
    [8449.00, '36', '..', 'Machinery for felt/nonwovens and hat blocks', 'Free'],

    # 8450
    [8450.11, '42', 'No', 'Fully-automatic washing machines (Top loading)', 'Free'],
    [8450.11, '04', 'No', 'Fully-automatic washing machines (Front loading)', 'Free'],
    [8450.12, '09', 'No', 'Other with centrifugal drier', 'Free'],
    [8450.19, '07', 'No', 'Other household machines ≤10 kg', 'Free'],
    [8450.20, '08', 'No', 'Machines >10 kg capacity', 'Free'],
    [8450.90, '41', '..', 'Parts for washing machines', '5%'],

    # 8451
    [8451.10, '11', 'No', 'Dry-cleaning machines', 'Free'],
    [8451.21, '18', 'No', 'Drying machines ≤10 kg', 'Free'],
    [8451.29, '14', 'No', 'Other drying machines', '5%'],
    [8451.30, '15', 'No', 'Ironing/pressing machines (Household)', 'Free'],
    [8451.30, '16', 'No', 'Ironing/pressing machines (Other)', 'Free'],
    [8451.40, '22', 'No', 'Washing, bleaching or dyeing machines', 'Free'],
    [8451.50, '19', '..', 'Machines for folding, cutting, pinking', 'Free'],
    [8451.80, '20', 'No', 'Other textile machinery', '5%'],
    [8451.90, '43', '..', 'Parts of above machines', '5%'],

    # 8452
    [8452.10, '10', 'No', 'Household sewing machines', 'Free'],
    [8452.10, '37', 'No', 'Overlockers', 'Free'],
    [8452.10, '15', 'No', 'Other household machines', 'Free'],
    [8452.21, '26', 'No', 'Automatic sewing units', 'Free'],
    [8452.29, '29', 'No', 'Other industrial sewing machines', 'Free'],
    [8452.30, '28', 'No', 'Sewing machine needles', 'Free'],
    [8452.90, '35', '..', 'Furniture/bases/parts for sewing machines', 'Free'],

    # 8453
    [8453.10, '31', '..', 'Machines for working hides/leather', 'Free'],
    [8453.20, '32', 'No', 'Footwear making or repairing machines', 'Free'],
    [8453.80, '33', '..', 'Other machinery for leather goods', 'Free'],
    [8453.90, '34', '..', 'Parts for 8453 machinery', 'Free'],

    # 8454
    [8454.10, '01', 'No', 'Converters (metallurgy)', '5%'],
    [8454.20, '02', 'No', 'Ingot moulds and ladles', 'Free'],
    [8454.30, '03', 'No', 'Casting machines', 'Free'],
    [8454.90, '04', '..', 'Parts for above', '5%'],
]

# Create the DataFrame
df = pd.DataFrame(data, columns=["Reference Number", "Statistical Code", "Unit", "Goods", "Rate#"])

# Save to Excel
output_file = "tariff_8444_to_8454.xlsx"
df.to_excel(output_file, index=False)

print(f"✅ Excel file '{output_file}' has been created successfully.")
import pandas as pd

# List of rows (each row = one product line)
data = [
    # 8455
    [8455.10, '05', 'No', 'Tube mills', 'Free'],
    [8455.21, '06', 'No', 'Hot or combination hot and cold rolling mills', 'Free'],
    [8455.22, '07', 'No', 'Cold rolling mills', 'Free'],
    [8455.30, '08', 'No', 'Rolls for rolling mills', 'Free'],
    [8455.90, '09', '..', 'Other parts for 8455', 'Free'],

    # 8456
    [8456.11, '11', 'No', 'Laser-operated machines', 'Free'],
    [8456.12, '12', 'No', 'Other photon/light beam operated', 'Free'],
    [8456.20, '16', 'No', 'Ultrasonic machines', 'Free'],
    [8456.30, '17', 'No', 'Electro-discharge machines', 'Free'],
    [8456.40, '13', 'No', 'Plasma arc machines', 'Free'],
    [8456.50, '49', 'No', 'Water-jet cutting machines', 'Free'],
    [8456.90, '50', 'No', 'Other', 'Free'],

    # 8457
    [8457.10, '14', 'No', 'Machining centres', 'Free'],
    [8457.20, '15', 'No', 'Unit construction machines (single station)', 'Free'],
    [8457.30, '16', 'No', 'Multi-station transfer machines', 'Free'],

    # 8458
    [8458.11, '17', 'No', 'Horizontal lathes - NC', 'Free'],
    [8458.19, '18', 'No', 'Horizontal lathes - Other', 'Free'],
    [8458.91, '19', 'No', 'Other lathes - NC', 'Free'],
    [8458.99, '20', 'No', 'Other lathes - Other', 'Free'],

    # 8459
    [8459.10, '21', 'No', 'Way-type unit head machines', 'Free'],
    [8459.21, '22', 'No', 'NC drilling machines', 'Free'],
    [8459.29, '23', 'No', 'Power operated drilling machines', 'Free'],
    [8459.29, '24', 'No', 'Other drilling machines', '5%'],
    [8459.31, '25', 'No', 'NC boring-milling machines', 'Free'],
    [8459.39, '26', 'No', 'Other boring-milling machines', 'Free'],
    [8459.41, '30', 'No', 'NC boring machines', 'Free'],
    [8459.49, '34', 'No', 'Other boring machines', 'Free'],
    [8459.51, '28', 'No', 'NC knee-type milling machines', 'Free'],
    [8459.59, '29', 'No', 'Other knee-type milling machines', 'Free'],
    [8459.61, '31', 'No', 'Other NC milling machines', 'Free'],
    [8459.69, '32', 'No', 'Other milling machines', 'Free'],
    [8459.70, '07', 'No', 'Other threading/tapping machines', 'Free'],

    # 8460
    [8460.12, '01', 'No', 'Flat-surface grinding machines - NC', 'Free'],
    [8460.19, '30', 'No', 'Flat-surface grinding machines - Other', 'Free'],
    [8460.22, '34', 'No', 'Centreless grinding - NC', 'Free'],
    [8460.23, '35', 'No', 'Other cylindrical grinding - NC', 'Free'],
    [8460.24, '36', 'No', 'Other grinding - NC', 'Free'],
    [8460.29, '37', 'No', 'Other grinding machines', 'Free'],
    [8460.31, '12', 'No', 'Sharpening machines - NC', 'Free'],
    [8460.39, '13', 'No', 'Sharpening - Power operated', 'Free'],
    [8460.39, '14', 'No', 'Sharpening - Other', '5%'],
    [8460.40, '15', 'No', 'Honing/lapping - Power operated', 'Free'],
    [8460.40, '16', 'No', 'Honing/lapping - Other', '5%'],
    [8460.90, '38', 'No', 'Other', 'Free'],

    # 8461
    [8461.20, '20', 'No', 'Shaping or slotting machines', 'Free'],
    [8461.30, '21', 'No', 'Broaching machines', 'Free'],
    [8461.40, '22', 'No', 'Gear cutting/grinding/finishing machines', 'Free'],
    [8461.50, '23', 'No', 'Sawing or cutting-off machines', 'Free'],
    [8461.90, '19', 'No', 'Other', 'Free'],

    # 8462
    [8462.11, '01', 'No', 'Closed die forging - Power operated', 'Free'],
    [8462.11, '02', 'No', 'Closed die forging - Other', 'Free'],
    [8462.19, '03', 'No', 'Other hot forming - Power operated', 'Free'],
    [8462.19, '04', 'No', 'Other hot forming - Other', 'Free'],
    [8462.22, '05', 'No', 'Profile forming - NC or power', 'Free'],
    [8462.22, '06', 'No', 'Profile forming - Other', '5%'],
    [8462.23, '07', 'No', 'NC press brakes', 'Free'],
    [8462.24, '08', 'No', 'NC panel benders', 'Free'],
    [8462.25, '09', 'No', 'NC roll forming machines', 'Free'],
    [8462.26, '10', 'No', 'Other NC bending/flattening machines', 'Free'],
    [8462.29, '19', 'No', 'Other - Power operated', 'Free'],
    [8462.29, '20', 'No', 'Other - Other', '5%'],
    [8462.32, '31', 'No', 'NC slitting/cut-to-length lines', 'Free'],
    [8462.32, '32', 'No', 'Other slitting/cut-to-length', 'Free'],
    [8462.33, '33', 'No', 'NC shearing machines', 'Free'],
    [8462.39, '38', 'No', 'Other shearing - Power operated', 'Free'],
    [8462.39, '39', 'No', 'Other shearing - Other', 'Free'],
    [8462.42, '41', 'No', 'NC punching/notching/nibbling', 'Free'],
    [8462.49, '42', 'No', 'Other - Power operated', 'Free'],
    [8462.49, '43', 'No', 'Nibbling machines', 'Free'],
    [8462.49, '49', 'No', 'Other - Other', '5%'],
    [8462.51, '51', 'No', 'NC tube/hollow bar working', 'Free'],
    [8462.59, '58', 'No', 'Other tube/bar - Power operated', 'Free'],
    [8462.59, '59', 'No', 'Other tube/bar - Other', '5%'],
    [8462.61, '61', 'No', 'Hydraulic presses - NC/power', 'Free'],
    [8462.61, '62', 'No', 'Hydraulic presses - Other', '5%'],
    [8462.62, '63', 'No', 'Mechanical presses - NC/power', 'Free'],
    [8462.62, '64', 'No', 'Mechanical presses - Other', '5%'],
    [8462.63, '65', 'No', 'Servo-presses - NC/power', 'Free'],
    [8462.63, '66', 'No', 'Servo-presses - Other', 'Free'],
    [8462.69, '67', 'No', 'Other - NC/power', 'Free'],
    [8462.69, '68', 'No', 'Other - Other', '5%'],
    [8462.90, '90', 'No', 'Other - NC/power', 'Free'],
    [8462.90, '91', 'No', 'Other - Other', '5%'],

    # 8463
    [8463.10, '08', 'No', 'Draw-benches for metal', 'Free'],
    [8463.20, '09', 'No', 'Thread rolling machines', 'Free'],
    [8463.30, '10', 'No', 'Machines for working wire', 'Free'],
    [8463.90, '12', 'No', 'Other machine-tools for metal/cermets', 'Free'],

    # 8464
    [8464.10, '10', '..', 'Sawing machines for mineral materials', '5%'],
    [8464.20, '20', '..', 'Grinding or polishing machines for stone/glass', 'Free'],
    [8464.90, '90', '..', 'Other stone/glass working machines', '5%']
]

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Reference Number", "Statistical Code", "Unit", "Goods", "Rate#"])

# Export to Excel
file_name = "tariff_8454_to_8464.xlsx"
df.to_excel(file_name, index=False)

print(f"✅ Excel file '{file_name}' created successfully.")
import pandas as pd

# Sample data dictionary simulating rows from HS codes 8465 to 8474
data = {
    "Reference Number": [
        8465, 8465, 8465, 8466, 8466, 8466, 8467, 8467, 8467, 8468, 8468, 8468,
        8470, 8470, 8471, 8471, 8472, 8472, 8473, 8473, 8474, 8474
    ],
    "Statistical Code": [
        "15", "22", "28", "40", "41", "42", "12", "21", "22", "16", "17", "18",
        "01", "81", "30", "70", "01", "81", "64", "46", "22", "25"
    ],
    "Unit": [
        "No", "No", "No", "No", "No", "No", "No", "No", "No", "..", "..", "..",
        "No", "..", "No", "No", "No", "..", "..", "..", "No", "No"
    ],
    "Goods": [
        "Machines which can carry out different types of machining operations",
        "Machining centres - bending; assembling; drilling, etc.",
        "Machining centres - sawing; planing; milling, etc.",
        "Tool holders and self-opening dieheads",
        "Work holders",
        "Dividing heads and other special attachments",
        "Rotary type pneumatic tools",
        "Rotary hammer drills <=13mm",
        "Rotary hammer drills >13mm",
        "Hand-held blow pipes",
        "Other gas-operated machinery",
        "Other machinery and apparatus",
        "Duplicating machines",
        "Mail inserting/sealing/cancelling machines",
        "Other units of automatic data processing machines",
        "Storage units - DVD drives",
        "Duplicating machines",
        "Stapling machines",
        "Parts of electronic calculating machines",
        "Parts and accessories for machines of 8472",
        "Sorting, screening, separating machines",
        "Mixing machines - bitumen"
    ],
    "Rate#": [
        "Free", "Free", "5%", "Free", "Free", "Free", "Free", "Free", "Free", "Free",
        "Free", "5%", "Free", "Free", "Free", "Free", "Free", "5%", "Free", "Free", "5%", "Free"
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to Excel
excel_path = "/mnt/data/hs_codes_8465_to_8474.xlsx"
df.to_excel(excel_path, index=False)

excel_path
import pandas as pd

# Sample data for HS codes 8475 to 8484 (structured from the text provided)
data = [
    {"Reference Number": "8475.10.00", "Statistical Code": 29, "Unit": "No", "Goods": "Machines for assembling electric or electronic lamps, tubes or valves or flash-bulbs, in glass envelopes", "Rate#": "Free"},
    {"Reference Number": "8475.21.00", "Statistical Code": 52, "Unit": "No", "Goods": "Machines for making optical fibres and preforms thereof", "Rate#": "Free"},
    {"Reference Number": "8476.21.00", "Statistical Code": 29, "Unit": "No", "Goods": "Automatic beverage-vending machines incorporating heating or refrigerating devices", "Rate#": "Free"},
    {"Reference Number": "8477.10.00", "Statistical Code": 50, "Unit": "No", "Goods": "Injection-moulding machines", "Rate#": "Free"},
    {"Reference Number": "8478.10.00", "Statistical Code": 12, "Unit": "No", "Goods": "Machinery for preparing or making up tobacco", "Rate#": "Free"},
    {"Reference Number": "8479.10.00", "Statistical Code": 14, "Unit": "No", "Goods": "Machinery for public works, building or the like", "Rate#": "5%"},
    {"Reference Number": "8480.10.00", "Statistical Code": 1, "Unit": "..", "Goods": "Moulding boxes for metal foundry", "Rate#": "Free"},
    {"Reference Number": "8481.10.00", "Statistical Code": 10, "Unit": "No", "Goods": "Pressure-reducing valves", "Rate#": "5%"},
    {"Reference Number": "8482.10.10", "Statistical Code": 47, "Unit": "No", "Goods": "Ball bearings: Of a kind used as components in passenger motor vehicles", "Rate#": "5%"},
    {"Reference Number": "8483.10.10", "Statistical Code": 46, "Unit": "No", "Goods": "Transmission shafts for outboard motors", "Rate#": "Free"},
    {"Reference Number": "8484.10.10", "Statistical Code": 21, "Unit": "No", "Goods": "Gaskets of a kind used as components in passenger motor vehicles", "Rate#": "5%"},
]

# Create a DataFrame
df = pd.DataFrame(data)

# Save to Excel file
excel_path = "/mnt/data/HS_Codes_8475_to_8484.xlsx"
df.to_excel(excel_path, index=False)

excel_path
import pandas as pd

# Data for HS codes 8484 to 8487
data = [
    # 8484
    ['8484.10.10', '21', 'No', 'Gaskets of metal sheeting for passenger motor vehicles', '5%', ''],
    ['8484.10.90', '22', 'No', 'Other gaskets and similar joints', '5% DCS:4% DCT:5%', 'View TCOs for 8484.10.90'],
    ['8484.20.00', '20', '..', 'Mechanical seals', '5%', 'View TCOs for 8484.20.00'],
    ['8484.90.10', '11', '..', 'Parts for 8484.10.10', '5%', ''],
    ['8484.90.90', '24', '..', 'Other parts', '5% DCS:4% DCT:5%', 'View TCOs for 8484.90.90'],
    
    # 8485
    ['8485.10.00', '01', 'No', 'Additive mfg. machines by metal deposit', 'Free', ''],
    ['8485.20.00', '02', 'No', 'Additive mfg. machines by plastics/rubber deposit', 'Free', 'View TCOs for 8485.20.00'],
    ['8485.30.10', '03', 'No', 'Additive mfg. by glass deposit', '5% DCS:4% DCT:5%', ''],
    ['8485.30.90', '04', 'No', 'Other additive mfg. by plaster/cement/ceramics', 'Free', ''],
    ['8485.80.10', '05', 'No', 'Additive mfg. by paper pulp or paperboard', 'Free', ''],
    ['8485.80.90', '06', 'No', 'Other additive mfg. (NSA)', '5%', 'View TCOs for 8485.80.90'],
    ['8485.90.10', '07', '..', 'Parts for 8485.10.00', 'Free', ''],
    ['8485.90.20', '08', '..', 'Parts for 8485.20.00 or 8485.30.10', '5% DCS:4% DCT:5%', 'View TCOs for 8485.90.20'],
    ['8485.90.90', '90', '..', 'Other parts', '5%', ''],
    
    # 8486 (simplified subset for clarity)
    ['8486.10.10', '10', '..', 'Machines for growing/pulling semiconductor boules', 'Free', ''],
    ['8486.20.10', '40', '..', 'Machines for semi devices/ICs (etching, deposition etc.)', 'Free', ''],
    ['8486.30.10', '52', '..', 'Machines for flat panel displays', 'Free', ''],
    ['8486.40.10', '54', '..', 'Machines specified in Note 11(C)', 'Free', ''],
    ['8486.90.10', '17', '..', 'Parts of 8486.10.10, 8486.20.10 etc.', 'Free', ''],
    
    # 8487
    ['8487.10.00', '10', 'No', "Ships' or boats' propellers and blades", '5% DCS:4% DCT:5%', 'View TCOs for 8487.10.00'],
    ['8487.90.00', '91', '..', 'Other machinery parts (non-electrical)', '5%', 'View TCOs for 8487.90.00']
]

# Define column names
columns = ['Reference Number', 'Statistical Code', 'Unit', 'Goods', 'Rate', 'Tariff Concession Orders']

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Export to Excel
df.to_excel('hs8484_to_8487.xlsx', index=False)

print("Excel file 'hs8484_to_8487.xlsx' has been created successfully.")
import pandas as pd

# Structured data for HS codes 8501 to 8505
data = [
    # 8501 - Electric motors and generators
    ['8501.10.00', '32', 'No', 'Motors of an output not exceeding 37.5 W', '5%', 'View TCOs for 8501.10.00'],
    ['8501.20.00', '03', 'No', 'Universal AC/DC motors of an output exceeding 37.5 W', '5%', 'View TCOs for 8501.20.00'],
    ['8501.31.00', '33', 'No', 'DC motor/generator ≤750W', '5%', 'View TCOs for 8501.31.00'],
    ['8501.32.00', '34', 'No', 'DC motor/generator >750W ≤75kW', '5%', 'View TCOs for 8501.32.00'],
    ['8501.33.00', '35', 'No', 'DC motor/generator >75kW ≤375kW', '5%', 'View TCOs for 8501.33.00'],
    ['8501.34.00', '36', 'No', 'DC motor/generator >375kW', '5%', 'View TCOs for 8501.34.00'],
    ['8501.51.00', '22', 'No', 'Multi-phase AC motor ≤750W', '5%', 'View TCOs for 8501.51.00'],
    ['8501.52.00', '15', 'No', 'Multi-phase AC motor >750W ≤75kW', '5%', 'View TCOs for 8501.52.00'],
    ['8501.53.00', '19', 'No', 'Multi-phase AC motor >75kW', '5%', 'View TCOs for 8501.53.00'],
    ['8501.61.00', '37', 'No', 'AC generator ≤75kVA', '5% DCS:4% DCT:5%', 'View TCOs for 8501.61.00'],
    ['8501.62.00', '39', 'No', 'AC generator >75kVA ≤375kVA', 'Free', 'View TCOs for 8501.62.00'],
    ['8501.63.00', '42', 'No', 'AC generator >375kVA ≤750kVA', 'Free', ''],
    ['8501.64.00', '43', 'No', 'AC generator >750kVA', 'Free', ''],
    ['8501.71.00', '51', 'No', 'Photovoltaic DC generator ≤50W', '5%', ''],
    ['8501.72.00', '52', 'No', 'Photovoltaic DC generator >50W', 'Free', ''],
    ['8501.80.10', '53', 'No', 'Photovoltaic AC generator ≤375kVA', '5% DCS:4% DCT:5%', 'View TCOs for 8501.80.10'],
    ['8501.80.90', '54', 'No', 'Other photovoltaic AC generators', 'Free', ''],

    # 8502 - Electric generating sets
    ['8502.11.00', '36', 'No', 'Diesel genset ≤75kVA', '5% DCS:4% DCT:5%', 'View TCOs for 8502.11.00'],
    ['8502.12.00', '03', 'No', 'Diesel genset >75kVA ≤375kVA', '5% DCS:4% DCT:5%', 'View TCOs for 8502.12.00'],
    ['8502.13.10', '04', 'No', 'AC genset >500kVA', 'Free', ''],
    ['8502.13.90', '05', 'No', 'Other diesel gensets >375kVA', 'Free', 'View TCOs for 8502.13.90'],
    ['8502.20.00', '38', 'No', 'Spark-ignition genset', 'Free', 'View TCOs for 8502.20.00'],
    ['8502.31.10', '31', 'No', 'Wind-powered AC genset >500kVA', 'Free', ''],
    ['8502.31.90', '32', 'No', 'Other wind-powered gensets', 'Free', 'View TCOs for 8502.31.90'],
    ['8502.39.10', '33', 'No', 'Other AC gensets >500kVA', 'Free', ''],
    ['8502.39.90', '34', 'No', 'Other gensets', '5% DCS:4% DCT:5%', ''],
    ['8502.40.00', '10', 'No', 'Electric rotary converters', '5%', ''],

    # 8503 - Parts for 8501/8502
    ['8503.00.00', '38', '..', 'Parts suitable for use with 8501 or 8502', '5%', 'View TCOs for 8503.00.00'],

    # 8504 - Transformers and inductors
    ['8504.10.00', '13', 'No', 'Ballasts for discharge lamps or tubes', '5%', 'View TCOs for 8504.10.00'],
    ['8504.21.00', '39', 'No', 'Liquid dielectric transformer ≤650kVA', '5%', 'View TCOs for 8504.21.00'],
    ['8504.22.00', '40', 'No', 'Liquid dielectric transformer >650kVA ≤10000kVA', '5%', 'View TCOs for 8504.22.00'],
    ['8504.23.00', '41', 'No', 'Liquid dielectric transformer >10000kVA', '5%', 'View TCOs for 8504.23.00'],
    ['8504.31.00', '27', 'No', 'Transformer ≤1kVA for AV/audio use', '5%', 'View TCOs for 8504.31.00'],
    ['8504.32.00', '29', 'No', 'Transformer >1kVA ≤16kVA', '5%', 'View TCOs for 8504.32.00'],
    ['8504.33.00', '30', 'No', 'Transformer >16kVA ≤500kVA', '5%', 'View TCOs for 8504.33.00'],
    ['8504.34.00', '91', 'No', 'Transformer >500kVA', '5%', 'View TCOs for 8504.34.00'],
    ['8504.40.30', '59', 'No', 'Static converters (special cases)', 'Free', ''],
    ['8504.50.10', '81', 'No', 'Inductors for telecom or computers', 'Free', ''],
    ['8504.50.90', '84', 'No', 'Other inductors', '5% (Free from 1 July 2019)', ''],
    ['8504.90.30', '30', '..', 'Parts of 8504.40.30', 'Free', ''],
    ['8504.90.90', '92', '..', 'Other parts', '5% (Free from 1 July 2019)', ''],

    # 8505 - Magnets and related devices
    ['8505.11.00', '13', '..', 'Permanent magnets of metal', '5%', 'View TCOs for 8505.11.00'],
    ['8505.19.00', '14', '..', 'Other permanent magnets', '5%', 'View TCOs for 8505.19.00'],
    ['8505.20.00', '15', '..', 'Electro-magnetic couplings, clutches, brakes', 'Free', ''],
    ['8505.90.00', '18', '..', 'Other electro-magnetic devices, including parts', 'Free', '']
]

# Column headers
columns = ['Reference Number', 'Statistical Code', 'Unit', 'Goods', 'Rate', 'Tariff Concession Orders']

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Export to Excel
df.to_excel('chapter85_8501_8505.xlsx', index=False)

print("Excel file 'chapter85_8501_8505.xlsx' has been created successfully.")

import pandas as pd

# Chapter 8515–8517 data
data = [
    # 8515
    [8515, '8515.11.00', '11', 'No', 'Soldering irons and guns', '5%'],
    [8515, '8515.19.10', '40', 'No', 'Electric or laser operated brazing or soldering machines, CNC', 'Free'],
    [8515, '8515.19.20', '41', 'No', 'Wave soldering machines for PCAs', 'Free'],
    [8515, '8515.19.90', '45', 'No', 'Other brazing or soldering machines', '5%'],
    [8515, '8515.21.10', '35', 'No', 'Resistance welding, CNC', 'Free'],
    [8515, '8515.21.90', '44', 'No', 'Resistance welding, other', '5%'],
    [8515, '8515.29.00', '43', 'No', 'Other resistance welding machines', '5%'],
    [8515, '8515.31.10', '42', 'No', 'Arc welding, CNC', 'Free'],
    [8515, '8515.31.90', '18', 'No', 'Arc welding, other', 'Free'],
    [8515, '8515.39.00', '19', 'No', 'Other arc welding machines', 'Free'],
    [8515, '8515.80.10', '20', 'No', 'Other welding machines, CNC', 'Free'],
    [8515, '8515.80.90', '90', 'No', 'Other welding machines', '5%'],
    [8515, '8515.90.10', '50', '..', 'Parts of 8515.19.20', 'Free'],
    [8515, '8515.90.90', '51', '..', 'Other parts', '5%'],

    # 8516
    [8516, '8516.10.00', '23', 'No', 'Electric water heaters & immersion heaters', '5%'],
    [8516, '8516.21.00', '24', 'No', 'Storage heating radiators', '5%'],
    [8516, '8516.29.00', '90', 'No', 'Other space/soil heating apparatus', '5%'],
    [8516, '8516.31.00', '26', 'No', 'Hair dryers', '5%'],
    [8516, '8516.32.00', '57', 'No', 'Other hair dressing apparatus', 'Free'],
    [8516, '8516.33.00', '28', 'No', 'Hand-drying apparatus', '5%'],
    [8516, '8516.40.00', '29', 'No', 'Electric smoothing irons', 'Free'],
    [8516, '8516.50.00', '39', 'No', 'Microwave ovens ≤ 23.9 L', 'Free'],
    [8516, '8516.50.00', '40', 'No', 'Microwave ovens 23.9–34.9 L', 'Free'],
    [8516, '8516.50.00', '41', 'No', 'Microwave ovens > 34.9 L', 'Free'],
    [8516, '8516.50.00', '14', 'No', 'Microwave ovens without digital display', 'Free'],
    [8516, '8516.60.00', '50', 'No', 'Cooking tops (non-portable)', '5%'],
    [8516, '8516.60.00', '51', 'No', 'Ovens (non-portable)', '5%'],
    [8516, '8516.60.00', '52', 'No', 'Ranges (non-portable)', '5%'],
    [8516, '8516.60.00', '53', 'No', 'Other cooking appliances (non-portable)', '5%'],
    [8516, '8516.71.00', '33', 'No', 'Coffee or tea makers – Dripolators', 'Free'],
    [8516, '8516.71.00', '34', 'No', 'Coffee or tea makers – Other', 'Free'],
    [8516, '8516.72.00', '05', 'No', 'Toasters', 'Free'],
    [8516, '8516.79.00', '35', 'No', 'Kettles', '5%'],
    [8516, '8516.79.00', '36', 'No', 'Deep fryers', '5%'],
    [8516, '8516.79.00', '37', 'No', 'Steam/rice cookers', '5%'],
    [8516, '8516.79.00', '38', 'No', 'Other appliances', '5%'],
    [8516, '8516.80.00', '42', 'No', 'Electric heating resistors', '5%'],
    [8516, '8516.90.00', '01', '..', 'Parts', '5%'],

    # 8517
    [8517, '8517.11.00', '81', 'No', 'Cordless phone sets with answering machine', 'Free'],
    [8517, '8517.11.00', '17', 'No', 'Other cordless phone sets', 'Free'],
    [8517, '8517.13.00', '01', 'No', 'Smartphones', 'Free'],
    [8517, '8517.14.00', '02', 'No', 'Other mobile phones', 'Free'],
    [8517, '8517.18.00', '20', 'No', 'Other telephone sets', 'Free'],
    [8517, '8517.61.00', '49', '..', 'Base stations', 'Free'],
    [8517, '8517.62.00', '50', 'No', 'Teleprinters', 'Free'],
    [8517, '8517.62.00', '51', 'No', 'Modems ≥ 300bps', 'Free'],
    [8517, '8517.62.00', '52', 'No', 'Multiplexors ≤ 2.5 Mbps', 'Free'],
    [8517, '8517.62.00', '60', 'No', 'Small business telephone switchboards', 'Free'],
    [8517, '8517.62.00', '61', '..', 'Other switching apparatus', 'Free'],
    [8517, '8517.62.00', '81', '..', 'Transmitters only (radio-telephony)', 'Free'],
    [8517, '8517.62.00', '82', '..', 'Transmitters with receivers (radio-telephony)', 'Free'],
    [8517, '8517.62.00', '90', '..', 'Other transmission equipment', 'Free'],
    [8517, '8517.69.10', '10', '..', 'Receivers for radio-telephony (non-paging)', 'Free'],
    [8517, '8517.69.90', '91', '..', 'Paging receivers', 'Free'],
    [8517, '8517.69.90', '95', '..', 'Other receivers', 'Free'],
    [8517, '8517.71.00', '10', '..', 'Aerials and aerial reflectors', 'Free'],
    [8517, '8517.79.00', '90', '..', 'Other parts', 'Free'],
]

# Define columns
columns = ['Chapter', 'Reference Number', 'Statistical Code', 'Unit', 'Goods', 'Rate']

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save to Excel
filename = 'Chapters_8515_to_8517.xlsx'
df.to_excel(filename, index=False)

print(f"✅ Excel file '{filename}' created successfully.")
import pandas as pd

# Chapter 8518–8523 data
data = [
    # 8518
    [8518, '8518.10.10', '30', 'No', 'Microphones (special spec & cordless)', 'Free'],
    [8518, '8518.10.90', '89', 'No', 'Wired microphones', 'Free'],
    [8518, '8518.10.90', '90', 'No', 'Wireless microphones', 'Free'],
    [8518, '8518.10.90', '91', 'No', 'Other microphones', 'Free'],
    [8518, '8518.21.00', '46', 'No', 'Single loudspeakers for motor vehicles', 'Free'],
    [8518, '8518.21.00', '73', 'No', 'Single loudspeakers for Hi-Fi', 'Free'],
    [8518, '8518.21.00', '48', 'No', 'Other single loudspeakers', 'Free'],
    [8518, '8518.22.00', '77', 'No', 'Multiple loudspeakers for Hi-Fi', 'Free'],
    [8518, '8518.22.00', '78', 'No', 'Multiple loudspeakers for PA systems', 'Free'],
    [8518, '8518.22.00', '79', 'No', 'Multiple loudspeakers for instruments', 'Free'],
    [8518, '8518.22.00', '83', 'No', 'Other multiple loudspeakers', 'Free'],
    [8518, '8518.29.10', '92', 'No', 'Loudspeakers (bare, telecom use)', 'Free'],
    [8518, '8518.29.90', '93', 'No', 'Packaged in pairs for vehicles', 'Free'],
    [8518, '8518.29.90', '94', 'No', 'For domestic Hi-Fi', 'Free'],
    [8518, '8518.29.90', '98', 'No', 'Other loudspeakers', 'Free'],
    [8518, '8518.30.10', '61', 'No', 'Radio-transmission headsets', 'Free'],
    [8518, '8518.30.10', '63', 'No', 'Other telephone headsets', 'Free'],
    [8518, '8518.30.90', '10', '..', 'Other headphones/sets', 'Free'],
    [8518, '8518.40.10', '03', 'No', 'Repeaters for telephony', 'Free'],
    [8518, '8518.40.90', '04', 'No', 'Amplifiers for motor vehicles', 'Free'],
    [8518, '8518.40.90', '05', 'No', 'Other amplifiers', 'Free'],
    [8518, '8518.50.00', '85', 'No', 'Amplifier sets for guitars', 'Free'],
    [8518, '8518.50.00', '86', 'No', 'Other amplifier sets', 'Free'],
    [8518, '8518.90.00', '35', '..', 'Parts', 'Free'],

    # 8519
    [8519, '8519.20.10', '05', 'No', 'Coin/disc operated record-players', 'Free'],
    [8519, '8519.20.90', '90', 'No', 'Other paid sound apparatus', 'Free'],
    [8519, '8519.30.00', '13', 'No', 'Turntables', 'Free'],
    [8519, '8519.81.10', '10', 'No', 'Transcribing machines', 'Free'],
    [8519, '8519.81.20', '16', 'No', 'Cassette-type reproducers', 'Free'],
    [8519, '8519.81.20', '17', 'No', 'Single disc CD players', 'Free'],
    [8519, '8519.81.20', '18', 'No', 'Multi disc CD players', 'Free'],
    [8519, '8519.81.20', '90', 'No', 'Other reproducers', 'Free'],
    [8519, '8519.81.30', '33', 'No', 'Dictating machines (power/cassette)', 'Free'],
    [8519, '8519.81.41', '41', 'No', 'Cassette-type tape recorders', 'Free'],
    [8519, '8519.81.49', '46', 'No', 'Other magnetic tape recorders', 'Free'],
    [8519, '8519.81.90', '51', 'No', 'Other sound recorders', 'Free'],
    [8519, '8519.89.10', '10', 'No', 'Transcribing machines', 'Free'],
    [8519, '8519.89.20', '22', 'No', 'Record players', 'Free'],
    [8519, '8519.89.30', '90', 'No', 'Other reproducers (non-recording)', 'Free'],
    [8519, '8519.89.90', '95', 'No', 'Other sound apparatus', 'Free'],

    # 8521
    [8521, '8521.10.00', '78', 'No', 'Magnetic tape-type video recorder', 'Free'],
    [8521, '8521.90.00', '19', 'No', 'Other video recorders', 'Free'],

    # 8522
    [8522, '8522.10.00', '20', '..', 'Pick-up cartridges', 'Free'],
    [8522, '8522.90.00', '24', '..', 'Other parts & accessories', 'Free'],

    # 8523
    [8523, '8523.21.00', '10', 'No', 'Magnetic stripe cards', 'Free'],
    [8523, '8523.29.00', '81', 'No', 'Unrecorded mag tapes ≤4mm', 'Free'],
    [8523, '8523.29.00', '10', 'No', 'Unrecorded mag tapes 4–6.5mm', 'Free'],
    [8523, '8523.29.00', '20', 'No', 'Unrecorded mag tapes 6.5–12.7mm (Computer)', 'Free'],
    [8523, '8523.29.00', '82', 'No', 'Unrecorded mag tapes (Video)', 'Free'],
    [8523, '8523.29.00', '83', 'No', 'Unrecorded mag tapes (Other)', 'Free'],
    [8523, '8523.29.00', '84', 'No', 'Unrecorded mag tapes >12.7mm', 'Free'],
    [8523, '8523.29.00', '85', 'No', 'Other unrecorded magnetic media', 'Free'],
    [8523, '8523.29.00', '86', 'No', 'Recorded mag tapes (not sound/image)', 'Free'],
    [8523, '8523.29.00', '87', 'No', 'Other recorded magnetic tapes', 'Free'],
    [8523, '8523.29.00', '88', 'No', 'Other recorded magnetic media', 'Free'],
    [8523, '8523.41.00', '27', 'No', 'Unrecorded optical media', 'Free'],
    [8523, '8523.49.00', '28', 'No', 'Other optical media', 'Free'],
    [8523, '8523.51.00', '50', 'No', 'Solid-state non-volatile storage', 'Free'],
    [8523, '8523.52.00', '10', 'No', '"Smart cards"', 'Free'],
    [8523, '8523.59.00', '25', 'No', 'Proximity cards and tags', 'Free'],
    [8523, '8523.59.00', '95', 'No', 'Other semiconductor media', 'Free'],
    [8523, '8523.80.00', '31', 'No', 'Other media for sound or data', 'Free'],
]

# Column names
columns = ['Chapter', 'Reference Number', 'Statistical Code', 'Unit', 'Goods', 'Rate']

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Write to Excel
filename = 'Chapters_8518_to_8523.xlsx'
df.to_excel(filename, index=False)

print(f"✅ Excel file '{filename}' created successfully.")
import pandas as pd

# Chapter 8524–8528 data
data = [
    # 8524
    [8524, '8524.11.00', '01', 'No', 'Flat panel display - liquid crystals (no drivers)', 'Free'],
    [8524, '8524.12.00', '02', 'No', 'Flat panel display - OLED (no drivers)', 'Free'],
    [8524, '8524.19.00', '03', 'No', 'Flat panel display - Other (no drivers)', 'Free'],
    [8524, '8524.91.00', '04', 'No', 'Flat panel display - liquid crystals (with control)', 'Free'],
    [8524, '8524.92.00', '05', 'No', 'Flat panel display - OLED (with control)', 'Free'],
    [8524, '8524.99.00', '06', 'No', 'Flat panel display - Other (with control)', 'Free'],

    # 8525
    [8525, '8525.50.00', '10', '..', 'Transmission apparatus', 'Free'],
    [8525, '8525.60.00', '60', '..', 'Transmission apparatus with reception', 'Free'],
    [8525, '8525.81.00', '11', 'No', 'High-speed television/digital/video cameras', 'Free'],
    [8525, '8525.82.00', '12', 'No', 'Radiation-hardened/tolerant digital cameras', 'Free'],
    [8525, '8525.83.00', '13', 'No', 'Night vision video cameras', 'Free'],
    [8525, '8525.89.00', '20', 'No', 'Web cameras', 'Free'],
    [8525, '8525.89.00', '30', 'No', 'Security cameras', 'Free'],
    [8525, '8525.89.00', '90', 'No', 'Other video/digital cameras', 'Free'],

    # 8526
    [8526, '8526.10.00', '29', '..', 'Radar apparatus', 'Free'],
    [8526, '8526.91.00', '30', '..', 'Radio navigational aid apparatus', 'Free'],
    [8526, '8526.92.00', '90', '..', 'Radio remote control apparatus', 'Free'],

    # 8527
    [8527, '8527.12.00', '54', 'No', 'Pocket-size radio cassette-players', 'Free'],
    [8527, '8527.13.00', '55', 'No', 'Radio with sound recording apparatus', 'Free'],
    [8527, '8527.19.00', '03', 'No', 'Other radio-broadcast receivers (portable)', 'Free'],
    [8527, '8527.21.10', '74', 'No', 'Vehicle radio with digital radio decoding', 'Free'],
    [8527, '8527.21.90', '75', 'No', 'Other vehicle radio receivers', 'Free'],
    [8527, '8527.29.00', '05', 'No', 'Other vehicle radios (not combined)', 'Free'],
    [8527, '8527.91.00', '10', 'No', 'Other radios with recording apparatus', 'Free'],
    [8527, '8527.92.00', '20', 'No', 'Radio with clock (no recording)', 'Free'],
    [8527, '8527.99.00', '90', 'No', 'Other radio receivers', 'Free'],

    # 8528
    [8528, '8528.42.00', '11', 'No', 'CRT monitor for data processing (8471)', 'Free'],
    [8528, '8528.49.00', '15', 'No', 'Other CRT monitors', 'Free'],
    [8528, '8528.52.00', '23', 'No', 'Flat screen monitor ≤5kg', 'Free'],
    [8528, '8528.52.00', '24', 'No', 'Flat screen monitor >5kg and ≤10kg', 'Free'],
    [8528, '8528.52.00', '25', 'No', 'Flat screen monitor >10kg', 'Free'],
    [8528, '8528.52.00', '34', 'No', 'Other flat screen monitors', 'Free'],
    [8528, '8528.59.00', '61', 'No', 'Other monitors - colour', 'Free'],
    [8528, '8528.59.00', '67', 'No', 'Other monitors - B/W or monochrome', 'Free'],
    [8528, '8528.62.00', '68', 'No', 'Projectors for data processing (8471)', 'Free'],
    [8528, '8528.69.00', '70', 'No', 'Other projectors', 'Free'],
    [8528, '8528.71.10', '10', 'No', 'TV reception - colour (no display)', 'Free'],
    [8528, '8528.71.20', '10', 'No', 'TV reception - monochrome (no display)', 'Free'],
    [8528, '8528.72.00', '01', 'No', 'TV receiver (colour) <3kg', 'Free'],
    [8528, '8528.72.00', '02', 'No', 'TV receiver (colour) 3-5kg', 'Free'],
    [8528, '8528.72.00', '03', 'No', 'TV receiver (colour) 5-8kg', 'Free'],
    [8528, '8528.72.00', '04', 'No', 'TV receiver (colour) 8-10kg', 'Free'],
    [8528, '8528.72.00', '05', 'No', 'TV receiver (colour) 10-12kg', 'Free'],
    [8528, '8528.72.00', '06', 'No', 'TV receiver (colour) 12-14kg', 'Free'],
    [8528, '8528.72.00', '07', 'No', 'TV receiver (colour) 14-16kg', 'Free'],
    [8528, '8528.72.00', '08', 'No', 'TV receiver (colour) 16-18kg', 'Free'],
    [8528, '8528.72.00', '09', 'No', 'TV receiver (colour) 18-20kg', 'Free'],
    [8528, '8528.72.00', '63', 'No', 'TV receiver (colour) 20-25kg', 'Free'],
    [8528, '8528.72.00', '64', 'No', 'TV receiver (colour) 25-30kg', 'Free'],
    [8528, '8528.72.00', '65', 'No', 'TV receiver (colour) 30-40kg', 'Free'],
    [8528, '8528.72.00', '66', 'No', 'TV receiver (colour) >40kg', 'Free'],
    [8528, '8528.73.00', '35', 'No', 'Other TV receiver - monochrome', 'Free'],
]

# Column names
columns = ['Chapter', 'Reference Number', 'Statistical Code', 'Unit', 'Goods', 'Rate']

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Write to Excel
filename = 'Chapters_8524_to_8528.xlsx'
df.to_excel(filename, index=False)

filename
import pandas as pd

# Define the structured data for chapters 8529–8537
data = [
    [8529, '8529.10.00', '01', '..', 'Aerials and aerial reflectors of all kinds; parts suitable for use therewith', 'Free'],
    [8529, '8529.90.00', '02', '..', 'Other', 'Free'],
    [8530, '8530.10.00', '30', '..', 'Equipment for railways or tramways', '5%'],
    [8530, '8530.80.00', '27', '..', 'Other equipment', 'Free'],
    [8530, '8530.90.00', '81', '..', 'Parts', '5%'],
    [8531, '8531.10.10', '56', '..', 'Burglar alarms', 'Free'],
    [8531, '8531.10.91', '55', '..', 'Other - used as components in passenger motor vehicles', '5%'],
    [8531, '8531.10.99', '53', '..', 'Other', '5%'],
    [8531, '8531.20.00', '32', '..', 'Indicator panels with LCD or LED', 'Free'],
    [8531, '8531.80.00', '33', '..', 'Other apparatus', 'Free'],
    [8531, '8531.90.10', '53', '..', 'Parts for 8531.20.00 or 8531.80.00', 'Free'],
    [8531, '8531.90.90', '54', '..', 'Other parts', '5%'],
    [8532, '8532.10.00', '40', 'No', 'Power capacitors (>=0.5 kvar)', 'Free'],
    [8532, '8532.21.00', '03', 'No', 'Tantalum capacitors', 'Free'],
    [8532, '8532.22.00', '04', 'No', 'Aluminium electrolytic capacitors', 'Free'],
    [8532, '8532.23.00', '11', 'No', 'Ceramic dielectric, single layer', 'Free'],
    [8532, '8532.24.00', '12', 'No', 'Ceramic dielectric, multilayer', 'Free'],
    [8532, '8532.25.00', '13', 'No', 'Dielectric of paper or plastics', 'Free'],
    [8532, '8532.29.00', '14', 'No', 'Other fixed capacitors', 'Free'],
    [8532, '8532.30.00', '55', 'No', 'Variable or adjustable capacitors', 'Free'],
    [8532, '8532.90.00', '56', '..', 'Parts', 'Free'],
    [8533, '8533.10.00', '17', 'No', 'Fixed carbon resistors', 'Free'],
    [8533, '8533.21.00', '18', 'No', 'Other fixed resistors (<=20W)', 'Free'],
    [8533, '8533.29.00', '19', 'No', 'Other fixed resistors', 'Free'],
    [8533, '8533.31.00', '20', 'No', 'Wirewound resistors (<=20W)', 'Free'],
    [8533, '8533.39.00', '21', 'No', 'Wirewound resistors - other', 'Free'],
    [8533, '8533.40.00', '22', 'No', 'Other variable resistors', 'Free'],
    [8533, '8533.90.00', '23', '..', 'Parts', 'Free'],
    [8534, '8534.00.00', '33', 'No', 'Single sided printed circuits', 'Free'],
    [8534, '8534.00.00', '38', 'No', 'Double sided printed circuits', 'Free'],
    [8534, '8534.00.00', '39', 'No', 'Multilayer printed circuits (4 layers)', 'Free'],
    [8534, '8534.00.00', '57', 'No', 'Multilayer printed circuits (6+ layers)', 'Free'],
    [8534, '8534.00.00', '43', 'No', 'Flexible circuits', 'Free'],
    [8534, '8534.00.00', '44', 'No', 'Other printed circuits', 'Free'],
    [8535, '8535.10.00', '25', 'No', 'Fuses >1000V', '5%'],
    [8535, '8535.21.00', '26', 'No', 'Auto circuit breakers <72.5kV', '5%'],
    [8535, '8535.29.00', '27', 'No', 'Other auto circuit breakers', '5%'],
    [8535, '8535.30.00', '28', 'No', 'Isolating and make-break switches', '5%'],
    [8535, '8535.40.10', '29', 'No', 'Lightning arresters for power supply protection', '5%'],
    [8535, '8535.40.90', '30', 'No', 'Other lightning protection', '5%'],
    [8535, '8535.90.00', '58', 'No', 'Other apparatus >1000V', '5%'],
    [8536, '8536.10.00', '70', 'No', 'Fuses <=1000V', '5%'],
    [8536, '8536.20.00', '03', 'No', 'Auto circuit breakers <=1000V', '5%'],
    [8536, '8536.30.00', '04', 'No', 'Other protective apparatus', '5%'],
    [8536, '8536.41.00', '05', 'No', 'Relays <=60V', '5%'],
    [8536, '8536.49.00', '06', 'No', 'Other relays', '5%'],
    [8536, '8536.50.10', '07', 'No', 'Time switches', '5%'],
    [8536, '8536.61.00', '09', '..', 'Lamp-holders', '5%'],
    [8537, '8537.10.10', '18', 'No', 'Programmable controllers <=1000V', 'Free'],
    [8537, '8537.10.90', '19', 'No', 'Other control boards <=1000V', '5%'],
    [8537, '8537.20.10', '20', 'No', 'Programmable controllers >1000V', 'Free'],
    [8537, '8537.20.90', '21', 'No', 'Other control boards >1000V', '5%'],
]

# Create DataFrame
columns = ['Chapter', 'Reference Number', 'Statistical Code', 'Unit', 'Goods', 'Rate']
df = pd.DataFrame(data, columns=columns)

# Export to Excel
file_path = "/mnt/data/Chapters_8529_to_8537.xlsx"
df.to_excel(file_path, index=False)

file_path
import pandas as pd

# Data dictionary for 8537 to 8539
data = {
    "Reference Number": [
        "8537", "8537.10", "8537.10.10", "8537.10.90", "8537.20", "8537.20.10", "8537.20.90",
        "8538", "8538.10", "8538.10.10", "8538.10.90", "8538.90", "8538.90.11", "8538.90.12",
        "8538.90.13", "8538.90.14", "8538.90.15", "8538.90.16", "8538.90.19", "8538.90.90",
        "8539", "8539.10", "8539.10.10", "8539.10.90", "8539.21.00", "8539.22.00", "8539.29.00",
        "8539.31.00", "8539.32.00", "8539.39.10", "8539.39.90", "8539.41.00", "8539.49.00",
        "8539.51.00", "8539.52.00", "8539.90.10", "8539.90.90"
    ],
    "Statistical Code": [
        "", "", "18", "19", "", "20", "21",
        "", "", "22", "23", "", "01", "02",
        "03", "04", "05", "06", "09", "90",
        "", "", "28", "29", "", "", "",
        "", "", "70", "71", "46", "49",
        "01", "", "32", "33"
    ],
    "Unit": [
        "", "", "No", "No", "", "No", "No",
        "", "", "No", "No", "", "No", "No",
        "No", "No", "No", "No", "No", "",
        "", "", "No", "No", "", "No", "No",
        "", "", "No", "No", "No", "No",
        "No", "", "No", "No"
    ],
    "Goods": [
        "BOARDS, PANELS, CONSOLES, DESKS, CABINETS AND OTHER BASES, EQUIPPED WITH TWO OR MORE APPARATUS OF 8535 OR 8536",
        "- For a voltage not exceeding 1 000 V:",
        "--- Programmable controllers",
        "--- Other",
        "- For a voltage exceeding 1 000 V:",
        "--- Programmable controllers",
        "--- Other",
        "PARTS SUITABLE FOR USE SOLELY OR PRINCIPALLY WITH THE APPARATUS OF 8535, 8536 OR 8537:",
        "- Boards, panels, consoles, desks, cabinets and other bases for the goods of 8537, not equipped with their apparatus:",
        "--- For programmable controllers",
        "--- Other",
        "- Other:",
        "--- Of goods of 8536.70.11",
        "--- Of goods of 8536.70.19",
        "--- Of goods of 8536.70.21",
        "--- Of goods of 8536.70.29",
        "--- Of goods of 8536.70.30",
        "--- Of goods of 8536.70.40",
        "--- Other",
        "--- Other",
        "ELECTRIC FILAMENT OR DISCHARGE LAMPS, INCLUDING SEALED BEAM LAMP UNITS AND ULTRA-VIOLET OR INFRA-RED LAMPS; ARC- LAMPS; LIGHT-EMITTING DIODE (LED) LIGHT SOURCES:",
        "- Sealed beam lamp units:",
        "--- For motorcycles",
        "--- Other",
        "- Other filament lamps, excluding ultra-violet or infra-red lamps:",
        "-- Other, of a power not exceeding 200 W and for a voltage exceeding 100 V",
        "-- Other",
        "- Discharge lamps, other than ultra-violet lamps:",
        "-- Mercury or sodium vapour lamps; metal halide lamps",
        "--- Cold-cathode fluorescent lamps (CCFLs) for backlighting of flat panel displays",
        "--- Other",
        "- Ultra-violet or infra-red lamps; arc-lamps:",
        "-- Other",
        "- Light-Emitting Diode (LED) light sources:",
        "-- Light-Emitting Diode (LED) modules",
        "-- Light-Emitting Diode (LED) lamps",
        "--- Of goods of 8539.51.00 or 8539.52.00",
        "--- Other"
    ],
    "Rate#": [
        "", "", "No", "No", "", "No", "No",
        "", "", "No", "5%", "", "5%", "5%",
        "5%", "5%", "Free", "5%", "Free", "",
        "", "", "Free", "5%", "", "5%", "5%",
        "", "", "5%", "5%", "5%", "5%",
        "Free", "", "Free", "5%"
    ],
    "Tariff concession orders": [
        "View TCOs for 8537.10", "View TCOs for 8537.10.10", "Free", "5% CA:Free", "View TCOs for 8537.20", "Free", "5% CA:Free",
        "", "", "Free", "5% CA:Free From 1 July 2018: 3.75% CA: Free From 1 July 2019: Free", "View TCOs for 8538.90",
        "5% CA:Free", "5% CA:Free", "5% CA:Free", "5% CA:Free", "Free", "Free View TCOs for 8538.90.16",
        "5% View TCOs for 8538.90.19", "Free", "", "View TCOs for 8539.10", "Free", "5%",
        "View TCOs for 8539.22", "5%", "DCS:4% DCT:5% View TCOs for 8539.29.00", "View TCOs for 8539.31.00", "View TCOs for 8539.32",
        "5% DCS:4% DCT:5% View TCOs for 8539.39.10 From 1 July 2018: 2.5% From 1 July 2019: Free",
        "DCS:4% DCT:5% View TCOs for 8539.39.90", "DCS:4% DCT:5% View TCOs for 8539.41.00", "DCS:4% DCT:5% View TCOs for 8539.49.00",
        "", "Free", "Free", "5% DCS:4% DCT:5%"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
excel_filename = "Tariff_Concession_8537_8539.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Excel file '{excel_filename}' created successfully.")
import pandas as pd

# Data dictionary for 8539 to 8547 (subset as per your data)
data = {
    "Reference Number": [
        # 8539 block (partial from previous + current)
        "8539", "8539.10", "8539.10.10", "8539.10.90", "8539.21.00", "8539.22.00", "8539.29.00",
        "8539.31.00", "8539.32.00", "8539.39.10", "8539.39.90", "8539.41.00", "8539.49.00",
        "8539.51.00", "8539.52.00", "8539.90.10", "8539.90.90",
        
        # 8540
        "8540", "8540.1", "8540.11.00", "8540.12.00", "8540.20.00", "8540.40.00", "8540.60.00",
        "8540.7", "8540.71.00", "8540.79.00", "8540.8", "8540.81.00", "8540.89.00",
        "8540.9", "8540.91.00", "8540.99.00",

        # 8541
        "8541", "8541.10.00", "8541.2", "8541.21.00", "8541.29.00", "8541.30.00", "8541.4",
        "8541.41.00", "8541.42.00", "8541.43.00", "8541.49.00", "8541.5", "8541.51.00", "8541.59.00",
        "8541.60.00", "8541.90.00",

        # 8542
        "8542", "8542.3", "8542.31.00", "8542.32.00", "8542.33.00", "8542.39.00", "8542.90.00",

        # 8543
        "8543", "8543.10.00", "8543.20.00", "8543.30", "8543.30.10", "8543.30.90", "8543.40.00",
        "8543.70.00", "8543.90.00",

        # 8544
        "8544", "8544.1", "8544.11.00", "8544.19.00", "8544.20.00", "8544.30.00", "8544.4",
        "8544.42", "8544.42.11", "8544.42.19", "8544.49", "8544.49.11", "8544.49.19",
        "8544.49.20", "8544.60.10", "8544.60.90", "8544.70.00"
    ],
    "Statistical Code": [
        "","", "28", "29", "", "","", "", "", "", "", "", "", "", "", "", "",
        "", "", "81", "04", "05", "06", "55", "", "56", "59", "", "10", "11",
        "", "82", "14",
        "", "15", "", "16", "39", "20", "", "01", "02", "03", "09", "", "10", "90",
        "", "", "", "", "", "", "",
        "", "70", "02", "", "64", "65", "66", "", "93",
        "", "", "10", "11", "", "5%", "", "", "03", "19", "", "39", "19",
        "20", "09", "34", "35", "22"
    ],
    "Unit": [
        "", "", "No", "No", "", "", "", "", "", "", "", "", "", "", "", "", "",
        "", "", "No", "No", "No", "No", "No", "", "No", "No", "", "No", "No",
        "", "No", "No",
        "", "No", "", "No", "No", "No", "", "No", "No", "No", "No", "", "No", "No",
        "", "", "", "", "", "", "",
        "", "No", "No", "", "No", "No", "No", "", "No",
        "", "", "kg", "kg", "", "", "", "", "kg", "", "", "m", "m",
        "m", "m", "kg", "kg", "m"
    ],
    "Goods": [
        "ELECTRIC FILAMENT OR DISCHARGE LAMPS, INCLUDING SEALED BEAM LAMP UNITS AND ULTRA-VIOLET OR INFRA-RED LAMPS; ARC- LAMPS; LIGHT-EMITTING DIODE (LED) LIGHT SOURCES:",
        "- Sealed beam lamp units:",
        "--- For motorcycles",
        "--- Other",
        "- Other filament lamps, excluding ultra-violet or infra-red lamps:",
        "-- Other, of a power not exceeding 200 W and for a voltage exceeding 100 V",
        "-- Other",
        "- Discharge lamps, other than ultra-violet lamps:",
        "-- Mercury or sodium vapour lamps; metal halide lamps",
        "--- Cold-cathode fluorescent lamps (CCFLs) for backlighting of flat panel displays",
        "--- Other",
        "- Ultra-violet or infra-red lamps; arc-lamps:",
        "-- Other",
        "- Light-Emitting Diode (LED) light sources:",
        "-- Light-Emitting Diode (LED) modules",
        "--- Other",
        "--- Other",
        "THERMIONIC, COLD CATHODE OR PHOTO- CATHODE VALVES AND TUBES:",
        "- Cathode-ray television picture tubes, including video monitor cathode-ray tubes:",
        "-- Colour",
        "-- Monochrome",
        "- Television camera tubes; image converters and intensifiers; other photo-cathode tubes",
        "- Data/graphic display tubes, monochrome; data/graphic display tubes, colour, with a phosphor dot screen pitch smaller than 0.4 mm",
        "- Other cathode-ray tubes",
        "- Microwave tubes (magnetrons, klystrons, travelling wave tubes, carcinotrons), excluding grid-controlled tubes:",
        "-- Magnetrons",
        "-- Other",
        "- Other valves and tubes:",
        "-- Receiver or amplifier valves and tubes",
        "-- Other",
        "- Parts:",
        "-- Of cathode-ray tubes",
        "-- Other",
        "SEMICONDUCTOR DEVICES:",
        "- Diodes, other than photosensitive or light-emitting diodes",
        "- Transistors, other than photosensitive transistors:",
        "-- With a dissipation rate of less than 1 W",
        "-- Other (power transistors, RF transistors, MOSFETS etc.)",
        "- Thyristors, diacs and triacs, other than photosensitive devices",
        "- Photosensitive semiconductor devices, including photovoltaic cells and LEDs:",
        "-- Light‑emitting diodes (LED)",
        "-- Photovoltaic cells not assembled in modules",
        "-- Photovoltaic cells assembled in modules",
        "-- Other",
        "- Other semiconductor devices:",
        "-- Semiconductor-based transducers",
        "-- Other",
        "- Mounted piezo-electric crystals",
        "- Parts",
        "ELECTRONIC INTEGRATED CIRCUITS:",
        "- Electronic integrated circuits:",
        "-- Processors and controllers, with or without memories, converters, logic circuits, amplifiers, clock and timing circuits",
        "Monolithic integrated circuits: Digital:",
        "..Application Specific (Digital) Integrated Circuits (ASIC)",
        "..Random Access Memory (RAM) including SIMMs, DIMMs, DRAM, SDRAM, RDRAM etc.",
        "-- Amplifiers",
        "-- Other",
        "Parts",
        "ELECTRICAL MACHINES AND APPARATUS, HAVING INDIVIDUAL FUNCTIONS, NOT SPECIFIED OR INCLUDED ELSEWHERE:",
        "- Particle accelerators",
        "- Signal generators",
        "- Machines and apparatus for electroplating, electrolysis or electrophoresis:",
        "--- Of a kind used solely or principally for the manufacture of printed circuits",
        "--- Other",
        "- Electronic cigarettes and similar personal electric vaporising devices",
        "- Other machines and apparatus:",
        "Electric fence energisers",
        "Signal processors (graphic equalisers, crossovers etc.)",
        "Mixing consoles with built-in amplifier, powered",
        "Other mixing consoles",
        "Other",
        "- Parts",
        "INSULATED (INCLUDING ENAMELLED OR ANODISED) WIRE, CABLE AND OTHER INSULATED ELECTRIC CONDUCTORS, WHETHER OR NOT FITTED WITH CONNECTORS; OPTICAL FIBRE CABLES:",
        "- Winding wire:",
        "-- Of copper",
        "-- Other",
        "- Co-axial cable and other co-axial electric conductors",
        "- Ignition wiring sets and other wiring sets used in vehicles, aircraft or ships",
        "- Other electric conductors, for voltage not exceeding 1000 V:",
        "-- Fitted with connectors:",
        "--- For a voltage not exceeding 80 V:",
        "Goods such as compensation or extension leads for thermo-couples, or used for telecommunications",
        "Other",
        "-- Other:",
        "--- For voltage not exceeding 80 V:",
        "Goods such as compensation or extension leads for thermo-couples, or used for telecommunications",
        "Other",
        "--- For voltage exceeding 80 V but not exceeding 1000 V",
        "--- Designed for working pressures exceeding 33 kV",
        "--- Other",
        "- Optical fibre cables"
    ],
    "Rate#": [
        "", "", "Free", "5%", "", "Free", "DCS:4% DCT:5%",
        "Free", "5%", "5%", "DCS:4% DCT:5%", "5%", "DCS:4% DCT:5%",
        "Free", "Free", "Free",
        "", "Free", "Free", "Free", "Free", "Free", "Free",
        "Free", "Free", "Free", "Free", "Free", "5%",
        "Free", "Free",
        "Free", "Free", "Free", "Free", "Free", "Free", "Free", "Free", "Free", "Free", "Free",
        "Free", "Free", "Free", "Free",
        "Free", "Free", "Free", "Free", "Free", "Free",
        "Free", "Free", "Free", "5%", "5%", "Free", "Free", "Free", "Free",
        "Free", "5%", "5%", "Free", "Free", "5%", "5%", "Free", "Free"
    ],
    "Tariff concession orders": [
        "View TCOs for 8539.10", "", "", "", "", "View TCOs for 8539.22", "View TCOs for 8539.29.00",
        "View TCOs for 8539.31.00", "View TCOs for 8539.32", "From 1 July 2019: Free", "View TCOs for 8539.39.90", "View TCOs for 8539.41.00", "View TCOs for 8539.49.00",
        "", "", "",
        "", "", "", "", "", "", "",
        "View TCOs for 8540.79.00", "", "View TCOs for 8540.89", "", "", "",
        "", "", "", "", "", "", "",
        "", "", "", "", "", "", "",
        "", "", "", "", "", "", "", "", "",
        "From 1 July 2019: Free", "From 1 July 2019: Free", "", "View TCOs for 8543.30.90", "",
        "", "", "", "", "", "",
        "View TCOs for 8544.11.00", "View TCOs for 8544.19.00", "View TCOs for 8544.20.00", "View TCOs for 8544.30.00",
        "View TCOs for 8544.42.19", "View TCOs for 8544.49.19", "View TCOs for 8544.49.20",
        "View TCOs for 8544.60.90", ""
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to Excel file
excel_filename = "Tariff_Concession_8539_8547.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Excel file '{excel_filename}' has been created successfully.")
import pandas as pd

# Data dictionary for 8544 to 8549
data = {
    "Reference Number": [
        # 8544
        "8544", "8544.1", "8544.11.00", "8544.19.00", "8544.20.00", "8544.30.00", "8544.4",
        "8544.42", "8544.42.11", "8544.42.19", "8544.49", "8544.49.11", "8544.49.19",
        "8544.49.20", "8544.60.10", "8544.60.90", "8544.70.00",
        
        # 8545
        "8545", "8545.1", "8545.11.00", "8545.19.00", "8545.20.00", "8545.90.00",
        "8545.90.00", "8545.90.00",
        
        # 8546
        "8546", "8546.10.00", "8546.20.00", "8546.90.00",
        
        # 8547
        "8547", "8547.10.00", "8547.20.00", "8547.90.00",
        
        # 8548
        "8548.00.00",
        
        # 8549
        "8549", "8549.1", "8549.11.00", "8549.12.00", "8549.13.00", "8549.14.00", "8549.19.00",
        "8549.2", "8549.21.00", "8549.29.00",
        "8549.3", "8549.31.00", "8549.39.00",
        "8549.9", "8549.91.00", "8549.99.00"
    ],
    "Statistical Code": [
        # 8544
        "", "", "10", "11", "", "", "", "", "03", "19", "", "39", "19", "20", "09", "34", "22",
        # 8545
        "", "", "24", "25", "26", "33", "57", "",
        # 8546
        "", "30", "31", "32",
        # 8547
        "", "01", "02", "10",
        # 8548
        "01",
        # 8549
        "", "", "01", "02", "03", "04", "09", "", "21", "29",
        "", "31", "39", "", "91", "99"
    ],
    "Unit": [
        # 8544
        "", "", "kg", "kg", "", "", "", "", "kg", "", "", "m", "m", "m", "m", "kg", "m",
        # 8545
        "", "", "kg", "kg", "No", "kg", "..", "",
        # 8546
        "", "No", "No", "No",
        # 8547
        "", "..", "..", "..",
        # 8548
        "..",
        # 8549
        "", "", "..", "..", "..", "..", "..", "", "..", "..",
        "", "..", "..", "", "..", ".."
    ],
    "Goods": [
        # 8544
        "INSULATED (INCLUDING ENAMELLED OR ANODISED) WIRE, CABLE AND OTHER INSULATED ELECTRIC CONDUCTORS;",
        "- Winding wire:",
        "-- Of copper",
        "-- Other",
        "- Co-axial cable and other co-axial electric conductors",
        "- Ignition wiring sets and other wiring sets of a kind used in vehicles, aircraft or ships",
        "- Other electric conductors, for a voltage not exceeding 1 000 V:",
        "-- Fitted with connectors:",
        "--- For a voltage not exceeding 80 V:",
        "---- Other",
        "-- Other:",
        "--- For a voltage not exceeding 80 V:",
        "---- Other",
        "--- For a voltage exceeding 80 V but not exceeding 1 000 V",
        "--- Designed for working pressures exceeding 33 kV",
        "--- Other",
        "- Optical fibre cables",
        
        # 8545
        "CARBON ELECTRODES, CARBON BRUSHES, LAMP CARBONS, BATTERY CARBONS AND OTHER ARTICLES OF GRAPHITE OR OTHER CARBON:",
        "- Electrodes:",
        "-- Of a kind used for furnaces",
        "-- Other",
        "- Brushes",
        "- Other",
        "Blocks, plates, slabs and rods",
        
        # 8546
        "ELECTRICAL INSULATORS OF ANY MATERIAL:",
        "- Of glass",
        "- Of ceramics",
        "- Other",
        
        # 8547
        "INSULATING FITTINGS FOR ELECTRICAL MACHINES, APPLIANCES OR EQUIPMENT:",
        "- Insulating fittings of ceramics",
        "- Insulating fittings of plastics",
        "- Other",
        
        # 8548
        "ELECTRICAL PARTS OF MACHINERY OR APPARATUS, NOT SPECIFIED OR INCLUDED ELSEWHERE IN THIS CHAPTER:",
        
        # 8549
        "ELECTRICAL AND ELECTRONIC WASTE AND SCRAP:",
        "‑Waste and scrap of primary cells, primary batteries and electric accumulators:",
        "‑‑Waste and scrap of lead‑acid accumulators; spent lead‑acid accumulators",
        "‑‑Other, containing lead, cadmium or mercury",
        "‑‑Sorted by chemical type and not containing lead, cadmium or mercury",
        "‑‑Unsorted and not containing lead, cadmium or mercury",
        "‑‑Other",
        "‑Of a kind used principally for the recovery of precious metal:",
        "‑‑Containing primary cells, primary batteries, electric accumulators, mercury‑switches, glass from cathode‑ray tubes or other activated glass, or electrical or electronic components containing cadmium, mercury, lead or polychlorinated biphenyls (PCBs)",
        "‑‑Other",
        "‑Other electrical and electronic assemblies and printed circuit boards:",
        "‑‑Containing primary cells, primary batteries, electric accumulators, mercury‑switches, glass from cathode‑ray tubes or other activated glass, or electrical or electronic components containing cadmium, mercury, lead or polychlorinated biphenyls (PCBs)",
        "‑‑Other",
        "‑Other:",
        "‑‑Containing primary cells, primary batteries, electric accumulators, mercury‑switches, glass from cathode‑ray tubes or other activated glass, or electrical or electronic components containing cadmium, mercury, lead or polychlorinated biphenyls (PCBs)",
        "‑‑Other"
    ],
    "Rate#": [
        # 8544
        "", "", "5% DCS:4% CA:Free DCT:5%", "5% DCS:4% CA:Free DCT:5%", "5%", "5%", "", "", "Free", "5% DCS:4% DCT:5%", "", "Free", "5% DCS:4% DCT:5%", "5% DCS:4% DCT:5%", "Free", "5% DCS:4% DCT:5%", "Free",
        # 8545
        "", "", "Free", "Free", "5% DCS:4% DCT:5%", "Free", "Free", "",
        # 8546
        "", "Free", "Free", "5%",
        # 8547
        "", "5%", "Free", "5%",
        # 8548
        "Free",
        # 8549
        "", "", "Free", "Free", "Free", "Free", "Free", "", "Free", "Free",
        "", "Free", "Free", "", "Free", "Free"
    ],
    "Tariff concession orders": [
        # 8544
        "", "", "View TCOs for 8544.11.00", "View TCOs for 8544.19.00", "View TCOs for 8544.20.00", "View TCOs for 8544.30.00", "", "", "", "View TCOs for 8544.42.19", "", "View TCOs for 8544.49.11", "View TCOs for 8544.49.19", "View TCOs for 8544.49.20", "", "View TCOs for 8544.60.90", "",
        # 8545
        "", "", "", "", "View TCOs for 8545.20.00", "", "", "",
        # 8546
        "", "View TCOs for 8546.10.00", "View TCOs for 8546.20.00", "View TCOs for 8546.90.00",
        # 8547
        "", "View TCOs for 8547.10", "", "View TCOs for 8547.90.00",
        # 8548
        "",
        # 8549
        "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
output_file = "Tariff_Concession_8544_8549.xlsx"
df.to_excel(output_file, index=False)

print(f"Excel file '{output_file}' created successfully.")
