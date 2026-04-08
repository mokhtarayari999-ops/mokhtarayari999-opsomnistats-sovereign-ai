import streamlit as st

# 1. إعدادات الصفحة الأساسية لدعم اللغة العربية
st.set_page_config(
    page_title="Arabic Pro | Sovereign AI",
    page_icon="🤖",
    layout="centered"
)

# 2. حقن كود CSS لتنسيق الواجهة من اليمين لليار (RTL) وتحسين الخطوط
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
    
    /* تنسيق الأزرار والقوائم */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. العنوان والوصف الرئيسي
st.title("🤖 مشروع Arabic Pro")
st.write("مرحباً بك في واجهة **Sovereign AI** المتطورة. لنبدأ بناء المستقبل!")

# 4. إدارة نظام الذاكرة للمحادثة (Session State)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. عرض سجل المحادثة السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. منطق إدخال المستخدم ومعالجة الرد الذكي
if prompt := st.chat_input("أدخل سؤالك هنا يا شريكي..."):
    # إضافة رسالة المستخدم للسجل
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # إنشاء رد تجريبي (يمكنك هنا ربط API الخاص بـ OpenAI أو Gemini)
    with st.chat_message("assistant"):
        response = f"أنا رهن إشارتك في مشروع Arabic Pro. لقد استلمت طلبك: '{prompt}'"
        st.markdown(response)
    
    # حفظ رد المساعد في السجل
    st.session_state.messages.append({"role": "assistant", "content": response})

# 7. التذييل (Footer) لمعلومات المشروع
st.sidebar.title("إعدادات Arabic Pro")
st.sidebar.info("هذا المشروع يهدف لتمكين اللغة العربية في نماذج الذكاء الاصطناعي السيادي.")
if st.sidebar.button("مسح سجل المحادثة"):
    st.session_state.messages = []
    st.rerun()

st.divider()
st.caption("تم التطوير بواسطة فريق Arabic Pro - Sovereign AI © 2024")
