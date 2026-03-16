# :material/sdk: Streamlit State-IO Demo

A modern, high-performance Streamlit dashboard designed to demonstrate **advanced session state persistence**. This project showcases how to bridge the gap between volatile web sessions and permanent storage using JSON serialization.

## :material/visibility: Overview
This repository serves as a technical demonstration of a **"Save & Resume"** workflow. Built with a flattened, non-nested UI architecture and official Google Material Symbols, it provides a sleek user experience while solving common data persistence challenges in Streamlit.

---

## :material/star: Key Features
* **:material/save_as: State Serialization**: Transform the active `st.session_state` into a portable JSON snapshot.
* **:material/restore: Instant Recovery**: Upload a previous save file to instantly reconstruct the UI and data models.
* **:material/calendar_sync: Smart Date Handling**: Automatically handles the conversion of `datetime` objects to and from JSON (a common pain point).
* **:material/bolt: No-Indentation UI**: A flattened code structure using modern Streamlit layout variables for better readability and performance.
* **:material/target: UI Syncing**: Implementation of widget `key` parameters to prevent "snap-back" bugs and state conflicts.

---

## :material/architecture: How the State Saving Works

The demo relies on the `state_io.py` utility module to manage the data lifecycle:

### :material/download: 1. Capturing the Snapshot
The `save_checkpoint()` function captures the current dictionary of user inputs. It performs a "date-check" on all keys; if a key contains the word "date," it converts the Python `datetime` object into a ISO-format string so it can be safely written to a JSON file.

### :material/upload: 2. Restoring the Snapshot
The `load_file_content()` function reads the uploaded bytes, decodes the UTF-8 string, and parses the JSON. Crucially, it reverses the serialization by searching for "date" keys and casting the strings back into native Python `date` objects so the Streamlit `date_input` widgets don't crash.

---

## :material/terminal: Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
