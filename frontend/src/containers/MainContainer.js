import React from "react";
import {Container, Row, Col} from "react-bootstrap";

export default function MainContainer(props) {
    return (
        <Container>
            <Row>
                <Col>{props.children}</Col>
            </Row>
        </Container>
    );
}
