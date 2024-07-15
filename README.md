# Tscreenshot
# Screenshot to SFTP

This project captures a screenshot from your Windows system and uploads it to an SFTP server. The script leverages the `Pillow` library for capturing the screenshot and `pysftp` for handling the SFTP connection.

## Prerequisites

Make sure you have Python installed. You can download it from the [official Python website](https://www.python.org).

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/screenshot-to-sftp.git
    cd screenshot-to-sftp
    ```

2. **Install required libraries**:
    ```bash
    pip install pillow pysftp
    ```

## Configuration

1. **Settings**:

Create a `settings.py` file in the project directory and specify your SFTP server details:

```python
# settings.py

SFTP_HOSTNAME = 'your_sftp_server.com'
SFTP_USERNAME = 'your_username'
SFTP_PASSWORD = 'your_password'
REMOTE_PATH = '/remote/path/screenshot.png'

```

2. **Run the scrip periodically**:

 Configure the task scheduler of windows to run your screenshot capture.


