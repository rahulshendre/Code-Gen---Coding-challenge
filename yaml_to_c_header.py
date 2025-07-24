import yaml

# Read the YAML file, while testing, you should change the file name here
with open("and.yaml", "r") as f:
    data = yaml.safe_load(f)

#this will convert a Python value to a C literal
def c_literal(val):
    if isinstance(val, bool):
        return "true" if val else "false"
    if isinstance(val, int):
        return str(val)
    if isinstance(val, str):
        return f'"{val}"'
    return "NULL"

# Generates C header content
header = []
header.append("// Auto-generated from and.yaml")
header.append("#ifndef AND_INST_H")
header.append("#define AND_INST_H")
header.append("#include <stdbool.h>")

# Top-level fields as macros or consts
for key, value in data.items():
    if isinstance(value, (str, int, bool)):
        if key not in ["operation()", "sail()"]:
            header.append(f'#define AND_{key.upper()} {c_literal(value)}')

# Struct for encoding variables
encoding = data.get("encoding", {})
variables = encoding.get("variables", [])
header.append("\n// Encoding variables")
header.append("typedef struct {")
header.append("    const char* name;")
header.append("    const char* location;")
header.append("} encoding_var_t;")
header.append(f"static const encoding_var_t and_encoding_vars[{len(variables)}] = {{")
for var in variables:
    header.append(f'    {{"{var["name"]}", "{var["location"]}"}},')
header.append("};")

# Access fields
access = data.get("access", {})
header.append("\n// Access fields")
header.append("typedef struct {")
for k in access:
    header.append(f"    const char* {k};")
header.append("} access_t;")
header.append("static const access_t and_access = {")
for k, v in access.items():
    header.append(f'    .{k} = "{v}",')
header.append("};")

# Add operation and sail as strings
for field in ["operation()", "sail()"]:
    if field in data:
        c_name = field.replace("()", "")
        val = data[field].replace('"', '\"').replace("\n", "\\n").replace("\r", "")
        val = val.replace("\n", "\\n")  # Ensure all newlines are escaped
        header.append(f'static const char* and_{c_name} = "{val}";')

header.append("#endif // AND_INST_H")

# Write to header file
with open("and_inst.h", "w") as f:
    f.write("\n".join(header))

print("C header file 'and_inst.h' generated successfully.")