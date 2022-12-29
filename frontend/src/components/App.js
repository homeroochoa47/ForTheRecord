import React from 'react'
import { VStack,} from "@chakra-ui/layout";
import { HomePage } from './pages/HomePage'
import { Comments } from './pages/Comments'
import {NavBar} from './layout/NavBar'
import { Footer } from './layout/Footer'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { useColorModeValue, useColorMode, Box } from '@chakra-ui/react';

//the frontend layout consists of a fixed navbar and footer, and the main content which we route to.
export default function App() {
  const { colorMode, toggleColorMode } = useColorMode();

  return (
    <Box p={5} bg={useColorModeValue('#D8CFB1', '#112836')}>
      <NavBar />
        <Box bg={useColorModeValue('#D8CFB1', '#112836')} height="auto">
          <Router>
            <Routes>
              <Route exact path="/home" element={<HomePage />} />
              <Route exact path="/comments" element={<Comments />} />
            </Routes>
          </Router>
        </Box>
      <Footer/>
    </Box>
  );
}