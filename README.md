### this is a repo I create to learn flask and try tro implement flask into our project
- POSIX Systems:
  ```bash
  cd frontend
  python -m venv .venv
  source .venv/bin/activate
  pip install -r ./requirements.txt
  deactivate
  ```
- Windows Systems:
  ```bash
  cd frontend
  python -m venv venv
  venv/Script/activate
  pip install -r ./requirements.txt
  deactivate
  ```
  
From the project root directory:

- POSIX Systems:
  ```bash
  cd frontend
  source .venv/bin/activate
  streamlit run ./main.py
  ```
- Windows Systems:
  ```bash
  cd frontend
  venv/Script/activate
  streamlit run ./main.py
  ```