# Huffman Cipher 🔐

![Project Logo](PLACEHOLDER_URL)

[![Language](https://img.shields.io/badge/Language-Python_3-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)](PLACEHOLDER_URL)

**Huffman Cipher** is a hybrid encryption system that combines **Huffman coding** for efficient data compression with the **RSA algorithm** for secure public-key encryption. This project demonstrates a "Compress-then-Encrypt" approach, achieving both storage efficiency and data security in a single workflow.

## 🏛️ Architecture

The system operates in two main phases: **Training** (building the compression model) and **Operation** (Encryption/Decryption).

```mermaid
graph TD
    subgraph "1. Training Phase"
    A[Corpus (LongText.txt)] -->|Frequency Analysis| B(Huffman Tree)
    B --> C{Huffman Codes}
    end

    subgraph "2. Encryption Flow"
    D[Plaintext] -->|Huffman Compress| E[Binary Data]
    E -->|Block & Pad| F[Integer Blocks]
    F -->|RSA Encrypt (M^e mod n)| G[Ciphertext]
    end

    subgraph "3. Decryption Flow"
    G -->|RSA Decrypt (C^d mod n)| H[Integer Blocks]
    H -->|Huffman Decompress| I[Recovered Plaintext]
    end

    C -.-> D
    C -.-> H
```

## ✨ Features

-   **📉 Efficient Compression:** Uses Huffman coding to reduce message size before encryption, based on character frequency analysis.
-   **🔑 RSA Encryption:** Implements the RSA public-key cryptosystem from scratch, including key generation and modular exponentiation.
-   **📊 Information Theory Metrics:** Calculates and displays entropy, absolute range, and redundancy of the training corpus.
-   **🐍 Pure Python:** Built entirely with standard Python libraries, making it an excellent educational resource for understanding cryptographic and compression algorithms.

## 🚀 Getting Started

### Prerequisites

-   **Python 3.x** installed on your system.
-   A text file named `LongText.txt` in the same directory (used as a corpus to train the Huffman tree).

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/adcondev/huffman-cipher.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd huffman-cipher
    ```

### Usage

1.  Run the main script:
    ```bash
    python HuffmanCipher.py
    ```

2.  **Key Generation**: The script will prompt you for prime numbers to generate RSA keys:
    -   `p`: A prime number (e.g., 61)
    -   `q`: Another prime number (e.g., 53)
    -   `e`: Public exponent (usually a small prime like 17 or 65537, must be coprime to `lcm(p-1, q-1)`)

3.  **Encryption**: Enter the message you want to encrypt. The script will output the encrypted integer blocks.

4.  **Decryption**: To decrypt, you will be prompted to enter the private key components (`n`, `e`, `d`) which were generated in the previous step.

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements or find bugs, please open an issue or submit a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
