import React, { useState, useEffect } from "react";
import { Heading, Text, Stack, Card, CardHeader, CardBody, Flex } from '@chakra-ui/react'

//we pass props from the comments page containing comment info and render here.
export function SongCard(props) {

    return(
        <Card
            direction={{ base: 'column', sm: 'row' }}
            overflow='hidden'
            variant='outline'>
            <Image
                objectFit='cover'
                maxW={{ base: '100%', sm: '200px' }}
                src='' //album cover link here
                alt=''/>
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