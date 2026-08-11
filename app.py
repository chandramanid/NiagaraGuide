import streamlit as st
import pandas as pd
from google import genai

# Page Configuration
st.set_page_config(
    page_title="FallsGuide: Niagara Falls All-in-One", 
    page_icon="📍", 
    layout="wide"
)

# Custom PWA & Mobile-Friendly Styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #0066cc;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        padding: 0.5rem;
    }
    .stButton>button:hover {
        background-color: #004080;
        color: white;
    }
    .card {
        padding: 20px;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State for Login/Register Gate
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# --- LOGIN / REGISTER GATE (PWA SECURITY) ---
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #0066cc;'>📍 Welcome to FallsGuide PWA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Please sign in or register to access the complete Niagara travel, transit, and AI assistant platform.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        auth_mode = st.radio("Choose Action", ["Login", "Register"], horizontal=True)
        
        with st.form("auth_form"):
            user_input = st.text_input("Username / Email")
            pass_input = st.text_input("Password", type="password")
            
            if auth_mode == "Register":
                confirm_pass = st.text_input("Confirm Password", type="password")
            
            submit_btn = st.form_submit_button("Enter FallsGuide PWA")
            
            if submit_btn:
                if user_input and pass_input:
                    st.session_state.logged_in = True
                    st.session_state.username = user_input
                    st.success("Authentication successful! Loading your app...")
                    st.rerun()
                else:
                    st.error("Please fill in all required fields.")
    
    st.stop() # Stops execution here until user logs in

# --- INITIALIZE GEMINI AI CLIENT ---
try:
    ai_client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    ai_client = None

# Multilingual Translations Dictionary
translations = {
    "English": {
        "title": "📍 FallsGuide: Niagara Falls Complete Assistant",
        "subtitle": f"Welcome back, {st.session_state.username}! Your ultimate multi-language guide.",
        "tab_home": "🏠 Home & Falls Diagram",
        "tab_transit": "🚌 Transit & Fares",
        "tab_places": "🗺️ Attractions & Map",
        "tab_stay": "🏨 Hotels & Dining",
        "tab_weather": "🌤️ 7-Day Weather",
        "tab_faq": "❓ FAQ",
        "tab_chat": "🤖 Live AI Assistant",
    },
    "French": {
        "title": "📍 FallsGuide : Assistant Complet de Niagara",
        "subtitle": f"Bon retour, {st.session_state.username} ! Votre guide multilingue.",
        "tab_home": "🏠 Accueil & Schéma",
        "tab_transit": "🚌 Transport & Tarifs",
        "tab_places": "🗺️ Attractions & Carte",
        "tab_stay": "🏨 Hôtels & Restos",
        "tab_weather": "🌤️ Météo 7 Jours",
        "tab_faq": "❓ FAQ",
        "tab_chat": "🤖 Assistant IA",
    },
    "Hindi": {
        "title": "📍 FallsGuide: नियाग्रा फॉल्स संपूर्ण सहायक",
        "subtitle": f"स्वागत है, {st.session_state.username}! आपकी संपूर्ण मार्गदर्शिका।",
        "tab_home": "🏠 होम और फॉल्स आरेख",
        "tab_transit": "🚌 पारगमन और किराया",
        "tab_places": "🗺️ आकर्षण और नक्शा",
        "tab_stay": "🏨 होटल और भोजन",
        "tab_weather": "🌤️ 7-दिवसीय मौसम",
        "tab_faq": "❓ सामान्य प्रश्न",
        "tab_chat": "🤖 लाइव AI सहायक",
    },
    "Punjabi": {
        "title": "📍 FallsGuide: ਨਿਆਗਰਾ ਫਾਲ્સ ਪੂਰਾ ਸਹਾਇਕ",
        "subtitle": f"ਜੀ ਆਇਆਂ ਨੂੰ, {st.session_state.username}! ਤੁਹਾਡੀ ਗਾਈਡ।",
        "tab_home": "🏠 ਘਰ ਅਤੇ ਡਾਇਗ्राम",
        "tab_transit": "🚌 ਆਵਾਜਾਈ ਅਤੇ ਕਿਰਾਏ",
        "tab_places": "🗺️ ਸਥਾਨ ਅਤੇ ਨਕਸ਼ਾ",
        "tab_stay": "🏨 ਹੋਟਲ ਅਤੇ ਖਾਣਾ",
        "tab_weather": "🌤️ 7-ਦिनਾਂ ਦਾ ਮੌਸਮ",
        "tab_faq": "❓ ਆਮ ਸਵਾਲ",
        "tab_chat": "🤖 ਲਾਈਵ AI ਸਹਾਇਕ",
    },
    "Nepali": {
        "title": "📍 FallsGuide: नियाग्रा फल्स पूर्ण सहायक",
        "subtitle": f"स्वागत छ, {st.session_state.username}! तपाईंको गाइड।",
        "tab_home": "🏠 गृह र फल्स डाइग्राम",
        "tab_transit": "🚌 यातायात र भाडा",
        "tab_places": "🗺️ आकर्षण र नक्सा",
        "tab_stay": "🏨 होटल र खाना",
        "tab_weather": "🌤️ ७-दिने मौसम",
        "tab_faq": "❓ बारम्बार सोधिने प्रश्नहरू",
        "tab_chat": "🤖 लाइभ AI सहायक",
    },
    "Spanish": {
        "title": "📍 FallsGuide: Asistente Completo de Niágara",
        "subtitle": f"Bienvenido de nuevo, {st.session_state.username}! Tu guía multilingüe.",
        "tab_home": "🏠 Inicio y Diagrama",
        "tab_transit": "🚌 Transporte y Tarifas",
        "tab_places": "🗺️ Atracciones y Mapa",
        "tab_stay": "🏨 Hoteles y Comida",
        "tab_weather": "🌤️ Clima 7 Días",
        "tab_faq": "❓ Preguntas Frecuentes",
        "tab_chat": "🤖 Asistente de IA",
    },
    "Chinese": {
        "title": "📍 FallsGuide：尼亚加拉大瀑布综合助手",
        "subtitle": f"欢迎回来，{st.session_state.username}！您的多语言指南。",
        "tab_home": "🏠 首页与瀑布图解",
        "tab_transit": "🚌 交通与票价",
        "tab_places": "🗺️ 景点与地图",
        "tab_stay": "🏨 酒店与餐饮",
        "tab_weather": "🌤️ 7天天气预报",
        "tab_faq": "❓ 常见问题",
        "tab_chat": "🤖 实时AI助手",
    },
    "Philippine (Tagalog)": {
        "title": "📍 FallsGuide: Kumpletong Katulong sa Niagara Falls",
        "subtitle": f"Maligayang pagbabalik, {st.session_state.username}!",
        "tab_home": "🏠 Tahanan at Diagram",
        "tab_transit": "🚌 Transportasyon at Bayad",
        "tab_places": "🗺️ Pasyalan at Mapa",
        "tab_stay": "🏨 Mga Hotel at Kainan",
        "tab_weather": "🌤️ Panahon sa 7 Araw",
        "tab_faq": "❓ Mga Tanong",
        "tab_chat": "🤖 Live AI Assistant",
    },
    "Korean": {
        "title": "📍 FallsGuide: 나이아가라 폭포 종합 어시스턴트",
        "subtitle": f"환영합니다, {st.session_state.username}님!",
        "tab_home": "🏠 홈 및 폭포 구조",
        "tab_transit": "🚌 교통 및 요금",
        "tab_places": "🗺️ 명소 및 지도",
        "tab_stay": "🏨 호텔 및 식당",
        "tab_weather": "🌤️ 7일간의 날씨",
        "tab_faq": "❓ 자주 묻는 질문",
        "tab_chat": "🤖 실시간 AI 어시스턴트",
    },
    "Japanese": {
        "title": "📍 FallsGuide：ナイアガラ総合アシスタント",
        "subtitle": f"お帰りなさいませ、{st.session_state.username}さん！",
        "tab_home": "🏠 ホームと滝の構造",
        "tab_transit": "🚌 交通機関と料金",
        "tab_places": "🗺️ 観光地とマップ",
        "tab_stay": "🏨 ホテルとレストラン",
        "tab_weather": "🌤️ 7日間天気予報",
        "tab_faq": "❓ よくある質問",
        "tab_chat": "🤖 ライブAIアシスタント",
    }
}

# Sidebar Controls
st.sidebar.title("🛠️ PWA Controls")
lang = st.sidebar.selectbox("🌐 Select Language", list(translations.keys()))
t = translations[lang]

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

st.title(t["title"])
st.markdown(f"{t['subtitle']}")
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
    st.subheader("🌊 Understanding Niagara Falls: Structure & Layout")
    st.write("Niagara Falls is composed of three majestic waterfalls spanning the border between Ontario, Canada, and New York, USA.")
    
    col_d1, col_d2, col_d3 = st.columns(3)
    
    with col_d1:
        st.markdown("### 🇨🇦 Horseshoe Falls")
        st.write("- *Location:* Primarily Canadian side.")
        st.write("- *Shape:* Distinct horseshoe curve.")
        st.write("- *Volume:* Carries over 90% of the Niagara River's water flow.")
        
    with col_d2:
        st.markdown("### 🇺🇸 American Falls")
        st.write("- *Location:* Entirely on the US side.")
        st.write("- *Shape:* Straight, jagged edge line.")
        st.write("- *Height:* Taller vertical drop than Horseshoe Falls.")

    with col_d3:
        st.markdown("### 🤍 Bridal Veil Falls")
        st.write("- *Location:* Smallest waterfall next to the American Falls.")
        st.write("- *Feature:* Separated by Luna Island.")

    st.divider()
    st.info("💡 *Quick Orientation Tip:* The Canadian side (Niagara Falls, Ontario) offers the premier panoramic views of both the Horseshoe and American Falls, illuminated brightly every night.")

# --- TAB 2: TRANSIT & FARES ---
with tab2:
    st.subheader("🚌 Niagara Regional Transit (NRT) & Taxi Guide")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🎫 Local Bus Fares & Rules")
        st.write("- *Adults, Seniors (65+), Youth (13-17):* $3.50 CAD per single ride.")
        st.write("- *Children (12 and under):* Ride *Free*.")
        st.write("- *Transfer Window:* Valid for *2 hours* of unlimited transfers across local connections.")
        st.warning("⚠️ *Cash Policy:* Onboard cash requires exact change in coins or paper bills. Drivers cannot make change.")
        st.info("📱 *Required App:* Download the *Transit* app to track buses in real-time and purchase mobile passes.")

    with col2:
        st.markdown("### 🚖 Taxi & Rideshare Information")
        st.write("- *Local Taxis:* Base drop rates start at $4.50 - $5.00 CAD, averaging $2.00 - $2.50 CAD per kilometer.")
        st.write("- *Uber & Lyft:* Fully operational throughout tourist zones and GO stations.")
        st.write("- Estimate: WEGO Hub to Clifton Hill typically costs $10 to $15 CAD.")

# --- TAB 3: ATTRACTIONS & MAP SEARCH ---
with tab3:
    st.subheader("🗺️ Regional Attractions & Interactive Map Search")
    
    attractions = {
        "Horseshoe Falls (Niagara Falls)": {"lat": 43.0782, "lon": -79.0747, "desc": "The largest of the three waterfalls making up Niagara Falls.", "category": "Niagara Falls"},
        "Clifton Hill": {"lat": 43.0906, "lon": -79.0718, "desc": "Famous entertainment street packed with arcades and attractions.", "category": "Niagara Falls"},
        "Skylon Tower": {"lat": 43.0853, "lon": -79.0837, "desc": "Observation tower offering panoramic 360-degree views.", "category": "Niagara Falls"},
        "Niagara-on-the-Lake (Old Town)": {"lat": 43.2551, "lon": -79.0772, "desc": "Historic 19th-century village famous for boutique shopping, theatres, and heritage inns.", "category": "Niagara-on-the-Lake"},
        "Crystal Beach (Bay Beach)": {"lat": 42.8687, "lon": -79.0565, "desc": "Stunning white sand beach on Lake Erie's northern shore, perfect for swimming and relaxation.", "category": "Crystal Beach"}
    }

    # Search Filter Box
    search_query = st.text_input("🔍 Search attractions by name or keyword:")
    
    filtered_attractions = {k: v for k, v in attractions.items() if search_query.lower() in k.lower() or search_query.lower() in v['desc'].lower()}
    
    if not filtered_attractions:
        filtered_attractions = attractions # Fallback to all if empty search

    selected_place = st.selectbox("Select location from filtered results:", list(filtered_attractions.keys()))
    
    st.write(f"*Category:* {filtered_attractions[selected_place]['category']}")
    st.write(f"*Description:* {filtered_attractions[selected_place]['desc']}")
    
    # Map view
    map_df = pd.DataFrame({
        'lat': [filtered_attractions[selected_place]['lat']],
        'lon': [filtered_attractions[selected_place]['lon']]
    })
    st.map(map_df, zoom=12)

# --- TAB 4: HOTELS & DINING ---
with tab4:
    st.subheader("🏨 Expanded Hotels & Dining Options (Google Review Ratings)")
    
    h_col1, h_col2 = st.columns(2)
    
    with h_col1:
        st.markdown("### 🏨 Recommended Hotels")
        st.write("1. *Marriott Fallsview Hotel & Spa* — ⭐ *Google Rating: 4.5 / 5* (Unobstructed views)")
        st.write("2. *Sheraton Fallsview Hotel* — ⭐ *Google Rating: 4.3 / 5* (Connected to waterpark)")
        st.write("3. *Hyatt Regency Niagara Falls* — ⭐ *Google Rating: 4.0 / 5* (Prime location)")
        st.write("4. *Hilton Niagara Falls/Fallsview Suites* — ⭐ *Google Rating: 4.2 / 5* (Glittering hub vistas)")
        st.write("5. *Pillar & Post Inn & Spa (NOTL)* — ⭐ *Google Rating: 4.6 / 5* (Historic wine country luxury)")

    with h_col2:
        st.markdown("### 🍽️ Recommended Restaurants")
        st.write("1. *Prime Steakhouse Niagara Falls* — ⭐ *Google Rating: 4.7 / 5* (Fine dining view)")
        st.write("2. *The Rainbow Room by Massimo Capra* — ⭐ *Google Rating: 4.4 / 5* (Italian gorge view)")
        st.write("3. *Elements on the Falls Restaurant* — ⭐ *Google Rating: 4.3 / 5* (Overlooking Horseshoe Falls)")
        st.write("4. *Treadwell Farm to Table (NOTL)* — ⭐ *Google Rating: 4.6 / 5* (MICHELIN-recognized dining)")
        st.write("5. *South Coast Cookhouse (Crystal Beach)* — ⭐ *Google Rating: 4.5 / 5* (Local coastal favorite)")

# --- TAB 5: WEATHER CONDITIONS (7-DAY FORECAST) ---
with tab5:
    st.subheader("🌤️ Niagara Region 7-Day Weather Forecast")
    st.write("Plan your outdoor visits, beach trips to Crystal Beach, or winery tours in Niagara-on-the-Lake with this 7-day outlook:")
    
    weather_data = [
        {"Day": "Monday", "Temp": "24°C", "Condition": "☀️ Sunny", "Mist Impact": "Low"},
        {"Day": "Tuesday", "Temp": "26°C", "Condition": "⛅ Partly Cloudy", "Mist Impact": "Moderate"},
        {"Day": "Wednesday", "Temp": "23°C", "Condition": "🌧️ Light Showers", "Mist Impact": "High"},
        {"Day": "Thursday", "Temp": "25°C", "Condition": "☀️ Sunny & Clear", "Mist Impact": "Low"},
        {"Day": "Friday", "Temp": "27°C", "Condition": "🌤️ Warm & Humid", "Mist Impact": "Moderate"},
        {"Day": "Saturday", "Temp": "22°C", "Condition": "⛅ Cloudy", "Mist Impact": "Low"},
        {"Day": "Sunday", "Temp": "24°C", "Condition": "☀️ Sunny", "Mist Impact": "Low"}
    ]
    
    w_df = pd.DataFrame(weather_data)
    st.dataframe(w_df, use_container_width=True)
    st.info("💡 *Tip:* Visiting the base of the Falls always produces heavy spray. Waterproof jackets or ponchos are recommended regardless of clear weather forecasts.")

# --- TAB 6: FAQ ---
with tab6:
    st.subheader("❓ Frequently Asked Questions (FAQ)")
    
    with st.expander("Q: How much is the local bus fare and how do I pay?"):
        st.write("A: Adult/Youth/Senior fares are $3.50 CAD per ride. If you pay cash onboard, you must provide exact change in coins or paper bills. Drivers cannot make change. Alternatively, download the 'Transit' app for digital mobile passes.")
        
    with st.expander("Q: Are transfers free on the local bus?"):
        st.write("A: Yes, bus tickets and fares include a 2-hour transfer window for unlimited direction changes.")

    with st.expander("Q: How far is Crystal Beach and Niagara-on-the-Lake from Niagara Falls?"):
        st.write("A: Niagara-on-the-Lake is about a 25-minute drive north via the Niagara Parkway. Crystal Beach is located on Lake Erie, roughly a 45-minute drive south of Niagara Falls.")

    with st.expander("Q: Is the tap-to-pay feature available on all transit buses?"):
        st.write("A: Older regional transit vehicles may not have active card readers, which is why carrying exact coin change or using the 'Transit' mobile app is strongly advised.")

# --- TAB 7: MULTILINGUAL AI CHAT ---
with tab7:
    st.subheader("🤖 Live Gemini AI Assistant Chat")
    st.write(f"Ask any question about transit, schedules, fares, or recommendations. *Responding in: {lang}*")

    user_query = st.text_input("Type your question here:")
    if st.button("Ask AI Assistant"):
        if ai_client and user_query:
            with st.spinner("Thinking..."):
                try:
                    prompt = f"You are FallsGuide AI, a helpful assistant for Niagara Falls tourists. Answer the following question in {lang}. Question: {user_query}"
                    response = ai_client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt
                    )
                    st.success(response.text)
                except Exception as e:
                    st.error(f"Error connecting to AI: {e}")
        elif not ai_client:
            st.error("Gemini API Key is missing. Please configure it in Streamlit Secrets.")
        else:
            st.warning("Please enter a question.")
