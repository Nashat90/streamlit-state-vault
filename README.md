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

To use this persistence layer in your main app, follow this pattern:

```python
from state_io import save_checkpoint, load_file_content

# Save current session
current_data = {key: st.session_state[key] for key in defaults.keys()}
json_data = save_checkpoint(current_data)

# Load uploaded session
if st.button(":material/upload: Load Last Save"):
    load_file_content(data_loader, st)


# 💾 Streamlit State Persistence Demo

A modern, high-performance dashboard designed to demonstrate **advanced session state persistence**. This project showcases how to bridge the gap between volatile web sessions and permanent storage using JSON serialization.

---

## 🛠️ State Persistence Layer (`state_io.py`)

The `state_io` module acts as the data persistence layer for the application, bridging the gap between volatile Streamlit sessions and permanent file storage.

### 📥 save_checkpoint()
**Purpose:** Converts the current `st.session_state` into a JSON-serializable format.

* **📅 Date Handling**: Automatically detects keys containing the word "date" and converts `datetime` objects into strings. This prevents the common `TypeError: Object of type datetime is not JSON serializable`.
* **⚙️ Logic**: It creates a shallow copy of the state dictionary to ensure the live application state remains unaffected during serialization.
* **📥 Export**: Returns a beautifully formatted, indented JSON string ready for immediate use in an `st.download_button`.

---

### 📤 load_file_content()
**Purpose:** Restores the application state from a user-uploaded JSON file.

* **✅ Validation**: Checks if a file is present before processing. If no file is detected, it triggers a Streamlit toast notification to alert the user.
* **🔄 Data Decoding**: Decodes the UTF-8 byte stream from the file uploader and parses it into a native Python dictionary.
* **🗓️ Date Reconstruction**: Scans the dictionary for "date" keys and converts string values back into proper `datetime.date` objects. This is critical for ensuring that Streamlit `date_input` widgets recognize the data.
* **📥 State Injection**: Dynamically updates `st.session_state` with the loaded values, allowing the UI to reflect the saved configuration instantly.
* **🎉 Success Feedback**: Provides a visual toast notification to the user upon successful state restoration.

---

## 💻 Module Implementation

To use this persistence layer in your main app, follow this pattern:

```python
from state_io import save_checkpoint, load_file_content

# Save current session
current_data = {key: st.session_state[key] for key in defaults.keys()}
json_data = save_checkpoint(current_data)

# Load uploaded session
if st.button("📂 Load Last Save"):
    load_file_content(data_loader, st)
