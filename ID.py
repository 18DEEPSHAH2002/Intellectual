import streamlit as st
from fpdf import FPDF

# ========================
# 1. Questions in Multiple Languages
# ========================
questions = {
    "English": [
        "Does your child take longer than peers to learn basic skills (reading, math, writing)?",
        "Does your child often need instructions repeated or simplified?",
        "Does your child forget what they learned even after practice?",
        "Does your child struggle with problem-solving or planning tasks?",
        "Does your child find it difficult to start or maintain conversations?",
        "Does your child struggle to understand jokes, sarcasm, or hidden meanings?",
        "Does your child find it hard to make or keep friends?",
        "Does your child sometimes miss social rules like taking turns or respecting personal space?",
        "Did your child learn toilet training, dressing, or bathing later than expected?",
        "Does your child still need help with self-care (brushing teeth, bathing, eating)?",
        "Does your child need frequent reminders for daily routines?",
        "Does your child struggle with money, time, or following schedules?",
        "Does your child sometimes act without thinking about safety (crossing roads, trusting strangers)?",
        "Does your child get distracted very easily?",
        "Does your child struggle to manage emotions in daily life?",
        "Does your child need extra help to plan or organize tasks?",
        "Did your child achieve big milestones (walking, talking) later than peers?",
        "Was your child born prematurely or had medical complications?",
        "Does your child have seizures, frequent illnesses, or neurological issues?",
        "Has a doctor ever mentioned a genetic condition (Down syndrome, Fragile X, etc.)?"
    ],
    "हिन्दी": [
        "क्या आपका बच्चा पढ़ाई, गणित या लिखाई जैसी बुनियादी चीजें सीखने में साथियों से अधिक समय लेता है?",
        "क्या आपके बच्चे को बार-बार निर्देश दोहराने या सरल बनाने की आवश्यकता होती है?",
        "क्या आपका बच्चा सीखी हुई बातें जल्दी भूल जाता है?",
        "क्या आपके बच्चे को समस्या हल करने या योजना बनाने में कठिनाई होती है?",
        "क्या आपके बच्चे को बातचीत शुरू करने या बनाए रखने में कठिनाई होती है?",
        "क्या आपका बच्चा मज़ाक, व्यंग्य या छिपे अर्थ समझने में कठिनाई महसूस करता है?",
        "क्या आपके बच्चे को दोस्त बनाने या उन्हें बनाए रखने में कठिनाई होती है?",
        "क्या आपका बच्चा कभी-कभी सामाजिक नियमों (जैसे बारी लेना, निजी दूरी) का पालन नहीं करता?",
        "क्या आपके बच्चे ने टॉयलेट ट्रेनिंग, कपड़े पहनना या नहाना देर से सीखा?",
        "क्या आपके बच्चे को अभी भी स्वयं देखभाल (ब्रश करना, नहाना, खाना) में मदद की ज़रूरत है?",
        "क्या आपके बच्चे को रोज़ाना की दिनचर्या के लिए बार-बार याद दिलाने की आवश्यकता होती है?",
        "क्या आपके बच्चे को पैसे, समय या समय-सारणी समझने में कठिनाई होती है?",
        "क्या आपका बच्चा कभी-कभी सुरक्षा का ध्यान नहीं रखता (सड़क पार करना, अजनबियों पर भरोसा करना)?",
        "क्या आपका बच्चा बहुत आसानी से ध्यान भटकाता है?",
        "क्या आपके बच्चे को भावनाओं को संभालने में कठिनाई होती है?",
        "क्या आपके बच्चे को काम की योजना बनाने या व्यवस्थित करने में मदद की ज़रूरत होती है?",
        "क्या आपके बच्चे ने बड़े मील के पत्थर (चलना, बोलना) साथियों से देर से हासिल किए?",
        "क्या आपका बच्चा समय से पहले पैदा हुआ था या जन्म के समय कोई जटिलता थी?",
        "क्या आपके बच्चे को दौरे (seizures), बार-बार बीमारियाँ या तंत्रिका संबंधी समस्याएँ होती हैं?",
        "क्या डॉक्टर ने कभी किसी आनुवंशिक समस्या (जैसे डाउन सिंड्रोम, फ्रैजाइल एक्स) का ज़िक्र किया है?"
    ],
    "ਪੰਜਾਬੀ": [
        "ਕੀ ਤੁਹਾਡਾ ਬੱਚਾ ਪੜ੍ਹਾਈ, ਗਣਿਤ ਜਾਂ ਲਿਖਣ ਵਰਗੀਆਂ ਬੁਨਿਆਦੀ ਚੀਜ਼ਾਂ ਸਿੱਖਣ ਵਿੱਚ ਹੋਰ ਬੱਚਿਆਂ ਨਾਲੋਂ ਵੱਧ ਸਮਾਂ ਲੈਂਦਾ ਹੈ?",
        "ਕੀ ਤੁਹਾਡੇ ਬੱਚੇ ਨੂੰ ਹਦਾਇਤਾਂ ਵਾਰ-ਵਾਰ ਦੁਹਰਾਉਣ ਜਾਂ ਸਧਾਰਨ ਕਰਨ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ?",
        "ਕੀ ਤੁਹਾਡਾ ਬੱਚਾ ਸਿੱਖੀਆਂ ਗੱਲਾਂ ਜਲਦੀ ਭੁੱਲ ਜਾਂਦਾ ਹੈ?",
        "ਕੀ ਤੁਹਾਡੇ ਬੱਚੇ ਨੂੰ ਸਮੱਸਿਆ ਹੱਲ ਕਰਨ ਜਾਂ ਯੋਜਨਾ ਬਣਾਉਣ ਵਿੱਚ ਮੁਸ਼ਕਲ ਆਉਂਦੀ ਹੈ?",
        "ਕੀ ਤੁਹਾਡੇ ਬੱਚੇ ਨੂੰ ਗੱਲਬਾਤ ਸ਼ੁਰੂ ਕਰਨ ਜਾਂ ਜਾਰੀ ਰੱਖਣ ਵਿੱਚ ਮੁਸ਼ਕਲ ਹੁੰਦੀ ਹੈ?",
        "ਕੀ ਤੁਹਾਡੇ ਬੱਚੇ ਨੂੰ ਮਜ਼ਾਕ, ਵਿਆੰਗ ਜਾਂ ਲੁਕਵੇਂ ਅਰਥ ਸਮਝਣ ਵਿੱਚ ਮੁਸ਼ਕਲ ਹੁੰਦੀ ਹੈ?",
        "ਕੀ ਤੁਹਾਡੇ ਬੱਚੇ ਨੂੰ ਦੋਸਤੀ ਬਣਾਉਣ ਜਾਂ ਕਾਇਮ ਰੱਖਣ ਵਿੱਚ ਮੁਸ਼ਕਲ ਹੁੰਦੀ ਹੈ?",
        "ਕੀ ਤੁਹਾਡਾ ਬੱਚਾ ਕਈ ਵਾਰ ਸਮਾਜਕ ਨਿਯਮਾਂ (ਜਿਵੇਂ ਵਾਰੀ ਲੈਣਾ, ਨਿੱਜੀ ਜਗ੍ਹਾ) ਦੀ ਪਾਲਣਾ ਨਹੀਂ ਕਰਦਾ?",
        "ਕੀ ਤੁਹਾਡੇ ਬੱਚੇ ਨੇ ਟਾਇਲਟ ਟ੍ਰੇਨਿੰਗ, ਕੱਪੜੇ ਪਹਿਨਣ ਜਾਂ ਨ੍ਹਾਉਣ ਦੇਰ ਨਾਲ ਸਿੱਖਿਆ?",
        "ਕੀ ਤੁਹਾਡੇ ਬੱਚੇ ਨੂੰ ਅਜੇ ਵੀ ਸਵੈ-ਦੇਖਭਾਲ (ਬਰਸ਼ ਕਰਨਾ, ਨ੍ਹਾਉਣਾ, ਖਾਣਾ) ਵਿੱਚ ਮਦਦ ਦੀ ਲੋੜ ਹੈ?",
        "ਕੀ ਤੁਹਾਡੇ ਬੱਚੇ ਨੂੰ ਰੋਜ਼ਾਨਾ ਦੀਆਂ ਗਤੀਵਿਧੀਆਂ ਲਈ ਵਾਰ-ਵਾਰ ਯਾਦ ਦਿਵਾਉਣ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ?",
        "ਕੀ ਤੁਹਾਡੇ ਬੱਚੇ ਨੂੰ ਪੈਸੇ, ਸਮਾਂ ਜਾਂ ਟਾਈਮ-ਟੇਬਲ ਸਮਝਣ ਵਿੱਚ ਮੁਸ਼ਕਲ ਹੁੰਦੀ ਹੈ?",
        "ਕੀ ਤੁਹਾਡਾ ਬੱਚਾ ਕਈ ਵਾਰ ਸੁਰੱਖਿਆ ਦਾ ਧਿਆਨ ਨਹੀਂ ਰੱਖਦਾ (ਸੜਕ ਪਾਰ ਕਰਨਾ, ਅਜਨਬੀਆਂ 'ਤੇ ਭਰੋਸਾ ਕਰਨਾ)?",
        "ਕੀ ਤੁਹਾਡੇ ਬੱਚੇ ਦਾ ਧਿਆਨ ਬਹੁਤ ਆਸਾਨੀ ਨਾਲ ਭਟਕ ਜਾਂਦਾ ਹੈ?",
        "ਕੀ ਤੁਹਾਡੇ ਬੱਚੇ ਨੂੰ ਭਾਵਨਾਵਾਂ ਨੂੰ ਸੰਭਾਲਣ ਵਿੱਚ ਮੁਸ਼ਕਲ ਹੁੰਦੀ ਹੈ?",
        "ਕੀ ਤੁਹਾਡੇ ਬੱਚੇ ਨੂੰ ਕੰਮ ਦੀ ਯੋਜਨਾ ਬਣਾਉਣ ਜਾਂ ਵਿਵਸਥਿਤ ਕਰਨ ਵਿੱਚ ਮਦਦ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ?",
        "ਕੀ ਤੁਹਾਡੇ ਬੱਚੇ ਨੇ ਵੱਡੇ ਵਿਕਾਸੀ ਮੀਲ-ਪੱਥਰ (ਤੁਰਨਾ, ਬੋਲਣਾ) ਹੋਰਾਂ ਨਾਲੋਂ ਦੇਰ ਨਾਲ ਪ੍ਰਾਪਤ ਕੀਤੇ?",
        "ਕੀ ਤੁਹਾਡਾ ਬੱਚਾ ਸਮੇਂ ਤੋਂ ਪਹਿਲਾਂ ਪੈਦਾ ਹੋਇਆ ਸੀ ਜਾਂ ਜਨਮ ਸਮੇਂ ਕੋਈ ਮੁਸ਼ਕਲ ਆਈ ਸੀ?",
        "ਕੀ ਤੁਹਾਡੇ ਬੱਚੇ ਨੂੰ ਦੌਰੇ (seizures), ਬਾਰ-ਬਾਰ ਬਿਮਾਰੀਆਂ ਜਾਂ ਨਰਵਸ ਸਿਸਟਮ ਦੀਆਂ ਸਮੱਸਿਆਵਾਂ ਹੁੰਦੀਆਂ ਹਨ?",
        "ਕੀ ਡਾਕਟਰ ਨੇ ਕਦੇ ਕਿਸੇ ਜੈਨੇਟਿਕ ਸਮੱਸਿਆ (ਜਿਵੇਂ ਡਾਊਨ ਸਿੰਡਰੋਮ, ਫ੍ਰੈਜਾਈਲ ਐਕਸ) ਦਾ ਜ਼ਿਕਰ ਕੀਤਾ ਹੈ?"
    ]
}

