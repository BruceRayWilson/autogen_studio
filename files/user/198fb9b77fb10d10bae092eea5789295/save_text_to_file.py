# filename: save_text_to_file.py
from autogen.core import skill
from skills import save_text_to_file

# Define the base name for the files
className = "Accounting"

# Define the content for the .h and .cpp files
hContent = "/* This is the header content for AccountingFixtures.h */"
cppContent = "/* This is the source content for AccountingTests.cpp */"

# Save the content to the respective files
save_text_to_file(f"/home/wilsonb/dl/github.com/BruceRayWilson/Accounting/{className}Fixtures.h", hContent)
save_text_to_file(f"/home/wilsonb/dl/github.com/BruceRayWilson/Accounting/{className}Tests.cpp", cppContent)