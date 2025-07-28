import pandas as pd

# Chapter 86 Data
data = [
    {"HS Code": "8601.10.00", "Stat Code": "01", "Unit": "No", "Goods": "Rail locomotives powered from external electricity", "Rate": "5%"},
    {"HS Code": "8601.20.00", "Stat Code": "02", "Unit": "No", "Goods": "Rail locomotives powered by electric accumulators", "Rate": "5%"},
    {"HS Code": "8602.10.00", "Stat Code": "03", "Unit": "No", "Goods": "Diesel-electric locomotives", "Rate": "5%"},
    {"HS Code": "8602.90.00", "Stat Code": "04", "Unit": "No", "Goods": "Other locomotives and tenders", "Rate": "5%"},
    {"HS Code": "8603.10.00", "Stat Code": "05", "Unit": "No", "Goods": "Electric self-propelled coaches/vans/trucks", "Rate": "5%"},
    {"HS Code": "8603.90.00", "Stat Code": "06", "Unit": "No", "Goods": "Other self-propelled coaches/vans/trucks", "Rate": "5%"},
    {"HS Code": "8604.00.00", "Stat Code": "07", "Unit": "No", "Goods": "Maintenance/service rail vehicles", "Rate": "5%"},
    {"HS Code": "8605.00.00", "Stat Code": "08", "Unit": "No", "Goods": "Non-self-propelled coaches and vans", "Rate": "Free"},
    {"HS Code": "8606.10.00", "Stat Code": "09", "Unit": "No", "Goods": "Tank wagons", "Rate": "5%"},
    {"HS Code": "8606.30.00", "Stat Code": "11", "Unit": "No", "Goods": "Self-discharging wagons", "Rate": "5%"},
    {"HS Code": "8606.91.00", "Stat Code": "23", "Unit": "No", "Goods": "Covered and closed wagons", "Rate": "Free"},
    {"HS Code": "8606.92.00", "Stat Code": "13", "Unit": "No", "Goods": "Open wagons with high non-removable sides", "Rate": "5%"},
    {"HS Code": "8606.99.00", "Stat Code": "14", "Unit": "No", "Goods": "Other wagons", "Rate": "5%"},
    {"HS Code": "8607.11.00", "Stat Code": "15", "Unit": "..", "Goods": "Driving bogies and bissel-bogies", "Rate": "5%"},
    {"HS Code": "8607.12.00", "Stat Code": "16", "Unit": "..", "Goods": "Other bogies and bissel-bogies", "Rate": "5%"},
    {"HS Code": "8607.21.00", "Stat Code": "18", "Unit": "..", "Goods": "Air brakes and parts", "Rate": "5%"},
    {"HS Code": "8607.29.00", "Stat Code": "19", "Unit": "..", "Goods": "Other brakes and parts", "Rate": "5%"},
    {"HS Code": "8607.30.00", "Stat Code": "20", "Unit": "..", "Goods": "Coupling devices, buffers, and parts", "Rate": "5%"},
    {"HS Code": "8607.91.00", "Stat Code": "21", "Unit": "..", "Goods": "Parts of locomotives", "Rate": "5%"},
    {"HS Code": "8607.99.00", "Stat Code": "22", "Unit": "..", "Goods": "Other parts", "Rate": "5%"},
    {"HS Code": "8608.00.00", "Stat Code": "29", "Unit": "..", "Goods": "Track fixtures, signals, control equipment", "Rate": "5%"},
    {"HS Code": "8609.00.00", "Stat Code": "26", "Unit": "No", "Goods": "Transport containers for rail", "Rate": "Free"},
]

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
output_file = "chapter_86_railways.xlsx"
df.to_excel(output_file, index=False)

print(f"✅ Excel file '{output_file}' created successfully.")
import pandas as pd

