import React, { useState, useEffect } from "react";
import { ChakraProvider, theme, Heading, Text, Box, useColorModeValue, useColorMode, Center, Stack, Avatar, Card, CardHeader, CardBody, Flex } from '@chakra-ui/react'

//we pass props from the comments page containing comment info and render here.
export function CommentCard(props) {

    return(
        <Card bg='useColorModeValue' p>
            <CardHeader>
                <Flex spacing='4'>
                    <Flex flex='1' gap='4' alignItems='center' flexWrap='wrap'>
                        <Avatar
                            src={props.commentData.image}
                            alt={'Author'}/>
                        <Box>
                            <Heading size='md'
                                color="green.400"
                            >{props.commentData.user}</Heading>
                        </Box>
                    </Flex>
                </Flex>
            </CardHeader>
            <CardBody>
                <Text
                    color={useColorModeValue("gray.600", "pink.100")}
                    fontWeight={700}
                    fontSize="sm"
                    justifyContent='center'>
                    {props.commentData.comment}
                </Text>
            </CardBody>
        </Card>
    )
};