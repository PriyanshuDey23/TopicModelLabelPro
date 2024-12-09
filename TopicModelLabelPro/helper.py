import gensim
from gensim import corpora,models
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Access API key from environment
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the Generative AI client
genai.configure(api_key=GOOGLE_API_KEY)

# Function for summarization
def summarization(input_text):
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash-8b")

        chat_session = model.start_chat(
            history=[{
                "role": "user",
                "parts": [f"Provide a short summary of the following text:\n\n{input_text}"]
            }]
        )

        response = chat_session.send_message("Please provide a more concise summary if necessary.")
        return response.text.strip()
    
    except Exception as e:
        return f"Error generating summary: {str(e)}"





# Hendle the text
# This tokenizes the text and removes stop words
def preprocess_text(text):
    tokens=gensim.utils.simple_preprocess(text) # Tokenization 
    stopwords=gensim.parsing.preprocessing.STOPWORDS # Stop words
    preprocessed_text=[token for token in tokens if token not in stopwords] # Exclude stopwords
    return preprocessed_text







# Function for Perfoming topic modeling on the text 
def perform_topic_modeling(transcript_text, num_topics, num_words):
    # Preprocess the transcript text
    preprocessed_text = preprocess_text(transcript_text)



    # Create a dictionary of all unique words in the transcripts
    # This line creates a dictionary of all unique words in the preprocessed text using the corpora.Dictionary class
    dictionary = corpora.Dictionary([preprocessed_text])

    # Convert the preprocessed transcripts into a bag-of-words representation
    corpus = [dictionary.doc2bow(preprocessed_text)]

    # Train an LDA model with the specified number of topics
    # LdaModel:- Helps to discover hidden topics or themes from large corpus
    # The id2word parameter is set to the dictionary variable, which maps word IDs to word strings.
    lda_model = models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics) 

    # Extract the most probable words for each topic
    topics = [] # This line initializes an empty list named topics that will store the extracted topics.
    for idx, topic in lda_model.print_topics(-1, num_words=num_words):
        # Extract the top words for each topic and store in a list
        topic_words = [word.split('*')[1].replace('"', '').strip() for word in topic.split('+')]
        topics.append((f"Topic {idx}", topic_words))

    return topics



# Labeling
def labeling(input_text):
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash-8b")

        chat_session = model.start_chat(
            history=[{
                "role": "user",
                "parts": [f"""Label the following text with relevant categories, 
                          and include domain/topic labeling for optimal context and accuracy
                          Give me in Bullet points:\n\n{input_text}"""]
            }]
        )

        response = chat_session.send_message("Please provide a label for the text.")
        return response.text.strip()
    
    except Exception as e:
        return f"Error generating label: {str(e)}"
    


# Convert csv to string Format
def csv_to_string(csv_data):

    # Convert DataFrame to CSV string
    csv_string = csv_data.to_csv(index=False)

    return csv_string



# Generate youtube transcript
prompt = """You are a YouTube Video Summarizer. You will take the transcript text and
            summarize the entire video, providing the clear summary  in a important points ."""

# Function to extract transcript from YouTube video
def extract_transcript(youtube_video_url):

        # Check if URL is in 'youtu.be' format and extract video ID
        if "youtu.be" in youtube_video_url:
            video_id = youtube_video_url.split("/")[-1]
        # Check if URL is in 'youtube.com' format and extract video ID
        elif "youtube.com" in youtube_video_url:
            video_id = youtube_video_url.split("v=")[1].split("&")[0]  # Ensure video ID is properly split
        else:
            raise ValueError("Invalid YouTube URL format.")
        
        # Fetch the transcript of the video
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id=video_id)
        
        # Combine all the transcript texts into a single string
        transcript = " ".join([item["text"] for item in transcript_data])
        
        return transcript
    

