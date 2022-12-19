import React from 'react'
import { BrowserRouter as Router, Routes, Route, useNavigate } from "react-router-dom";
import { useColorMode } from "@chakra-ui/color-mode";
import { IconButton } from "@chakra-ui/button";
import { Button, Box, ButtonGroup } from "@chakra-ui/react"
import { Flex, VStack, Heading, Spacer } from "@chakra-ui/layout";
import { FaSun, FaMoon, } from 'react-icons/fa'

export function NavBar() {
  const { colorMode, toggleColorMode } = useColorMode();
  const isDark = colorMode === "dark";

  return (
    <Flex width='90%' alignItems='center'>
    <a href="home">
      <Heading
        ml="8" size="lg" fontWeight='semibold' color="green.400">ForTheRecord
        </Heading>
    </a>
    <Spacer></Spacer>
    <ButtonGroup gap='2'>
        <a href="/home"><Button colorScheme='green' bg='green.400' size='md'>Home</Button></a>
        <a href="comments"><Button colorScheme='green' bg='green.400' size='md' href="/search/comment_search">Find My Song</Button></a>
    </ButtonGroup>
    <IconButton ml={8} icon={isDark ? <FaSun /> : <FaMoon />} isRound='true' onClick={toggleColorMode}></IconButton>
    </Flex>
  );
} 