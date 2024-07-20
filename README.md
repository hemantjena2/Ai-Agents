# Educational AI System

## Description
This Educational AI System is an intelligent tutoring platform that uses the Gemini API to provide personalized learning experiences. The system consists of multiple AI agents, each specialized in different aspects of the learning process, working together to assist students in their educational journey.

## Features
- Master Agent for query analysis and task delegation
- Tutor Agent for managing student profiles and interests
- Learning Tracking Agent for progress assessment and question generation
- Roadmap Agent for creating personalized learning paths
- Coach Agent for providing detailed explanations and feedback

## Prerequisites
- Python 3.7+
- Google Generative AI library
- Gemini API key

## Installation
1. Clone the repository
2. Install the required dependencies
3. Set up your Gemini API key:
- Obtain an API key from the [Google AI Studio](https://makersuite.google.com/app/apikey)
- Replace `"YOUR_API_KEY"` in `main.py` with your actual API key

## Usage
Run the main script to start the Educational AI System.
The system will process a set of predefined queries, demonstrating how different agents handle various types of educational requests.

## Project Structure
- `main.py`: The entry point of the system, containing the `EducationalAISystem` class
- `master_agent.py`: Implements the MasterAgent for query analysis
- `tutor_agent.py`: Implements the TutorAgent for student profile management
- `learning_tracking_agent.py`: Implements the LearningTrackingAgent for progress tracking
- `roadmap_agent.py`: Implements the RoadmapAgent for creating learning paths
- `coach_agent.py`: Implements the CoachAgent for providing explanations and feedback

## Customization
You can extend the system by adding new agents or modifying existing ones. Update the `process_request` method in `EducationalAISystem` to incorporate new functionalities.

## Contributing
Contributions to improve the Educational AI System are welcome. Please feel free to submit pull requests or open issues to discuss potential enhancements.

## License
[MIT License](LICENSE)

## Acknowledgments
- This project uses the Gemini API provided by Google    
- Inspired by advanced tutoring systems and personalized learning approaches
