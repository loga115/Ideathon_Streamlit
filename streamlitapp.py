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
st.pyplot(fig)

# Create buttons for each Subsystem
for subsystem in total_costs.index:
    if st.button(subsystem):
        # Perform some action when the button is clicked
        # You can add your code here
        st.write(data[data['Subsystem'] == subsystem].drop('Subsystem', axis=1))