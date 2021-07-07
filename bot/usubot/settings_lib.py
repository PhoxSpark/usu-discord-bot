import os
import logging

from configparser import ConfigParser


log = logging.getLogger('usubot')


class SettingsFile():
    """
    Object for the settings file.
    """

    file = {"file_name":str(), "exists":False, "error":None}

    def __init__(self, file="settings.ini"):
        """
        Initialize the object.
        """
        self.file["file_name"] = file


    def create_settings(self):
        """
        It will create a new settings file if it doesn't exist.
        """
        #Check if file exists. If not, try to create it. Will handle permission error.
        if os.path.exists(self.file["file_name"]):
            log.debug("'"+ self.file["file_name"] + "' found.")
            self.file["exists"] = True
        else:
            log.debug("'"+ self.file["file_name"] + "' not found.")
            self.file["exists"] = False
            try:
                open(self.file["file_name"], 'a').close()
                self.file["exists"] = True
                self.file["error"] = None
                log.info("'"+ self.file["file_name"] + "' created.")
            except PermissionError:
                self.file["error"] = "PermissionError"
                log.error("Permission error creating settings file.")


    def set_data(self, section, option_name=None, option=None):
        """
        Allows to add data to the settings file. It can be used just to add a new section without
        new options or just new options to an existing section.
        """
        #Check if file exists to prevent exceptions trying to reach it.
        if self.file["exists"]:
            log.debug("File exists, setting up ConfigParser.")
            config = ConfigParser()
            config.read(self.file["file_name"])

            #Check if the section bot exists and add it if not.
            if not config.has_section(section):
                log.debug("Section not found, it will be added.")
                config.add_section(section)
            
            #If a option is specified, it will add it to the section.
            if option_name != None:
                log.debug("Option specified, it will be added.")
                config.set(section, option_name, option)

            #Write the config file.
            log.debug("Writing to settings file.")
            with open(self.file["file_name"], 'w') as f:
                config.write(f)
            
            log.info("Data added to '" + self.file["file_name"] + "' file.")
        else:
            log.error("Can't set token because the settings file is missing. Last error: " +
                      self.file["error"])
    

    def get_data(self, section, option_name):
        """
        Taking the section name and the option name, returns the data of the settings file. It will
        return None if the section or the data requested is none existent.
        """
        data = None

        #Check if file exists to prevent exceptions trying to reach it.
        if self.file["exists"]:
            log.debug("File exists, setting up ConfigParser.")
            config = ConfigParser()
            config.read(self.file["file_name"])

            #Check if the section exists.
            if config.has_section(section):
                log.debug("Section '" + section + "' found.")
                #Check if the option exists.
                if config.has_option(section, option_name):
                    log.debug("Option '" + option_name + "' found.")
                    data = config.get(section, option_name)
                    log.info("Data obtained correctly.")
                else:
                    log.warning("Option requested not found!")
            else:
                log.warning("Section requested not found!")
        else:
            log.error("Can't set token because the settings file is missing. Last error: " +
                      self.file["error"])
        return data
