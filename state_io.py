from datetime import datetime
import json
import streamlit as st

def save_checkpoint(state_data_dictionary,file_name="settings.json",streamlit_object=st):
    # Convert a dictionary into a json file
    data_to_save = state_data_dictionary.copy()
    for i in state_data_dictionary.keys():
        if "date" in str.lower(i):
            data_to_save[i] = str(data_to_save[i])
    if isinstance(data_to_save.get("start_date"), datetime):
        data_to_save["start_date"] = str(data_to_save["start_date"])
    with open(file_name,"w") as writer:
        json_string = json.dumps(data_to_save,indent=4)
        writer.write(json_string)
    return json_string

def load_file_content(file_uploader_object, streamlit_object=st, is_rerun=False):
    if file_uploader_object is None : 
        st.toast("No file is uploaded...")
        return
    jsondata = json.loads(file_uploader_object.getvalue().decode("utf-8"))
    if isinstance(jsondata, dict):
        # check if it's proper dictionary and then load and convert available dates
        for i in jsondata.keys():
            if "date" in str.lower(i):
                jsondata[i] =datetime.strptime(jsondata[i], "%Y-%m-%d").date()
        # after date convetion continue with regular data pushing to state
        for key, val in jsondata.items():
            st.session_state[key] = val
        streamlit_object.toast(f"💡 Loaded {len(jsondata.keys())} Settings !")
        if is_rerun: streamlit_object.rerun()
