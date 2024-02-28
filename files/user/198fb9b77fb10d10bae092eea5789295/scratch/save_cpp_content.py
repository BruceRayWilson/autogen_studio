# filename: save_cpp_content.py
from skills import save_text_to_file

# Define the base name for the file
className = "Accounting"

# Define the content for the .cpp file (this should be the actual content you want to save)
cppContent = "/* This is the source content for AccountingTests.cpp */"

# Save the content to the .cpp file
save_text_to_file(f"/home/wilsonb/dl/github.com/BruceRayWilson/Accounting/{className}Tests.cpp", cppContent)