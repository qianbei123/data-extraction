import os
import time
import argparse
import requests

# Default API key from Jupyter Notebook
import os
from dotenv import load_dotenv
load_dotenv()
MINERU_API_KEY = os.getenv("MINERU_API_KEY", "")

def parse_pdf(pdf_path: str, token: str):
    """
    Upload a PDF to MinerU API, poll for extraction results,
    and download the extracted zip file automatically.
    """
    if not os.path.exists(pdf_path):
        print(f"Error: {pdf_path} does not exist.")
        return

    url_batch = "https://mineru.net/api/v4/file-urls/batch"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    
    pdf_name = os.path.basename(pdf_path)
    # Generate an arbitrary data_id as per API requirements
    data_id = "abcd_" + str(int(time.time()))
    
    data = {
        "files": [
            {"name": pdf_name, "data_id": data_id}
        ],
        "model_version": "vlm" # As per the notebook payload
    }
    
    # 1. Upload Phase
    try:
        response = requests.post(url_batch, headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            if result.get("code") == 0:
                batch_id = result["data"]["batch_id"]
                urls = result["data"]["file_urls"]
                
                print(f"Uploading {pdf_name}...")
                with open(pdf_path, 'rb') as f:
                    res_upload = requests.put(urls[0], data=f)
                    if res_upload.status_code == 200:
                        print(f"Upload successful! Batch ID: {batch_id}")
                    else:
                        print(f"Upload failed to the presigned URL. Status: {res_upload.status_code}")
                        return
            else:
                print('Failed to apply for upload URL. Reason:', result.get("msg"))
                return
        else:
            print('Initial request failed. Status:' , response.status_code, response.text)
            return
    except Exception as err:
        print(f"Error during upload phase: {err}")
        return

    # 2. Extract & Download Phase
    url_extract = f"https://mineru.net/api/v4/extract-results/batch/{batch_id}"
    print("Waiting for extraction to complete (this may take a while)...")
    
    while True:
        try:
            res = requests.get(url_extract, headers=headers)
            if res.status_code == 200:
                data = res.json()
                if data.get("code") == 0:
                    extract_result = data["data"]["extract_result"][0]
                    state = extract_result.get("state")
                    
                    if state == "done":
                        file_url = extract_result["full_zip_url"]
                        print(f"Extraction done! Downloading from: {file_url}")
                        
                        file_response = requests.get(file_url, stream=True)
                        if file_response.status_code == 200:
                            # Use original path and substitute extension
                            download_path = os.path.splitext(pdf_path)[0] + ".zip"
                            with open(download_path, 'wb') as f:
                                for chunk in file_response.iter_content(chunk_size=8192):
                                    f.write(chunk)
                            print(f"File downloaded successfully to: {download_path}")
                        else:
                            print(f"Failed to download file. Status code: {file_response.status_code}")
                        break
                    elif state == "failed":
                        err_msg = extract_result.get("err_msg", "Unknown error")
                        print(f"Extraction failed on server: {err_msg}")
                        break
                    else:
                        # State could be 'extracting', 'waiting', etc.
                        print(f"Current state is '{state}'... waiting 5 seconds.")
                        time.sleep(5)
                else:
                    print("Failed to get extract result Payload:", data)
                    break
            else:
                print("Failed to poll result, status code:", res.status_code)
                break
        except Exception as err:
            print(f"Error while polling/downloading: {err}")
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload a PDF to MinerU and download the extracted zip results.")
    parser.add_argument("pdf_path", type=str, help="Absolute or relative path to the PDF file.")
    parser.add_argument("--token", type=str, default=MINERU_API_KEY, help="MinerU Access Token (optional).")
    
    args = parser.parse_args()
    parse_pdf(args.pdf_path, args.token)
