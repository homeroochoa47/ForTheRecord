import React, { useState, useEffect, useLayoutEffect, useCallback } from "react";
import { ChakraProvider, theme, Heading, Text, Box, useColorModeValue, useColorMode, Center, Stack, Avatar,SimpleGrid, Grid } from '@chakra-ui/react'
import { CommentCard } from "../cards/CommentCard";
import { SongCard } from "../cards/songCard";

//this component fetches data from the REST API and generates card components with the comments.
//TODO: send song data from the API along with comment data. It mihgt be best to make this call on the songCard component since theres only one object/component to render.

export function Comments() {
    const [songInfo, setSongInfo] = useState([]);

    useEffect(() => {
        async function fetchData() {
          const response = await fetch('search/check_for_auth');
          const data = await response.json();
          console.log(data)
          setSongInfo(data);
        }
        fetchData();
      }, []);

      return(
        <Stack align='center'>
            {songInfo && songInfo.song && <SongCard song={songInfo.song} />}
            <SimpleGrid spacing={6} px="150px" pt="60px" templateColumns='repeat(3, minmax(200px, 1fr))'>
                {songInfo && songInfo.new_comments && songInfo.new_comments.map(comment => (
                    <CommentCard key={comment.comment} commentData={comment}/>
                ))}
            </SimpleGrid>
        </Stack>
      )
};