# Sample data for Chapter 87 (expanded set)
data = [
    ["8701.10.00", "01", "No", "Single axle tractors", "Free"],
    ["8701.21.00", "10", "No", "Road tractors - diesel or semi‑diesel", "5%"],
    ["8701.22.00", "20", "No", "Road tractors - diesel & electric", "5%"],
    ["8701.23.00", "30", "No", "Road tractors - petrol & electric", "5%"],
    ["8701.24.00", "40", "No", "Road tractors - only electric", "5%"],
    ["8701.29.00", "90", "No", "Other road tractors", "5%"],
    ["8701.30.00", "11", "No", "Track-laying tractors", "Free"],
    ["8701.91.11", "02", "No", "Agricultural tractors <=18 kW", "Free"],
    ["8701.91.19", "03", "No", "Other tractors <=18 kW", "5%"],
    ["8701.92.10", "06", "No", "Agricultural tractors >18kW <=37kW", "Free"],
    ["8702.10.10", "78", "No", "Motor vehicles >10 persons - diesel", "5%"],
    ["8702.20.10", "16", "No", "Motor vehicles >10 persons - diesel & electric", "5%"],
    ["8702.30.10", "18", "No", "Motor vehicles >10 persons - petrol & electric", "5%"],
    ["8702.40.10", "20", "No", "Motor vehicles >10 persons - electric", "5%"],
    ["8702.90.10", "82", "No", "Motor vehicles >10 persons - other", "5%"],
]

# Create DataFrame
df = pd.DataFrame(data, columns=["Reference Number", "Statistical Code", "Unit", "Goods", "Rate"])

# Save to Excel
file_path = "/mnt/data/chapter_87_part_2_vehicles.xlsx"
df.to_excel(file_path, index=False)

file_path
import pandas as pd

# Data for Chapter 87.03 - Motor Cars and Other Motor Vehicles
data = [
    ["8703.10.00", "01", "No", "Vehicles specially designed for travelling on snow; golf cars and similar vehicles", "5%", "CA:Free"],
    ["8703.21.11", "03", "No", "Passenger motor vehicles - Used or second-hand vehicles", "5%", "CA:Free"],
    ["8703.21.19", "14", "No", "Passenger motor vehicles - Other", "5%", "CA:Free"],
    ["8703.21.20", "22", "No", "Goods, NSA - g.v.w. > 3.5t or <= 3.5t, assembled", "5%", "CA:Free"],
    ["8703.21.90", "71", "No", "Other", "5%", "DCS:4%, CA:Free, DCT:5%"],
    ["8703.22.11", "15", "No", "Passenger motor vehicles - Used or second-hand vehicles", "5%", "CA:Free"],
    ["8703.22.19", "24", "No", "Passenger motor vehicles - Other", "5%", "CA:Free"],
    ["8703.22.20", "23", "No", "Goods, NSA - g.v.w. > 3.5t or <= 3.5t, assembled", "5%", "CA:Free"],
    ["8703.22.90", "86", "No", "Other", "5%", "DCS:4%, CA:Free, DCT:5%"],
    ["8703.23.11", "18", "No", "Passenger motor vehicles - Used or second-hand vehicles - Less than 5 years of age", "5%", "CA:Free"],
    ["8703.23.11", "27", "No", "Passenger motor vehicles - Used or second-hand vehicles - 5 years of age or more", "5%", "CA:Free"],
    ["8703.23.19", "20", "No", "Passenger motor vehicles - Other", "5%", "CA:Free"],
    ["8703.23.19", "25", "No", "Passenger motor vehicles - Assembled four-wheel drive vehicles", "5%", "CA:Free"],
    ["8703.23.90", "87", "No", "Other", "5%", "DCS:4%, CA:Free, DCT:5%"],
    ["8703.24.11", "29", "No", "Passenger motor vehicles - Used or second-hand vehicles - Less than 5 years of age", "5%", "CA:Free"],
    ["8703.24.11", "30", "No", "Passenger motor vehicles - Used or second-hand vehicles - 5 years of age or more", "5%", "CA:Free"],
    ["8703.24.19", "31", "No", "Passenger motor vehicles - Other", "5%", "CA:Free"],
    ["8703.24.20", "88", "No", "Goods, NSA - Off-road vehicles", "5%", "CA:Free"],
    ["8703.24.20", "89", "No", "Goods, NSA - Other", "5%", "CA:Free"],
    ["8703.24.20", "90", "No", "Goods, NSA - Other", "5%", "CA:Free"],
    ["8703.24.90", "91", "No", "Other", "5%", "DCS:4%, CA:Free, DCT:5%"]
]

