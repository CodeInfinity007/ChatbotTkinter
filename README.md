
# Chatbot Application using Tkinter

This project is a **Chatbot Application** built using **Tkinter** for the user interface. It provides various functionalities such as encrypting and decrypting user credentials, collecting user feedback, automating tasks by opening applications, and listing all installed software for easy access.

----------

## Features

-   **Credential Privacy:**
    -   Securely store user credentials in `credentials.txt`.
    -   Encrypt and decrypt credentials for privacy.
-   **Feedback Option:**
    -   Collect and save user feedback for further improvements.
-   **Task Automation:**
    -   Open commonly used applications directly from the chatbot interface.
-   **Software Discovery:**
    -   Detect and list all installed software on the device.
    -   Allow users to open any software from the chatbot.

----------

## Installation

1.  Clone this repository:
    
    ```bash
    git clone https://github.com/CodeInfinity007/ChatbotTkinter.git
    cd ChatbotTkinter
    
    ```
    
2.  Create and activate a virtual environment (optional but recommended):
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    
    ```
    
3.  Install the required dependencies:
    
    ```bash
    pip install -r requirements.txt
    
    ```
    

----------

## Usage

1.  Run the chatbot application:
    
    ```bash
    python main.py
    
    ```
    
2.  Use the interface to:
    -   Encrypt and save your credentials.
    -   Provide feedback.
    -   Open applications.
    -   View and access installed software.

----------

## Security

-   The `credentials.txt` file has been removed due to privacy concerns.
-   Ensure that any sensitive data is encrypted before storing.
-   Example encryption methods include AES (part of the `cryptography` package).

----------

## Feedback

User feedback is stored in `feedback.txt` and mailed to me automatically.

----------

## Future Improvements

-   Enhance task automation with voice commands.
-   Add cloud-based storage for credentials.
-   Implement advanced NLP for more dynamic chatbot responses.

