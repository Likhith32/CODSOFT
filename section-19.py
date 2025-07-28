import pandas as pd

# Chapter 93 data
data = [
    {"HS Code": "9301.10.00", "Stat Code": "24", "Unit": "No", "Goods": "Artillery weapons", "Rate": "Free"},
    {"HS Code": "9301.20.00", "Stat Code": "25", "Unit": "No", "Goods": "Rocket launchers, flame-throwers, etc.", "Rate": "Free"},
    {"HS Code": "9301.90.00", "Stat Code": "26", "Unit": "No", "Goods": "Other military weapons", "Rate": "Free"},
    {"HS Code": "9302.00.00", "Stat Code": "02", "Unit": "No", "Goods": "Revolvers and pistols", "Rate": "Free"},
    {"HS Code": "9303.10.00", "Stat Code": "03", "Unit": "No", "Goods": "Muzzle-loading firearms", "Rate": "Free"},
    {"HS Code": "9303.20.00", "Stat Code": "04", "Unit": "No", "Goods": "Sporting/hunting shotguns", "Rate": "Free"},
    {"HS Code": "9303.30.00", "Stat Code": "05", "Unit": "No", "Goods": "Sporting/hunting rifles", "Rate": "Free"},
    {"HS Code": "9303.90.00", "Stat Code": "06", "Unit": "No", "Goods": "Other firearms", "Rate": "Free"},
    {"HS Code": "9304.00.00", "Stat Code": "07", "Unit": "No", "Goods": "Spring, air or gas guns, truncheons", "Rate": "Free"},
    {"HS Code": "9305.10.00", "Stat Code": "08", "Unit": "..", "Goods": "Parts of revolvers or pistols", "Rate": "5% DCS:Free"},
    {"HS Code": "9305.20.10", "Stat Code": "09", "Unit": "..", "Goods": "Shotgun barrels", "Rate": "Free"},
    {"HS Code": "9305.20.90", "Stat Code": "10", "Unit": "..", "Goods": "Other parts of shotguns or rifles", "Rate": "5% DCS:Free"},
    {"HS Code": "9305.91.00", "Stat Code": "27", "Unit": "..", "Goods": "Parts of military weapons", "Rate": "5% DCS:4% DCT:5%"},
    {"HS Code": "9305.99.00", "Stat Code": "28", "Unit": "..", "Goods": "Other parts and accessories", "Rate": "5% DCS:4% DCT:5%"},
    {"HS Code": "9306.21.00", "Stat Code": "21", "Unit": "No", "Goods": "Shotgun cartridges", "Rate": "5%"},
    {"HS Code": "9306.29.00", "Stat Code": "16", "Unit": "..", "Goods": "Other parts of shotgun cartridges", "Rate": "Free"},
    {"HS Code": "9306.30.00", "Stat Code": "13", "Unit": "No", "Goods": "Other cartridges - loaded", "Rate": "5%"},
    {"HS Code": "9306.30.00", "Stat Code": "14", "Unit": "..", "Goods": "Other cartridges - other", "Rate": "5%"},
    {"HS Code": "9306.90.00", "Stat Code": "19", "Unit": "..", "Goods": "Other ammunition and parts", "Rate": "Free"},
    {"HS Code": "9307.00.00", "Stat Code": "20", "Unit": "..", "Goods": "Swords, bayonets, lances, and scabbards", "Rate": "Free"},
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to Excel
output_file = "chapter_93_arms_ammunition.xlsx"
df.to_excel(output_file, index=False)

print(f"✅ Excel file '{output_file}' created successfully.")
