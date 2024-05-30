import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Milestones = () => {
    const [milestones, setMilestones] = useState([]);

    useEffect(() => {
        axios.get('/api/v1/milestones')
            .then(response => setMilestones(response.data))
            .catch(error => console.error('Error fetching milestones:', error));
    }, []);

    return (
        <div>
            <h1>Milestones</h1>
            <ul>
                {milestones.map((milestone, index) => (
                    <li key={index}>{milestone.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default Milestones;
