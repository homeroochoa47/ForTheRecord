import React from 'react'
import { useColorMode } from "@chakra-ui/color-mode";
import { IconButton } from "@chakra-ui/button";
import { Button, Box, ButtonGroup, Container } from "@chakra-ui/react"
import { Flex, VStack, Heading, Spacer } from "@chakra-ui/layout";
import { FaSun, FaMoon, FaInstagram, FaGithub, FaLinkedin } from 'react-icons/fa'
import { HomePage } from './pages/HomePage'
import { Comments } from './pages/Comments'
import {NavBar} from './layout/NavBar'
import { Footer } from './layout/Footer'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";


export default function App() {
  return (
    <VStack p={5}>
      <NavBar/>
        <Router>
          <Routes>
            <Route exact path="/home" element={<HomePage/>}/>
            <Route exact path="/comments" element={<Comments/>}/>
          </Routes>  
        </Router>
      <Footer/>
    </VStack>
  );
}