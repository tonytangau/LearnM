# LearnM: AI-Powered Learning Companion

LearnM is an AI-powered app designed to help users **learn and understand topics deeply**. It uses the DeepSeek API to generate structured study guides, including key concepts, examples, FAQs, and suggested resources.

## Features

- **Learn Mode**:
  - Enter a topic, and the app generates a detailed study guide.
  - Includes **key concepts**, **examples**, **FAQs**, and **suggested resources**.
- **Interactive Feedback**:
  - Provides clear and engaging explanations.
  - Encourages critical thinking with interactive questions.

## How to Use

1. **Set Up**:
   - Clone the repository:
     ```bash
     git clone https://github.com/tonytangau/LearnM.git
     ```
   - Install dependencies:
     ```bash
     pip install streamlit openai python-dotenv
     ```
   - Create a `.env` file and add your DeepSeek API key:
     ```env
     DEEP_SEEK_API_KEY=your_api_key_here
     ```

2. **Run the App**:
   - Start the Streamlit app:
     ```bash
     streamlit run learn_mode.py
     ```
   - Open your browser and go to `http://localhost:8501`.

3. **Generate a Study Guide**:
   - Enter a topic in the input box (e.g., "Photosynthesis").
   - Click **Generate Study Guide**.
   - View the structured study guide with key concepts, examples, FAQs, and resources.

## Requirements

- Python 3.7+
- DeepSeek API key

## License

This project is licensed under the MIT License.

## Acknowledgments

- Powered by [DeepSeek API](https://www.deepseek.com/).
- Built with [Streamlit](https://streamlit.io/).
