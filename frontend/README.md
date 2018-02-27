# Controlato - Frontend

### Development mode

To start the Figwheel compiler, navigate to the project folder and run the following command in the terminal:

    $ lein figwheel
    
Figwheel will automatically push cljs changes to the browser. Once Figwheel starts up, you should be able to open the address http://localhost:3449/ in the browser, if Figwheel didn't already did it for you.

### Building for production

    $ lein clean
    $ lein package
