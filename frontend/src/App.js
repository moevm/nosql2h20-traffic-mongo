import React, { useState } from 'react';
import L from 'leaflet';
import { Map, TileLayer, Marker, Popup } from 'react-leaflet';
import InteractiveLayer from "./components/InteractiveLayer";
import './App.css';

function App() {
    let [pos, setPos] = useState([59.9190, 30.3078]);
    let [zoom, setZoom] = useState(14);
    return (
        <div className="map">
            <Map className="map" center={pos} zoom={zoom}>
                <TileLayer
                    attribution="&amp;copy <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors and Chat location by Iconika from the Noun Project"
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />
                <InteractiveLayer/>
            </Map>
        </div>
    );
}

export default App;
