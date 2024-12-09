
# Topic Modeling and Labeling Application

## Overview

The **Topic Modeling and Labeling Application** is a powerful tool designed to analyze various data sources such as text, PDFs, URLs, videos, and CSV files. Leveraging advanced AI models and NLP libraries, it identifies underlying topics, summarizes content, and labels the key information in a structured format.

## Features

- **Support for Multiple Input Types**: Analyze text, CSV files, PDFs, YouTube videos, and web URLs.
- **Topic Modeling**: Extract topics with a specified number of words for better insights.
- **Content Summarization**: Summarize the uploaded or extracted content for quick understanding.
- **Topic Labeling**: Automatically generate labels for the identified topics.
- **Download Results**: Export results in TXT and DOCX formats.

## Tech Stack

This project utilizes the following libraries and technologies:

### Core Technologies
- **[Google Generative AI](https://ai.google/)**: AI-powered generative models for summarization and topic labeling.
- **[Streamlit](https://streamlit.io/)**: Interactive and user-friendly web application framework.

### NLP and Topic Modeling
- **[Gensim](https://radimrehurek.com/gensim/)**: Efficient topic modeling and document similarity analysis.

### Video Processing
- **[Pytube](https://pytube.io/)**: Extract and process video metadata and transcripts from YouTube.
- **[YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/)**: Extract closed captions and transcripts from YouTube videos.

### Data Handling and Parsing
- **[NumPy](https://numpy.org/)**: Numerical computation and data manipulation.
- **[Pandas](https://pandas.pydata.org/)**: Advanced data analysis and manipulation.

### File Parsing and Scraping
- **[Fitz (PyMuPDF)](https://pymupdf.readthedocs.io/)**: Extract text from PDFs efficiently.
- **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)**: Scrape and parse HTML content.
- **[Requests](https://docs.python-requests.org/)**: Simplify HTTP requests for fetching web data.

## Installation

Follow the steps below to set up the project:

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/PriyanshuDey23/TopicModelLabelPro.git
    cd TopicModelingAndLabelingApp
    ```

2. **Set up a Virtual Environment**:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

    > **Note**: Ensure you have Python 3.9 or higher installed.

4. **Set Up Environment Variables**:

Create a `.env` file in the root directory of the project and add the following environment variables:

```bash
GOOGLE_API_KEY=<your-google-api-key>

```

5. **Run the Application**:

    ```bash
    streamlit run app.py
    ```

## Usage

1. Select the type of data you wish to analyze (e.g., Text, CSV, PDF, URL, or Video).
2. Upload the file or enter the URL/link as prompted.
3. Specify the number of topics and words per topic for modeling.
4. View the summarized content, extracted topics, and labeled data.
5. Download results in your preferred format (TXT or DOCX).

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Inspired by advancements in AI and NLP technologies.
- Special thanks to the developers and maintainers of the open-source libraries used in this project.

---

Feel free to explore and contribute to enhance this application!
