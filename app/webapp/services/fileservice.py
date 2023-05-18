import requests

from app.webapp.config import config


class FileService:
    def send_file(self, file):
        """
        Example of sending file to any other service\n
        :param file: Received file from request
        :type file: BinaryIO
        :return: Returns service answer
        :rtype: dict
        """

        headers = {
            "accept": "text/plain",
            "Content-Type": "multipart/form-data"
        }

        requests.post(
            url=f"http://{config.host()}:{config.port()}/webapp/loadFile/",
            headers=headers,
            data=file
        )
        return 200
