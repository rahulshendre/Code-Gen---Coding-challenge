#include <stdio.h>
#include "and_inst.h"

int main() {
    printf("$schema: %s\n", AND_$SCHEMA);
    printf("kind: %s\n", AND_KIND);
    printf("name: %s\n", AND_NAME);
    printf("long_name: %s\n", AND_LONG_NAME);
    printf("description: %s\n", AND_DESCRIPTION);
    printf("definedBy: %s\n", AND_DEFINEDBY);
    printf("assembly: %s\n", AND_ASSEMBLY);

    printf("encoding:\n");
    printf("  variables:\n");
    for (int i = 0; i < 3; ++i) {
        printf("    - name: %s\n", and_encoding_vars[i].name);
        printf("      location: %s\n", and_encoding_vars[i].location);
    }

    printf("access:\n");
    printf("  s: %s\n", and_access.s);
    printf("  u: %s\n", and_access.u);
    printf("  vs: %s\n", and_access.vs);
    printf("  vu: %s\n", and_access.vu);

    printf("data_independent_timing: %s\n", AND_DATA_INDEPENDENT_TIMING ? "true" : "false");
    printf("operation(): %s\n", and_operation);
    printf("sail(): |\n");
    // Print sail string with indentation
    const char* p = and_sail;
    printf("  ");
    while (*p) {
        if (*p == '\n') {
            printf("\n  ");
        } else {
            putchar(*p);
        }
        p++;
    }
    printf("\n");
    return 0;
} 