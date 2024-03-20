import streamlit as st
import pandas as pd
import streamlit as st
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

cdir = Path.cwd().resolve()

mod_path = (Path(__file__).parent).resolve()

data = pd.read_excel(mod_path / 'data_set.xlsx')
total_costs = data.groupby('Subsystem')['Total Cost'].sum()

# Create a pie chart
fig, ax = plt.subplots()
pie1 = ax.pie(total_costs, labels=total_costs.index, autopct='%1.1f%%')
ax.set_title('Subsystem Cost Distribution')

# Add interactivity on mouse hover
def hover(event):
    if event.inaxes == ax:
        for wedge in pie1:
            wedge.set_alpha(0.5)
        wedge = pie1[event.ind[0]]  # Update the assignment here
        wedge.set_alpha(1)
        fig.canvas.draw_idle()

fig.canvas.mpl_connect('motion_notify_event', hover)

# Display the plot using st.pyplot()
# Create a widget to accept user input for editing the data_set.xlsx file
line_number = len(data) + 1

area_of_commodity = st.text_input(f"Area of Commodity (Line {line_number})")
assm_part = st.text_input(f"Assm / Part # (Line {line_number})")
assembly_component = st.text_input(f"Assembly Component (Line {line_number})")
description = st.text_input(f"Description (Line {line_number})")
unit_cost = st.number_input(f"Unit Cost (Line {line_number})")
qty = st.number_input(f"QTY (Line {line_number})")
material_cost = st.number_input(f"Material Cost (Line {line_number})")
process_cost = st.number_input(f"Process Cost (Line {line_number})")
fastener_cost = st.number_input(f"Fastener Cost (Line {line_number})")
tooling_cost = st.number_input(f"Tooling Cost (Line {line_number})")
total_cost = st.number_input(f"Total Cost (Line {line_number})")
details = st.text_input(f"Details (Line {line_number})")

# Create a new row with the user input
new_row = {
    'Area of Commodity': area_of_commodity,
    'Assm / Part #': assm_part,
    'Assembly Component': assembly_component,
    'Description': description,
    'Unit Cost': unit_cost,
    'QTY': qty,
    'MaterialCost': material_cost,
    'Process Cost': process_cost,
    'Fastener Cost': fastener_cost,
    'Tooling Cost': tooling_cost,
    'Total Cost': total_cost,
    'Details': details
}

# Append the new row to the dataset
data = data.append(new_row, ignore_index=True)

# Save the updated dataset to the data_set.xlsx file
data.to_excel(mod_path / 'data_set.xlsx', index=False)

# Display a success message
st.success("Data updated successfully!")
if st.button("Edit Data"):
    # Create input fields for each column in the dataset
    area_of_commodity = st.text_input("Area of Commodity")
    assm_part = st.text_input("Assm / Part #")
    assembly_component = st.text_input("Assembly Component")
    description = st.text_input("Description")
    unit_cost = st.number_input("Unit Cost")
    qty = st.number_input("QTY")
    material_cost = st.number_input("Material Cost")
    process_cost = st.number_input("Process Cost")
    fastener_cost = st.number_input("Fastener Cost")
    tooling_cost = st.number_input("Tooling Cost")
    total_cost = st.number_input("Total Cost")
    details = st.text_input("Details")

    # Create a new row with the user input
    new_row = {
        'Area of Commodity': area_of_commodity,
        'Assm / Part #': assm_part,
        'Assembly Component': assembly_component,
        'Description': description,
        'Unit Cost': unit_cost,
        'QTY': qty,
        'MaterialCost': material_cost,
        'Process Cost': process_cost,
        'Fastener Cost': fastener_cost,
        'Tooling Cost': tooling_cost,
        'Total Cost': total_cost,
        'Details': details
    }

    # Append the new row to the dataset
    data = data.append(new_row, ignore_index=True)

    # Save the updated dataset to the data_set.xlsx file
    data.to_excel(mod_path / 'data_set.xlsx', index=False)

    # Display a success message
    st.success("Data updated successfully!")

# Create buttons for each Subsystem
for subsystem in total_costs.index:
    if st.button(subsystem):
        if st.session_state.get(subsystem):
            st.session_state[subsystem] = False
        else:
            st.session_state[subsystem] = True
        st.write(data[data['Subsystem'] == subsystem].drop('Subsystem', axis=1) if st.session_state[subsystem] else None)
