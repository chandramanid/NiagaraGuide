import streamlit as st
import pandas as pd
from google import genai

# Page Configuration
st.set_page_config(
    page_title="FallsGuide PWA", 
    page_icon="📍", 
    layout="wide"
)

# Clean, High-Contrast Modern Styling (Full-Width Responsive)
st.markdown("""
    <style>
    /* Clean background and readable text color */
    .stApp {
        background-color: #f8f9fa;
        color: #212529;
    }
    
    /* Professional button styling */
    .stButton>button {
        width: 100%;
        background-color: #0066cc;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        padding: 0.6rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #004080;
        color: white;
    }
    
    /* Card containers */
    .card {
        padding: 20px;
        border-radius: 12px;
        background-color: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State for Login Gate
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# --- LOGIN / REGISTER GATE ---
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #0066cc; padding-top: 2rem;'>📍 FallsGuide PWA Portal</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #555;'>Please sign in or register to access the Niagara travel assistant.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("auth_form"):
            user_input = st.text_input("Username or Email")
            pass_input = st.text_input("Password", type="password")
            submit_btn = st.form_submit_button("Access FallsGuide")
            
            if submit_btn:
                if user_input and pass_input:
                    st.session_state.logged_in = True
                    st.session_state.username = user_input
                    st.rerun()
                else:
                    st.error("Please fill in all fields.")
    st.stop()

# --- INITIALIZE GEMINI AI CLIENT ---
try:
    ai_client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    ai_client = None

# Multilingual Translations Dictionary
translations = {
    "English": {
        "title": "📍 FallsGuide: Niagara Falls All-in-One",
        "subtitle": f"Welcome back, {st.session_state.username}!",
        "tab_home": "🏠 Home & Diagram",
        "tab_transit": "🚌 Transit & Fares",
        "tab_places": "🗺️ Map & Search",
        "tab_stay": "🏨 Hotels & Dining",
        "tab_weather": "🌤️ 7-Day Weather",
        "tab_faq": "❓ FAQ",
        "tab_chat": "🤖 Live AI Assistant",
    },
    "French": {
        "title": "📍 FallsGuide : Assistant Niagara",
        "subtitle": f"Bon retour, {st.session_state.username} !",
        "tab_home": "🏠 Accueil",
        "tab_transit": "🚌 Transport",
        "tab_places": "🗺️ Carte",
        "tab_stay": "🏨 Hôtels",
        "tab_weather": "🌤️ Météo",
        "tab_faq": "❓ FAQ",
        "tab_chat": "🤖 Assistant IA",
    },
    "Hindi": {
        "title": "📍 FallsGuide: नियाग्रा फॉल्स सहायक",
        "subtitle": f"स्वागत है, {st.session_state.username}!",
        "tab_home": "🏠 होम",
        "tab_transit": "🚌 पारगमन",
        "tab_places": "🗺️ नक्शा",
        "tab_stay": "🏨 होटल",
        "tab_weather": "🌤️ मौसम",
        "tab_faq": "❓ प्रश्न",
        "tab_chat": "🤖 AI सहायक",
    },
    "Punjabi": {
        "title": "📍 FallsGuide: ਨਿਆਗਰਾ ਸਹਾਇਕ",
        "subtitle": f"ਜੀ ਆਇਆਂ ਨੂੰ, {st.session_state.username}!",
        "tab_home": "🏠 ਘਰ",
        "tab_transit": "🚌 ਆਵਾਜਾਈ",
        "tab_places": "🗺️ ਨਕਸ਼ਾ",
        "tab_stay": "🏨 ਹੋਟਲ",
        "tab_weather": "🌤️ ਮੌਸਮ",
        "tab_faq": "❓ ਸਵਾਲ",
        "tab_chat": "🤖 AI ਚੈਟ",
    },
    "Nepali": {
        "title": "📍 FallsGuide: नियाग्रा सहायक",
        "subtitle": f"स्वागत छ, {st.session_state.username}!",
        "tab_home": "🏠 गृह",
        "tab_transit": "🚌 यातायात",
        "tab_places": "🗺️ नक्सा",
        "tab_stay": "🏨 होटल",
        "tab_weather": "🌤️ मौसम",
        "tab_faq": "❓ प्रश्न",
        "tab_chat": "🤖 AI सहायक",
    },
    "Spanish": {
        "title": "📍 FallsGuide: Asistente Niágara",
        "subtitle": f"¡Bienvenido, {st.session_state.username}!",
        "tab_home": "🏠 Inicio",
        "tab_transit": "🚌 Transporte",
        "tab_places": "🗺️ Mapa",
        "tab_stay": "🏨 Hoteles",
        "tab_weather": "🌤️ Clima",
        "tab_faq": "❓ FAQ",
        "tab_chat": "🤖 Chat IA",
    },
    "Chinese": {
        "title": "📍 FallsGuide：尼亚加拉助手",
        "subtitle": f"欢迎回来，{st.session_state.username}！",
        "tab_home": "🏠 首页",
        "tab_transit": "🚌 交通",
        "tab_places": "🗺️ 地图",
        "tab_stay": "🏨 酒店",
        "tab_weather": "🌤️ 天气",
        "tab_faq": "❓ 常见问题",
        "tab_chat": "🤖 AI助手",
    },
    "Philippine (Tagalog)": {
        "title": "📍 FallsGuide: Niagara Assistant",
        "subtitle": f"Maligayang pagbabalik, {st.session_state.username}!",
        "tab_home": "🏠 Tahanan",
        "tab_transit": "🚌 Biyahe",
        "tab_places": "🗺️ Mapa",
        "tab_stay": "🏨 Hotel",
        "tab_weather": "🌤️ Panahon",
        "tab_faq": "❓ FAQ",
        "tab_chat": "🤖 AI Chat",
    },
    "Korean": {
        "title": "📍 FallsGuide: 나이아가라 어시스턴트",
        "subtitle": f"환영합니다, {st.session_state.username}님!",
        "tab_home": "🏠 홈",
        "tab_transit": "🚌 교통",
        "tab_places": "🗺️ 지도",
        "tab_stay": "🏨 호텔",
        "tab_weather": "🌤️ 날씨",
        "tab_faq": "❓ FAQ",
        "tab_chat": "🤖 AI 채팅",
    },
    "Japanese": {
        "title": "📍 FallsGuide：ナイアガラアシスタント",
        "subtitle": f"お帰りなさいませ、{st.session_state.username}さん！",
        "tab_home": "🏠 ホーム",
        "tab_transit": "🚌 交通",
        "tab_places": "🗺️ マップ",
        "tab_stay": "🏨 ホテル",
        "tab_weather": "🌤️ 天気",
        "tab_faq": "FAQ",
        "tab_chat": "🤖 AIチャット",
    }
}

# Sidebar and Header Layout
col_title, col_lang, col_logout = st.columns([3, 2, 1])
with col_title:
    st.title("📍 FallsGuide PWA")
with col_lang:
    lang = st.selectbox("🌐 Language", list(translations.keys()))
    t = translations[lang]
with col_logout:
    st.write("") # spacing
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

st.caption(t["subtitle"])
st.divider()

# Navigation Tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    t["tab_home"],
    t["tab_transit"], 
    t["tab_places"], 
    t["tab_stay"], 
    t["tab_weather"], 
    t["tab_faq"],
    t["tab_chat"]
])

# --- TAB 1: HOME & FALLS DIAGRAM ---
with tab1:
    st.subheader("🌊 Niagara Falls: Structure & Layout")
    st.write("Niagara Falls spans the border between Ontario, Canada, and New York, USA, consisting of three grand sections:")
    
    col_d1, col_d2, col_d3 = st.columns(3)
    with col_d1:
        st.markdown("### 🇨🇦 Horseshoe Falls")
        st.write("- *Location:* Canadian side")
        st.write("- *Volume:* Carries 90% of water flow")
    with col_d2:
        st.markdown("### 🇺🇸 American Falls")
        st.write("- *Location:* US side")
        st.write("- *Shape:* Straight vertical drop")
    with col_d3:
        st.markdown("### 🤍 Bridal Veil Falls")
        st.write("- *Location:* Adjacent to American Falls")
        st.write("- *Feature:* Separated by Luna Island")

# --- TAB 2: TRANSIT & FARES ---
with tab2:
    st.subheader("🚌 Niagara Regional Transit (NRT) & Fares")
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.markdown("### 🎫 Bus Fares & Rules")
        st.write("- *Adults, Seniors, Youth:* $3.50 CAD per ride.")
        st.write("- *Children (12 & under):* Free.")
        st.write("- *Transfer Window:* Valid for 2 hours.")
        st.warning("⚠️ *Cash Policy:* Exact coin change required onboard.")
        st.info("📱 Download the *Transit* app for live tracking.")
    with col_t2:
        st.markdown("### 🚖 Taxis & Rideshare")
        st.write("- *Local Taxis:* Base rates $4.50 - $5.00 CAD, ~$2.00/km.")
        st.write("- *Uber & Lyft:* Available across tourist hubs.")

# --- TAB 3: MAP & SEARCH ---
with tab3:
    st.subheader("🗺️ Regional Attractions & Search")
    attractions = {
        "Horseshoe Falls": {"lat": 43.0782, "lon": -79.0747, "desc": "The largest waterfall."},
        "Clifton Hill": {"lat": 43.0906, "lon": -79.0718, "desc": "Famous entertainment strip."},
        "Skylon Tower": {"lat": 43.0853, "lon": -79.0837, "desc": "360-degree observation tower."},
        "Niagara-on-the-Lake (NOTL)": {"lat": 43.2551, "lon": -79.0772, "desc": "Historic heritage village & wineries."},
        "Crystal Beach (Bay Beach)": {"lat": 42.8687, "lon": -79.0565, "desc": "Stunning Lake Erie white sand beach."}
    }
    
    query = st.text_input("🔍 Search location:")
    filtered = {k: v for k, v in attractions.items() if query.lower() in k.lower() or query.lower() in v['desc'].lower()}
    if not filtered:
        filtered = attractions
        
    choice = st.selectbox("Select destination:", list(filtered.keys()))
    st.write(f"*Description:* {filtered[choice]['desc']}")
    
    map_df = pd.DataFrame({'lat': [filtered[choice]['lat']], 'lon': [filtered[choice]['lon']]} )
    st.map(map_df, zoom=12)

# --- TAB 4: HOTELS & DINING ---
with tab4:
    st.subheader("🏨 Top Hotels & Restaurants (Google Reviews)")
    h1, h2 = st.columns(2)
    with h1:
        st.markdown("### 🏨 Hotels")
        st.write("1. *Marriott Fallsview Hotel* — ⭐ 4.5 / 5")
        st.write("2. *Sheraton Fallsview Hotel* — ⭐ 4.3 / 5")
        st.write("3. *Pillar & Post (NOTL)* — ⭐ 4.6 / 5")
    with h2:
        st.markdown("### 🍽️ Dining")
        st.write("1. *Prime Steakhouse* — ⭐ 4.7 / 5")
        st.write("2. *The Rainbow Room* — ⭐ 4.4 / 5")
        st.write("3. *South Coast Cookhouse (Crystal Beach)* — ⭐ 4.5 / 5")

# --- TAB 5: WEATHER ---
with tab5:
    st.subheader("🌤️ 7-Day Regional Weather Forecast")
    forecast = [
        {"Day": "Monday", "Temp": "24°C", "Condition": "☀️ Sunny", "Mist": "Low"},
        {"Day": "Tuesday", "Temp": "26°C", "Condition": "⛅ Partly Cloudy", "Mist": "Moderate"},
        {"Day": "Wednesday", "Temp": "23°C", "Condition": "🌧️ Showers", "Mist": "High"},
        {"Day": "Thursday", "Temp": "25°C", "Condition": "☀️ Sunny", "Mist": "Low"},
        {"Day": "Friday", "Temp": "27°C", "Condition": "🌤️ Warm", "Mist": "Moderate"},
        {"Day": "Saturday", "Temp": "22°C", "Condition": "⛅ Cloudy", "Mist": "Low"},
        {"Day": "Sunday", "Temp": "24°C", "Condition": "☀️ Sunny", "Mist": "Low"}
    ]
    st.dataframe(pd.DataFrame(forecast), use_container_width=True)

# --- TAB 6: FAQ ---
with tab6:
    st.subheader("❓ Frequently Asked Questions")
    with st.expander("How much is the local bus fare?"):
        st.write("$3.50 CAD per ride. Exact coin change is required if paying cash onboard.")
    with st.expander("Are bus transfers free?"):
        st.write("Yes, fares include a 2-hour unlimited transfer window.")
    with st.expander("How far is Crystal Beach?"):
        st.write("Crystal Beach is about a 45-minute drive south of Niagara Falls on Lake Erie.")

# --- TAB 7: AI CHAT ---
with tab7:
    st.subheader("🤖 Live Gemini AI Assistant")
    st.write(f"Ask any question about travel, transit, or hotels. *Language: {lang}*")
    
    q = st.text_input("Type your question:")
    if st.button("Ask Assistant"):
        if ai_client and q:
            with st.spinner("Thinking..."):
                try:
                    res = ai_client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=f"You are FallsGuide AI. Answer in {lang}. Question: {q}"
                    )
                    st.success(res.text)
                except Exception as e:
                    st.error(f"Error: {e}")
        elif not ai_client:
            st.error("Gemini API Key missing in Streamlit Secrets.")
        else:
            st.warning("Please type a question.")
