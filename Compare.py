import streamlit as st

image_url_1 = "/workspaces/20241222/2016-10-28-00_00_2016-10-28-23_59_Sentinel-2_L2A_Scene_classification_map_ (1)_1.jpg"
image_url_2 = "/workspaces/20241222/2024-12-20-00_00_2024-12-20-23_59_Sentinel-2_L2A_Scene_classification_map_ (1).jpg"

col1, col2 = st.columns(2)

with col1:
    st.image(image_url_1, caption="2016",width=600,use_container_width=True)

with col2:
    st.image(image_url_2, caption="2024",width=600,use_container_width=True)