import React from 'react'
import { useColorMode } from "@chakra-ui/color-mode";
import { IconButton } from "@chakra-ui/button";
import { Button, Box, ButtonGroup } from "@chakra-ui/react"
import { Flex, VStack, Heading, Spacer } from "@chakra-ui/layout";
import { FaSun, FaMoon, FaInstagram, FaGithub, FaLinkedin } from 'react-icons/fa'
import { HomePage } from './HomePage'
import { Comments } from './Comments'
import {BrowserRouter as Router,
  Routes,
  Route, 
  Link, 
  Redirect,
} from 'react-router-dom';


export default function App() {
  const { colorMode, toggleColorMode } = useColorMode();
  const isDark = colorMode === "dark";

  return (
    <VStack p={5}>
      <Flex width='90%' alignItems='center'>
        <Heading
          ml="8" size="lg" fontWeight='semibold' color="green.400">CommentFinder</Heading>
        <Spacer></Spacer>
        <ButtonGroup gap='2'>
          <Button colorScheme='teal' size='md'>Home</Button>
          <Button colorScheme='teal' size='md'>Find My Song</Button>
        </ButtonGroup>
        <IconButton ml={8} icon={isDark ? <FaSun /> : <FaMoon />} isRound='true' onClick={toggleColorMode}></IconButton>
      </Flex>
      <Router>
        <Routes>
          <Route exact path="/home" element={<HomePage/>}/>
          <Route exact path="/comments" element={<Comments/>}/>
        </Routes>
      </Router>
    </VStack>
  );
}