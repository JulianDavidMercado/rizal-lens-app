import streamlit as st

# Page Configuration
st.set_page_config(page_title="Rizal Lens", layout="wide")

# Main Header
st.title("👁️ Rizal Lens: 19th Century Forces")
st.write("An interactive exploration of the historical forces that shaped the life and work of Jose Rizal.")

# Sidebar Selector
st.sidebar.header("Select a Lens")
lens = st.sidebar.radio(
    "Choose a perspective to explore:",
    ["Economic Lens", "Religious Lens", "Educational Lens"]
)

# Dashboard Content based on selection
if lens == "Economic Lens":
    st.header("The Economic Lens")
    
    st.subheader("The Suez Canal & Global Trade")
    st.write("The opening of the Suez Canal in 1869 drastically shortened the travel time between the Philippines and Spain. This led to an influx of progressive ideas, global revolutions penetrating the Philippine landscape, and a boom in agricultural exports.")
    
    st.subheader("Rise of the Chinese Mestizos")
    st.write("The economic boom gave rise to a new middle class, the *inquilinos* (which included the Rizal family). They leased large estates but faced eventual agrarian disputes in areas like Calamba as the economy shifted.")

elif lens == "Religious Lens":
    st.header("The Religious Lens")
    
    st.subheader("The Frailocracy")
    st.write("The Spanish friars held immense political and economic power. Their grip on the lands cascaded down to the raising of rents in the Hacienda de Calamba, severely impacting the Rizal family and further pushing Rizal toward his 'secret mission.'")
    
    st.subheader("Martyrdom of GOMBURZA")
    st.write("The execution of priests Gomez, Burgos, and Zamora in 1872 was a devastating display of colonial power. It awakened the national consciousness and deeply influenced a young Jose Rizal to fight against injustices.")

elif lens == "Educational Lens":
    st.header("The Educational Lens")
    
    st.subheader("The Ilustrados & Intellectual Hustle")
    st.write("Access to higher education allowed young Filipinos to become *Ilustrados*. This period saw high-speed modernization where these students used their intellectual 'hustle' for the progress of the nation.")
    
    st.subheader("La Solidaridad")
    st.write("Through publications like *La Solidaridad*, the Ilustrados pushed for reforms. They proved that the 19th century was not an era devoid of opportunities, but a time of significant social awakening and global shifts.")

# Footer
st.markdown("---")
st.caption("Project: Rizal Lens | RZL110_A28 | Developed to transpose studies about the hero into an interactive performance.")