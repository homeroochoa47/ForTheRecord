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
            bg={useColorModeValue('gray.50', 'gray.900')}
            pos="fixed"
            w="100%"
            bottom="0">
            <Container
                maxW="100%"
                py={4}
                direction={{ base: 'column', md: 'row' }}
                spacing={4}
                justify={{ base: 'center', md: 'space-between' }}
                align="center">
                    <Link href="https://github.com/homeroochoa47" 
                        color="green.400"
                        fontWeight={500}
                        fontSize="ml"
                    > By Homero</Link>
            </Container>
        </Box>
    );
  }
