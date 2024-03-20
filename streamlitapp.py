import streamlit as st
import pandas as pd
import streamlit as st
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from openpyxl import Workbook

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
if st.button("Show Pie Chart"):                 # this is called in Streamlit as a "session state" hack, to preserve the state of buttons and make them act as toggles
    if st.session_state.get("show_chart"):      # and not one-offs
        st.session_state["show_chart"] = False
    else:
        st.session_state["show_chart"] = True
    if st.session_state["show_chart"]:
        st.pyplot(fig)
    else:
        st.empty()

def write_to_xlsx(data):
    wb = Workbook()
    sheet = wb.active
    sheet.append(data)
    wb.save('data_set.xlsx')

def newrow():
    
    st.title("Add New Row")
    line_no = len(data) + 1
    pageno = 1
    subsystem = st.selectbox("Subsystem", data['Subsystem'].unique())
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
    details = st.text_area("Details")

    if st.button("Submit"):
        new_row = [line_no, area_of_commodity, assm_part, assembly_component, description, unit_cost, qty, material_cost, process_cost, fastener_cost, tooling_cost, total_cost, details, pageno, subsystem]
        data.loc[len(data)] = new_row
        write_to_xlsx(data)
        st.success("Data written to data_set.xlsx")
    
    


# Create buttons for each Subsystem
for subsystem in total_costs.index:
    if st.button(subsystem):
        if st.session_state.get(subsystem):
            st.session_state[subsystem] = False     
        else:
            st.session_state[subsystem] = True
        if st.session_state[subsystem]:
            st.write(data[data['Subsystem'] == subsystem].drop('Subsystem', axis=1))
        else:
            st.empty()


newrow()