# Define DataFrame
df = pd.DataFrame(data, columns=["Reference Number", "Statistical Code", "Unit", "Goods", "Rate#", "Tariff concession orders"])

# Save to Excel
file_path = "/mnt/data/chapter_87_part_3_motor_cars.xlsx"
df.to_excel(file_path, index=False)

file_path
import pandas as pd

# Data extracted from the full 8704 to 8706 description
data = [
    {"Reference Number": "8704.10.00", "Statistical Code": "", "Unit": "", "Goods": "Dumpers designed for off-highway use", "Rate": "5%", "Tariff Concession Orders": "CA:Free"},
    {"Reference Number": "8704.21.10", "Statistical Code": "10", "Unit": "No", "Goods": "g.v.w. exceeding 3.5 t", "Rate": "5%", "Tariff Concession Orders": "CA:Free"},
    {"Reference Number": "8704.21.90", "Statistical Code": "90", "Unit": "No", "Goods": "Other", "Rate": "5%", "Tariff Concession Orders": "DCS:4%, CA:Free, DCT:5%"},
    {"Reference Number": "8704.22.00", "Statistical Code": "08", "Unit": "No", "Goods": "g.v.w. exceeding 5 t but not exceeding 20 t", "Rate": "5%", "Tariff Concession Orders": "CA:Free"},
    {"Reference Number": "8704.23.00", "Statistical Code": "35", "Unit": "No", "Goods": "g.v.w. exceeding 20 t", "Rate": "5%", "Tariff Concession Orders": "CA:Free"},
    {"Reference Number": "8704.31.10", "Statistical Code": "69", "Unit": "No", "Goods": "g.v.w. exceeding 3.5 t", "Rate": "5%", "Tariff Concession Orders": "CA:Free"},
    {"Reference Number": "8704.31.90", "Statistical Code": "90", "Unit": "No", "Goods": "Other", "Rate": "5%", "Tariff Concession Orders": "DCS:4%, CA:Free, DCT:5%"},
    {"Reference Number": "8704.32.00", "Statistical Code": "12", "Unit": "No", "Goods": "g.v.w. exceeding 5 t", "Rate": "5%", "Tariff Concession Orders": "CA:Free"},
    {"Reference Number": "8704.41.10", "Statistical Code": "01", "Unit": "No", "Goods": "g.v.w. exceeding 3.5 t", "Rate": "5%", "Tariff Concession Orders": "CA:Free"},
    {"Reference Number": "8704.41.90", "Statistical Code": "90", "Unit": "No", "Goods": "Other", "Rate": "5%", "Tariff Concession Orders": "DCS:4%, CA:Free, DCT:5%"},
    {"Reference Number": "8704.42.00", "Statistical Code": "20", "Unit": "No", "Goods": "g.v.w. exceeding 5 t but not exceeding 20 t", "Rate": "5%", "Tariff Concession Orders": "CA:Free"},
    {"Reference Number": "8704.43.00", "Statistical Code": "30", "Unit": "No", "Goods": "g.v.w. exceeding 20 t", "Rate": "5%", "Tariff Concession Orders": "CA:Free"},
    {"Reference Number": "8704.51.10", "Statistical Code": "40", "Unit": "No", "Goods": "g.v.w. exceeding 3.5 t", "Rate": "5%", "Tariff Concession Orders": "CA:Free"},
    {"Reference Number": "8704.51.90", "Statistical Code": "90", "Unit": "No", "Goods": "Other", "Rate": "5%", "Tariff Concession Orders": "DCS:4%, CA:Free, DCT:5%"},
    {"Reference Number": "8704.52.00", "Statistical Code": "60", "Unit": "No", "Goods": "g.v.w. exceeding 5 t", "Rate": "5%", "Tariff Concession Orders": "CA:Free"},
    {"Reference Number": "8704.60.10", "Statistical Code": "70", "Unit": "No", "Goods": "Assembled electric vehicles", "Rate": "5%", "Tariff Concession Orders": "CA:Free"},
    {"Reference Number": "8704.60.90", "Statistical Code": "90", "Unit": "No", "Goods": "Other electric vehicles", "Rate": "5%", "Tariff Concession Orders": "DCS:4%, CA:Free, DCT:5%"},
    {"Reference Number": "8704.90.10", "Statistical Code": "80", "Unit": "No", "Goods": "Other assembled", "Rate": "5%", "Tariff Concession Orders": "CA:Free"},
    {"Reference Number": "8704.90.90", "Statistical Code": "90", "Unit": "No", "Goods": "Other", "Rate": "5%", "Tariff Concession Orders": "DCS:4%, CA:Free, DCT:5%"},
    {"Reference Number": "8705.10.00", "Statistical Code": "15", "Unit": "No", "Goods": "Crane lorries", "Rate": "5%", "Tariff Concession Orders": "View TCOs for 8705.10.00"},
    {"Reference Number": "8705.20.00", "Statistical Code": "24", "Unit": "No", "Goods": "Mobile drilling derricks", "Rate": "5%", "Tariff Concession Orders": ""},
    {"Reference Number": "8705.30.00", "Statistical Code": "25", "Unit": "No", "Goods": "Fire fighting vehicles", "Rate": "5%", "Tariff Concession Orders": "View TCOs for 8705.30.00"},
    {"Reference Number": "8705.40.00", "Statistical Code": "26", "Unit": "No", "Goods": "Concrete-mixer lorries", "Rate": "5%", "Tariff Concession Orders": "View TCOs for 8705.40.00"},
    {"Reference Number": "8705.90.00", "Statistical Code": "27", "Unit": "No", "Goods": "Other special purpose motor vehicles", "Rate": "5%", "Tariff Concession Orders": "View TCOs for 8705.90.00"},
    {"Reference Number": "8706.00.10", "Statistical Code": "23", "Unit": "No", "Goods": "For use in assembly/manufacture of passenger vehicles", "Rate": "5%", "Tariff Concession Orders": "CA:Free"},
    {"Reference Number": "8706.00.91", "Statistical Code": "83", "Unit": "No", "Goods": "Used as components in passenger motor vehicles", "Rate": "5%", "Tariff Concession Orders": "CA:Free"},
    {"Reference Number": "8706.00.99", "Statistical Code": "84", "Unit": "No", "Goods": "Other chassis", "Rate": "5%", "Tariff Concession Orders": "CA:Free"},
]

