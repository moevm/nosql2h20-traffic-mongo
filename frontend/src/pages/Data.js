import React, {useEffect, useState} from "react";
import {Form, Button, FormControl} from "react-bootstrap";
import MainContainer from "../containers/MainContainer";


export default function Data() {
    const [file, setFile] = useState("");

    const onFileChange = event => {
        setFile(event.target.files[0]);
    };

    useEffect(() => {
        if (file !== "")
        {
            const formData = new FormData();
            formData.append(
                "myFile",
                file,
                file.name
            );
        }
    }, [file])

    return (<MainContainer>
        <Form>
            <h2>Import</h2>
            <FormControl
                type="file"
                onChange={onFileChange}/>

            <h2>Export</h2>
            <Button variant="primary" type="submit">
                Export
            </Button>
        </Form>
    </MainContainer>)
}
