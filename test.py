import os
from dotenv import load_dotenv
import google.generativeai as genai

def main():
    # Load environment variables
    load_dotenv()

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError("❌ GOOGLE_API_KEY not found. Set it in .env or environment variables.")

    # Configure Gemini
    genai.configure(api_key=api_key)

    # Load model
    model = genai.GenerativeModel("gemini-3-flash-preview")

    # Test prompt
    prompt = "Explain what a Large Language Model is in simple words."

    # Generate response
    response = model.generate_content(prompt)

    print("\n✅ Gemini API Test Successful\n")
    print("Prompt:")
    print(prompt)
    print("\nResponse:")
    print(response.text)

if __name__ == "__main__":
    main()







