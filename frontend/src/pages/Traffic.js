import React from "react";
import {Form, FormControl, InputGroup, Table} from "react-bootstrap";
import MainContainer from "../containers/MainContainer";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import Button from "react-bootstrap/Button";

export default function Traffic() {
    return <>
        <MainContainer>
          <br/>
          <h2>Traffic jams levels</h2>
          <br/>
          <Form>
            <Form.Row>
              <Col>
                <Form.Control placeholder="Min range (default - 0)" />
              </Col>
              <Col>
                <Form.Control placeholder="Max range  (default - 10)" />
              </Col>
            </Form.Row>
          </Form>
          <br/>
          <Row>
            <h2>Collection <i>Ways</i></h2>
            <InputGroup className="mb-3">
              <FormControl
                  placeholder="Find way by id"
                  aria-label="Recipient's username"
                  aria-describedby="basic-addon2"
              />
              <InputGroup.Append>
                <Button variant="primary">search</Button>
              </InputGroup.Append>
            </InputGroup>
          </Row>
          <br/>
            <Table striped bordered hover>
  <thead>
    <tr>
      <th>#</th>
      <th>id Way</th>
      <th>Coordinate</th>
      <th>traffic jams level </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>3124</td>
      <td>175.12 - 1243.312</td>
      <td>3</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3126</td>
      <td>41243.21312 -  213123.123</td>
      <td>8</td>
    </tr>
  </tbody>
</Table>
        </MainContainer>
    </>
}
