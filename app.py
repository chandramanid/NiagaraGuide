import streamlit as st

st.set_page_config(page_title="FallsGuide: Niagara Falls All-in-One", page_icon="📍", layout="wide")

# Multilingual Translations Dictionary
translations = {
    "English": {
        "title": "📍 FallsGuide: Niagara Falls Complete Assistant",
        "subtitle": "Your ultimate guide for transit, top attractions, hotels, dining, and weather.",
        "tab_transit": "🚌 Transit & Fares",
        "tab_places": "🗺️ Attractions & Map",
        "tab_stay": "🏨 Hotels & Dining",
        "tab_weather": "🌤️ Weather",
        "tab_chat": "🤖 Multilingual AI Chat",
    },
    "French": {
        "title": "📍 FallsGuide : Assistant Complet de Niagara",
        "subtitle": "Votre guide ultime pour le transport, les attractions, les hôtels et la météo.",
        "tab_transit": "🚌 Transport & Tarifs",
        "tab_places": "🗺️ Attractions & Carte",
        "tab_stay": "🏨 Hôtels & Restos",
        "tab_weather": "🌤️ Météo",
        "tab_chat": "🤖 Chat IA Multilingue",
    },
    "Hindi": {
        "title": "📍 FallsGuide: नियाग्रा फॉल्स संपूर्ण सहायक",
        "subtitle": "परिवहन, आकर्षण, होटल और मौसम के लिए आपकी संपूर्ण मार्गदर्शिका।",
        "tab_transit": "🚌 पारगमन और किराया",
        "tab_places": "🗺️ आकर्षण और नक्शा",
        "tab_stay": "🏨 होटल और भोजन",
        "tab_weather": "🌤️ मौसम",
        "tab_chat": "🤖 बहुभाषी AI चैट",
    },
    "Punjabi": {
        "title": "📍 FallsGuide: ਨਿਆਗਰਾ ਫਾਲ્સ ਪੂਰਾ ਸਹਾਇਕ",
        "subtitle": "ਆਵਾਜਾਈ, ਆਕਰਸ਼ਣ, ਹੋਟਲ ਅਤੇ ਮੌਸਮ ਲਈ ਤੁਹਾਡੀ ਗਾਈਡ।",
        "tab_transit": "🚌 ਆਵਾਜਾਈ ਅਤੇ ਕਿਰਾਏ",
        "tab_places": "🗺️ ਸਥਾਨ ਅਤੇ ਨਕਸ਼ਾ",
        "tab_stay": "🏨 ਹੋਟਲ ਅਤੇ ਖਾਣਾ",
        "tab_weather": "🌤️ ਮੌਸਮ",
        "tab_chat": "🤖 ਬਹੁ-ਭাষਾਈ AI ਚੈਟ",
    },
    "Nepali": {
        "title": "📍 FallsGuide: नियाग्रा फल्स पूर्ण सहायक",
        "subtitle": "यातायात, आकर्षण, होटल र मौसमका लागि तपाईंको गाइड।",
        "tab_transit": "🚌 यातायात र भाडा",
        "tab_places": "🗺️ आकर्षण र नक्सा",
        "tab_stay": "🏨 होटल र खाना",
        "tab_weather": "🌤️ मौसम",
        "tab_chat": "🤖 बहुभाषी AI च्याट",
    },
    "Spanish": {
        "title": "📍 FallsGuide: Asistente Completo de Niágara",
        "subtitle": "Tu guía definitiva para transporte, atracciones, hoteles y clima.",
        "tab_transit": "🚌 Transporte y Tarifas",
        "tab_places": "🗺️ Atracciones y Mapa",
        "tab_stay": "🏨 Hoteles y Comida",
        "tab_weather": "🌤️ Clima",
        "tab_chat": "🤖 Chat IA Multilingüe",
    },
    "Chinese": {
        "title": "📍 FallsGuide：尼亚加拉大瀑布综合助手",
        "subtitle": "您出行的交通、景点、酒店、美食和天气指南。",
        "tab_transit": "🚌 交通与票价",
        "tab_places": "🗺️ 景点与地图",
        "tab_stay": "🏨 酒店与餐饮",
        "tab_weather": "🌤️ 天气",
        "tab_chat": "🤖 多语言AI聊天",
    },
    "Philippine (Tagalog)": {
        "title": "📍 FallsGuide: Kumpletong Katulong sa Niagara Falls",
        "subtitle": "Ang iyong gabay sa transportasyon, mga pasyalan, at panahon.",
        "tab_transit": "🚌 Transportasyon at Bayad",
        "tab_places": "🗺️ Pasyalan at Mapa",
        "tab_stay": "🏨 Mga Hotel at Kainan",
        "tab_weather": "🌤️ Panahon",
        "tab_chat": "🤖 Multilingual AI Chat",
    },
    "Korean": {
        "title": "📍 FallsGuide: 나이아가라 폭포 종합 어시스턴트",
        "subtitle": "교통, 명소, 호텔, 맛집, 날씨를 위한 완벽한 가이드.",
        "tab_transit": "🚌 교통 및 요금",
        "tab_places": "🗺️ 명소 및 지도",
        "tab_stay": "🏨 호텔 및 식당",
        "tab_weather": "🌤️ 날씨",
        "tab_chat": "🤖 다국어 AI 채팅",
    },
    "Japanese": {
        "title": "📍 FallsGuide：ナイアガラ総合アシスタント",
        "subtitle": "交通、観光地、ホテル、グルメ、天気の完全ガイド。",
        "tab_transit": "🚌 交通機関と料金",
        "tab_places": "🗺️ 観光地とマップ",
        "tab_stay": "🏨 ホテルとレストラン",
        "tab_weather": "🌤️ 天気",
        "tab_chat": "🤖 多言語AIチャット",
    }
}

