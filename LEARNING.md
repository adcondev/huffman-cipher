# LEARNING.md

## Project Overview

This project implements a hybrid cryptographic system that combines Huffman coding for data compression with the RSA algorithm for encryption. The primary objective is to efficiently and securely encrypt text data by first reducing its size using Huffman coding and then encrypting the compressed data with RSA. This approach leverages the benefits of both compression and public-key cryptography.

## Tech Stack and Key Technologies

*   **Language:** Python
*   **Algorithms:**
    *   RSA (Rivest–Shamir–Adleman) for public-key cryptography.
    *   Huffman Coding for lossless data compression.
    *   Modular Exponentiation (Fast Exponentiation) for efficient RSA calculations.
*   **Core Concepts:**
    *   Public-Key Cryptography
    *   Data Compression
    *   Number Theory (Euclidean Algorithm for GCD, Extended Euclidean Algorithm for modular inverse)

## Notable Libraries

The project is implemented primarily using standard Python libraries, demonstrating a strong understanding of core programming concepts without reliance on external frameworks. The key components are built from scratch, including:

*   **collections.defaultdict:** Used for efficiently counting character frequencies in the Huffman coding implementation.
*   **math.log:** Used to calculate the entropy of the text data.

## Major Achievements and Skills Demonstrated

*   **Implemented the RSA Public-Key Cryptosystem:** Designed and implemented the RSA algorithm from scratch, including key generation (public and private keys), encryption, and decryption.
*   **Applied Huffman Coding for Data Compression:** Developed a Huffman tree implementation to generate variable-length codes for characters based on their frequencies, effectively compressing the input text before encryption.
*   **Developed a Hybrid Encryption System:** Integrated Huffman coding and RSA to create a single, efficient workflow that both compresses and encrypts data.
*   **Implemented Core Cryptographic and Compression Algorithms:** Demonstrated a deep understanding of the underlying principles of both RSA and Huffman coding by implementing them without high-level libraries.
*   **Optimized RSA with Modular Exponentiation:** Utilized the fast exponentiation algorithm to perform the modular exponentiation required for RSA encryption and decryption efficiently.

## Skills Gained/Reinforced

*   **Cryptography:** Gained practical experience in implementing a widely-used public-key cryptosystem (RSA) and understanding its components, including key generation and the encryption/decryption processes.
*   **Data Compression:** Reinforced knowledge of data compression techniques by implementing the Huffman coding algorithm.
*   **Algorithm Implementation:** Demonstrated the ability to translate complex mathematical and algorithmic concepts into functional Python code.
*   **Object-Oriented Programming (OOP):** Applied OOP principles to structure the Huffman tree and related components in a modular and reusable way.
*   **Python Programming:** Enhanced proficiency in Python, including file I/O, data structures, and algorithmic implementation.
