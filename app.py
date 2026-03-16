import streamlit as st
from state_io import *
from datetime import datetime

# Step 1: Assign Session State
state = st.session_state

# Step 2: Create default template
defaults = {
    "project_name": "New Project",
    "difficulty": "Medium",
    "tags": ["Research"],
    "is_active": True,
    "start_date": datetime.now().date(),
    "team_size": 1,
    "description": ""
}

# Step 3: Ensure keys exist in state
for key, val in defaults.items():
    if key not in state:
        state[key] = val

# --- HEADER & ACTION BAR ---
st.title(":material/rocket_launch: Project Hub")
st.caption("Manage configurations and track project checkpoints.")

col_up, col_load, col_save = st.columns([2, 1, 1])
data_loader = col_up.file_uploader("Upload settings", label_visibility="collapsed")

if col_load.button(":material/upload_file: Load", use_container_width=True):
    load_file_content(data_loader, st)
    st.rerun() # Force a rerun to update sliders/inputs with loaded data

current_data = {key: state[key] for key in defaults.keys()}
json_data = save_checkpoint(current_data)
col_save.download_button(":material/save: Save", data=json_data, 
 on_click="ignore", use_container_width=True,file_name="proj-da-snapshot.json")

st.divider()

# Using 'key' instead of direct assignment prevents the "snap-back" bug
st.text_input(":material/label: Project Name", key="project_name")

c1, c2 = st.columns(2)
c1.date_input(":material/calendar_today: Start Date", key="start_date")
c2.select_slider(":material/signal_cellular_alt: Difficulty Level", options=["Easy", "Medium", "Hard"], key="difficulty")

st.text_area(":material/description: Project Description", key="description", placeholder="Enter details...")
st.multiselect(":material/style: Project Tags", ["Research", "Development", "Design", "Marketing"], key="tags")

c3, c4 = st.columns(2)
c3.number_input(":material/groups: Team Size", min_value=1, max_value=50, key="team_size")
c4.toggle(":material/bolt: Project is Active", key="is_active")

# --- FOOTER STATUS ---
st.divider()
status_color = "green" if state.is_active else "red"
status_icon = ":material/check_circle:" if state.is_active else ":material/error:"

st.markdown(f"### {status_icon} Status: :{status_color}[{'Active' if state.is_active else 'Inactive'}]")
st.info(f"**Current Project:** {state.project_name} | **Active Members:** {state.team_size}")