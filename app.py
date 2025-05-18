# app.py
import streamlit as st
from Modules.summarization import TextSummarizer
from Modules.translation import Translator
from Modules.entity_recognition import EntityRecognizer
from Modules.sentiment_analysis import SentimentAnalyzer

# Set page config
st.set_page_config(
    page_title="NLP Suite",
    page_icon=":brain:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS
st.markdown("""
<style>
    :root {
        --primary: #4a90e2;
        --secondary: #6c757d;
        --success: #28a745;
        --danger: #dc3545;
        --light: #f8f9fa;
        --dark: #343a40;
    }

    .reportview-container {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    }

    .sidebar .sidebar-content {
        background: white;
        box-shadow: 2px 0 10px rgba(0,0,0,0.1);
        padding: 1.5rem;
    }

    .task-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        min-height: 500px;
    }

    .task-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.1);
    }

    .stTextArea textarea {
        border-radius: 10px !important;
        border: 2px solid var(--primary) !important;
        transition: border-color 0.3s ease;
    }

    .stTextArea textarea:focus {
        border-color: var(--secondary) !important;
        box-shadow: 0 0 8px rgba(74, 144, 226, 0.2) !important;
    }

    .stButton button {
        width: 100%;
        border-radius: 25px;
        background: var(--primary);
        color: white;
        padding: 0.75rem 1.5rem;
        transition: all 0.3s ease;
        border: none;
    }

    .stButton button:hover {
        background: #357abd;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }

    .success-message {
        padding: 1rem;
        background: #e6f4ea;
        border-left: 4px solid var(--success);
        border-radius: 8px;
        margin: 1rem 0;
        animation: slideIn 0.5s ease;
    }

    @keyframes slideIn {
        from { transform: translateX(20px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }

    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        text-align: center;
    }

    .entity-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        background: var(--light);
        border-radius: 20px;
        margin: 0.25rem;
        font-size: 0.9rem;
    }

    .sidebar-header {
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(135deg, var(--primary), #6c5ce7);
        color: white;
        border-radius: 12px;
        margin-bottom: 1.5rem;
    }

    footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background: var(--dark);
        color: white;
        padding: 1rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Initialize modules with caching
@st.cache_resource
def load_models():
    return {
        'summarizer': TextSummarizer(),
        'translator': Translator(),
        'entity_recognizer': EntityRecognizer(),
        'sentiment_analyzer': SentimentAnalyzer()
    }

def main():
    # Sidebar with image and module selection
    with st.sidebar:
        st.image("hf.png", use_column_width=True)
        task = st.selectbox(
            "Choose Task",
            ["Text Summarization", "Translation", "Entity Recognition", "Sentiment Analysis"],
            key='task_selector'
        )
        st.markdown("---")
        st.markdown('<div class="sidebar-header"><h1>NLP Suite</h1><p>Advanced Text Processing Toolkit</p><p>Version 1.0.0</p></div>', unsafe_allow_html=True)
    
    models = load_models()
    

    st.markdown(f"## {task}")


    TEXT_AREA_HEIGHT = 250
    COLUMN_RATIO = [1, 1]

    with st.container():
        if task == "Text Summarization":
            col1, col2 = st.columns(COLUMN_RATIO, gap="large")
            with col1:
                with st.container():
                    st.markdown("### Input Text")
                    input_text = st.text_area("", height=TEXT_AREA_HEIGHT, label_visibility="collapsed")
                    
                    # Button moved inside the container and column context
                    if st.button("✨ Generate Summary", key="summarize_btn"):
                        with st.spinner("Analyzing content..."):
                            try:
                                summary = models['summarizer'].summarize(input_text)
                                with col2:
                                    with st.container():
                                        st.markdown("### Summary")
                                        st.text_area("", summary, height=TEXT_AREA_HEIGHT, label_visibility="collapsed")
                                        st.markdown('<div class="success-message">✅ Summary generated successfully!</div>', unsafe_allow_html=True)
                            except Exception as e:
                                st.error(f"⚠️ Error: {str(e)}")

        elif task == "Translation":
            col1, col2 = st.columns(COLUMN_RATIO, gap="large")
            with col1:
                with st.container():
                    st.markdown("### English Text")
                    input_text = st.text_area("", height=TEXT_AREA_HEIGHT, label_visibility="collapsed")
                    if st.button("🌐 Translate to Hindi", key="translate_btn"):
                        with st.spinner("Translating..."):
                            try:
                                translation = models['translator'].translate(input_text)
                                with col2:
                                    with st.container():
                                        st.markdown("### Hindi Translation")
                                        st.text_area("", translation, height=TEXT_AREA_HEIGHT, label_visibility="collapsed")
                                        st.markdown('<div class="success-message">✅ Translation completed!</div>', unsafe_allow_html=True)
                            except Exception as e:
                                st.error(f"⚠️ Error: {str(e)}")

        elif task == "Entity Recognition":
            col1, col2 = st.columns(COLUMN_RATIO, gap="large")
            with col1:
                with st.container():
                    st.markdown("### Input Text")
                    input_text = st.text_area("", height=TEXT_AREA_HEIGHT, label_visibility="collapsed")
                    if st.button("🔍 Extract Entities", key="ner_btn"):
                        with st.spinner("Processing..."):
                            try:
                                entities = models['entity_recognizer'].get_entities(input_text)
                                with col2:
                                    with st.container():
                                        st.markdown("### Detected Entities")
                                        if entities:
                                            for entity, label in entities:
                                                st.markdown(f'<div class="entity-badge">{entity} <small>({label})</small></div>', unsafe_allow_html=True)
                                            st.markdown('<div class="success-message">✅ Found {0} entities!</div>'.format(len(entities)), unsafe_allow_html=True)
                                        else:
                                            st.info("ℹ️ No entities found in the text")
                            except Exception as e:
                                st.error(f"⚠️ Error: {str(e)}")

        elif task == "Sentiment Analysis":
            col1, col2 = st.columns(COLUMN_RATIO, gap="large")
            with col1:
                with st.container():
                    st.markdown("### Input Text")
                    input_text = st.text_area("", height=TEXT_AREA_HEIGHT, label_visibility="collapsed")
                    if st.button("🧠 Analyze Sentiment", key="sentiment_btn"):
                        with st.spinner("Evaluating..."):
                            try:
                                result = models['sentiment_analyzer'].analyze(input_text)
                                with col2:
                                    with st.container():
                                        label = result['label']
                                        score = result['score']
                                        emoji = "😊" if "POSITIVE" in label else "😞"
                                        display_label = label.split('_')[-1].capitalize()
                                        
                                        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                                        st.metric(
                                            label="Sentiment",
                                            value=f"{display_label} {emoji}",
                                            help=f"Confidence: {score:.2f}"
                                        )
                                        st.progress(score, text=f"Confidence: {score*100:.1f}%")
                                        st.markdown('</div>', unsafe_allow_html=True)
                                        st.markdown('<div class="success-message">✅ Analysis complete!</div>', unsafe_allow_html=True)
                            except Exception as e:
                                st.error(f"⚠️ Error: {str(e)}")


if __name__ == "__main__":
    main()