from selenium import webdriver
#import chromedriver_binary
import time

#driver = webdriver.Chrome("")
class WhatsappBot:
    def __init__(self):
        self.mensagem = "Bom dia pessoal, veja esse..."
        self.grupos = ["Abc"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def Enviarmensagens(self):
        #<span dir="auto" title="Abc" class="_35k-1 _1adfa _3-8er">Abc</span>
        #<div tabindex="-1" class="_2A8P4"><div tabindex="-1" class="_1JAUF _2x4bz"><div class="OTBsx" style="visibility: visible;">Digite uma mensagem</div><div class="_2_1wd copyable-text selectable-text" contenteditable="true" data-tab="6" dir="ltr" spellcheck="true"></div></div></div>
        #<span data-testid="send" data-icon="send" class=""><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path fill="currentColor" d="M1.101 21.757L23.8 12.028 1.101 2.3l.011 7.912 13.623 1.816-13.623 1.817-.011 7.912z"></path></svg></span>
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        grupo = self.driver.find_element_by_xpath("//span[title='Abc']")
        time.sleep(3)
        grupo.click()
        chat_box = self.driver.find_element_by_class_name('_2A8P4')
        time.sleep(3)
        chat_box.click()
        chat_box.send_keys(self.mensagem)
        botao_enviar = self.driver.find_elements_by_xpath("//span[data-icon='send']")
        time.sleep(3)
        botao_enviar.click()
        time.sleep(5)

bot = WhatsappBot()
bot.Enviarmensagens()