# Create DataFrame
df = pd.DataFrame(data)

# Write to Excel
excel_path = "/mnt/data/Chapter_8704_to_8706_Tariff.xlsx"
df.to_excel(excel_path, index=False)

excel_path
import pandas as pd

# Create a list of dictionaries (sample structure; extend as needed)
data = [
    {"Reference Number": "8707.10.10", "Statistical Code": "25", "Unit": "..", "Goods": "For use in the assembly or manufacture of passenger motor vehicles", "Rate": "5%", "Tariff concession orders": "CA:Free"},
    {"Reference Number": "8707.10.91", "Statistical Code": "85", "Unit": "..", "Goods": "Of a kind used as components in passenger motor vehicles", "Rate": "5%", "Tariff concession orders": "CA:Free"},
    {"Reference Number": "8708.10.10", "Statistical Code": "89", "Unit": "..", "Goods": "Bumpers - Of a kind used as components in passenger motor vehicles", "Rate": "5%", "Tariff concession orders": "CA:Free"},
    {"Reference Number": "8708.21.10", "Statistical Code": "91", "Unit": "No", "Goods": "Safety seat belts - Of a kind used as components in passenger motor vehicles", "Rate": "5%", "Tariff concession orders": "CA:Free"},
    {"Reference Number": "8708.22.10", "Statistical Code": "20", "Unit": "No", "Goods": "Front windscreens - For tractors other than for dumpers", "Rate": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8708.30.12", "Statistical Code": "12", "Unit": "No", "Goods": "Disc brake pads - For passenger motor vehicles", "Rate": "5%", "Tariff concession orders": "CA:Free"},
    {"Reference Number": "8708.80.42", "Statistical Code": "46", "Unit": "No", "Goods": "Suspension shock-absorbers - For passenger motor vehicles", "Rate": "5%", "Tariff concession orders": "CA:Free"},
    {"Reference Number": "8708.95.20", "Statistical Code": "78", "Unit": "..", "Goods": "Safety airbags - For passenger motor vehicles", "Rate": "5%", "Tariff concession orders": "CA:Free"},
    {"Reference Number": "8708.99.30", "Statistical Code": "09", "Unit": "..", "Goods": "Chassis - For use in the assembly or manufacture of passenger motor vehicles", "Rate": "5%", "Tariff concession orders": "CA:Free"},
]

# Create a DataFrame
df = pd.DataFrame(data)

# Save to Excel file
output_file = "vehicle_tariff_data.xlsx"
df.to_excel(output_file, index=False)

print(f"Excel file '{output_file}' has been created successfully.")
import pandas as pd

# Sample data based on your latest block (extend as needed)
data = [
    {"Reference Number": "8709.11.00", "Statistical Code": "12", "Unit": "No", "Goods": "WORKS TRUCKS - Electrical", "Rate": "5%", "Tariff concession orders": "View TCOs for 8709.11.00"},
    {"Reference Number": "8709.19.00", "Statistical Code": "13", "Unit": "No", "Goods": "WORKS TRUCKS - Other", "Rate": "5%", "Tariff concession orders": "View TCOs for 8709.19.00"},
    {"Reference Number": "8709.90.00", "Statistical Code": "54", "Unit": "..", "Goods": "Parts", "Rate": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8710.00.00", "Statistical Code": "16", "Unit": "..", "Goods": "TANKS AND OTHER ARMOURED VEHICLES", "Rate": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8711.10.00", "Statistical Code": "55", "Unit": "No", "Goods": "Motorcycles ≤ 50cc", "Rate": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8711.60.00", "Statistical Code": "06", "Unit": "No", "Goods": "Motorcycles - Electric", "Rate": "5%", "Tariff concession orders": "DCS: 4%, DCT: 5%"},
    {"Reference Number": "8712.00.00", "Statistical Code": "52", "Unit": "No", "Goods": "Bicycles ≤ 508mm", "Rate": "5%", "Tariff concession orders": "View TCOs for 8712.00.00"},
    {"Reference Number": "8713.10.00", "Statistical Code": "01", "Unit": "No", "Goods": "Carriages for disabled - Not mechanically propelled", "Rate": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8714.10.10", "Statistical Code": "03", "Unit": "..", "Goods": "Motorcycle exhaust systems", "Rate": "5%", "Tariff concession orders": "View TCOs for 8714.10.10"},
    {"Reference Number": "8715.00.00", "Statistical Code": "40", "Unit": "No", "Goods": "Baby carriages", "Rate": "Free", "Tariff concession orders": ""},
    {"Reference Number": "8716.10.00", "Statistical Code": "15", "Unit": "No", "Goods": "Caravan trailers", "Rate": "5%", "Tariff concession orders": ""},
    {"Reference Number": "8716.31.00", "Statistical Code": "40", "Unit": "No", "Goods": "Tanker trailers", "Rate": "Free", "Tariff concession orders": "View TCOs for 8716.31.00"},
    {"Reference Number": "8716.90.00", "Statistical Code": "39", "Unit": "..", "Goods": "Trailer parts - Other", "Rate": "5%", "Tariff concession orders": "View TCOs for 8716.90.00"},
]

# Convert list of dictionaries to DataFrame
df = pd.DataFrame(data)

# Save to Excel
excel_file = "vehicle_tariff_data_complete.xlsx"
df.to_excel(excel_file, index=False)

print(f"Excel file '{excel_file}' has been created successfully.")
import pandas as pd

# Create a DataFrame for Chapter 88 - Aircraft, spacecraft, and parts thereof
chapter_88_data = [
    ["8801.00.00", 21, "No", "Balloons and dirigibles; gliders, hang gliders and other non-powered aircraft", "Free"],
    ["8802.11.00", 4, "No", "Helicopters - Of an unladen weight not exceeding 2 000 kg", "Free"],
    ["8802.12.00", 5, "No", "Helicopters - Of an unladen weight exceeding 2 000 kg", "Free"],
    ["8802.20.00", 6, "No", "Aeroplanes and other aircraft, of an unladen weight not exceeding 2 000 kg", "Free"],
    ["8802.30.00", 7, "No", "Aeroplanes and other aircraft, of an unladen weight exceeding 2 000 kg but not exceeding 15 000 kg", "Free"],
    ["8802.40.00", 8, "No", "Aeroplanes and other aircraft, of an unladen weight exceeding 15 000 kg", "Free"],
    ["8802.60.00", 17, "No", "Spacecraft (including satellites) and suborbital and spacecraft launch vehicles", "Free"],
    ["8804.00.00", 14, "..", "Parachutes and rotochutes; parts and accessories", "Free"],
    ["8805.10.00", 15, "..", "Aircraft launching gear and parts; deck-arrestor gear", "Free"],
    ["8805.21.00", 18, "No", "Air combat simulators", "Free"],
    ["8805.21.00", 19, "..", "Parts of air combat simulators", "Free"],
    ["8805.29.00", 20, "..", "Other ground flying trainers and parts", "Free"],
    ["8806.10.00", 1, "No", "Unmanned aircraft - Designed for carriage of passengers, With one or more rotors", "Free"],
    ["8806.10.00", 2, "No", "Unmanned aircraft - Designed for carriage of passengers, Other", "Free"],
    ["8806.21.00", 10, "No", "Unmanned aircraft <= 250g, With rotors", "Free"],
    ["8806.21.00", 11, "No", "Unmanned aircraft <= 250g, Other", "Free"],
    ["8806.22.00", 20, "No", "Unmanned aircraft > 250g <= 7kg, With rotors", "Free"],
    ["8806.22.00", 21, "No", "Unmanned aircraft > 250g <= 7kg, Other", "Free"],
    ["8806.23.00", 30, "No", "Unmanned aircraft > 7kg <= 25kg, With rotors", "Free"],
    ["8806.23.00", 31, "No", "Unmanned aircraft > 7kg <= 25kg, Other", "Free"],
    ["8806.24.00", 40, "No", "Unmanned aircraft > 25kg <= 150kg, With rotors", "Free"],
    ["8806.24.00", 41, "No", "Unmanned aircraft > 25kg <= 150kg, Other", "Free"],
    ["8806.29.00", 90, "No", "Other unmanned aircraft, With rotors", "Free"],
    ["8806.29.00", 91, "No", "Other unmanned aircraft, Other", "Free"],
    ["8806.91.00", 50, "No", "Other unmanned aircraft <= 250g, With rotors", "Free"],
    ["8806.91.00", 51, "No", "Other unmanned aircraft <= 250g, Other", "Free"],
    ["8806.92.00", 60, "No", "Other unmanned aircraft > 250g <= 7kg, With rotors", "Free"],
    ["8806.92.00", 61, "No", "Other unmanned aircraft > 250g <= 7kg, Other", "Free"],
    ["8806.93.00", 70, "No", "Other unmanned aircraft > 7kg <= 25kg, With rotors", "Free"],
    ["8806.93.00", 71, "No", "Other unmanned aircraft > 7kg <= 25kg, Other", "Free"],
    ["8806.94.00", 80, "No", "Other unmanned aircraft > 25kg <= 150kg, With rotors", "Free"],
    ["8806.94.00", 81, "No", "Other unmanned aircraft > 25kg <= 150kg, Other", "Free"],
    ["8806.99.00", 90, "No", "Other unmanned aircraft, With rotors", "Free"],
    ["8806.99.00", 91, "No", "Other unmanned aircraft, Other", "Free"],
    ["8807.10.00", 1, "..", "Propellers and rotors and parts thereof", "Free"],
    ["8807.20.00", 10, "..", "Undercarriages and parts thereof", "Free"],
    ["8807.30.00", 20, "..", "Other parts of aeroplanes, helicopters or unmanned aircraft", "Free"],
    ["8807.90.00", 90, "..", "Other parts", "Free"],
]

df_ch88 = pd.DataFrame(chapter_88_data, columns=[
    "Reference Number", "Statistical Code", "Unit", "Goods", "Rate"
])

# Save to Excel
excel_path = "/mnt/data/tariff_chapter_88_aircraft.xlsx"
df_ch88.to_excel(excel_path, index=False)

excel_path
import pandas as pd

# Define the data
data = [
    ["8901.10.10", "01", "No", "Cruise ships/excursion boats/ferry-boats not exceeding 150 gross construction tons", "5%"],
    ["8901.10.90", "08", "No", "Other cruise ships/excursion boats/ferry-boats", "Free"],
    ["8901.20.10", "03", "No", "Tankers not exceeding 150 gross construction tons", "5%"],
    ["8901.20.90", "04", "No", "Other tankers", "Free"],
    ["8901.30.10", "05", "No", "Refrigerated vessels not exceeding 150 gross construction tons", "5%"],
    ["8901.30.90", "06", "No", "Other refrigerated vessels", "Free"],
    ["8901.90.10", "07", "No", "Other vessels for transport not exceeding 150 gross construction tons", "5%"],
    ["8901.90.90", "35", "No", "Self transported goods vessels (under own power)", "Free"],
    ["8901.90.90", "36", "No", "Other transport vessels", "Free"],
    ["8902.00.10", "09", "No", "Fishing vessels not exceeding 150 gross construction tons", "Free"],
    ["8902.00.90", "10", "No", "Other fishing vessels", "Free"],
    ["8903.11.00", "01", "No", "Inflatable motor boats not exceeding 100 kg", "5%"],
    ["8903.12.00", "02", "No", "Non-motor inflatable boats not exceeding 100 kg", "5%"],
    ["8903.19.00", "90", "No", "Other inflatable boats", "5%"],
    ["8903.21.00", "01", "No", "Sailboats not exceeding 7.5 m", "5%"],
    ["8903.22.00", "10", "No", "Sailboats 7.5 m to 24 m", "5%"],
    ["8903.23.10", "01", "No", "Sailboats >24 m and ≤150 gross tons", "5%"],
    ["8903.23.90", "90", "No", "Sailboats >24 m (other)", "Free"],
    ["8903.31.00", "01", "No", "Motorboats not exceeding 7.5 m", "5%"],
    ["8903.32.00", "10", "No", "Motorboats 7.5 m to 24 m", "5%"],
    ["8903.33.10", "01", "No", "Motorboats >24 m and ≤150 gross tons", "5%"],
    ["8903.33.90", "90", "No", "Motorboats >24 m (other)", "Free"],
    ["8903.93.00", "01", "No", "Other boats not exceeding 7.5 m", "5%"],
    ["8903.99.10", "10", "No", "Other boats ≤150 gross tons", "5%"],
    ["8903.99.90", "19", "No", "Other boats", "Free"],
    ["8904.00.10", "20", "No", "Tugs/pushers ≤150 gross tons", "5%"],
    ["8904.00.90", "21", "No", "Other tugs/pushers", "Free"],
    ["8905.10.10", "22", "No", "Dredgers ≤150 gross tons", "5%"],
    ["8905.10.90", "23", "No", "Other dredgers", "Free"],
    ["8905.20.10", "24", "No", "Floating/submersible platforms ≤150 gross tons", "5%"],
    ["8905.20.90", "25", "No", "Other platforms", "Free"],
    ["8905.90.10", "26", "No", "Other vessels ≤150 gross tons", "5%"],
    ["8905.90.90", "29", "No", "Other", "Free"],
    ["8906.10.10", "41", "No", "Warships ≤150 gross tons", "5%"],
    ["8906.10.90", "42", "No", "Other warships", "Free"],
    ["8906.90.10", "43", "No", "Other vessels ≤150 gross tons", "5%"],
    ["8906.90.90", "44", "No", "Other", "Free"],
    ["8907.10.00", "30", "No", "Inflatable rafts", "5%"],
    ["8907.90.00", "31", "No", "Other floating structures", "5%"],
    ["8908.00.00", "32", "No", "Floating structures for breaking up", "Free"]
]

# Create DataFrame
df = pd.DataFrame(data, columns=["Reference Number", "Statistical Code", "Unit", "Goods", "Rate"])

# Export to Excel
df.to_excel("chapter_89_ships.xlsx", index=False)
