import React, {useState} from "react";
import {Form, Button, FormControl} from "react-bootstrap";
import MainContainer from "../containers/MainContainer";
import axios from 'axios';

export default function Data() {
    const [file, setFile] = useState("");

    const onFileChange = event => {
        setFile(event.target.files[0]);
    };

    const onFileUpload = () => {
        const formData = new FormData();
        formData.append(
            "myFile",
            file,
            file.name
        );

        axios.post("/api/bd", formData).then(res => {
            console.log(res.status);
        });
    };


    return (<MainContainer>
        <Form>
            <br/>
            <h2>Import</h2>
            <br/>
            <Button variant={"success"} onClick={onFileUpload}>
                Import
            </Button>
            <br/>
            <br/>
            <FormControl
                type="file"
                onChange={onFileChange}/>


            <h2>Export</h2>
            <a href={"api/bd"} target="_blank" rel="noopener noreferrer" download>
                <Button>
                    <i className="fas fa-download"/>
                    Download File
                </Button>
            </a>
        </Form>
    </MainContainer>)
}
