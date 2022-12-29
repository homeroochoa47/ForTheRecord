import React from 'react'
import { useColorMode } from "@chakra-ui/color-mode";
import { IconButton } from "@chakra-ui/button";
import { Button, Box, ButtonGroup } from "@chakra-ui/react"
import { Flex, VStack, Heading, Spacer, Container } from "@chakra-ui/layout";
import { FaSun, FaMoon, } from 'react-icons/fa'

// TODO: have a login/logout button that also shows the users spotify username and profile picture somewhere on the screen at all times.

export function NavBar() {
  const { colorMode, toggleColorMode } = useColorMode();
  const isDark = colorMode === "dark";

  return (
    <Flex width='100%' alignItems='center' justifyContent={{base: 'space-around', sm: 'space-between', md: 'space-around', lg: 'space-around'}}>
      <a href="home">
        <Heading
          size="lg" fontWeight='semibold' color='#698396'>ForTheRecord
          </Heading>
      </a>
      <Flex>
        <ButtonGroup gap={{base: 2, sm: 1}}>
            <a href="/home"><Button colorScheme='green' bg='#698396' size='md'>Home</Button></a>
            <a href="comments"><Button colorScheme='green' bg='#698396' size='md' href="/search/comment_search">Find My Song</Button></a>
        </ButtonGroup>
        <IconButton ml={{base: 8, sm: 4}} icon={isDark ? <FaSun /> : <FaMoon />} isRound='true' onClick={toggleColorMode}></IconButton>
      </Flex>
    </Flex>
  );
} 