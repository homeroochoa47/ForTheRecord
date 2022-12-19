import React, { useState, useEffect, useLayoutEffect } from "react";
import { ChakraProvider, theme, Heading, Text, Box, useColorModeValue, useColorMode, Center, Stack, Avatar } from '@chakra-ui/react'
import { CommentCard } from "../cards/CommentCard";

// TODO: have a login/logout button that also shows the users spotify username and profile picture somewhere on the screen at all times.

//this component fetches data from the REST API and generates card components with the comments.
//TODO: make a new component consisting of a header with song/artist info.
export function Comments() {
    const [songInfo, setSongInfo] = useState(
        {songInfo: null}
        );


    const fetchData = async () => {
        try {
            const response = await fetch('search/check_for_auth');
            if (response.ok) {
                const jsonResponse = await response.json();
                return jsonResponse[0]
            };
        }
        catch(error) {
            console.log(error);
        };
    };
    
    //TODO: make sure we dont need this and delete.
    function handleClick() {
        fetchData().then((data) =>{
            setSongInfo({
                songInfo: data
            })
        });
    };

    //useEffect fetches the data from the api as soon as the user reaches this link, and then sets the state of this component as the data from the comments.
    //TODO: need to set state based on if we receive the data or an error
    useEffect(() => {
        fetchData().then((data) => {
            console.log(data)
            setSongInfo({
                songInfo: data
            })
        }).then(
            console.log(songInfo)
        )
    }, [])

    return(
        <div>
            <button onClick={handleClick}>SEARCH</button>
            <CommentCard/>
        </div>
    )
};