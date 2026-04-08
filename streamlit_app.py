import streamlit as st

# 1. إعدادات الصفحة الأساسية لدعم اللغة العربية
st.set_page_config(
    page_title="Arabic Pro | Sovereign AI",
    page_icon="🤖",
    layout="centered"
)

# 2. كود CSS لتنسيق الواجهة من اليمين لليار (RTL) وتحسين الخطوط العربية
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    html, body, [class*="css"], .stMarkdown {
        font-family: 'Tajawal', sans-serif;
        direction: RTL;
        text-align: right;
    }
    
    /* تنسيق صندوق الإدخال ليكون عربياً */
    .stTextInput > div > div > input {
        text-align: right;
        direction: RTL;
    }
    
    /* تنسيق الرسائل (User vs Assistant) */
    .stChatMessage {
        direction: RTL;
        text-align: right;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. واجهة المستخدم الرئيسية للمشروع
st.title("🤖 مشروع Arabic Pro")
st.markdown("### مرحباً بك في واجهة **Sovereign AI** المتقدمة")
st.write("لنقم ببناء الذكاء الاصطناعي السيادي باللغة العربية معاً!")

# 4. نظام ذاكرة المحادثة (Session State)
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض سجل المحادثة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. منطقة إدخال المستخدم ومعالجة الردود
if prompt := st.chat_input("أدخل طلبك هنا يا شريكي..."):
    # إضافة رسالة المستخدم للسجل وعرضها
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # رد تجريبي (يمكنك ربط أي نموذج ذكاء اصطناعي هنا)
    with st.chat_message("assistant"):
        response = f"أنا رهن إشارتك في مشروع Arabic Pro. لقد تلقيت رسالتك: '{prompt}'"
        st.markdown(response)
    
    # حفظ رد المساعد في السجل
    st.session_state.messages.append({"role": "assistant", "content": response})

# 6. الشريط الجانبي للإعدادات
with st.sidebar:
    st.title("⚙️ إعدادات المشروع")
    st.info("Arabic Pro: مشروع يهدف لتمكين اللغة العربية برمجياً.")
    if st.button("مسح سجل المحادثة"):
        st.session_state.messages = []
        st.rerun()

st.divider()
st.caption("تم التطوير بواسطة فريق Arabic Pro - Sovereign AI © 2024")
        
