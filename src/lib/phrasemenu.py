import gtk, time
from configurationmanager import *

from phrase import PhraseFolder # remove later

class PhraseMenu(gtk.Menu):
    """
    A popup menu that allows the user to select a phrase.
    """

    def __init__(self, expansionService, phraseFolders=[], phrases=[], expandFolders=True):
        gtk.Menu.__init__(self)
        self.set_take_focus(ConfigurationManager.SETTINGS[MENU_TAKES_FOCUS])
        
        if ConfigurationManager.SETTINGS[SORT_BY_USAGE_COUNT]:
            phraseFolders.sort(reverse=True)
            phrases.sort(reverse=True)
        
        if len(phraseFolders) == 1 and len(phrases) == 0 and expandFolders:
            # Only one folder - create menu with just its folders and phrases
            for folder in phraseFolders[0].folders:
                menuItem = gtk.MenuItem(folder.title)
                menuItem.set_submenu(PhraseMenu(expansionService, folder.folders, folder.phrases))
                self.append(menuItem)
    
            if len(phraseFolders[0].folders) > 0:
                self.append(gtk.SeparatorMenuItem())
            
            self.__addPhrasesToSelf(phraseFolders[0].phrases, expansionService)
        
        else:
            # Create phrase folder section
            for folder in phraseFolders:
                menuItem = gtk.MenuItem(folder.title)
                menuItem.set_submenu(PhraseMenu(expansionService, folder.folders, folder.phrases))
                self.append(menuItem)
    
            if len(phraseFolders) > 0:
                self.append(gtk.SeparatorMenuItem())
    
            self.__addPhrasesToSelf(phrases, expansionService)
            
        self.show_all()


    def show_on_desktop(self):
        gtk.gdk.threads_enter()
        self.popup(None, None, None, 1, 0)
        gtk.gdk.threads_leave()
        
    def remove_from_desktop(self):
        gtk.gdk.threads_enter()
        self.popdown()
        gtk.gdk.threads_leave()
        
    def __addPhrasesToSelf(self, phrases, expansionService):
        # Create phrase section
        if ConfigurationManager.SETTINGS[SORT_BY_USAGE_COUNT]:
            phrases.sort(reverse=True)
            
        for phrase in phrases:
            menuItem = gtk.MenuItem(phrase.description)
            menuItem.connect("activate", expansionService.phrase_selected, phrase)
            self.append(menuItem)        

# Testing stuff - remove later ----

class MockPhrase:

    def __init__(self, description):
        self.description = description


class MockExpansionService:

    def phrase_selected(self, event, phrase):
        print phrase.description


if __name__ == "__main__":
    gtk.gdk.threads_init()
    
    myFolder = PhraseFolder("Some phrases")
    myFolder.add_phrase(MockPhrase("phrase 1"))
    myFolder.add_phrase(MockPhrase("phrase 2"))
    myFolder.add_phrase(MockPhrase("phrase 3"))

    myPhrases = []
    myPhrases.append(MockPhrase("phrase 1"))
    myPhrases.append(MockPhrase("phrase 2"))
    myPhrases.append(MockPhrase("phrase 3"))

    menu = PhraseMenu(MockExpansionService(), [myFolder], myPhrases)
    menu.show_on_desktop()
    
    gtk.main()