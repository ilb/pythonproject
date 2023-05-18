import inject

from app.webapp.services.fileservice import FileService


class SendToFileService:

    @inject.autoparams()
    def __init__(self, file_service: FileService):
        self.file_service = file_service

    def send_file_usecase(self, file):
        return self.file_service.send_file(file=file)
