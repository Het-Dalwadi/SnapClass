# SnapClass

SnapClass is a Streamlit-based classroom attendance project designed to simplify attendance management through a dedicated student and teacher interface, with face and voice attendance-related features.

## Features

- **Student Portal** — Student-facing interface.
- **Teacher Portal** — Teacher-facing interface for classroom management.
- **Attendance Management** — Attendance-related workflows and results.
- **Face Attendance Pipeline** — Face-based attendance processing.
- **Voice Attendance Pipeline** — Voice-based attendance processing.
- **Subject Management** — Create, enroll in, and share subjects.
- **Photo Management** — Photo-related attendance workflows.

## Tech Stack

- **Language:** Python
- **Frontend / UI:** Streamlit
- **Database / Backend:** Supabase
- **Other:** Face and voice processing pipelines

## Project Structure

```text
snapclass/
├── app.py
├── requirements.txt
└── src/
    ├── UI/
    ├── components/
    ├── screens/
    ├── database/
    └── pipelines/
```

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Het-Dalwadi/SnapClass.git
   cd SnapClass
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the required environment variables and Supabase credentials locally. Never publish real API keys, passwords, or secrets.

5. Run the application:

   ```bash
   streamlit run app.py
   ```

## Security

Sensitive configuration files and local virtual environments should not be committed to the repository. Configure credentials locally before running the application.

## Author

**Het Dalwadi**

GitHub: [Het-Dalwadi](https://github.com/Het-Dalwadi)