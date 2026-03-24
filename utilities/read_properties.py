import configparser


config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")

class Read_Config:
    @staticmethod
    def get_admin_page_url():
        url = config.get('admin login info','admin_page_url')
        return url

    def get_username():
        username = config.get('admin login info','username')
        return username

    def get_password():
        password = config.get('admin login info','password')
        return password

    def get_invalid_username():
        invalid_username = config.get('admin login info','invalid_username')
        return invalid_username