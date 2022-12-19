import React from 'react'
import { VStack,} from "@chakra-ui/layout";
import { HomePage } from './pages/HomePage'
import { Comments } from './pages/Comments'
import {NavBar} from './layout/NavBar'
import { Footer } from './layout/Footer'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

//the frontend layout consists of a fixed navbar and footer, and the main content which we route to.
export default function App() {
  return (
    <VStack p={5}>
      <NavBar/>
        <Router>
          <Routes>
            <Route exact path="/home" element={<HomePage/>}/>
            <Route exact path="/comments" element={<Comments/>}/>
          </Routes>  
        </Router>
      <Footer/>
    </VStack>
  );
}