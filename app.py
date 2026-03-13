import streamlit as st

# ==========================================
# PAGE CONFIGURATION & ADVANCED CSS
# ==========================================
st.set_page_config(page_title="Rizal Lens: The Ultimate 19th Century Dashboard", layout="wide", page_icon="👁️")

st.markdown("""
    <style>
    .main-header { font-size: 3rem; color: #1E3A8A; font-weight: 900; letter-spacing: -1px; }
    .sub-header { font-size: 1.75rem; color: #2563EB; border-bottom: 2px solid #E5E7EB; padding-bottom: 10px; margin-bottom: 20px;}
    .quote-box { border-left: 6px solid #2563EB; background-color: #EFF6FF; padding: 20px; font-size: 1.1rem; font-style: italic; border-radius: 0px 10px 10px 0px; margin: 20px 0; }
    .highlight-text { background-color: #FEF08A; padding: 2px 5px; border-radius: 3px; font-weight: bold; }
    .timeline-date { color: #DC2626; font-weight: bold; font-size: 1.2rem; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR NAVIGATION & PROGRESS
# ==========================================
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Jose_Rizal_full.jpg/800px-Jose_Rizal_full.jpg", width=180)
st.sidebar.title("Rizal Lens Navigation")
st.sidebar.markdown("A comprehensive digital humanities project mapping the life of Jose Rizal against 19th-century macro-events.")

pages = [
    "📊 Executive Dashboard",
    "🌱 Roots & Early Education",
    "💰 The Economic Crucible", 
    "⚖️ Politics & The Frailocracy", 
    "🌴 Romancing Tropicality",
    "🇵🇭 Master Narratives (The Novels)",
    "⚔️ Propaganda & Civic Action",
    "🕊️ Exile, Trial, & Martyrdom"
]

menu = st.sidebar.radio("Select a Module:", pages)

st.sidebar.markdown("---")
st.sidebar.caption("👨‍💻 Developed by Julian David T. Mercado")
st.sidebar.caption("📚 Course: RZL110_A28")

# ==========================================
# 1. EXECUTIVE DASHBOARD
# ==========================================
if menu == "📊 Executive Dashboard":
    st.markdown('<p class="main-header">👁️ Rizal Lens: Executive Dashboard</p>', unsafe_allow_html=True)
    st.write("This interactive timeline and dashboard completely recontextualizes the 19th-century Philippines. It dispels the myth of a stagnant era and highlights it as a dynamic period of high-speed modernization, agrarian disputes, and the birth of an imagined political community.")
    
    st.markdown("### 📈 Key Historical Metrics")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Suez Canal Length", "103 Miles", "Opened in 1869")
    col2.metric("Calamba Sugar Rent (1840s)", "15 pesos", "Per quiñon")
    col3.metric("Calamba Sugar Rent (1890s)", "30 pesos", "100% Increase", delta_color="inverse")
    col4.metric("GOMBURZA Execution", "1872", "Sparked Nationalism", delta_color="off")
    
    st.markdown("### 🌍 The Three Great Revolutions")
    st.write("The 19th century was fundamentally shaped by three global revolutions that eventually penetrated the Philippine landscape:")
    t1, t2, t3 = st.columns(3)
    t1.info("**🏭 Industrial Revolution**\nBrought radical technological and socio-economic changes, shrinking the globe via steamships.")
    t2.success("**⚔️ French Revolution**\nA period of political upheaval that introduced the concepts of liberty, equality, and fraternity.")
    t3.warning("**📜 American Revolution**\nProved that colonies could successfully rebel against mighty imperial powers.")

# ==========================================
# 2. ROOTS & EARLY EDUCATION
# ==========================================
elif menu == "🌱 Roots & Early Education":
    st.markdown('<p class="main-header">🌱 Roots & Early Education</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<p class="sub-header">The Inquilino Family</p>', unsafe_allow_html=True)
        st.write("Born on June 19, 1861, in Calamba, Laguna, José Protacio Rizal Mercado y Alonso Realonda was born into the *principalia* class. His family were wealthy *inquilinos* (leaseholders) on the Dominican friar estates. This status gave him access to elite education but made his family a direct target of colonial agrarian abuses.")
        
        st.markdown('<p class="sub-header">Ateneo Municipal and UST</p>', unsafe_allow_html=True)
        st.write("Rizal's education was heavily influenced by the Jesuit system at Ateneo Municipal, where he excelled academically and developed his artistic and literary talents. He later transferred to the Dominican-run University of Santo Tomas to study medicine, driven by a desire to cure his mother's failing eyesight. He observed firsthand the stark discrimination between Spanish and native students, catalyzing his eventual departure for Europe in 1882.")
    
    with col2:
        st.error("**The Name 'Rizal'**\nTo avoid association with his outspoken brother Paciano (who was linked to the martyred priest Jose Burgos), Jose adopted the surname 'Rizal', derived from the Spanish word *ricial*, meaning 'green field'.")

# ==========================================
# 3. THE ECONOMIC CRUCIBLE
# ==========================================
elif menu == "💰 The Economic Crucible":
    st.markdown('<p class="main-header">💰 The Economic Crucible</p>', unsafe_allow_html=True)
    
    st.write("The opening of the Suez Canal facilitated global trade, leading to the rise of a new middle class called the *Mestizos* and *Ilustrados*. However, this economic boom exacerbated agrarian tensions.")
    
    tab1, tab2 = st.tabs(["🌾 The Hacienda de Calamba", "🔥 The Evictions"])
    
    with tab1:
        st.markdown('<p class="sub-header">Predatory Rent & Friar Lands</p>', unsafe_allow_html=True)
        st.write("The Hacienda de Calamba was an enclaved economy managed by a corporate religious entity. The Rizal family rented approximately 382 hectares of sugar land and 9.8 hectares of rice land.")
        st.warning("Rent for a *quiñon* of first-class sugar land skyrocketed from 15 pesos in the 1840s to 30 pesos by the end of the century. If annual rent could not be paid due to agricultural crises or rinderpest epidemics (as in 1886 and 1887), the friar administration mercilessly doubled the rent for the following year.")

    with tab2:
        st.markdown('<p class="sub-header">The Wrath of Valeriano Weyler</p>', unsafe_allow_html=True)
        st.write("Governor-General Valeriano Weyler threw his full military prestige behind the Dominicans in Calamba.")
        st.error("Under his orders, around 400 tenants were brutally evicted, their homes dismantled or burned. 25 individuals, including Rizal's 78-year-old father, were deported to Jolo. This event shattered Rizal's illusions of Spanish justice.")

# ==========================================
# 4. POLITICS & THE FRAILOCRACY
# ==========================================
elif menu == "⚖️ Politics & The Frailocracy":
    st.markdown('<p class="main-header">⚖️ Politics & The Frailocracy</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<p class="sub-header">The Rule of the Friars</p>', unsafe_allow_html=True)
        st.write("The union of Church and State in the 19th-century Philippines resulted in the 'Frailocracy'. The friars held immense socio-political power, controlling education, local governance, and vast tracts of land. Their oppressive control over the estates directly cascaded down to the native *inquilinos*.")
        
    with col2:
        st.markdown('<p class="sub-header">The Cavite Mutiny (1872)</p>', unsafe_allow_html=True)
        st.write("Governor-General Rafael Izquierdo's iron-fisted rule sparked the Cavite Mutiny. The administration used this local uprising to execute three secular priests: Mariano Gomez, Jose Burgos, and Jacinto Zamora (GOMBURZA).")
        st.info("The martyrdom of GOMBURZA became the generative trauma that awakened the national consciousness.")

# ==========================================
# 5. ROMANCING TROPICALITY
# ==========================================
elif menu == "🌴 Romancing Tropicality":
    st.markdown('<p class="main-header">🌴 Romancing Tropicality</p>', unsafe_allow_html=True)
    
    st.write("Spanish conservatives like Casimiro Herrero argued that the heat of the Torrid Zone caused a 'lamentable predisposition' to indolence. Europe-based *Ilustrados* fought back by actively romanticizing the tropical climate.")
    
    with st.expander("🍷 The 1884 Brindis Speech", expanded=True):
        st.write("During his toast to Luna and Hidalgo, Rizal brilliantly reversed the racist narrative. He claimed that the spectacular, terrible phenomena of tropical nature were actually the generative fount of their creative genius.")

    with st.expander("🥵 The Demon of Comparisons & Indolence", expanded=True):
        st.write("Upon returning to the Philippines in 1887, Rizal suffered from the intense heat and faced the 'demon of comparisons,' altering his idealized view.")
        st.markdown('<div class="quote-box">In his essay "Sobre la indolencia de los filipinos", Rizal conceded that the heat naturally encourages rest. However, he powerfully proved that the true cause of exaggerated indolence was the disastrous misgovernance, exploitation, and backwardness inflicted by the colonial state, which destroyed the natives\' incentive to work.</div>', unsafe_allow_html=True)

# ==========================================
# 6. MASTER NARRATIVES (THE NOVELS)
# ==========================================
elif menu == "🇵🇭 Master Narratives (The Novels)":
    st.markdown('<p class="main-header">🇵🇭 Master Narratives of the Nation</p>', unsafe_allow_html=True)
    
    st.write("Theorist Benedict Anderson defines a nation as an 'imagined political community', a deep, horizontal comradeship.")
    
    st.markdown('<p class="sub-header">Noli Me Tangere & El Filibusterismo</p>', unsafe_allow_html=True)
    st.write("Rizal's novels emerged as the founding texts of Philippine nationalism. Through literary procedure, they conjured up a knowable Filipino community that was entirely separate from Spain.")
    
    c1, c2 = st.columns(2)
    c1.error("**Exposing Institutional Violence**\nThe novels enveloped the reader by exposing the colonial government's evils, disciplinary power, and the violence of the regime.")
    c2.success("**Ethical Political Decision**\nRizal made the ethical and political decision to speak directly to his fellow Filipinos, challenging colonial assumptions and teaching them a love for their land worth dying for.")

# ==========================================
# 7. PROPAGANDA & CIVIC ACTION
# ==========================================
elif menu == "⚔️ Propaganda & Civic Action":
    st.markdown('<p class="main-header">⚔️ Propaganda & The Final Break</p>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📰 La Solidaridad", "🏛️ La Liga Filipina"])
    
    with tab1:
        st.write("In Madrid, Marcelo H. del Pilar established *La Solidaridad*, supported by regular articles from Rizal, Antonio Luna, and Mariano Ponce. However, Rizal eventually clashed with Del Pilar.")
        st.error("**The Final Break:** Rizal realized that writing articles in Spain was useless. He declared that 'the medicine must be brought near the sick man,' signifying that the true battlefield was the Philippines, not Madrid.")
        
    with tab2:
        st.write("Disillusioned with the Propaganda Movement, Rizal returned to Manila in 1892 and founded a secret civic society: **La Liga Filipina**.")
        st.write("Its revolutionary goals included:")
        st.markdown("""
        1. The unification of the whole Archipelago into a compact, vigorous, and homogeneous body.
        2. Mutual protection in every want and necessity.
        3. Defense against all violence and injustice.
        4. Encouragement of education, agriculture, and commerce.
        """)

# ==========================================
# 8. EXILE, TRIAL, & MARTYRDOM
# ==========================================
elif menu == "🕊️ Exile, Trial, & Martyrdom":
    st.markdown('<p class="main-header">🕊️ Exile, Trial, & Martyrdom</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="sub-header">The Dapitan Interlude (1892 - 1896)</p>', unsafe_allow_html=True)
    st.write("Immediately after founding La Liga Filipina, Rizal was arrested and exiled to Dapitan in Mindanao. Instead of succumbing to despair, he put his civic ideals into practice. He built a school for boys, established a clinic to treat the poor, designed a waterworks system, and collected biological specimens. Dapitan became a microcosm of his vision for a progressive Filipino nation.")
    
    st.markdown('<p class="sub-header">Trial and Execution at Bagumbayan</p>', unsafe_allow_html=True)
    st.write("When the Philippine Revolution broke out in 1896 under the Katipunan, the Spanish authorities wrongly implicated Rizal as the mastermind. Following a mock military trial, he was convicted of rebellion, sedition, and illegal association.")
    
    st.markdown('<div class="quote-box">On the morning of December 30, 1896, at the age of 35, Jose Rizal was executed by firing squad at Bagumbayan (now Rizal Park). On the eve of his death, he penned his final masterpiece, "Mi Ultimo Adios" (My Last Farewell), cementing his status as the ultimate martyr of the Philippine Revolution.</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Rizal Lens © 2026 | Capstone Integration Project | Built with Streamlit</p>", unsafe_allow_html=True)
