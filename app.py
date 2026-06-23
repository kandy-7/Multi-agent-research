import os
import streamlit as st

from src.graph.workflow import graph

st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🤖"
)

st.title("🤖 AI Research Agent")

topic = st.text_input(
    "Research Topic"
)

if st.button("Start Research"):

    if not topic.strip():
        st.warning("Please enter a research topic.")
        st.stop()

    with st.spinner("Researching..."):

        result = graph.invoke(
            {
                "topic": topic
            }
        )

    st.markdown(result["report"])

    os.makedirs(
        "data/reports",
        exist_ok=True
    )

    filename = (
        topic.replace(" ", "_")
        .replace("/", "_")
        + ".md"
    )

    filepath = os.path.join(
        "data/reports",
        filename
    )

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            result["report"]
        )

    st.success(
        f"Report saved: {filename}"
    )

    st.download_button(
        "📥 Download Report",
        result["report"],
        file_name=filename
    )