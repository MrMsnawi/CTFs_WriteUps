#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stdbool.h>

bool next_permutation(int *array, int n);

// Function to check if a file has expected file signature/magic bytes
bool is_valid_file(const char* data, long size) {
    // Add your file signature checks here
    // For example, for PNG: 89 50 4E 47
    // For JPEG: FF D8 FF
    // This is just a basic example
    return data[0] == 0x89 && data[1] == 0x50;  // PNG check
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <shredded_file> <n>\n", argv[0]);
        return 1;
    }

    const char *filename = argv[1];
    const int n = atoi(argv[2]);

    if (n > 50) {
        fprintf(stderr, "Invalid number of chunks\n");
        return 1;
    }

    // Open shredded file
    FILE *file = fopen(filename, "rb");
    if (!file) {
        fprintf(stderr, "Cannot open file\n");
        return 1;
    }

    // Get file size
    fseek(file, 0, SEEK_END);
    long filesize = ftell(file);
    fseek(file, 0, SEEK_SET);

    // Calculate chunk size
    long chunk_size = (filesize + n - 1) / n;

    // Allocate memory for chunks
    char **chunks = calloc(n, sizeof(char *));
    for (int i = 0; i < n; i++) {
        chunks[i] = calloc(chunk_size, 1);
        fread(chunks[i], 1, chunk_size, file);
    }
    fclose(file);

    // Create array for permutation
    int *indices = calloc(n, sizeof(int));
    int *best_indices = calloc(n, sizeof(int));
    
    // Try all possible permutations until we find a valid file
    bool found = false;
    char *test_buffer = calloc(filesize, 1);
    
    // Start with identity permutation
    for (int i = 0; i < n; i++) {
        indices[i] = i;
    }

    // Try different permutations
    do {
        // Combine chunks according to current permutation
        for (int i = 0; i < n; i++) {
            memcpy(test_buffer + (i * chunk_size), 
                   chunks[indices[i]], 
                   chunk_size);
        }

        // Check if this combination creates a valid file
        if (is_valid_file(test_buffer, filesize)) {
            // Save the successful permutation
            memcpy(best_indices, indices, n * sizeof(int));
            found = true;
            break;
        }
    } while (next_permutation(indices, n));  // Generate next permutation

    if (found) {
        // Create output filename by removing .shredded extension
        char *output_filename = strdup(filename);
        char *dot = strrchr(output_filename, '.');
        if (dot) *dot = '\0';
        strcat(output_filename, ".recovered");

        // Write recovered file
        FILE *outfile = fopen(output_filename, "wb");
        for (int i = 0; i < n; i++) {
            fwrite(chunks[best_indices[i]], 1, chunk_size, outfile);
        }
        fclose(outfile);
        printf("File recovered as %s\n", output_filename);
        free(output_filename);
    } else {
        printf("Could not recover the file\n");
    }

    // Cleanup
    for (int i = 0; i < n; i++) {
        free(chunks[i]);
    }
    free(chunks);
    free(indices);
    free(best_indices);
    free(test_buffer);

    return found ? 0 : 1;
}

// Helper function to generate next permutation
bool next_permutation(int *array, int n) {
    int i = n - 2;
    while (i >= 0 && array[i] >= array[i + 1]) {
        i--;
    }
    if (i < 0) return false;

    int j = n - 1;
    while (array[j] <= array[i]) {
        j--;
    }

    int temp = array[i];
    array[i] = array[j];
    array[j] = temp;

    for (int l = i + 1, r = n - 1; l < r; l++, r--) {
        temp = array[l];
        array[l] = array[r];
        array[r] = temp;
    }

    return true;
}