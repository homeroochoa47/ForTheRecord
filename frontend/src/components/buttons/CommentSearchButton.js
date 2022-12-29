import React from "react";
import { Button, Link } from '@chakra-ui/react';
import { Link as RouterLink} from "react-router-dom"


// this button sends the user to the coments route using a link as a routerlink. Note the button text prop
export function CommentSearchButton(props) {
  return(
    <Link as={RouterLink} to='/comments' style={{ textDecoration: 'none' }}>
      <Button
      colorScheme='green' 
      bg={'#698396'} 
      size='lg' 
      hover={{bg: 'green.500'}}>
      {props.buttonText}
      </Button>
    </Link>
  )
};