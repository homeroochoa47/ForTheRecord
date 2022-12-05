import App from "./components/App";
import { ChakraProvider, ColorModeScript } from '@chakra-ui/react';
import React from 'react';
import { createRoot } from 'react-dom/client'


const root = createRoot(document.getElementById('app'));
root.render(
  <React.StrictMode>
      <ChakraProvider>
        <App/>
      </ChakraProvider>
  </React.StrictMode>
);