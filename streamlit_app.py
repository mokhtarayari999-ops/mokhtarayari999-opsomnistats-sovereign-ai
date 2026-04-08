import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعداد الصفحة والسمة الاحترافية (Black & Gold)
st.set_page_config(page_title="Arabic Pro | محلل المباريات الشامل", layout="wide")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .stApp { background-color: #000000; color: #ffffff; font-family: 'Cairo', sans-serif; direction: RTL; text-align: right; }
    h1, h2, h3 { color: #D4AF37 !important; text-align: center; }
    .stSlider [data-baseweb="slider"] { color: #D4AF37; }
    .stButton>button { 
        background-color: #D4AF37; color: black; font-weight: bold; 
        border-radius: 20px; width: 100%; border: none; height: 3em;
    }
    div[data-testid="stMetric"] { background-color: #1a1a1a; border: 1px solid #D4AF37; padding: 15px; border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏆 ARABIC PRO: نظام التوقيع والتحليل اليدوي")

# 2. تهيئة سجل النتائج (History)
if "match_history" not in st.session_state:
    st.session_state.match_history = []

# 3. واجهة الإدخال اليدوي المفصلة
st.subheader("📝 إدخال بيانات المباراة يدوياً")
col_h, col_a = st.columns(2)

with col_h:
    st.markdown("<h3 style='color:white;'>🏠 الفريق المضيف</h3>", unsafe_allow_html=True)
    home_name = st.text_input("اسم الفريق المضيف", "الأهلي")
    h_attack = st.slider("قوة الهجوم (المضيف)", 0, 100, 75)
    h_defense = st.slider("قوة الدفاع (المضيف)", 0, 100, 70)
    h_mid = st.slider("قوة خط الوسط (المضيف)", 0, 100, 65)

with col_a:
    st.markdown("<h3 style='color:white;'>✈️ الفريق الضيف</h3>", unsafe_allow_html=True)
    away_name = st.text_input("اسم الفريق الضيف", "الزمالك")
    a_attack = st.slider("قوة الهجوم (الضيف)", 0, 100, 70)
    a_defense = st.slider("قوة الدفاع (الضيف)", 0, 100, 75)
    a_mid = st.slider("قوة خط الوسط (الضيف)", 0, 100, 60)

# 4. محرك التحليل (Logic)
st.write("---")
if st.button("✨ تنفيذ التحليل العميق"):
    # حساب القوة الإجمالية بناءً على الهجوم والدفاع والوسط
    home_total = (h_attack * 0.4) + (h_defense * 0.3) + (h_mid * 0.3) + 5  # +5 ميزة الأرض
    away_total = (a_attack * 0.4) + (a_defense * 0.3) + (a_mid * 0.3)
    
    total = home_total + away_total
    win_p = round((home_total / total) * 100, 1)
    loss_p = round(100 - win_p, 1)
    
    # عرض النتائج في البطاقات الذهبية
    c1, c2, c3 = st.columns(3)
    with c1: st.metric(label="فرصة فوز " + home_name, value=f"{win_p}%")
    with c2: st.metric(label="النتيجة المتوقعة", value=f"{int(h_attack/30)}-{int(a_attack/35)}")
    with c3: st.metric(label="فرصة فوز " + away_name, value=f"{loss_p}%")
    
    # إضافة النتيجة للسجل
    st.session_state.match_history.append({
        "الوقت": datetime.now().strftime("%H:%M:%S"),
        "المباراة": f"{home_name} vs {away_name}",
        "التوقع": f"{int(h_attack/30)}-{int(a_attack/35)}",
        "الأفضلية": home_name if win_p > loss_p else away_name
    })

# 5. سجل النتائج (كل ما بنيناه سوياً)
st.write("---")
st.subheader("📜 سجل نتائج التحليلات")
if st.session_state.match_history:
    df = pd.DataFrame(st.session_state.match_history)
    st.table(df)
else:
    st.info("السجل فارغ حالياً، ابدأ بإدخال بيانات أول مباراة.")

# الجانب الجانبي (Sidebar)
st.sidebar.markdown("<h2 style='color:#D4AF37;'>ARABIC PRO AI</h2>", unsafe_allow_html=True)
st.sidebar.write("نظام تحليل سيادي خاص")
if st.sidebar.button("🗑️ تفريغ السجل"):
    st.session_state.match_history = []
    st.rerun()
    
