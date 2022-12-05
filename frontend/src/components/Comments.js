import React from "react";
import { ChakraProvider, theme, Heading, Text, Box } from '@chakra-ui/react'

// TODO: have a login/logout button that also shows the users spotify username and profile picture somewhere on the screen at all times.

export class Comments extends React.Component {
    constructor(props) {
        super(props);
        this.state = {songInfo: null};
        this.handleClick = this.handleClick.bind(this);
    }


    fetchData = async () => {
        try {
            const response = await fetch('api/comments');
            if (response.ok) {
                const jsonResponse = await response.json();
                return jsonResponse
            }
        } 
        catch(error) {
            console.log(error);
        }
    }

    handleClick () {
        const data = this.fetchData()
        this.setState({songInfo: data }),
                   () => console.log(this.state.songInfo);
    }

    render() {
        return(
            <div>
                <button onClick={this.handleClick}>SEARCH</button>
                
            </div>
            )
    }
    
}

