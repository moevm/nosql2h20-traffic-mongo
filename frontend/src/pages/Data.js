import React from "react";
import {Form, Button} from "react-bootstrap";
import MainContainer from "../containers/MainContainer";


export default function Data() {
    return (<MainContainer>
<Form>
    <h2>Import</h2>
  <Form.Group controlId="formBasicEmail">
    <Form.File/>
    <Form.Text className="text-muted">
      import bd
    </Form.Text>
  </Form.Group>
  <h2>Exprort</h2>
  <Button variant="primary" type="submit">
    Export
  </Button>
</Form>
</MainContainer>)
}
