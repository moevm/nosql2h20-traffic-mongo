import React from "react";
import {Nav, Navbar} from "react-bootstrap";
import {Link} from "react-router-dom";

export default function MainNavbar() {
    return (
        <Navbar bg="dark" variant="dark">
            <Navbar.Brand as={Link} to="/">
                <i>Traffic Way</i>
            </Navbar.Brand>
            <Nav defaultActiveKey="/">
                <Nav.Item>
                    <Nav.Link as={Link} to="/">Home</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link as={Link} to="/stat">Stat</Nav.Link>
                </Nav.Item>                
                <Nav.Item>
                    <Nav.Link as={Link} to="/traffic">Traffic</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link as={Link} to="/data">Data</Nav.Link>
                </Nav.Item>
            </Nav>
        </Navbar>
    );

}
