import React, { useState, useEffect } from "react";
import { Heading, Text, Stack, Card, CardHeader, CardBody, CardFooter, Button, Image } from '@chakra-ui/react'

//we pass props from the comments page containing comment info and render here.
export function SongCard(props) {

    return(
        <Card width='45%'
            direction={{ base: 'column', sm: 'row' }}
            overflow='hidden'
            mt="50px">
            <Image
            objectFit='cover'
            maxW={{ base: '100%', sm: '200px' }}
            src='https://images.unsplash.com/photo-1667489022797-ab608913feeb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw5fHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=800&q=60'
            alt='Caffe Latte'
            />
            <Stack>
                <CardBody>
                    <Heading size='md'>Song Name</Heading>
                    <Text py='2'>
                        Artist
                    </Text>
                    <Text py='2'>
                        Album Name
                    </Text>
                    <Text py='2'>
                        Release Date
                    </Text>
                </CardBody>
                <CardFooter>
                    <Button variant='solid' colorScheme='blue'>
                        More about this artist
                    </Button>
                </CardFooter>
            </Stack>
        </Card>
    )
};