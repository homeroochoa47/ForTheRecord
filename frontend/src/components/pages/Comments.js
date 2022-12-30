import React, { useState, useEffect } from "react";
import { ChakraProvider, Box, useColorModeValue, Stack, SimpleGrid, Spinner } from '@chakra-ui/react'
import { CommentCard } from "../cards/CommentCard";
import { SongCard } from "../cards/songCard";

//this component fetches data from the REST API and generates card components with the comments.
//TODO: send song data from the API along with comment data. It mihgt be best to make this call on the songCard component since theres only one object/component to render.

export function Comments() {
  const [songInfo, setSongInfo] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
      async function fetchData() {
        const response = await fetch('search/check_for_auth');
        const data = await response.json();
        if ('spotify_auth_url' in data) {
          window.open(data.spotify_auth_url)
        }
        console.log(data)
        setSongInfo(data);
        setIsLoading(false);
      }
      fetchData();
    }, []);

  return(
    <Stack align='center'>
        {isLoading ? (
            <Spinner size="xl" mt="200px" />
        ) : (
            <>
                {songInfo && songInfo.song && <SongCard song={songInfo.song} />}
                <SimpleGrid spacing={6} px="100px" py="60px" minChildWidth={{sm:"450px", lg:'350px'}} spacing="20px">
                    {songInfo && songInfo.new_comments && songInfo.new_comments.map(comment => (
                        <CommentCard key={comment.comment} commentData={comment}/>
                    ))}
                </SimpleGrid>
            </>
        )}
    </Stack>
  )
};


