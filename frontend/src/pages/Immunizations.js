import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Immunizations = () => {
    const [immunizations, setImmunizations] = useState([]);

    useEffect(() => {
        axios.get('/api/v1/immunizations')
            .then(response => setImmunizations(response.data))
            .catch(error => console.error('Error fetching immunizations:', error));
    }, []);

    return (
        <div>
            <h1>Immunizations</h1>
            <ul>
                {immunizations.map((immunization, index) => (
                    <li key={index}>{immunization.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default Immunizations;
