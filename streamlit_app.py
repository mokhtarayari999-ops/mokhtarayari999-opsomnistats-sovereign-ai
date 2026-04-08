import streamlit as st
import random

# 1. إعدادات الصفحة والعنوان
st.set_page_config(page_title="Arabic Pro | تحليل المباريات", page_icon="⚽", layout="wide")

# 2. تنسيق الواجهة للعربية (RTL)
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: RTL; text-align: right;
    }
    .stNumberInput, .stSelectbox { direction: RTL; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚽ محلل المباريات الذكي - Arabic Pro")
st.write("أهلاً بك في نظام التوقع السيادي للمباريات (Sovereign Predictor)")

# 3. مدخلات المباراة
col1, col2 = st.columns(2)

with col1:
    home_team = st.text_input("الفريق المضيف", "الأهلي")
    home_rank = st.number_input("ترتيب المضيف في الدوري", min_value=1, value=1)
    home_form = st.slider("مستوى الفريق المضيف (آخر 5 مباريات)", 0, 100, 70)

with col2:
    away_team = st.text_input("الفريق الضيف", "الزمالك")
    away_rank = st.number_input("ترتيب الضيف في الدوري", min_value=1, value=2)
    away_form = st.slider("مستوى الفريق الضيف (آخر 5 مباريات)", 0, 100, 65)

# 4. منطق التحليل (الخوارزمية البسيطة)
st.divider()
if st.button("تحليل المباراة وإظهار التوقعات"):
    with st.spinner('جاري تحليل البيانات الإحصائية...'):
        # معادلة بسيطة للتوقع (يمكن تطويرها بربطها بـ AI حقيقي)
        score_home = (100 - home_rank) + (home_form * 0.5) + 10 # 10 نقاط عامل الأرض
        score_away = (100 - away_rank) + (away_form * 0.5)
        
        total = score_home + score_away
        win_prob = round((score_home / total) * 100, 1)
        draw_prob = 25 # نسبة افتراضية للتعادل
        loss_prob = round(100 - win_prob - draw_prob, 1)

        # 5. عرض النتائج
        st.subheader(f"📊 نتائج التحليل: {home_team} vs {away_team}")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("فوز " + home_team, f"{win_prob}%")
        c2.metric("تعادل", f"{draw_prob}%")
        c3.metric("فوز " + away_team, f"{loss_prob}%")

        # نصيحة المحلل
        if win_prob > 50:
            st.success(f"💡 نصيحة Arabic Pro: الأفضلية تميل لـ {home_team} بناءً على الترتيب وعامل الأرض.")
        elif loss_prob > 50:
            st.success(f"💡 نصيحة Arabic Pro: {away_team} يمتلك فرصة قوية جداً للفوز خارج دياره.")
        else:
            st.warning("💡 نصيحة Arabic Pro: المباراة متكافئة جداً، قد تنتهي بالتعادل.")

# 6. قسم التاريخ والإحصائيات
st.sidebar.header("إعدادات المحلل")
st.sidebar.info("هذا النظام يستخدم خوارزميات Arabic Pro لتحليل أداء الفرق.")
if st.sidebar.checkbox("عرض إحصائيات متقدمة"):
    st.sidebar.write("قوة الهجوم: 85% | قوة الدفاع: 70%")

st.divider()
st.caption("حقوق الطبع محفوظة - فريق Arabic Pro الرياضي 2024")
        
