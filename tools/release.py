import zipfile
import json
import os

with open("info.json") as info:
    j = json.load(info)

v = j["version"]
v_number = 0

for c in v:
    if c != '.':
        v_number *= 10
        v_number += (ord(c) - ord('0'))

v_number += 1

v_str = str(v_number)
v_str = v_str[:-2] + '.' + v_str[-2] + '.' + v_str[-1]
j["version"] = v_str

with open("info.json", "w") as info:
    json.dump(j, info, indent='\t')

zip_name = "./Release/ModLanguagePack_" + v_str + ".zip"

with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk("."):
        for file in files:
            written = os.path.join(root, file)
            if written not in [zip_name, "./README.md"] and not written.startswith(("./Release", "./tools", "./.git", "./.vscode")):
                zipf.write(os.path.join(root, file), os.path.join(root, file))