# Sidebar Language Selection
lang = st.sidebar.selectbox("🌐 Choose Language", list(translations.keys()))
t = translations[lang]

st.title(t["title"])
st.write(t["subtitle"])
st.divider()

# Create App Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    t["tab_transit"], 
    t["tab_places"], 
    t["tab_stay"], 
    t["tab_weather"], 
    t["tab_chat"]
])

# --- TAB 1: TRANSIT & FARES ---
with tab1:
    st.subheader("🚌 Niagara Regional Transit (NRT) & Taxi Guide")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🎫 Local Bus Fares & Rules")
        st.write("- *Adults (18-64), Seniors (65+), Youth (13-17):* $3.50 CAD per single ride.")
        st.write("- *Children (12 and under):* Ride *Free*.")
        st.write("- *Transfer Window:* Valid for *2 hours* of unlimited transfers in any direction.")
        st.warning("⚠️ *Cash Policy:* Onboard cash requires exact change in coins or paper bills (US currency accepted at par). Drivers cannot make change, and card tapping is unavailable on older buses.")
        st.info("📱 *Required App:* Download the *Transit* app to purchase mobile tickets/passes and view live bus tracking.")

    with col2:
        st.markdown("### 🚖 Taxi & Rideshare Information")
        st.write("- *Local Taxis (e.g., Niagara Falls Taxi, Central Taxi):* Standard flag-drop base rates start around $4.50 - $5.00 CAD, with per-kilometer charges averaging $2.00 - $2.50 CAD.")
        st.write("- *Uber & Lyft:* Widely available throughout the tourist district and GO station, dynamically priced based on demand.")
        st.write("- Tip: Taxis from the WEGO Hub to Clifton Hill typically range from $10 to $15 CAD depending on traffic.")

# --- TAB 2: ATTRACTIONS & MAP ---
with tab2:
    st.subheader("🗺️ Top Locations to Visit in Niagara Falls")
    
    attractions = {
        "Horseshoe Falls": {"lat": 43.0782, "lon": -79.0747, "desc": "The largest of the three waterfalls making up Niagara Falls."},
        "Clifton Hill": {"lat": 43.0906, "lon": -79.0718, "desc": "Famous street packed with attractions, arcades, and the Niagara SkyWheel."},
        "Skylon Tower": {"lat": 43.0853, "lon": -79.0837, "desc": "Observation tower offering panoramic 360-degree views of the Falls."},
        "Journey Behind the Falls": {"lat": 43.0801, "lon": -79.0772, "desc": "Portals cut straight through the rock leading behind the roaring water."}
    }

    selected_place = st.selectbox("Select an attraction to view details:", list(attractions.keys()))
    
    st.write(f"*Description:* {attractions[selected_place]['desc']}")
    
    # Google Maps Integration via Streamlit Map View
    import pandas as pd
    map_data = pd.DataFrame({
        'lat': [attractions[selected_place]['lat']],
        'lon': [attractions[selected_place]['lon']]
    })
    st.map(map_data, zoom=14)

# --- TAB 3: HOTELS & DINING ---
with tab3:
    st.subheader("🏨 Nearby Hotels & Restaurants (Google Review Ratings)")
    
    h_col1, h_col2 = st.columns(2)
    
    with h_col1:
        st.markdown("### 🏨 Recommended Hotels")
        st.write("1. *Marriott Fallsview Hotel & Spa*")
        st.write("   - ⭐ *Google Rating:* 4.5 / 5")
        st.write("   - Highlight: Direct, unobstructed views of the Horseshoe Falls.")
        st.write("2. *Sheraton Fallsview Hotel*")
        st.write("   - ⭐ *Google Rating:* 4.3 / 5")
        st.write("   - Highlight: Connected to the Fallsview Indoor Waterpark.")

    with h_col2:
        st.markdown("### 🍽️ Recommended Restaurants")
        st.write("1. *Prime Steakhouse Niagara Falls*")
        st.write("   - ⭐ *Google Rating:* 4.7 / 5")
        st.write("   - Highlight: Fine dining with a floor-to-ceiling view of the illumination.")
        st.write("2. *The Rainbow Room by Massimo Capra*")
        st.write("   - ⭐ *Google Rating:* 4.4 / 5")
        st.write("   - Highlight: Italian cuisine overlooking the gorge.")

# --- TAB 4: WEATHER CONDITIONS ---
with tab4:
    st.subheader("🌤️ Live Niagara Falls Weather Conditions")
    st.info("Current Season Overview: Niagara Falls experiences warm summers (averaging 25°C) and snowy winters. Dress in layers if visiting the mist-heavy boat tours!")
    
    col_w1, col_w2, col_w3 = st.columns(3)
    col_w1.metric("Temperature", "22°C", "Pleasant")
    col_w2.metric("Condition", "Partly Cloudy", "Good for walking")
    col_w3.metric("Mist Spray Impact", "High near Falls", "Ponchos recommended")

# --- TAB 5: MULTILINGUAL AI CHAT ---
with tab5:
    st.subheader("🤖 Multilingual AI Transit & Tourism Assistant")
    user_query = st.text_input("Ask any question about transit, fares, hotels, or directions:")
    if st.button("Ask Assistant"):
        if user_query:
            st.success(f"*Assistant Reply:* I received your question: '{user_query}'. As your FallsGuide AI, remember that local buses cost $3.50 CAD, require exact change if paying cash, and can be tracked using the Transit app!")
        else:
            st.warning("Please type a question first.")
