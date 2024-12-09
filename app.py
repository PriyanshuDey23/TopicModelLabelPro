import streamlit as st
from TopicModelLabelPro.helper import *
from TopicModelLabelPro.utils import *
import pandas as pd

# Page config
st.set_page_config(layout="wide")

# Title
st.title("Topic Modeling And Labeling App")

# Choice menu
choice = st.selectbox("Select your choice", ["Select your choice","Text", "Video", "CSV","URL","PDF"])


# For CSV
if choice == "CSV":
    st.subheader("Topic Modeling and Labeling App On CSV")
    upload_csv=st.file_uploader("Upload a CSV File",type="csv")
    num_topics = st.number_input("Enter the Number of Topics", min_value=1, step=1)  # No of topics
    num_words = st.number_input("Enter the Number of Words", min_value=1, step=1)  # No of words

    if upload_csv :
        if st.button("Analyze your CSV"):
            with st.spinner("Analyzing your CSV..."):
                csv_file = upload_csv.name
                with open(os.path.join(csv_file),"wb") as f: 
                    f.write(upload_csv.getbuffer()) 
                print(csv_file)
                df = pd.read_csv(csv_file, encoding= 'unicode_escape')
                st.subheader("Extracted Data From CSV")
                st.dataframe(df)

                # Summarized CSV
                with st.spinner("Performing Summarization..."):
                    st.subheader("The Summarized CSV")
                    summarized_text = summarization(df)
                    st.write(summarized_text)

                # Topics CSV
                with st.spinner("Performing topic modeling..."):
                    text_input=csv_to_string(df)
                    topics = perform_topic_modeling(text_input, num_topics, num_words)
                    st.subheader("Topics in the CSV")
                    topics_result = ""
                    for idx, topic in enumerate(topics, start=1):
                        topics_result += f"Topic {idx}: {', '.join(topic[1])}\n\n"
                    st.write(topics_result)

                # Labeling of text
                with st.spinner("Performing Labeling ..."):
                    st.subheader("Label Topic")
                    text_input=csv_to_string(df)
                    labeled_text = labeling(text_input)
                    st.write(labeled_text)

                # Download options
                result = f"Summarized CSV:\n\n{summarized_text}\n\nTopics in the CSV:\n\n{topics_result}\n\nLabel Topic:\n\n{labeled_text}"
                st.download_button(
                    label="Download Results as TXT",
                    data=convert_to_txt(result),
                    file_name="topic.txt",
                    mime="text/plain",
                )
                st.download_button(
                    label="Download Results as DOCX",
                    data=convert_to_docx(result),
                    file_name="topic.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                )


                



# For Video(Youtube)
if choice == "Video":
    st.subheader("Topic Modeling and Labeling App On Video")
    text_input = st.text_input("Insert your video url ")
    num_topics = st.number_input("Enter the Number of Topics", min_value=1, step=1)  # No of topics
    num_words = st.number_input("Enter the Number of Words", min_value=1, step=1)  # No of words

    # Check if the URL is valid and display the thumbnail
    if text_input:
                    
        # Extract the video ID correctly from both youtube.com and youtu.be URLs
        if "youtube.com" in text_input:
            video_id = text_input.split("v=")[1].split("&")[0]  # Extract video ID after 'v='
        elif "youtu.be" in text_input:
            ideo_id = text_input.split("/")[-1]  # Extract video ID after the last '/'
        else:
            raise ValueError("Invalid YouTube URL format.")
                        
        # Display the video thumbnail
        image=st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)  


    if text_input:
        if st.button("Analyze your Video"):
            with st.spinner("Analyzing your Video..."):
                # Display extracted 
                extracted_text = extract_transcript(text_input)
                st.text_area(f"Extracted Text from {choice}", extracted_text, height=200)

                

                # Summarized Video
                with st.spinner("Performing Summarization..."):
                    st.subheader("The Summarized Video")
                    summarized_text = summarization(extracted_text)
                    st.write(summarized_text)

                # Topics in the video
                with st.spinner("Performing topic modeling..."):
                    topics = perform_topic_modeling(extracted_text, num_topics, num_words)
                    st.subheader("Topics in the Video")
                    topics_result = ""
                    for idx, topic in enumerate(topics, start=1):
                        topics_result += f"Topic {idx}: {', '.join(topic[1])}\n\n"
                    st.write(topics_result)

                # Labeling of video
                with st.spinner("Performing Labeling of Video..."):
                    st.subheader("Label Topic")
                    labeled_text = labeling(extracted_text)
                    st.write(labeled_text)

                # Download options
                result = f"Summarized Video:\n\n{summarized_text}\n\nTopics in the Video:\n\n{topics_result}\n\nLabel Topic:\n\n{labeled_text}"
                st.download_button(
                    label="Download Results as TXT",
                    data=convert_to_txt(result),
                    file_name="topic.txt",
                    mime="text/plain",
                )
                st.download_button(
                    label="Download Results as DOCX",
                    data=convert_to_docx(result),
                    file_name="topic.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                )








# For Text
if choice == "Text":
    st.subheader("Topic Modeling and Labeling App On Text")
    text_input = st.text_area("Insert your Input Text ", height=300)
    num_topics = st.number_input("Enter the Number of Topics", min_value=1, step=1)  # No of topics
    num_words = st.number_input("Enter the Number of Words", min_value=1, step=1)  # No of words

    if text_input:
        if st.button("Analyze your text"):
            with st.spinner("Analyzing your text..."):
                # Display extracted or entered text
                st.text_area(f"Extracted Text from {choice}", text_input, height=200)

                # Summarized text
                with st.spinner("Performing Summarization..."):
                    st.subheader("The Summarized text")
                    summarized_text = summarization(text_input)
                    st.write(summarized_text)

                # Topics in the text
                with st.spinner("Performing topic modeling..."):
                    topics = perform_topic_modeling(text_input, num_topics, num_words)
                    st.subheader("Topics in the Text")
                    topics_result = ""
                    for idx, topic in enumerate(topics, start=1):
                        topics_result += f"Topic {idx}: {', '.join(topic[1])}\n\n"
                    st.write(topics_result)

                # Labeling of text
                with st.spinner("Performing Labeling of Text..."):
                    st.subheader("Label Topic")
                    labeled_text = labeling(text_input)
                    st.write(labeled_text)

                # Download options
                result = f"Summarized Text:\n\n{summarized_text}\n\nTopics in the Text:\n\n{topics_result}\n\nLabel Topic:\n\n{labeled_text}"
                st.download_button(
                    label="Download Results as TXT",
                    data=convert_to_txt(result),
                    file_name="topic.txt",
                    mime="text/plain",
                )
                st.download_button(
                    label="Download Results as DOCX",
                    data=convert_to_docx(result),
                    file_name="topic.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                )





# For PDF
if choice == "PDF":
    st.subheader("Topic Modeling and Labeling App On PDF")
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    num_topics = st.number_input("Enter the Number of Topics", min_value=1, step=1)  # No of topics
    num_words = st.number_input("Enter the Number of Words", min_value=1, step=1)  # No of words


    if uploaded_file:
        if st.button("Analyze your PDF"):
            with st.spinner("Analyzing your PDF ..."):
                # Display extracted or entered text
                extracted_text = extract_text_from_pdf(uploaded_file)
                st.text_area(f"Extracted Text from {choice}", extracted_text, height=200)

                # Summarized PDF
                with st.spinner("Performing Summarization..."):
                    st.subheader("The Summarized PDF")
                    summarized_text = summarization(extracted_text)
                    st.write(summarized_text)

                # Topics in the PDF
                with st.spinner("Performing topic modeling..."):
                    topics = perform_topic_modeling(extracted_text, num_topics, num_words)
                    st.subheader("Topics in the PDF")
                    topics_result = ""
                    for idx, topic in enumerate(topics, start=1):
                        topics_result += f"Topic {idx}: {', '.join(topic[1])}\n\n"
                    st.write(topics_result)

                # Labeling of PDF
                with st.spinner("Performing Labeling of PDF..."):
                    st.subheader("Label Topic")
                    labeled_text = labeling(extracted_text)
                    st.write(labeled_text)

                # Download options
                result = f"Summarized PDF:\n\n{summarized_text}\n\nTopics in the PDF:\n\n{topics_result}\n\nLabel Topic:\n\n{labeled_text}"
                st.download_button(
                    label="Download Results as TXT",
                    data=convert_to_txt(result),
                    file_name="topic.txt",
                    mime="text/plain",
                )
                st.download_button(
                    label="Download Results as DOCX",
                    data=convert_to_docx(result),
                    file_name="topic.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                )







# For URl
if choice == "URL":
    st.subheader("Topic Modeling and Labeling App On URL")
    text_input = st.text_input("Insert your Url ")
    num_topics = st.number_input("Enter the Number of Topics", min_value=1, step=1)  # No of topics
    num_words = st.number_input("Enter the Number of Words", min_value=1, step=1)  # No of words


    if text_input:
        if st.button("Analyze your URL"):
            with st.spinner("Analyzing your URL..."):
                # Display extracted or entered text
                extracted_text = extract_text_from_url(text_input)
                st.text_area(f"Extracted Text from {choice}", extracted_text, height=200)

                # Summarized URL
                with st.spinner("Performing Summarization..."):
                    st.subheader("The Summarized URL")
                    summarized_text = summarization(extracted_text)
                    st.write(summarized_text)

                # Topics in the URL
                with st.spinner("Performing topic modeling..."):
                    topics = perform_topic_modeling(extracted_text, num_topics, num_words)
                    st.subheader("Topics in the URL")
                    topics_result = ""
                    for idx, topic in enumerate(topics, start=1):
                        topics_result += f"Topic {idx}: {', '.join(topic[1])}\n\n"
                    st.write(topics_result)

                # Labeling of URL
                with st.spinner("Performing Labeling of URL..."):
                    st.subheader("Label Topic")
                    labeled_text = labeling(extracted_text)
                    st.write(labeled_text)

                # Download options
                result = f"Summarized URL:\n\n{summarized_text}\n\nTopics in the URL:\n\n{topics_result}\n\nLabel Topic:\n\n{labeled_text}"
                st.download_button(
                    label="Download Results as TXT",
                    data=convert_to_txt(result),
                    file_name="topic.txt",
                    mime="text/plain",
                )
                st.download_button(
                    label="Download Results as DOCX",
                    data=convert_to_docx(result),
                    file_name="topic.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                )







