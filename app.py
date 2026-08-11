import streamlit as st
import pandas as pd
from google import genai

# Page Configuration & Mobile Viewport Locking
st.set_page_config(
    page_title="FallsGuide PWA", 
    page_icon="📍", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# PWA & Native Mobile App Styling (Hides Streamlit UI, adds app feel)
st.markdown("""
    <style>
    /* Hide Streamlit Header, Footer, and Menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* App Shell Background & Padding */
    .stApp {
        background-color: #f4f6f9;
        max-width: 480px;
        margin: auto;
    }
    
    @media (min-width: 768px) {
        .stApp {
            max-width: 100%;
        }
    }

    /* Mobile Touch-Friendly Buttons */
    .stButton>button {
        width: 100%;
        background-color: #0066cc;
        color: white;
        border-radius: 12px;
        font-weight: bold;
        padding: 0.75rem;
        font-size: 16px;
        border: none;
        box-shadow: 0 4px 10px rgba(0,102,204,0.3);
    }
    .stButton>button:hover {
        background-color: #004080;
        color: white;
    }

    /* Modern Mobile Card Design */
    .pwa-card {
        padding: 16px;
        border-radius: 14px;
        background-color: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        margin-bottom: 16px;
    }
    </style>
    
    <!-- PWA Mobile Meta Tags for Browser App Experience -->
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
""", unsafe_allow_html=True)

# Initialize Session State for Login Gate
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# --- MOBILE LOGIN / REGISTER GATE (PWA SECURITY) ---
if not st.session_state.logged_in:
    st.markdown("<h2 style='text-align: center; color: #0066cc; padding-top: 2rem;'>📍 FallsGuide PWA</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Sign in to access your offline-ready Niagara travel assistant.</p>", unsafe_allow_html=True)
    
    with st.form("auth_form"):
        user_input = st.text_input("Username or Email")
        pass_input = st.text_input("Password", type="password")
        submit_btn = st.form_submit_button("Launch App")
        
        if submit_btn:
            if user_input and pass_input:
                st.session_state.logged_in = True
                st.session_state.username = user_input
                st.rerun()
            else:
                st.error("Please enter your credentials.")
    st.stop()

# --- INITIALIZE GEMINI AI CLIENT ---
try:
    ai_client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    ai_client = None

# Multilingual Translations Dictionary
translations = {
    "English": {
        "title": "📍 FallsGuide",
        "subtitle": f"Hello, {st.session_state.username}!",
        "tab_home": "🏠 Home",
        "tab_transit": "🚌 Transit",
        "tab_places": "🗺️ Map",
        "tab_stay": "🏨 Hotels",
        "tab_weather": "🌤️ Weather",
        "tab_faq": "❓ FAQ",
        "tab_chat": "🤖 AI Chat",
    },
    "French": {
        "title": "📍 FallsGuide",
        "subtitle": f"Bonjour, {st.session_state.username} !",
        "tab_home": "🏠 Accueil",
        "tab_transit": "🚌 Transport",
        "tab_places": "🗺️ Carte",
        "tab_stay": "🏨 Hôtels",
        "tab_weather": "🌤️ Météo",
        "tab_faq": "❓ FAQ",
        "tab_chat": "🤖 IA Chat",
    },
    "Hindi": {
        "title": "📍 FallsGuide",
        "subtitle": f"नमस्ते, {st.session_state.username}!",
        "tab_home": "🏠 होम",
        "tab_transit": "🚌 पारगमन",
        "tab_places": "🗺️ नक्शा",
        "tab_stay": "🏨 होटल",
        "tab_weather": "🌤️ मौसम",
        "tab_faq": "❓ प्रश्न",
        "tab_chat": "🤖 AI चैट",
    },
    "Punjabi": {
        "title": "📍 FallsGuide",
        "subtitle": f"ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ, {st.session_state.username}!",
        "tab_home": "🏠 ਘਰ",
        "tab_transit": "🚌 ਆਵਾਜਾਈ",
        "tab_places": "🗺️ ਨਕਸ਼ਾ",
        "tab_stay": "🏨 ਹੋਟਲ",
        "tab_weather": "🌤️ ਮੌਸम",
        "tab_faq": "❓ ਸਵਾਲ",
        "tab_chat": "🤖 AI ਚੈਟ",
    },
    "Nepali": {
        "title": "📍 FallsGuide",
        "subtitle": f"नमस्कार, {st.session_state.username}!",
        "tab_home": "🏠 गृह",
        "tab_transit": "🚌 यातायात",
        "tab_places": "🗺️ नक्सा",
        "tab_stay": "🏨 होटल",
        "tab_weather": "🌤️ मौसम",
        "tab_faq": "❓ प्रश्न",
        "tab_chat": "🤖 AI च्याट",
    },
    "Spanish": {
        "title": "📍 FallsGuide",
        "subtitle": f"¡Hola, {st.session_state.username}!",
        "tab_home": "🏠 Inicio",
        "tab_transit": "🚌 Transporte",
        "tab_places": "🗺️ Mapa",
        "tab_stay": "🏨 Hoteles",
        "tab_weather": "🌤️ Clima",
        "tab_faq": "❓ FAQ",
        "tab_chat": "🤖 Chat IA",
    },
    "Chinese": {
        "title": "📍 FallsGuide",
        "subtitle": f"您好，{st.session_state.username}！",
        "tab_home": "🏠 首页",
        "tab_transit": "🚌 交通",
        "tab_places": "🗺️ 地图",
        "tab_stay": "🏨 酒店",
        "tab_weather": "🌤️ 天气",
        "tab_faq": "❓ 常见问题",
        "tab_chat": "🤖 AI聊天",
    },
    "Philippine (Tagalog)": {
        "title": "📍 FallsGuide",
        "subtitle": f"Kamusta, {st.session_state.username}!",
        "tab_home": "🏠 Tahanan",
        "tab_transit": "🚌 Biyahe",
        "tab_places": "🗺️ Mapa",
        "tab_stay": "🏨 Hotel",
        "tab_weather": "🌤️ Panahon",
        "tab_faq": "❓ FAQ",
        "tab_chat": "🤖 AI Chat",
    },
    "Korean": {
        "title": "📍 FallsGuide",
        "subtitle": f"안녕하세요, {st.session_state.username}님!",
        "tab_home": "🏠 홈",
        "tab_transit": "🚌 교통",
        "tab_places": "🗺️ 지도",
        "tab_stay": "🏨 호텔",
        "tab_weather": "🌤️ 날씨",
        "tab_faq": "❓ FAQ",
        "tab_chat": "🤖 AI 채팅",
    },
    "Japanese": {
        "title": "📍 FallsGuide",
        "subtitle": f"こんにちは、{st.session_state.username}さん！",
        "tab_home": "🏠 ホーム",
        "tab_transit": "🚌 交通",
        "tab_places": "🗺️ マップ",
        "tab_stay": "🏨 ホテル",
        "tab_weather": "🌤️ 天気",
        "tab_faq": "FAQ",
        "tab_chat": "🤖 AIチャット",
    }
}

# Top App Header bar
col_h1, col_h2 = st.columns([3, 1])
with col_h1:
    lang = st.selectbox("🌐", list(translations.keys()), label_visibility="collapsed")
t = translations[lang]
with col_h2:
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

st.title(t["title"])
st.caption(t["subtitle"])
st.divider()

# App Bottom/Top Tabs Navigation
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
    st.markdown("### 🌊 Niagara Falls Structure")
    st.write("Explaining the 3 majestic sections of the falls border:")
    st.info("🇨🇦 *Horseshoe Falls:* Carries 90% of water flow.\n\n🇺🇸 *American Falls:* Jagged vertical drop.\n\n🤍 *Bridal Veil Falls:* Smallest neighboring waterfall.")

# --- TAB 2: TRANSIT & FARES ---
with tab2:
    st.markdown("### 🚌 NRT Transit & Fares")
    st.write("- *Adults/Seniors/Youth:* $3.50 CAD / ride.")
    st.write("- *Children (12 & under):* Free.")
    st.write("- *Transfer:* Valid for 2 hours.")
    st.warning("⚠️ Exact coin change required if paying cash onboard.")
    st.info("📱 Use the *Transit* app for live tracking.")

# --- TAB 3: ATTRACTIONS & MAP ---
with tab3:
    st.markdown("### 🗺️ Regional Search")
    attractions = {
        "Horseshoe Falls": {"lat": 43.0782, "lon": -79.0747, "desc": "The largest waterfall."},
        "Clifton Hill": {"lat": 43.0906, "lon": -79.0718, "desc": "Entertainment strip."},
        "Niagara-on-the-Lake": {"lat": 43.2551, "lon": -79.0772, "desc": "Historic heritage village."},
        "Crystal Beach": {"lat": 42.8687, "lon": -79.0565, "desc": "Lake Erie white sand beach."}
    }
    query = st.text_input("Search location:")
    filtered = {k: v for k, v in attractions.items() if query.lower() in k.lower()}
    if not filtered:
        filtered = attractions
    
    choice = st.selectbox("Select place:", list(filtered.keys()))
    st.write(filtered[choice]["desc"])
    
    df = pd.DataFrame({'lat': [filtered[choice]['lat']], 'lon': [filtered[choice]['lon']]})
    st.map(df, zoom=11)

# --- TAB 4: HOTELS & DINING ---
with tab4:
    st.markdown("### 🏨 Hotels & Dining")
    st.write("1. *Marriott Fallsview Hotel* — ⭐ 4.5 / 5")
    st.write("2. *Sheraton Fallsview Hotel* — ⭐ 4.3 / 5")
    st.write("3. *Prime Steakhouse* — ⭐ 4.7 / 5")
    st.write("4. *Treadwell Farm to Table (NOTL)* — ⭐ 4.6 / 5")

# --- TAB 5: WEATHER (7-DAY) ---
with tab5:
    st.markdown("### 🌤️ 7-Day Forecast")
    forecast = [
        {"Day": "Mon", "Temp": "24°C", "Cond": "☀️ Sunny"},
        {"Day": "Tue", "Temp": "26°C", "Cond": "⛅ Partly Cloudy"},
        {"Day": "Wed", "Temp": "23°C", "Cond": "🌧️ Showers"},
        {"Day": "Thu", "Temp": "25°C", "Cond": "☀️ Sunny"},
        {"Day": "Fri", "Temp": "27°C", "Cond": "🌤️ Warm"},
        {"Day": "Sat", "Temp": "22°C", "Cond": "⛅ Cloudy"},
        {"Day": "Sun", "Temp": "24°C", "Cond": "☀️ Sunny"}
    ]
    st.dataframe(pd.DataFrame(forecast), use_container_width=True)

# --- TAB 6: FAQ ---
with tab6:
    st.markdown("### ❓ FAQ")
    with st.expander("How much is bus fare?"):
        st.write("$3.50 CAD exact coin change.")
    with st.expander("How far is Crystal Beach?"):
        st.write("About 45 minutes south by car.")

# --- TAB 7: AI CHAT ---
with tab7:
    st.markdown("### 🤖 Live AI Assistant")
    q = st.text_input("Ask a travel question:")
    if st.button("Send Query"):
        if ai_client and q:
            with st.spinner("Processing..."):
                try:
                    res = ai_client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=f"Answer in {lang}: {q}"
                    )
                    st.success(res.text)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a question.")
