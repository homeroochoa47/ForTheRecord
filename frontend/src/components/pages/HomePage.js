import React from "react";
import {
  Box,
  Heading,
  Container,
  Text,
  Button,
  Stack,
  Icon,
  useColorModeValue,
  createIcon,
} from '@chakra-ui/react';
import { CommentSearchButton } from "../buttons/CommentSearchButton";

// TODO: have a login/logout button that also shows the users spotify username and profile picture somewhere on the screen at all times.

export function HomePage() {
  return (
    <Container minW={"100%"}>
      <Stack
        as={Box}
        textAlign={"center"}
        spacing={{ base: 8, md: 4 }}
        py={{ base: 20, md: 36 }}
      >
        <Heading
          paddingTop={"5%"}
          fontWeight={600}
          fontSize={{ base: "2xl", sm: "4xl", md: "6xl" }}
          lineHeight={"110%"}
        >
          See what the <br />
          <Text as={"span"} color={"#698396"}>
            world has to say.
          </Text>
        </Heading>
        <Text color={"gray.500"} fontSize="2xl">
          Click below to find out what people are saying about your currently playing song on Spotify.
        </Text>
        <Stack
          direction={"column"}
          spacing={3}
          align={"center"}
          alignSelf={"center"}
          position={"relative"}
        >
          {/* Passing a button text prop since this button component is also in the navbar */}
          <CommentSearchButton buttonText="Lets do it!" />
        </Stack>
      </Stack>
    </Container>
  );
}