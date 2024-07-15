from datetime import datetime
from PIL import ImageGrab
import pysftp, os, logging
import settings  # Import the settings module
hostname = settings.SFTP_HOST
username = settings.SFTP_USER
password = settings.SFTP_PASSWORD
remote_path = settings.SFTP_REMOTE_PATH

logging.basicConfig(
    filename='Tscreenshot.log',  # Log file name
    level=logging.INFO,         # Log level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
)
tnow = datetime.now().strftime('%Y%m%d%H')
try:
    os.mkdir(f'./{tnow}')
except:
    pass
tnowl = datetime.now().strftime('%Y%m%d%H%M')
fname = f"{settings.TV_ID}_{tnowl}.png"
fulllp = f"./{tnow}/{fname}"
# Step 1: Take a Screenshot
def take_screenshot():
    try:
        screenshot = ImageGrab.grab()
        screenshot.save(fulllp)
        logging.error(f"Captura exitosa archivo {fulllp}")
    except Exception as e: 
        logging.error(f"Error capturando la pantalla archivo {fulllp}: {e}")
        raise

# Step 2: Send the Screenshot to an SFTP Server
def upload_to_sftp():
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None  # Disable host key checking
    try:
        with pysftp.Connection(
                        host=hostname, 
                        username=username, 
                        password=password, 
                        cnopts=cnopts) as sftp:
            sftp.put(fulllp, f'{remote_path}/{fname}')
            logging.info(f"Captura {fulllp} enviada al servidor SFTP {remote_path}.")
    except Exception as e:
        logging.error(f"Error enviando la captura {fulllp} al servidor SFTP {remote_path}: {e}")
        raise


if __name__ == "__main__":
    take_screenshot()
    upload_to_sftp()

