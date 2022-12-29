import App from "./components/App";
import { ChakraProvider, extendTheme } from '@chakra-ui/react';
import React from 'react';
import { createRoot } from 'react-dom/client'
import { mode } from "@chakra-ui/theme-tools";

const theme = extendTheme({
  styles: {
    global: (props) => ({
      body: {
        bg: mode('#D8CFB1', '#112836')(props),
      }
    })
  },
})

const root = createRoot(document.getElementById('app'));
root.render(
    <ChakraProvider theme={theme}>
      <App/>
    </ChakraProvider>
);