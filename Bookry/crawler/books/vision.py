import argparse
import base64
import httplib2
import subprocess
import os


from googleapiclient.discovery import build
from oauth2client.client import GoogleCredentials


BASE_DIR = os.path.dirname(__file__)


def main(photo_file):
    api_discovery_file = 'https://vision.googleapis.com/$discovery/rest?version=v1'
    http = httplib2.Http()

    credentials = GoogleCredentials.get_application_default().create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform']
    )
    credentials.authorize(http)

    service = build(
        'vision',
        'v1',
        http,
        discoveryServiceUrl=api_discovery_file
    )

    with open(photo_file, 'rd') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(
            body={
                'requests': [{
                    'image': {
                        'content': image_content
                    },
                    'features': [{
                        'type': 'TEXT_DETECTION',
                        'maxResults': 1,
                    }]
                }]
            }
        )
        response = service_request.execute()
        text = response['responses'][0]['textAnnotations'][0]['description']
        print('Found text: %s for %s' % (text.replace(' ', ''), photo_file))
        return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'image_file', help='The image you\'d like to identify'
    )
    args = parser.parse_args()
    subprocess.call([
        'export',
        'GOOGLE_APPLICATION_CREDENTIALS='+os.path.join(
            os.getcwd(),
            '/.res/bookry-vision-6f2d87c63e33.json'
        )
    ],
        shell=True,
        stdout=subprocess.PIPE
    )
    main(args.image_file)
