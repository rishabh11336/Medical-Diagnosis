# Medical Diagnosis Flask App

![GitHub](https://img.shields.io/github/license/rishabh11336/medical-diagnosis-app)
![GitHub repo size](https://img.shields.io/github/repo-size/rishabh11336/medical-diagnosis-app)

Medical Diagnosis Flask App is a simple web application that uses the OpenAI API to provide potential medical diagnoses based on the symptoms provided by the user. It offers a quick assessment of the severity of the condition, helping users decide whether a hospital visit might be necessary.

**Disclaimer: This app is intended for informational purposes only and should not be used as a substitute for professional medical advice. Always consult a healthcare professional for accurate diagnosis and treatment.**

## Features

- **User-friendly Interface:** A clean and simple web interface that allows users to enter their symptoms easily.

- **AI-powered Diagnosis:** Utilizes the power of OpenAI's API to analyze symptoms and suggest possible medical conditions based on provided information.

- **Severity Assessment:** Provides an estimate of the severity of the condition, helping users decide whether they should seek medical attention urgently.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/rishabh11336/Medical-Diagnosis-App.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Medical-Diagnosis-App
   ```

3. Create a virtual environment (recommended) and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Obtain your OpenAI API key by signing up on the [OpenAI platform](https://beta.openai.com/signup/).

2. Rename the `.env.example` file to `.env` and replace `YOUR_OPENAI_API_KEY` with your actual API key.

3. Start the Flask development server:

   ```bash
   flask run
   ```

4. Access the app in your web browser at `http://127.0.0.1:5000`.

## Configuration

You can customize the behavior of the app by modifying the `config.py` file. You can adjust settings such as severity thresholds and API request parameters.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the app, feel free to create a pull request. Please make sure to follow the [code of conduct](CODE_OF_CONDUCT.md).

## License

This project is licensed under the [MIT License](LICENSE).

---
