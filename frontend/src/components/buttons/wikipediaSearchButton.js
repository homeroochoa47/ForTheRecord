import React, { useState } from 'react';
import { Button, useColorModeValue } from '@chakra-ui/react'

async function getWikipediaPageId(artistName) {
    try {
      // Replace "artistName" with the artist name that was passed in as a prop
      const query = `?action=query&format=json&list=search&srsearch=${artistName}&utf8=1&formatversion=2&origin=*`;
      const response = await fetch(`https://en.wikipedia.org/w/api.php${query}`);
      const data = await response.json();
      console.log(data)
      // Get the Wikipedia page id of the first search result
      const pageId = data.query.search[0].pageid;
      return pageId;
    } catch (error) {
      console.error(error);
    }
  }

export function WikipediaSearchButton(props) {
    
    const handleClick = async () => {
      const pageId = await getWikipediaPageId(props.artist);
      // Redirect the user to the Wikipedia page for the artist
      window.open(`https://en.wikipedia.org/?curid=${pageId}`, '_blank');
    }

    return (
      <Button variant='solid' bg={useColorModeValue("gray.300", "gray.600")} onClick={handleClick}>
        More about this artist
      </Button>
    );
  }


