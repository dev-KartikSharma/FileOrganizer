from main import scan_directory, move_files
import streamlit as st
import threading

# UI
st.title("File Organizer 🧹")
st.caption("Built by Kartik ✨ | Powered by Python threads and Streamlit simplicity.")

path = st.text_input("📁 Enter the path to your Downloads folder:", "C:\\Users\\HP\\Downloads")

if st.button("Organize"):
    file_list = scan_directory(path)

    if file_list is None:
        st.error("❌ Directory not found. Please check the path and try again.")
        st.stop()
    elif not file_list:
        st.warning("⚠️ No files found in the specified directory.")
        st.stop()
    else:
        st.success(f"✅ Found {len(file_list)} files to organize.")
        st.text("Starting file classification...")

        # Launching only move thread
        move_thread = threading.Thread(target=move_files, args=(path,))
        move_thread.start()
        move_thread.join()

        st.success("🎯 File organization completed!")