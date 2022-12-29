import React from 'react'
import {
    Box,
    Container,
    Stack,
    Text,
    Link,
    useColorModeValue,
  } from '@chakra-ui/react';
  import { useColorMode } from "@chakra-ui/color-mode";

export function Footer() {
    return (
        <Box
            bg={useColorModeValue('#D8CFB1', 'gray.900')}
            pos="fixed"
            minW="100%"
            bottom="0"
            left="0">
            <Container
                maxW="100%"
                py={4}
                direction={{ base: 'column', md: 'row' }}
                spacing={4}
                justify={{ base: 'center', md: 'space-between' }}
                align="center">
                    <Link href="https://github.com/homeroochoa47" 
                        color="#698396"
                        fontWeight={500}
                        fontSize="ml"
                    > By Homero</Link>
            </Container>
        </Box>
    );
  }
