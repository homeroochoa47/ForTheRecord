import React, { useState, useEffect, useLayoutEffect, useCallback } from "react";
import { ChakraProvider, theme, Heading, Text, Box, useColorModeValue, useColorMode, Center, Stack, Avatar,SimpleGrid, Grid } from '@chakra-ui/react'
import { CommentCard } from "../cards/CommentCard";
import { SongCard } from "../cards/songCard";

//this component fetches data from the REST API and generates card components with the comments.
//TODO: send song data from the API along with comment data. It mihgt be best to make this call on the songCard component since theres only one object/component to render.
export function Comments() {
    const [songInfo, setSongInfo] = useState([]);
    //the loaded state reloads the comment card component once the data has finished requesting.     
    const [loaded, setLoaded] = React.useState(false);


    const fetchData = async () => {
        try {
            const response = await fetch('search/check_for_auth');
            if (response.ok) {
                const jsonResponse = await response.json();
                if ('spotify_auth_url' in jsonResponse) {
                    window.open(jsonResponse.spotify_auth_url)
                } else {return jsonResponse}
            };
        }
        catch(error) {
            console.log(error);
        };
    };

    //useEffect fetches the data from the api as soon as the user reaches this link, and then sets the state of this component as the data from the comments and the loaded state to true to refresh the child component.
    useEffect(() => {
        fetchData().then(data => {
            setSongInfo(data)
        })
        setLoaded(true)
    }, [])

    return(
        <Stack align='center'>
            <SongCard />
            <SimpleGrid spacing={6} p={10} templateColumns='repeat(3, minmax(200px, 1fr))'>
                {loaded && songInfo?.comments?.map(comment => (
                    <CommentCard key={comment.user} commentData={comment}/>
                ))}
            </SimpleGrid>
        </Stack>
    )
};