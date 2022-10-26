import configparser
import os

assert os.path.exists("/Users/khan/PycharmProjects/Hudl/Configurations/config.ini")

config = configparser.RawConfigParser()
config.read("/Users/khan/PycharmProjects/Hudl/Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def get_email():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return  password

    @staticmethod
    def get_invalid_email():
        invalid_email = config.get('common info', 'invalid_email')
        return invalid_email

    @staticmethod
    def get_unregistered_email():
        unregistered_email = config.get('common info', 'unregistered_email')
        return unregistered_email

    @staticmethod
    def get_incorrect_password():
        incorrect_password = config.get('common info', 'incorrect_password')
        return incorrect_password

    @staticmethod
    def get_logged_out_title():
        logged_out_title = config.get('common info', 'logged_out_title')
        return logged_out_title

    @staticmethod
    def get_org_login_title():
        org_login_title = config.get('common info', 'org_login_title')
        return org_login_title

    @staticmethod
    def get_homepage_title():
        homepage_title = config.get('common info', 'homepage_title')
        return homepage_title

    @staticmethod
    def get_help_title():
        help_title = config.get('common info', 'help_title')
        return help_title

    @staticmethod
    def get_login_validation():
        login_validation = config.get('common info', 'login_validation')
        return login_validation

    @staticmethod
    def get_org_validation():
        org_validation = config.get('common info', 'org_validation')
        return org_validation

    @staticmethod
    def get_reset_password_validation():
        reset_password_validation = config.get('common info', 'reset_password_validation')
        return reset_password_validation

    @staticmethod
    def get_unregistered_email_validation():
        unregistered_email_validation = config.get('common info', 'unregistered_email_validation')
        return unregistered_email_validation
