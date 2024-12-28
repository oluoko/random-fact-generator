# Random Fact Generator

This repo contains the code for Random Facts Generator websites built using various technologies.

- ##[Python](https://factgen.streamlit.app/)
  Click [`Here`](https://factgen.streamlit.app/) to go to the demo. You may need to install streamlit first.

  - Start by installing [`python3`](https://www.python.org/downloads/) using `apt`

    ```bash
    sudo apt install python3
    ```

  - If `pip` is not installed, install it with:

    ```bash
    sudo apt install python3-pip
    ```

  - Create a virtual environment:

    ```bash
    python3 -m venv streamlit_env
    ```

  - Activate the virtual environment:

    ```bash
    source streamlit_env/bin/activate
    ```

  - Install Streamlit in the virtual environment:

    ```bash
    pip install streamlit
    ```

  - Run Streamlit: After installation, you can use streamlit commands within the virtual environment:

    ```bash
    streamlit run factGen.py
    ```

  - Deactivate the virtual environment (when done):

    ```bash
    deactivate
    ```
