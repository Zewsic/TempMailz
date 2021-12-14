"""
    The module allows you to interact with temporary mail
    :author: zewsic

    :copyright: (c) 2019 python273
"""

import requests
import json
import sys

TempMailz_api_address = 'https://www.1secmail.com/api/v1/?action='

class TempMailz():

    """
        Work with temporary mail
        
        Each object of the Temp Mailz class is a separate temporary mailbox
    """
    
    #Temporary mail api URL
    TempMailz_api_address = 'https://www.1secmail.com/api/v1/?action='
    
    #Full address of the temporary mailbox. e.g: user@1secmail.com
    address = ''
    
    #Login of the temporary mailbox. e.g: user
    login = ''
    
    #Domain of the temporary mailbox. e.g: 1secmail.com
    domain = ''
    
    #Mailbox archive, required for the listen method
    lastInbox = []
    
    def __init__(self, login='', domain='', random=True):
        """
            It is called and immediately creates a new temporary mailbox with the necessary settings.
            
            If the random parameter is True, then a random temporary mailbox with a random address is created. 
            If the random parameter is False, then a mailbox is created with the selected login and domain parameters
            
            :params:
                login: Login for the temporary mailbox, e.g: user26274
                domain: Domain for the temporary mailbox, e.g: 1secmail.com
                random: If true, it creates a random mailbox with a random address
        """
        
        if not random or not login == "" and not domain == "":
            domains = json.loads(requests.get(TempMailz_api_address + 'getDomainList').text)
            if domain in domains:
                self.address = login + '@' + domain
                self.login = login
                self.domain = domain
            else:
                print(f'The domain {domain} does not exist!')
                sys.exit(12)
        else:
            self.address = json.loads(requests.get(TempMailz_api_address + 'genRandomMailbox&count=1').text)[0]
            self.login = self.address.split('@')[0]
            self.domain = self.address.split('@')[1]
    
    @staticmethod 
    def getDomainList():
        """
            Returns a list with all possible temporary mail domains
        """
    
        return json.loads(requests.get(TempMailz_api_address + 'getDomainList').text)
    
    def get_inbox(self):
        """
            Returns a list of messages for the current mailbox
        """
    
        inbox = json.loads(requests.get(TempMailz_api_address + f'getMessages&login={self.login}&domain={self.domain}').text)
        return inbox
       
    def get_msg(self, id_):
        """
            Returns detailed information about the required message
            
            :params:
                id_: ID of the message to get information about
        """
    
        msg = json.loads(requests.get(TempMailz_api_address + f'readMessage&login={self.login}&domain={self.domain}&id={id_}').text)
        return msg   
            
    def listen(self):
        """
               Allows you to receive new messages immediately after they arrive on the temporary mail server. 
               
               :example:
                    mail = TempMailz()
                    for event in mail.listen():
                        print(event)
        """
        
        while True:
            for event in self.get_inbox():
                if not event in self.lastInbox:
                    self.lastInbox.append(event)
                    yield event
