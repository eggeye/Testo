import streamlit as st
import pandas as pd
from streamlit_elements import elements, mui

# Skapa exempeldata
data = {
    "ID": [1, 2, 3, 4, 5],
    "Namn": ["Anna", "Björn", "Carla", "David", "Ella"],
}
df = pd.DataFrame(data)

# Initiera klickstatus i session state
if "clicked_cells" not in st.session_state:
    st.session_state.clicked_cells = set()

# Klickhanterare
def handle_click(event):
    # Få rad och kolumn från händelsen
    row = int(event["row"])
    col = int(event["col"])
    cell_key = (row, col)

    if cell_key in st.session_state.clicked_cells:
        st.session_state.clicked_cells.remove(cell_key)
    else:
        st.session_state.clicked_cells.add(cell_key)

# Visa tabellen med interaktiva celler
with elements("interactive_table"):
    with mui.TableContainer():
        with mui.Table():
            with mui.TableBody():
                for i, row in df.iterrows():
                    with mui.TableRow():
                        for j, value in enumerate(row):
                            cell_key = (i, j)
                            is_clicked = cell_key in st.session_state.clicked_cells
                            bgcolor = "lightgreen" if is_clicked else "white"
                            mui.TableCell(
                                value,
                                sx={"backgroundColor": bgcolor, "cursor": "pointer"},
                                onClick={"row": i, "col": j},
                                key=f"cell-{i}-{j}"
                            )

# Registrera klickhändelser
elements.call_event("handle_click", handle_click)

# Visa klickade celler
st.write("Klickade celler:", st.session_state.clicked_cells)
