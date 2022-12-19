import React, { useState, useEffect } from "react";
import { ChakraProvider, theme, Heading, Text, Box, useColorModeValue, useColorMode, Center, Stack, Avatar } from '@chakra-ui/react'

//we pass props from the comments page containing comment info and render here.
export function CommentCard(props) {

    return(
        <Center py="6">
        <Box
            maxW={'445px'}
            w={'full'}
            bg={useColorModeValue('white', 'gray.700')}
            boxShadow={'2xl'}
            rounded={'md'}
            p={6}
            overflow={'hidden'}>
            <Stack>
                <Text
                    color="green.500"
                    textTransform="uppercase"
                    fontWeight={800}
                    fontSize="sm"
                    letterSpacing={1.1}>
                    Text
                </Text>
                <Heading
                    fontSize="2xl"
                    fontFamily={'body'}>
                    Heading Here
                </Heading>
                <Text color='gray.500'>
                    Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
                    nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam
                    erat, sed diam voluptua. At vero eos et accusam et justo duo dolores
                    et ea rebum.
                </Text>
            </Stack>
            <Stack mt={6} direction={'row'} spacing={4} align={'center'}>
                <Avatar
                    src={'https://avatars0.githubusercontent.com/u/1164541?v=4'}
                    alt={'Author'}
                />
                <Stack direction="column" spacing={0} fontSize="sm">
                    <Text fontWeight={600}>Commenter username</Text>
                    <Text color="gray.500">Date/Time Posted</Text>
                </Stack>
            </Stack>
        </Box>
    </Center>
    )
}