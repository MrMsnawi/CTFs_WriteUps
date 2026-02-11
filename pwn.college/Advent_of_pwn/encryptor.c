#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>

#define XOR_KEY 0x42

void encrypt_buffer(unsigned char *buffer, size_t size) {
    for (size_t i = 0; i < size; i++) {
        buffer[i] ^= XOR_KEY;
    }
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <executable>\n", argv[0]);
        return 1;
    }

    // Open the executable file
    FILE *input = fopen(argv[1], "rb");
    if (!input) {
        perror("fopen");
        return 1;
    }

    // Get file size
    struct stat st;
    if (stat(argv[1], &st) != 0) {
        perror("stat");
        fclose(input);
        return 1;
    }
    size_t file_size = st.st_size;

    // Read the entire file
    unsigned char *buffer = malloc(file_size);
    if (!buffer) {
        perror("malloc");
        fclose(input);
        return 1;
    }

    if (fread(buffer, 1, file_size, input) != file_size) {
        fprintf(stderr, "Failed to read file\n");
        free(buffer);
        fclose(input);
        return 1;
    }
    fclose(input);

    // Encrypt the buffer
    encrypt_buffer(buffer, file_size);

    // Generate the loader program
    FILE *output = fopen("encrypted_loader.c", "w");
    if (!output) {
        perror("fopen output");
        free(buffer);
        return 1;
    }

    fprintf(output, "#include <stdio.h>\n");
    fprintf(output, "#include <stdlib.h>\n");
    fprintf(output, "#include <string.h>\n");
    fprintf(output, "#include <unistd.h>\n");
    fprintf(output, "#include <sys/stat.h>\n\n");
    fprintf(output, "#define XOR_KEY 0x42\n");
    fprintf(output, "#define DATA_SIZE %zu\n\n", file_size);

    // Write encrypted data
    fprintf(output, "unsigned char encrypted_data[DATA_SIZE] = {\n    ");
    for (size_t i = 0; i < file_size; i++) {
        fprintf(output, "0x%02x", buffer[i]);
        if (i < file_size - 1) {
            fprintf(output, ", ");
            if ((i + 1) % 12 == 0) {
                fprintf(output, "\n    ");
            }
        }
    }
    fprintf(output, "\n};\n\n");

    // Write decryption and execution code
    fprintf(output, "void decrypt_buffer(unsigned char *buffer, size_t size) {\n");
    fprintf(output, "    for (size_t i = 0; i < size; i++) {\n");
    fprintf(output, "        buffer[i] ^= XOR_KEY;\n");
    fprintf(output, "    }\n");
    fprintf(output, "}\n\n");

    fprintf(output, "int main(int argc, char *argv[], char *envp[]) {\n");
    fprintf(output, "    // Decrypt the data\n");
    fprintf(output, "    decrypt_buffer(encrypted_data, DATA_SIZE);\n\n");

    fprintf(output, "    // Write decrypted binary to temp file\n");
    fprintf(output, "    const char *temp_path = \"/tmp/decrypted_binary\";\n");
    fprintf(output, "    FILE *f = fopen(temp_path, \"wb\");\n");
    fprintf(output, "    if (!f) {\n");
    fprintf(output, "        perror(\"fopen\");\n");
    fprintf(output, "        return 1;\n");
    fprintf(output, "    }\n\n");

    fprintf(output, "    if (fwrite(encrypted_data, 1, DATA_SIZE, f) != DATA_SIZE) {\n");
    fprintf(output, "        fprintf(stderr, \"Failed to write decrypted binary\\n\");\n");
    fprintf(output, "        fclose(f);\n");
    fprintf(output, "        return 1;\n");
    fprintf(output, "    }\n");
    fprintf(output, "    fclose(f);\n\n");

    fprintf(output, "    // Make it executable\n");
    fprintf(output, "    chmod(temp_path, 0755);\n\n");

    fprintf(output, "    // Execute it\n");
    fprintf(output, "    char *exec_argv[] = {(char *)temp_path, NULL};\n");
    fprintf(output, "    execve(temp_path, exec_argv, envp);\n\n");

    fprintf(output, "    // If execve returns, it failed\n");
    fprintf(output, "    perror(\"execve\");\n");
    fprintf(output, "    unlink(temp_path);\n");
    fprintf(output, "    return 1;\n");
    fprintf(output, "}\n");

    fclose(output);
    free(buffer);

    printf("Successfully generated encrypted_loader.c\n");
    printf("Compile with: gcc encrypted_loader.c -o encrypted_loader\n");

    return 0;
}
