import streamlit as st
import numpy as np

st.title("🚌 Multi-Bus Headway Calculator")

st.write("Enter between 2 and 6 bus arrival times in **HH:MM** format:")

times = []
for i in range(6):
    t = st.text_input(f"Bus {i+1} Arrival (HH:MM)", key=f"time_{i}")
    if t:
        try:
            h, m = map(int, t.split(":"))
            minutes = h * 60 + m
            times.append(minutes)
        except:
            st.error(f"Invalid time format for Bus {i+1}. Use HH:MM (e.g. 14:05).")

target = st.number_input("Target Headway (minutes)", min_value=1, value=8)

if len(times) >= 2:
    times.sort()
    headways = [times[i+1] - times[i] for i in range(len(times)-1)]

    st.subheader("📊 Results")
    for i, h in enumerate(headways):
        st.write(f"Headway {i+1} (Bus {i+1} → Bus {i+2}): **{h} minutes**")

    avg = np.mean(headways)
    std_dev = np.std(headways)

    st.write(f"\n**Average Headway:** {avg:.2f} minutes")
    st.write(f"**Standard Deviation (spread):** {std_dev:.2f} minutes")

    if target > 0:
        diff_pct = ((avg - target) / target) * 100
        st.write(f"**Average vs Target:** {diff_pct:.2f}% difference")
else:
    st.info("👉 Please enter at least 2 valid bus times to calculate headways.")
