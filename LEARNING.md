# LEARNING.md

## Project Overview
**Huffman Cipher** is a hybrid cryptographic and compression system developed in Python. It integrates **Huffman Coding** for lossless data compression with the **RSA (Rivest–Shamir–Adleman)** algorithm for public-key encryption. The system demonstrates a "Compress-then-Encrypt" architecture, where a message is first compressed to reduce its size and entropy, and then encrypted to ensure confidentiality. It also includes a module for calculating information-theoretic metrics like entropy and redundancy.

## Tech Stack and Key Technologies
*   **Language:** Python 3
*   **Core Concepts:**
    *   **Cryptography:** RSA (Public/Private key generation, Modular Arithmetic).
    *   **Data Compression:** Huffman Coding (Binary Trees, Priority Queues).
    *   **Information Theory:** Entropy, Redundancy calculation.
    *   **Algorithms:** Extended Euclidean Algorithm, Modular Exponentiation (Square-and-Multiply).

## Notable Libraries
The project relies almost entirely on Python's standard library, showcasing the ability to implement complex algorithms from first principles.
*   **`collections.defaultdict`**: Used for efficient frequency counting of characters in the corpus.
*   **`math.log`**: Utilized for calculating the Shannon entropy of the source text.
*   **`sys`**: Used for system-level operations (though usage is minimal).

*Note: The project implements its own Priority Queue (`PQ` class) and Graph structures (`HuffmanTree`, `Vertices`, `Arista`) instead of using pre-built libraries like `heapq` or `networkx`.*

## Major Achievements and Skills Demonstrated
*   **Full RSA Implementation**: Designed the complete RSA workflow from scratch, including:
    *   Key generation (deriving $n, e, d$ from primes $p, q$).
    *   Implementation of the **Extended Euclidean Algorithm** to find the modular multiplicative inverse for the private key.
    *   **Modular Exponentiation**: Implemented an efficient "square-and-multiply" algorithm (visible in `FastExp.py` and `HuffmanCipher.py`) to handle large number powers required by RSA.
*   **Custom Huffman Compression Engine**:
    *   Built a custom **Priority Queue** and **Binary Tree** structure to generate Huffman codes.
    *   Implemented serialization of compressed bitstreams into blocks for RSA encryption.
    *   Developed a frequency analysis tool to train the Huffman tree on a corpus (`LongText.txt`).
*   **Hybrid System Architecture**: Successfully integrated two distinct algorithms (compression and encryption) into a seamless pipeline (`HuffmanCipher.py`), handling the conversion between binary strings, integers, and ciphertext.
*   **Information Theory Analysis**: Implemented functionality to calculate and report the **Entropy** (bits/letter), **Absolute Range**, and **Redundancy** of the source text, demonstrating a theoretical understanding of data compression limits.

## Skills Gained/Reinforced
*   **Algorithm Design & Analysis**: Deepened understanding of greedy algorithms (Huffman) and number-theoretic algorithms (RSA).
*   **Low-Level Data Manipulation**: Experience with bit-level operations, binary string manipulation, and block padding schemes.
*   **Object-Oriented Programming (OOP)**: Designed modular classes (`HuffmanTree`, `Arista`, `Vertices`, `PQ`) to encapsulate logic and state.
*   **Secure Coding Practices**: Understanding the mathematical foundations of public-key cryptography and the importance of key management.
*   **Python Proficiency**: Advanced usage of Python generators (`yield`), dictionary comprehensions, and list manipulations.
