import webbrowser

class main():
    
    
    def __init__(self,url):
        self.url = url
        print('Test Github actions with test case')
        
        
    def openWindow(self):
        webbrowser.open(self.url)
        #os.system("open \"\" https://www.google.com")
        
        
p1 = main("http://www.microsoft.com")
p1.openWindow()
