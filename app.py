import streamlit as st

# Page Configuration
st.set_page_config(page_title="Rizal Lens: 19th Century Forces", layout="wide", page_icon="👁️")

# Main Header
st.title("👁️ Rizal Lens: The 19th Century Web of Causality")
st.markdown("An interactive exploration of the macro-events, ideologies, and local struggles that shaped the life, works, and eventual martyrdom of Jose Rizal.")

# Sidebar Selector
st.sidebar.header("Select a Historical Lens")
lens = st.sidebar.radio(
    "Choose a perspective to explore:",
    [
        "Childhood & Early Life",
        "Economic Lens", 
        "Political & Religious Lens", 
        "Cultural & Educational Lens",
        "Nationalism & The Final Break"
    ]
)

# ---------------------------------------------------------
# LENS 1: Childhood & Early Life
# ---------------------------------------------------------
if lens == "Childhood & Early Life":
    st.header("🌱 Childhood and Formative Years")
    st.write("Jose Rizal was born on June 19, 1861, in Calamba, Laguna. His early environment heavily influenced his lifelong pursuit of knowledge and justice.")
    
    st.subheader("Early Precociousness")
    st.write("Raised by his father, Francisco Mercado, and his mother, Teodora Alonso, Rizal showed immense intellectual capacity at a very young age. He learned the alphabet by age three and wrote his first poem by age five.")
    
    st.subheader("The Inquilino Class")
    st.write("Rizal's family belonged to the *principalia* and functioned as *inquilinos* (leaseholders) on a massive friar estate in Calamba. This upper-middle-class standing provided him the means to pursue an elite education, but it also placed his family at the direct mercy of the Dominican friars who owned the land—a dynamic that would drastically alter his life's trajectory.")

# ---------------------------------------------------------
# LENS 2: Economic Lens
# ---------------------------------------------------------
elif lens == "Economic Lens":
    st.header("💰 The Economic Lens: Agrarian Relations and Trade")
    
    st.subheader("Global Trade and the Rise of the Middle Class")
    st.write("The opening of the 103-mile-long Suez Canal connected the Mediterranean to global trade routes, facilitating an influx of progressive ideas and giving rise to a new middle class of Mestizos and Ilustrados in the Philippines.")
    
    st.subheader("The Friar Lands and Hacienda de Calamba")
    st.write("The friar estates originated from Spanish land grants, but because early Spanish colonizers were unable or unwilling to exploit the lands, religious orders eventually acquired them through donations, purchases, and assumed mortgages.")
    
    with st.expander("Explore the Calamba Sugar Economy"):
        st.write("""
        * The Hacienda de Calamba was an enclaved economy managed by a corporate religious entity.
        * The Rizal family was one of the largest leaseholders (*inquilinos*), renting approximately 382 hectares of sugar land and 9.8 hectares of rice land.
        * Rent for these sugar lands was systematically increased; it doubled from 15 pesos in the 1840s to 30 pesos by the end of the century.
        * In 1886 and 1887, if annual rent could not be paid due to agricultural crises or rinderpest epidemics, the friar administration doubled the rent for the following year.
        """)

# ---------------------------------------------------------
# LENS 3: Political & Religious Lens
# ---------------------------------------------------------
elif lens == "Political & Religious Lens":
    st.header("⚖️ The Political & Religious Lens: Power and Oppression")
    
    st.subheader("The Frailocracy and Instability")
    st.write("The 19th-century Philippines was defined by the union of Church and State, resulting in the rule of the friars, or 'Frailocracy'. This was compounded by highly unstable and corrupt colonial administrations led by figures like Rafael Izquierdo and Valeriano Weyler.")
    
    st.subheader("The Martyrdom of GOMBURZA")
    st.write("The Cavite Mutiny led to the tragic execution of three secular priests: Mariano Gomez, Jose Burgos, and Jacinto Zamora (GOMBURZA). This injustice served as a major catalyst for the growth of Philippine nationalism.")

    with st.expander("The Calamba Evictions and Deportations"):
        st.write("""
        * Governor-General Valeriano Weyler threw the full weight of his military prestige behind the Dominicans to crush the agrarian resistance in Calamba.
        * Under Weyler's orders, some 400 tenants were evicted, their houses were dismantled or burned, and 25 individuals—including Rizal's 78-year-old father—were deported to Jolo.
        * This extreme brutality shattered any remaining illusions Rizal had about obtaining justice from the Spanish courts.
        """)

# ---------------------------------------------------------
# LENS 4: Cultural & Educational Lens
# ---------------------------------------------------------
elif lens == "Cultural & Educational Lens":
    st.header("🌴 The Cultural Lens: Romancing Tropicality")
    
    st.subheader("Reversing the Imperial Narrative")
    st.write("Spanish conservatives like Casimiro Herrero argued that the heat of the Torrid Zone caused enervated spirits, lethargy, and a 'lamentable predisposition' to indolence among the natives. In response, Ilustrados in Europe actively romanticized the tropical climate to reverse this racial prejudice.")
    
    st.subheader("The 1884 Brindis Speech")
    st.write("During his famous toast to painters Juan Luna and Felix Resurrección Hidalgo, Rizal argued that the spectacular and terrible phenomena of tropical nature served as the generative fount of their creative genius.")
    
    with st.expander("The Demon of Comparisons & Native Indolence"):
        st.write("""
        * When Rizal returned to the Philippines in 1887, he suffered under the intense heat and encountered the 'demon of comparisons,' which altered his idealized view of the tropics.
        * In his essay *Sobre la indolencia de los filipinos*, Rizal conceded that the tropical climate naturally encourages rest and inactivity.
        * However, he powerfully argued that the true cause of the Filipinos' exaggerated indolence was the disastrous misgovernance, backwardness, and exploitation inflicted by the Spanish colonial state, which robbed the natives of any incentive to work.
        """)

# ---------------------------------------------------------
# LENS 5: Nationalism & The Final Break
# ---------------------------------------------------------
elif lens == "Nationalism & The Final Break":
    st.header("🇵🇭 Nationalism, Literature, and La Liga Filipina")
    
    st.subheader("Conjuring an Imagined Community")
    st.write("According to Benedict Anderson, a nation is an 'imagined political community' conceived as a deep, horizontal comradeship. Rizal's novels, *Noli Me Tangere* and *El Filibusterismo*, served as master narratives that conjured this knowable Filipino community into existence.")
    
    st.subheader("The Break with Del Pilar")
    st.write("Rizal eventually clashed with Marcelo H. del Pilar because Rizal realized that political campaigns in Spain (such as through *La Solidaridad*) were a waste of time. He believed that the medicine must be brought near the sick man, and the true field of battle was the Philippines itself.")
    
    with st.expander("The Founding of La Liga Filipina"):
        st.write("""
        * Disillusioned with the Madrid campaign, Rizal returned to Manila in 1892 to organize *La Liga Filipina*.
        * The secret society's primary goal was the unification of the whole Archipelago into a compact, vigorous, and homogeneous body.
        * It also aimed to provide mutual protection against violence, stimulate agriculture and business, and foster the education needed to eventually sustain a mature nation.
        """)

# Footer
st.markdown("---")
st.caption("Project: Rizal Lens | RZL110_A28 | Developed by Julian David T. Mercado | Promoting an understanding of the 19th-century web of causality.")