# ========================
# 2. Streamlit UI
# ========================
st.title("🧸 Intellectual Disability Parent Screening Tool")
language = st.selectbox("Choose Language / भाषा चुनें / ਭਾਸ਼ਾ ਚੁਣੋ", ["English", "हिन्दी", "ਪੰਜਾਬੀ"])

responses = []
options = {"Yes": 2, "Sometimes": 1, "No": 0}

st.write("Please answer the following questions:")

for i, q in enumerate(questions[language], 1):
    response = st.radio(f"{i}. {q}", list(options.keys()), key=i)
    responses.append((q, response, options[response]))

# ========================
# 3. Calculate Score
# ========================
if st.button("Submit"):
    total_score = sum(r[2] for r in responses)

    # Interpretation
    if total_score <= 10:
        result = "Low Concern – Mostly on track, but monitor if worries continue."
    elif total_score <= 20:
        result = "Mild Concern – Some challenges noticed. Discuss with a teacher or pediatrician."
    elif total_score <= 30:
        result = "Moderate Concern – Multiple difficulties. Professional evaluation recommended."
    else:
        result = "High Concern – Strong signs. Seek developmental specialist evaluation."

    st.success(f"✅ Total Score: {total_score} / {len(responses)*2}")
    st.info(f"Result: {result}")

    # ========================
    # 4. Generate PDF
    # ========================
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Intellectual Disability Screening Report", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Language: {language}", ln=True, align="L")
    pdf.ln(5)

    for idx, (q, ans, sc) in enumerate(responses, 1):
        pdf.multi_cell(0, 10, f"{idx}. {q}\nAnswer: {ans}\n")
    
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Total Score: {total_score} / {len(responses)*2}", ln=True)
    pdf.multi_cell(0, 10, f"Result: {result}")

    pdf_output = "screening_report.pdf"
    pdf.output(pdf_output)

    with open(pdf_output, "rb") as file:
        st.download_button("📥 Download Report (PDF)", file, file_name=pdf_output, mime="application/pdf")
