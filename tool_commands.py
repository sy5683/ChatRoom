import os


class ToolCommand:
    @staticmethod
    def create_folder():
        folder_paths = ["static", "static\\css", "static\\font", "static\\image", "static\\js", "templates"]
        for folder_path in folder_paths:
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

    @staticmethod
    def create_app(app_name=''):
        assert app_name, "app_name不能为空"
        os.system(f"python manage.py startapp {app_name}")

    @staticmethod
    def run_server():
        os.system("python manage.py runserver 0.0.0.0:8080")

    def main(self):
        # self.create_folder()

        # self.create_app("")

        self.run_server()


if __name__ == '__main__':
    ToolCommand().main()
