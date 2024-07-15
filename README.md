# Tscreenshot
# Screenshot to SFTP

This project captures a screenshot from your Windows system and uploads it to an SFTP server. The script leverages the `Pillow` library for capturing the screenshot and `pysftp` for handling the SFTP connection.

## Prerequisites

Make sure you have Python installed. You can download it from the [official Python website](https://www.python.org).

- This project was built against Python 3.12.4.


## Installation

1. **Clone the repository**:
    ```git clone git@github.com:pjmakey2/Tscreenshot.git
    cd Tscreenshot
    ```

2. **Install required libraries**:
    ```pip install pillow pysftp```

## Configuration

1. **Settings**:

Create a `settings.py` file in the project directory and specify your SFTP server details:

```python
    # settings.py
    SFTP_USER = 'loquillo_sftp'
    SFTP_PASSWORD = 'SniffPicture'
    SFTP_HOST = '127.128.129.130'
    SFTP_PORT = '1238'
    TV_ID = 'vvtv'
    SFTP_REMOTE_PATH = f'/path/{TV_ID}/'

```

2. **Run the scrip periodically**:

 Configure the task scheduler of windows to run your screenshot capture.


