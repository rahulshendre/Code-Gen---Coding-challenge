Code Gen: From UDB to Implementations - Coding Challenge

Write a Python program that reads at least one of the YAML files in the RISC-V Unified Database project (https://github.com/riscv-software-src/riscv-unified-db) under spec/std/isa/inst.
Same Python program then emits the data in the YAML file as a C header file, format of your choosing.
Write a C program that includes the C header file generated in step 2.
Same C program should emit the contents of the C header file in YAML. The YAML file does NOT need to match the original YAML file.
Repeat steps 1-4 using the generated YAML file as input. The emitted YAML file should match the generated YAML file this time.



**Explaining the task in my words (hopefully I don't mess it up):**

- Taking the example YAML file as `and.yaml`, but it can be anything.
- Creating a Python script which converts the YAML file (which we downloaded from the path given) to a C header file.
- When this is done, we use the C program (`emit_and_yaml.c`) to convert the header file into a YAML file, which will be named as `and_yaml`.
- Now this shows that the Python program gives a header file and the C program gives out a YAML file from the header file.

**We do a test now:**

- Changing the name of the `and_yaml` to `and2.yaml`, or any name.
- Deleting the `and_inst.h`, the header file, so that we know that it is a fresh and a new one for the test.
- After this, we give the `and2.yaml` as input to the Python script and we generate a new header file. This header file is used to generate a new YAML file by using the C program.
- Now we can verify the content of the `and2.yaml` and `and_yaml`, the new file which just got generated. They are the same.
- Concluding that our test is correct.

---

## How to Run

1. **Place your YAML file** (e.g., `and.yaml`) in the same directory as the scripts.
2. **Run the Python script** to generate the C header file:
   ```sh
   python yaml_to_c_header.py
   ```
3. **Compile the C program**:
   ```sh
   gcc emit_and_yaml.c -o emit_and_yaml
   ```
4. **Run the C program to emit YAML**:
   ```sh
   ./emit_and_yaml > and_out.yaml
   ```
5. **(Round-Trip Test)**:
   - Rename or copy `and_out.yaml` to `and2.yaml`.
   - Delete `and_inst.h` to start fresh.
   - Edit the Python script to read from `and2.yaml` instead of `and.yaml`.
   - Repeat steps 2–4.
   - Compare the contents of `and2.yaml` and the new output YAML—they should be the same.



**A step by step handwritten flow (excuse me for the handwriting):**
![WhatsApp Image 2025-07-24 at 13 35 03_f250a09a](https://github.com/user-attachments/assets/6785c0db-d135-415d-8a7f-c8f060934482)
