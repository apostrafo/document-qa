import streamlit as st
from transformers import pipeline  # Assuming DeepSeek is a Hugging Face model

# Show title and description.
st.title("📄 Document question answering")
st.write(
    "Upload a document below and ask a question about it – DeepSeek LLM will answer! "
)

# Let the user upload a file via `st.file_uploader`.
uploaded_file = st.file_uploader(
    "Upload a document (.txt or .md)", type=("txt", "md")
)

# Ask the user for a question via `st.text_area`.
question = st.text_area(
    "Now ask a question about the document!",
    placeholder="Can you give me a short summary?",
    disabled=not uploaded_file,
)

if uploaded_file and question:
    # Process the uploaded file and question.
    document = uploaded_file.read().decode()
    prompt = f"Here's a document: {document} \n\n---\n\n {question}"

    # Load the DeepSeek model (replace with the correct model name)
    generator = pipeline("text-generation", model="deepseek-ai/DeepSeek-R1")  # Replace with the actual model name

    # Generate a response using the DeepSeek model
    response = generator(prompt, max_length=500, do_sample=True)

    # Display the response
    st.write("### Answer:")
    st.write(response[0]['generated_text'])