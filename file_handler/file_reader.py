import os
import logging

logging.basicConfig(filename='psd_tools.log', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
import tempfile
from psd_tools import PSDImage

def read_psd(file):
    try:
        with tempfile.NamedTemporaryFile(suffix=".psd", delete=False) as tmp:
            tmp.write(file.read())
            tmp_path = tmp.name
        print(f"Temporary file created at: {tmp_path}")
        
        try:
            psd = PSDImage.open(tmp_path)
            print("PSD file successfully opened.")
        except Exception as e:
            print(f"Error while opening PSD file: {e}")
            raise e
        finally:
            os.remove(tmp_path)
        
        return psd

    except Exception as e:
        print(f"Unexpected error: {e}")
        raise e
