# Streamlit State Manager
A modern, Material Design-inspired Streamlit dashboard for project configuration. This application demonstrates advanced Session State management, including the ability to save progress to a local JSON file and reload settings dynamically.

# 📦 Project Structure
app.py: The main Streamlit entry point featuring a flattened, high-performance UI layout.
state_io.py: A utility module handling the serialization and deserialization of the application state as a json string dump.

# 📂 Logic Overview: state_io.py
The state_io module acts as the data persistence layer for the application.

save_checkpoint()
Converts the current st.session_state into a JSON-serializable format.

Date Handling: Automatically detects keys containing "date" and converts datetime objects into strings to prevent JSON serialization errors.

Export: Returns a formatted JSON string ready for the st.download_button.

load_file_content()
Restores the application state from a user-uploaded file.

Validation: Checks if a file is present and decodes the UTF-8 byte stream into a Python dictionary.

Date Reconstruction: Scans for "date" keys and converts string values back into proper datetime.date objects for Streamlit widgets.

State Injection: Dynamically updates st.session_state with the loaded values and provides a visual toast notification upon success.
