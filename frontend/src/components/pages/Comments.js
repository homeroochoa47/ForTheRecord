import React, { useState, useEffect, useLayoutEffect } from "react";
import { ChakraProvider, theme, Heading, Text, Box, useColorModeValue, useColorMode, Center, Stack, Avatar,SimpleGrid, Grid } from '@chakra-ui/react'
import { CommentCard } from "../cards/CommentCard";

// TODO: have a login/logout button that also shows the users spotify username and profile picture somewhere on the screen at all times.

//this component fetches data from the REST API and generates card components with the comments.
//TODO: make a new component consisting of a header with song/artist info.
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
    //TODO: need to set state based on if we receive the data or an error
    useEffect(() => {
        fetchData().then(data => {
            console.log("DATA: ", data)
            setSongInfo(data)
            console.log(songInfo)
        })
        setLoaded(true)
    }, [])

    return(
        <div>
            <SimpleGrid spacing={6} p={10} templateColumns='repeat(3, minmax(200px, 1fr))'>
                {loaded && songInfo.map(comment => (
                    <CommentCard commentData={comment}/>
                ))}
            </SimpleGrid>
        </div>
    )
};