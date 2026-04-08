import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعدادات الصفحة والواجهة الفاخرة
st.set_page_config(page_title="Arabic Pro | التوقعات الذهبية", page_icon="⚽", layout="wide")

# 2. تصميم CSS (الأسود والذهبي) مع دعم RTL
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    /* الخلفية والنصوص الأساسية */
    .stApp {
        background-color: #0e1117;
        color: #e5e5e5;
        font-family: 'Cairo', sans-serif;
        direction: RTL;
        text-align: right;
    }
    
    /* العناوين باللون الذهبي */
    h1, h2, h3, .stMetric label {
        color: #D4AF37 !important;
        text-shadow: 2px 2px 4px #000000;
    }
    
    /* تنسيق الأزرار الذهبية */
    .stButton>button {
        background-color: #D4AF37;
        color: #000;
        border-radius: 10px;
        font-weight: bold;
        border: 1px solid #D4AF37;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #B8860B;
        color: white;
    }
    
    /* تنسيق المدخلات */
    input, .stSelectbox, .stNumberInput {
        background-color: #1a1c23 !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. العنوان الرئيسي
st.title("🏆 ARABIC PRO | محلل التوقعات الذهبي")
st.write("---")

# 4. تهيئة سجل النتائج في ذاكرة المتصفح
if "history" not in st.session_state:
    st.session_state.history = []

# 5. منطقة إدخال بيانات المباراة
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏠 الفريق المضيف")
    home_team = st.text_input("اسم الفريق", "ريال مدريد")
    home_power = st.slider("قوة الهجوم (%)", 0, 100, 85, key="h_p")

with col2:
    st.markdown("### ✈️ الفريق الضيف")
    away_team = st.text_input("اسم الفريق ", "برشلونة")
    away_power = st.slider("قوة الدفاع (%)", 0, 100, 75, key="a_p")

# 6. منطق التوقع وعرض النتيجة
if st.button("✨ تشغيل التحليل الذهبي"):
    # حساب احتمالية بسيطة (خوارزمية Arabic Pro)
    total_power = home_power + away_power
    win_prob = round((home_power / total_power) * 100, 1)
    loss_prob = round(100 - win_prob, 1)
    
    # النتيجة المتوقعة (عشوائية ذكية بناءً على القوة)
    predicted_score = f"{random.randint(1,3)} - {random.randint(0,2)}" if win_prob > 50 else f"{random.randint(0,2)} - {random.randint(1,3)}"
    
    # عرض النتائج في بطاقات ذهبية
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    c1.metric("احتمالية الفوز", f"{win_prob}%")
    c2.metric("النتيجة المتوقعة", predicted_score)
    c3.metric("احتمالية الخسارة", f"{loss_prob}%")
    
    # 7. إضافة النتيجة إلى سجل النتائج
    new_entry = {
        "التاريخ": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "المباراة": f"{home_team} vs {away_team}",
        "التوقع": predicted_score,
        "نسبة الفوز": f"{win_prob}%"
    }
    st.session_state.history.insert(0, new_entry)

# 8. سجل النتائج (History Log)
st.write("---")
st.subheader("📜 سجل نتائج التحليلات السابقة")
if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)
    st.table(df)
else:
    st.info("لا يوجد نتائج مسجلة بعد. ابدأ أول تحليل الآن!")

# 9. التذييل
st.sidebar.markdown("<h2 style='color:#D4AF37;'>ARABIC PRO</h2>", unsafe_allow_html=True)
st.sidebar.info("نظام التحليل السيادي للمباريات - الإصدار الذهبي 2024")
if st.sidebar.button("🗑️ مسح السجل"):
    st.session_state.history = []
    st.rerun()

st.divider()
st.caption("تم التطوير بواسطة شريكك في البرمجة - Arabic Pro Sovereign Team")
    
