import requests

def upload_to_b2_presigned_url(file_path, presigned_url):
    try:
        # Read file content
        with open(file_path, 'rb') as f:
            file_data = f.read()

        # Optional: Set appropriate content-type if known (e.g., 'text/plain', 'application/pdf', etc.)
        headers = {
            'Content-Type': 'application/octet-stream'
        }

        # Make PUT request
        response = requests.put(presigned_url, data=file_data, headers=headers)

        # Check response
        if response.status_code in [200, 204]:
            print("✅ Upload successful!")
        else:
            print(f"❌ Upload failed with status code {response.status_code}")
            print("Response:", response.text)

    except Exception as e:
        print(f"⚠️ Error: {e}")

# Example usage
# Replace these with your actual values
file_path = ''
presigned_url = ''

upload_to_b2_presigned_url(file_path, presigned_url)

