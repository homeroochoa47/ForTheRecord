import React, { useState, useEffect } from "react";
import { Heading, Text, Stack, Card, CardHeader, CardBody, CardFooter, Box, Image, useColorModeValue, Flex } from '@chakra-ui/react'
import { WikipediaSearchButton } from "../buttons/wikipediaSearchButton"; 

//we pass props from the comments page containing comment info and render here.
export function SongCard(props) {

    return(
        <Card mt="50px"
            bg={useColorModeValue("#698396", "#5A745D")}
            borderRadius='lg'>
            <Flex
            direction='row'
            minW={{ sm: '100px', md: '600px', lg: '750px' }}
            maxH={{ sm: '225px', md: '250px', lg: '300px'}}
            overflow='auto'>
                <Image
                borderRadius='lg'
                objectFit='contain'
                width={{ sm: '225px', md: '250px', lg: '300px' }}
                height={{ sm: '225px', md: '250px', lg: '300px' }}
                src={props.song.image_url}
                />
                <Flex flexDirection="column" justifyContent="space-between">
                    <Flex flexDirection="column" justifyContent="flex-start" alignItems="flex-start"
                    p="10px">
                        <Heading size={{sm: 'sm', lg: 'md'}}>{props.song.song_name}</Heading>
                        <Text py='2' fontSize={{sm: 'sm', lg: 'md'}}>{props.song.artists}</Text>
                        <Text py='2' fontSize={{sm: 'sm', lg: 'md'}}>{props.song.album_name}</Text>
                        <Text py='2' fontSize={{sm: 'sm', lg: 'md'}}>{props.song.album_release_date}</Text>
                    </Flex>
                    <Flex justifyContent="flex-start" alignItems="flex-end" p='10px'>
                        <WikipediaSearchButton artist={props.song.artists}/>
                    </Flex>
                </Flex>
            </Flex>
        </Card>
    )
};