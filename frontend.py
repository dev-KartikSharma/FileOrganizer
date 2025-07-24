from main import scan_directory, move_files
import streamlit as st
import threading, time

# Title
st.title("File organizer 🧹")
# st.title("")

path = st.text_input("📁 Enter the path to your Downloads folder: ", "C:\\Users\\HP\\Downloads")

if st.button("Organize"):
        
    # using threads
    scan_thread = threading.Thread(target=scan_directory, args=(path,))
    move_thread = threading.Thread(target=move_files, args=(path,))

    scan_thread.start()
    st.success(f"🔍 Found files")
    st.text("Starting file classification...")
    time.sleep(3)
    move_thread.start()
    st.success("✅ File organization completed!")

    scan_thread.join()
    move_thread.join()