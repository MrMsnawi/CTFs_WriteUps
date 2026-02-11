# AI Agent Instructions for Shredder Project

## Project Overview
This project implements a file shredding system that splits files into chunks and randomly reorders them. The project consists of two main components:
- A shredder program that splits and scrambles files
- A recovery program that attempts to reconstruct shredded files

## Core Components

### Shredder (`shredder.c`)
- Takes input file and number of chunks (n) as arguments
- Splits file into n equal-sized chunks
- Randomly shuffles chunks using time-based seed
- Creates output with `.shredded` extension

Key implementation details:
```c
long chunk_size = (filesize + n - 1) / n;  // Chunk size calculation
```

### File Processing Pattern
The project uses a common C file processing pattern:
1. Calculate file size using seek operations
2. Split into chunks
3. Process chunks in memory
4. Write transformed output

## Development Guidelines

### Build Instructions
```bash
gcc -o shredder shredder.c
gcc -o recover recover.c
```

### Usage
```bash
./shredder <input_file> <n_chunks>  # n_chunks must be ≤ 50
./recover <shredded_file> <n_chunks>
```

### Key Constraints
- Maximum 50 chunks allowed for shredding
- Files are processed in binary mode
- Chunk sizes are calculated to ensure complete file coverage

### Memory Management
The codebase follows these memory patterns:
- Use of `calloc` for zero-initialized memory allocation
- Explicit cleanup of allocated memory
- Proper file handle management with `fclose`

### Error Handling
Critical error checks include:
- Command line argument validation
- File open/close operations
- Memory allocation success

## Testing
Test files by:
1. Creating a known input file
2. Shredding with different chunk sizes
3. Attempting recovery
4. Validating output matches input

## Project Limitations
- Random seed based on time makes exact reproduction difficult
- No built-in file integrity verification
- Limited to file sizes that fit in memory