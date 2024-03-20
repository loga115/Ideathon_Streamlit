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

