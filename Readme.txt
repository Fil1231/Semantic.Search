# Instructions to set up Python virtual environment and install dependencies

1. Create a virtual environment (recommended name: .venv):

    python3 -m venv .venv

2. Activate the virtual environment:
    - On macOS/Linux:
        source .venv/bin/activate
    - On Windows:
        .venv\Scripts\activate

3. Install required packages:

    pip install -r requirements.txt

4. Run the script:

    python sematic_search.py

# Requirements
See requirements.txt for the list of required packages.
 wget -r -np -l 1 -A html http://www.actualno.com/
 