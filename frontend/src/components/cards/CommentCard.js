import React, { useState, useEffect } from "react";
import { ChakraProvider, theme, Heading, Text, Box, useColorModeValue, useColorMode, Center, Stack, Avatar, Card, CardHeader, CardBody, Flex } from '@chakra-ui/react'

//we pass props from the comments page containing comment info and render here.
export function CommentCard(props) {

    return(
        <Card bg={useColorModeValue("#698396", "#5A745D")}>
            <CardHeader>
                <Flex spacing='4'>
                    <Flex flex='1' gap='4' alignItems='center' flexWrap='wrap'>
                        <Avatar
                            src={props.commentData.image}
                            alt={'Author'}/>
                        <Box>
                            <Heading size='md'
                                color={useColorModeValue("black", "white")}
                            >{props.commentData.user}</Heading>
                        </Box>
                    </Flex>
                </Flex>
            </CardHeader>
            <CardBody>
                <Box display='flex' alignItems='baseline'>
                    <Text
                        color={useColorModeValue("black", "white")}
                        fontWeight={500}
                        fontSize="sm">
                        {props.commentData.comment}
                    </Text>
                </Box>
            </CardBody>
        </Card>
    )
};