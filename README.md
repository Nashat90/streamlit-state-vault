# Streamlit State Manager
A modern, Material Design-inspired Streamlit dashboard for project configuration. This application demonstrates advanced Session State management, including the ability to save progress to a local JSON file and reload settings dynamically.

## 📦 Project Structure
**app.py:** The main Streamlit entry point featuring a flattened, high-performance UI layout.
**state_io.py:** A utility module handling the serialization and deserialization of the application state as a json string dump.

## 💻 Getting Started

To run this project locally on your machine, follow these steps:

1. **Download the Repository**: Clone or download this repository to your local drive.
2. **Install Dependencies**: Ensure you have Streamlit installed:
   ```bash
   pip install streamlit

# 💾 Streamlit State Persistence Demo

A modern, high-performance dashboard designed to demonstrate **advanced session state persistence**. This project showcases how to bridge the gap between volatile web sessions and permanent storage using JSON serialization.

---

## 🚀 How to Use the App

Follow these steps to manage your project configurations and utilize the state-saving features:

### 📝 1. Configure Settings
Interact with the UI components (Project Name, Date, Difficulty, etc.) to set your desired values. The application stores these temporarily in the session state as you change them.

### 💾 2. Save Progress
Click the **"Save Progress"** button. This will trigger a download of a file named `proj-da-snapshot.json`. This file contains all your current UI settings in a structured format.

### 📂 3. Prepare for Reload
To get your settings back at a later time (or after refreshing the page), use the file uploader at the top to **drag and drop** your previously saved `.json` file.

### 🔄 4. Load Snapshot
Once the file is uploaded, click the **"Load Last Save"** button. The app will process the file, reconstruct the data types (like dates), and instantly refresh the UI with your saved values.

---

## 🛠️ State Persistence Layer (`state_io.py`)

The `state_io` module acts as the data persistence layer, managing the technical conversion between Streamlit widgets and JSON files.

### 📥 save_checkpoint()
* **📅 Date Handling**: Automatically detects keys containing the word "date" and converts `datetime` objects into strings. This prevents serialization errors.
* **⚙️ Logic**: Creates a shallow copy of the state to ensure the live app remains stable during the export process.
* **📥 Export**: Returns a formatted JSON string ready for the download button.

### 📤 load_file_content()
* **✅ Validation**: Ensures a file is present before attempting to parse. Triggers a toast notification if the uploader is empty.
* **🔄 Data Decoding**: Decodes the UTF-8 byte stream and parses the JSON into a Python dictionary.
* **🗓️ Date Reconstruction**: Converts ISO strings back into native Python `date` objects so widgets remain interactive.
* **🎉 Success Feedback**: Provides a visual toast notification once the data is successfully injected into the UI.

---

## 💻 Implementation Pattern

```python
from state_io import save_checkpoint, load_file_content

# Logic for saving
current_data = {key: st.session_state[key] for key in defaults.keys()}
json_data = save_checkpoint(current_data)

# Logic for loading
if st.button("📂 Load Last Save"):
    load_file_content(data_loader, st)


## 💾 Streamlit State Persistence Demo

A modern, high-performance dashboard designed to demonstrate **advanced session state persistence**. This project showcases how to bridge the gap between volatile web sessions and permanent storage using JSON serialization.
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
