import React from "react";
import {Table} from "react-bootstrap";
import MainContainer from "../containers/MainContainer";

export default function Traffic() {
    return <>
        <MainContainer>
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
