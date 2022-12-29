import React, { useState, useEffect } from "react";
import { Heading, Text, Stack, Card, CardHeader, CardBody, CardFooter, Button, Image } from '@chakra-ui/react'
import { WikipediaSearchButton } from "../buttons/wikipediaSearchButton"; 

//we pass props from the comments page containing comment info and render here.
export function SongCard(props) {

    return(
        <Card width='45%'
            direction={{ base: 'column', sm: 'row' }}
            overflow='hidden'
            mt="50px">
            <Image
            objectFit='cover'
            maxW={{ base: '100%', sm: '400px' }}
            src={props.song.image_url}
            />
            <Stack>
                <CardBody>
                    <Heading size='md'>{props.song.song_name}</Heading>
                    <Text py='2'>
                        {props.song.artists}
                    </Text>
                    <Text py='2'>
                        {props.song.album_name}
                    </Text>
                    <Text py='2'>
                        {props.song.album_release_date}
                    </Text>
                </CardBody>
                <CardFooter>
                    <WikipediaSearchButton artist={props.song.artists}/>
                </CardFooter>
            </Stack>
        </Card>
    )
};